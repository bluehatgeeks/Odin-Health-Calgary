// src/graphics/beats/Beat.tsx
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { C, ci } from "../../brand";

const ENTER_DUR = 14;
const EXIT_DUR = 14;

export const Beat: React.FC<{
  startFrame: number;
  durationInFrames: number;
  children: React.ReactNode;
}> = ({ startFrame, durationInFrames, children }) => {
  const frame = useCurrentFrame();
  const endFrame = startFrame + durationInFrames;

  if (frame < startFrame || frame >= endFrame) {
    return null;
  }

  const enterProgress = ci(frame, [startFrame, startFrame + ENTER_DUR], [0, 1]);
  const exitProgress = ci(
    frame,
    [endFrame - EXIT_DUR, endFrame],
    [1, 0],
  );
  const progress = Math.min(enterProgress, exitProgress);

  const scale = 0.9 + 0.1 * progress;
  const opacity = progress;

  return (
    <AbsoluteFill style={{ backgroundColor: C.bgDeep }}>
      <div
        style={{
          width: "100%",
          height: "100%",
          transform: `scale(${scale})`,
          opacity,
        }}
      >
        {children}
      </div>
    </AbsoluteFill>
  );
};
