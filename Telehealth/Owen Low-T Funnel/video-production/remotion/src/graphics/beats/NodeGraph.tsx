import { useCurrentFrame, useVideoConfig } from "remotion";
import { C } from "../../brand";
import { IconGlyph } from "./IconGlyph";
import { getActiveTarget, matchesTarget, sameTargetSet } from "./FocusStep";
import type { NodeGraphSpec, GraphNode } from "./nodeGraphTypes";
import { RiseFallBars } from "../RiseFallBars";

const NODE_ICON_SIZE = 110;
// Bars overlay: kept as an explicit named constant (not a bare magic
// number) so it's easy to find and re-tune. Bumped from the original
// 0.7 — at 0.7 the bars read as a tiny afterthought at 1920x1080; this
// size makes them a clearly legible focal element without colliding
// with the node icons above or the frame's bottom edge.
const BARS_SCALE = 1.2;
// Generously oversized relative to RiseFallBars' actual rendered
// footprint at BARS_SCALE (two ~64px-wide bars up to 180px tall, plus
// labels, gap, and arrows) so nothing is hard-clipped by the
// foreignObject's own box — the same class of bug already fixed once
// for node labels by moving them to real SVG <text>.
const BARS_BOX_WIDTH = 500;
const BARS_BOX_HEIGHT = 400;
const MAX_ACTIVE_SCALE = 1.18; // top of the global 1.08–1.18 active-scale range
const NODE_ICON_BOX = NODE_ICON_SIZE * MAX_ACTIVE_SCALE; // ~130, icon-only foreignObject
const LABEL_FONT_SIZE = 20;
const LABEL_OFFSET_Y = NODE_ICON_SIZE / 2 + 26; // label baseline below icon center
// Approximate on-screen footprint of the whole icon+label unit (at max
// active scale) used only for the frame-edge safety clamp below.
const NODE_BOX_WIDTH = NODE_ICON_BOX;
const NODE_BOX_HEIGHT = (NODE_ICON_SIZE + 36) * MAX_ACTIVE_SCALE; // ~172
const SAFE_MARGIN = 40;

function nodeCenter(
  node: GraphNode,
  width: number,
  height: number,
): { x: number; y: number } {
  const rawX = (node.xPct / 100) * width;
  const rawY = (node.yPct / 100) * height;
  const x = Math.min(
    Math.max(rawX, SAFE_MARGIN + NODE_BOX_WIDTH / 2),
    width - SAFE_MARGIN - NODE_BOX_WIDTH / 2,
  );
  const y = Math.min(
    Math.max(rawY, SAFE_MARGIN + NODE_BOX_HEIGHT / 2),
    height - SAFE_MARGIN - NODE_BOX_HEIGHT / 2,
  );
  return { x, y };
}

export const NodeGraph: React.FC<{
  spec: NodeGraphSpec;
  absStartSeconds: number;
}> = ({ spec, absStartSeconds }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const absSeconds = absStartSeconds + frame / fps;
  const activeId = getActiveTarget(spec.focusSteps, absSeconds);

  // Find the specific FocusStep that activates the bars (its `target`
  // set-equals spec.bars.activeWhenTarget), so we know the absolute-VSL
  // second at which the bars themselves should start animating from —
  // NOT the Beat's own start. Without this, RiseFallBars' internal
  // rise/fall + fade-in animation is already long past frame 50 by the
  // time the bars first become visible (they only appear partway
  // through the Beat), so they'd hard-pop in fully formed.
  const barsFocusStep = spec.bars
    ? spec.focusSteps.find(
        (step) =>
          Array.isArray(step.target) &&
          sameTargetSet(step.target, spec.bars!.activeWhenTarget),
      )
    : undefined;
  const barsVisible =
    spec.bars &&
    Array.isArray(activeId) &&
    sameTargetSet(activeId, spec.bars.activeWhenTarget);
  const barsStartFrame = barsFocusStep
    ? (barsFocusStep.at - absStartSeconds) * fps
    : 0;

  return (
    <svg width="100%" height="100%" viewBox={`0 0 ${width} ${height}`}>
      {spec.edges.map((edge) => {
        const fromNode = spec.nodes.find((n) => n.id === edge.from);
        const toNode = spec.nodes.find((n) => n.id === edge.to);
        if (!fromNode || !toNode) return null;
        const a = nodeCenter(fromNode, width, height);
        const b = nodeCenter(toNode, width, height);
        const edgeActive = matchesTarget(activeId, edge.from) || matchesTarget(activeId, edge.to);
        return (
          <line
            key={`${edge.from}-${edge.to}`}
            x1={a.x}
            y1={a.y}
            x2={b.x}
            y2={b.y}
            stroke={edgeActive ? C.lime : C.muted}
            strokeWidth={edgeActive ? 3 : 2}
            opacity={edgeActive ? 1 : 0.35}
          />
        );
      })}
      {spec.nodes.map((node) => {
        const center = nodeCenter(node, width, height);
        const isActive = matchesTarget(activeId, node.id);
        const scale = activeId === null ? 1 : isActive ? 1.14 : 0.92;
        const filter = !isActive
          ? "grayscale(1) brightness(0.32)"
          : "none";
        return (
          <g key={node.id}>
            <foreignObject
              x={center.x - NODE_ICON_BOX / 2}
              y={center.y - NODE_ICON_BOX / 2}
              width={NODE_ICON_BOX}
              height={NODE_ICON_BOX}
            >
              <div
                style={{
                  width: NODE_ICON_SIZE,
                  margin: "0 auto",
                  transform: `scale(${scale})`,
                  transformOrigin: "center center",
                  filter,
                }}
              >
                <IconGlyph name={node.icon} size={NODE_ICON_SIZE} />
              </div>
            </foreignObject>
            {/* Label is a real SVG <text>, not HTML-in-foreignObject: SVG
                text is never clipped by a foreignObject's box regardless
                of string length, and textAnchor="middle" centers it
                correctly for any label. The same scale/desaturation
                treatment as the icon is mirrored here so the label stays
                in sync with its node's active/inactive state. */}
            <text
              x={center.x}
              y={center.y + LABEL_OFFSET_Y}
              textAnchor="middle"
              style={{
                fill: C.offWhite,
                fontSize: LABEL_FONT_SIZE,
                fontWeight: 600,
                transform: `scale(${scale})`,
                transformOrigin: `${center.x}px ${center.y + LABEL_OFFSET_Y}px`,
                filter,
              }}
            >
              {node.label}
            </text>
          </g>
        );
      })}
      {barsVisible && spec.bars && (
        <foreignObject
          x={(spec.bars.xPct / 100) * width - BARS_BOX_WIDTH / 2}
          y={(spec.bars.yPct / 100) * height - BARS_BOX_HEIGHT / 2}
          width={BARS_BOX_WIDTH}
          height={BARS_BOX_HEIGHT}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              overflow: "visible",
            }}
          >
            <RiseFallBars
              frame={frame}
              startFrame={barsStartFrame}
              falling={spec.bars.falling}
              rising={spec.bars.rising}
              scale={BARS_SCALE}
              showLabels={false}
            />
          </div>
        </foreignObject>
      )}
    </svg>
  );
};
