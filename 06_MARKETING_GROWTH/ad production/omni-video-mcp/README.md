# omni-video-mcp

MCP server for **Gemini Omni Flash** (`gemini-omni-flash-preview`) — generate and
conversationally edit video ads from Claude Code.

## Setup

1. Get an API key at https://aistudio.google.com/apikey (needs a Google Cloud
   billing account for video generation — ~$0.10/second, so ~$1 per 10s clip).
2. Export it so the MCP server can see it:
   ```sh
   # add to ~/.zshrc
   export GEMINI_API_KEY="your-key-here"
   ```
3. The server is registered in the project's `.mcp.json`. Restart Claude Code in
   this project and approve the `omni-video` server when prompted.

Dependencies are managed by `uv` (`uv sync` in this directory, already done).

## Tools

| Tool | What it does |
|---|---|
| `generate_video` | Text → 10s clip. Optional reference images for product/character consistency. 16:9 or 9:16. |
| `edit_video` | Stateful edit of a prior generation via `interaction_id` ("swap the bottle", "bigger logo"). Max 3 sequential edits per chain (preview limit). |
| `edit_uploaded_video` | Upload an existing mp4 (e.g. an avatar clip exported from the Gemini app) and edit it with a prompt. |
| `stitch_videos` | ffmpeg-concat clips into 15–30s ads. |
| `list_generations` | Show this session's clips and interaction IDs. |

Videos are saved to `output/` (override with `OMNI_VIDEO_OUTPUT_DIR`).

## Avatar workflow (API doesn't expose avatars yet — July 2026)

Google's account-bound avatar mode is consumer-only for now (Gemini app →
settings gear → Avatar; biometric face + voice training, 18+). Until it lands in
the API:

1. **Reference images**: pass 2–3 photos of the person to `generate_video` via
   `reference_images` for consistent likeness across ad variants.
2. **Hybrid**: generate avatar clips in the Gemini app with the account that owns
   the avatar, download them, then iterate with `edit_uploaded_video`.

Note: generation can take 1–3 minutes per clip. If MCP tool calls time out,
raise the timeout with `export MCP_TIMEOUT=300000` before starting Claude Code.
