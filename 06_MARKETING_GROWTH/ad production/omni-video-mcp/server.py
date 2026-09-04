"""MCP server wrapping the Gemini Omni Flash Interactions API.

Tools:
  generate_video        — text/image/reference → 10s video clip
  edit_video            — stateful conversational edit of a prior generation
  edit_uploaded_video   — upload an existing video file, then edit it with a prompt
  stitch_videos         — concat clips with ffmpeg for ads longer than 10s
  list_generations      — show this session's interaction chain

Auth: set GEMINI_API_KEY (from https://aistudio.google.com/apikey).
Output dir: OMNI_VIDEO_OUTPUT_DIR (default: ./output next to this file).

Preview limits (July 2026): 10s clips, up to 3 sequential edits per chain,
$0.10/sec. Avatar mode is not yet exposed in the API — use reference images
for character consistency, or edit avatar clips exported from the Gemini app.
"""

import base64
import mimetypes
import os
import subprocess
import time
from pathlib import Path

from google import genai
from mcp.server.fastmcp import FastMCP

MODEL = "gemini-omni-flash-preview"
OUTPUT_DIR = Path(
    os.environ.get("OMNI_VIDEO_OUTPUT_DIR", Path(__file__).parent / "output")
)

mcp = FastMCP("omni-video")

_client: genai.Client | None = None
# interaction_id -> {"prompt": str, "path": str, "edits": int}
_generations: dict[str, dict] = {}


def client() -> genai.Client:
    global _client
    if _client is None:
        if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
            raise RuntimeError(
                "GEMINI_API_KEY is not set. Get a key at https://aistudio.google.com/apikey"
            )
        _client = genai.Client()
    return _client


def _save_output(interaction, output_name: str) -> Path:
    """Save an interaction's output video to OUTPUT_DIR, polling if URI-delivered."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / (output_name if output_name.endswith(".mp4") else f"{output_name}.mp4")

    video = interaction.output_video
    if getattr(video, "uri", None):
        # URI looks like .../v1beta/files/<id>:download?alt=media — extract bare id
        file_id = video.uri.split("/")[-1].split(":")[0]
        deadline = time.monotonic() + 600
        while True:
            f_info = client().files.get(name=f"files/{file_id}")
            if f_info.state.name == "ACTIVE":
                break
            if f_info.state.name == "FAILED":
                raise RuntimeError("Video generation failed on Google's side.")
            if time.monotonic() > deadline:
                raise TimeoutError("Timed out after 10 minutes waiting for video processing.")
            time.sleep(5)
        path.write_bytes(client().files.download(file=f"files/{file_id}"))
    else:
        path.write_bytes(base64.b64decode(video.data))
    return path


def _image_part(image_path: str) -> dict:
    p = Path(image_path).expanduser()
    if not p.is_file():
        raise FileNotFoundError(f"Image not found: {p}")
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    return {
        "type": "image",
        "data": base64.b64encode(p.read_bytes()).decode(),
        "mime_type": mime,
    }


def _record(interaction, prompt: str, path: Path, edits: int) -> str:
    _generations[interaction.id] = {"prompt": prompt, "path": str(path), "edits": edits}
    return (
        f"Saved to {path}\n"
        f"interaction_id: {interaction.id} (pass this to edit_video to iterate; "
        f"{3 - edits} sequential edits remaining in this chain)"
    )


@mcp.tool()
def generate_video(
    prompt: str,
    output_name: str,
    aspect_ratio: str = "16:9",
    reference_images: list[str] | None = None,
) -> str:
    """Generate a ~10s video clip with Gemini Omni Flash.

    Args:
        prompt: What to generate. Be specific about subject, motion, camera, style.
        output_name: Filename for the saved mp4 (e.g. "hydrogen_ad_v1").
        aspect_ratio: "16:9" (YouTube/landscape) or "9:16" (Reels/Shorts/portrait).
        reference_images: Optional paths to reference images (product shots, a
            person's photos for character consistency). Up to 3 recommended.
    """
    if aspect_ratio not in ("16:9", "9:16"):
        return 'aspect_ratio must be "16:9" or "9:16"'

    if reference_images:
        input_parts: list | str = [_image_part(p) for p in reference_images]
        input_parts.append({"type": "text", "text": prompt})
    else:
        input_parts = prompt

    interaction = client().interactions.create(
        model=MODEL,
        input=input_parts,
        response_format={"type": "video", "aspect_ratio": aspect_ratio, "delivery": "uri"},
    )
    path = _save_output(interaction, output_name)
    return _record(interaction, prompt, path, edits=0)


@mcp.tool()
def edit_video(previous_interaction_id: str, prompt: str, output_name: str) -> str:
    """Edit a previously generated/edited video conversationally (stateful).

    The model keeps full scene context, so prompts can be incremental:
    "make the logo bigger", "swap the bottle for the blue variant".
    Preview limit: 3 sequential edits per chain.

    Args:
        previous_interaction_id: The interaction_id returned by generate_video,
            edit_video, or edit_uploaded_video.
        prompt: The edit instruction.
        output_name: Filename for the saved mp4.
    """
    prior = _generations.get(previous_interaction_id)
    edits = (prior["edits"] + 1) if prior else 1
    if edits > 3:
        return (
            "This chain already has 3 edits (the preview maximum). "
            "Start a fresh chain: re-generate, or upload the last mp4 with edit_uploaded_video."
        )

    interaction = client().interactions.create(
        model=MODEL,
        previous_interaction_id=previous_interaction_id,
        input=prompt,
        response_format={"type": "video", "delivery": "uri"},
    )
    path = _save_output(interaction, output_name)
    return _record(interaction, prompt, path, edits=edits)


@mcp.tool()
def edit_uploaded_video(video_path: str, prompt: str, output_name: str) -> str:
    """Upload an existing video file (e.g. an avatar clip from the Gemini app,
    or previous ad footage) and edit it with a natural-language prompt.

    Args:
        video_path: Path to the local video file to upload.
        prompt: The edit instruction.
        output_name: Filename for the saved mp4.
    """
    p = Path(video_path).expanduser()
    if not p.is_file():
        return f"Video not found: {p}"

    video_file = client().files.upload(file=str(p))
    deadline = time.monotonic() + 600
    while video_file.state == "PROCESSING":
        if time.monotonic() > deadline:
            return "Timed out waiting for the upload to process."
        time.sleep(10)
        video_file = client().files.get(name=video_file.name)
    if video_file.state == "FAILED":
        return f"Upload processing failed for {p}"

    interaction = client().interactions.create(
        model=MODEL,
        input=[
            {"type": "document", "uri": video_file.uri},
            {"type": "text", "text": prompt},
        ],
        response_format={"type": "video", "delivery": "uri"},
    )
    path = _save_output(interaction, output_name)
    return _record(interaction, prompt, path, edits=0)


@mcp.tool()
def stitch_videos(video_paths: list[str], output_name: str) -> str:
    """Concatenate clips into one video with ffmpeg (for 15–30s ads built from
    multiple 10s Omni clips). Clips must share resolution/aspect ratio.

    Args:
        video_paths: Ordered list of mp4 paths to join.
        output_name: Filename for the combined mp4.
    """
    paths = [Path(p).expanduser() for p in video_paths]
    missing = [str(p) for p in paths if not p.is_file()]
    if missing:
        return f"Files not found: {', '.join(missing)}"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / (output_name if output_name.endswith(".mp4") else f"{output_name}.mp4")
    concat_list = OUTPUT_DIR / ".concat_list.txt"
    concat_list.write_text("".join(f"file '{p.resolve()}'\n" for p in paths))

    result = subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
         "-c", "copy", str(out)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        # Codec mismatch between clips — fall back to re-encoding
        result = subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
             "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-c:a", "aac", str(out)],
            capture_output=True, text=True,
        )
    concat_list.unlink(missing_ok=True)
    if result.returncode != 0:
        return f"ffmpeg failed:\n{result.stderr[-2000:]}"
    return f"Stitched {len(paths)} clips into {out}"


@mcp.tool()
def list_generations() -> str:
    """List videos generated in this session with their interaction IDs and edit counts."""
    if not _generations:
        return "No videos generated in this session yet."
    lines = [
        f"- {info['path']} — id {iid} — {info['edits']} edit(s) — \"{info['prompt'][:80]}\""
        for iid, info in _generations.items()
    ]
    return "\n".join(lines)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
