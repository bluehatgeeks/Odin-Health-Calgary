import { useCurrentFrame, useVideoConfig } from "remotion";
import { C } from "../../brand";
import { IconGlyph } from "./IconGlyph";
import { getActiveTarget } from "./FocusStep";
import type { NodeGraphSpec, GraphNode } from "./nodeGraphTypes";

const NODE_ICON_SIZE = 110;
const MAX_ACTIVE_SCALE = 1.18; // top of the global 1.08–1.18 active-scale range
const NODE_BOX_WIDTH = NODE_ICON_SIZE * MAX_ACTIVE_SCALE; // ~130
const NODE_BOX_HEIGHT = (NODE_ICON_SIZE + 36) * MAX_ACTIVE_SCALE; // ~172

function nodeCenter(node: GraphNode, width: number, height: number) {
  return { x: (node.xPct / 100) * width, y: (node.yPct / 100) * height };
}

export const NodeGraph: React.FC<{
  spec: NodeGraphSpec;
  absStartSeconds: number;
}> = ({ spec, absStartSeconds }) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const absSeconds = absStartSeconds + frame / fps;
  const activeId = getActiveTarget(spec.focusSteps, absSeconds);

  return (
    <svg width="100%" height="100%" viewBox={`0 0 ${width} ${height}`}>
      {spec.edges.map((edge) => {
        const fromNode = spec.nodes.find((n) => n.id === edge.from);
        const toNode = spec.nodes.find((n) => n.id === edge.to);
        if (!fromNode || !toNode) return null;
        const a = nodeCenter(fromNode, width, height);
        const b = nodeCenter(toNode, width, height);
        const edgeActive = activeId === edge.from || activeId === edge.to;
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
        const isActive = activeId === null || activeId === node.id;
        const scale = activeId === null ? 1 : isActive ? 1.14 : 0.92;
        const filter = !isActive
          ? "grayscale(1) brightness(0.32)"
          : "none";
        return (
          <foreignObject
            key={node.id}
            x={center.x - NODE_BOX_WIDTH / 2}
            y={center.y - NODE_ICON_SIZE / 2}
            width={NODE_BOX_WIDTH}
            height={NODE_BOX_HEIGHT}
          >
            <div
              style={{
                width: NODE_ICON_SIZE,
                margin: "0 auto",
                transform: `scale(${scale})`,
                transformOrigin: "center top",
                filter,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                gap: 8,
              }}
            >
              <IconGlyph name={node.icon} size={NODE_ICON_SIZE} />
              <div
                style={{
                  color: C.offWhite,
                  fontSize: 20,
                  fontWeight: 600,
                  textAlign: "center",
                  whiteSpace: "nowrap",
                }}
              >
                {node.label}
              </div>
            </div>
          </foreignObject>
        );
      })}
    </svg>
  );
};
