import { FONT, ci, fadeIn } from "../brand";

// ── T/E or T/Cortisol rising-falling bar motif ────────────────────
// Per cut-sheet.md: built once (Cause 1, aromatase — T vs E), reused
// identically just relabeled for Cause 2 (cortisol vs T). A simple
// two-bar visual grammar: one hormone rises, one falls, in sync — the
// "one goes up because the other goes down" resource-competition idea.

export interface RiseFallBarsProps {
  /** Label + color for the bar that falls. */
  falling: { label: string; color: string };
  /** Label + color for the bar that rises. */
  rising: { label: string; color: string };
  startFrame?: number;
  frame: number;
  /** Overall scale — the diagrams that embed this need it smaller than a standalone hero shot. */
  scale?: number;
  /** Render each bar's own text label. Default true. Set false when the
   * caller already labels the same concept nearby (e.g. NodeGraph's node
   * labels) to avoid duplicate/redundant text. */
  showLabels?: boolean;
}

const BAR_HEIGHT = 180;
const BAR_WIDTH = 64;

export const RiseFallBars: React.FC<RiseFallBarsProps> = ({
  falling,
  rising,
  startFrame = 0,
  frame,
  scale = 1,
  showLabels = true,
}) => {
  const relFrame = frame - startFrame;
  const progress = ci(relFrame, [10, 50], [0, 1]);
  const fallHeight = BAR_HEIGHT * (1 - progress * 0.65);
  const riseHeight = BAR_HEIGHT * (0.35 + progress * 0.65);
  const opacity = fadeIn(relFrame, 0, 12);

  return (
    <div
      style={{
        opacity,
        transform: `scale(${scale})`,
        display: "flex",
        alignItems: "flex-end",
        gap: 48,
      }}
    >
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 10 }}>
        <div
          style={{
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 20,
            color: falling.color,
          }}
        >
          ↓
        </div>
        <div
          style={{
            width: BAR_WIDTH,
            height: fallHeight,
            background: falling.color,
            borderRadius: "6px 6px 0 0",
            opacity: 0.85,
          }}
        />
        {showLabels && (
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 18, color: falling.color }}>
            {falling.label}
          </div>
        )}
      </div>

      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 10 }}>
        <div
          style={{
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 20,
            color: rising.color,
          }}
        >
          ↑
        </div>
        <div
          style={{
            width: BAR_WIDTH,
            height: riseHeight,
            background: rising.color,
            borderRadius: "6px 6px 0 0",
            opacity: 0.85,
          }}
        />
        {showLabels && (
          <div style={{ fontFamily: FONT, fontWeight: 700, fontSize: 18, color: rising.color }}>
            {rising.label}
          </div>
        )}
      </div>
    </div>
  );
};
