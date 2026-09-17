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

export type NodeGraphBars = {
  /** The exact FocusStep.target array value that makes these bars visible. */
  activeWhenTarget: string[];
  falling: { label: string; color: string };
  rising: { label: string; color: string };
  xPct: number;
  yPct: number;
};

export type NodeGraphSpec = {
  nodes: GraphNode[];
  edges: GraphEdge[];
  focusSteps: FocusStep[];
  bars?: NodeGraphBars;
};
