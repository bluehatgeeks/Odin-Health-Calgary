// src/graphics/beats/nodeGraphTypes.ts
import type { IconName } from "./IconGlyph";
import type { FocusStep } from "./FocusStep";

export type GraphNode = {
  id: string;
  icon: IconName;
  label: string;
  xPct: number;
  yPct: number;
};

export type GraphEdge = { from: string; to: string };

export type NodeGraphSpec = {
  nodes: GraphNode[];
  edges: GraphEdge[];
  focusSteps: FocusStep[];
};
