// src/graphics/beats/BeatBackground.tsx
import { AbsoluteFill } from "remotion";
import { C } from "../../brand";

export const BeatBackground: React.FC<{ children?: React.ReactNode }> = ({
  children,
}) => {
  return (
    <AbsoluteFill style={{ backgroundColor: C.bgDeep }}>
      <svg
        width="100%"
        height="100%"
        style={{ position: "absolute", inset: 0 }}
      >
        <defs>
          <pattern
            id="beat-dot-grid"
            width="28"
            height="28"
            patternUnits="userSpaceOnUse"
          >
            <circle cx="2" cy="2" r="1.4" fill={C.white} opacity={0.06} />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#beat-dot-grid)" />
      </svg>
      <AbsoluteFill>{children}</AbsoluteFill>
    </AbsoluteFill>
  );
};
