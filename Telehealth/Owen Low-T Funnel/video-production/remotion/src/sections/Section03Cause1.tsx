import { useCurrentFrame } from "remotion";
import { s } from "../timeline";
import { KineticText } from "../graphics/KineticText";
import { LabelChip } from "../graphics/StatCard";
import { Beat } from "../graphics/beats/Beat";
import { BeatBackground } from "../graphics/beats/BeatBackground";
import { NodeGraph } from "../graphics/beats/NodeGraph";
import type { NodeGraphSpec } from "../graphics/beats/nodeGraphTypes";

// ── Section 3: Cause 1 — Metabolic Suppression (3:07.7 – 5:10.1) ──
// v4 (2026-09-17): rebuilt on the Beat/NodeGraph engine per
// docs/superpowers/specs/2026-09-17-owen-lowt-beat-composition-design.md.
// No component or measured region from the prior FullFrameInfographic/
// RegionHighlight system is reused.

const ABS_START = 187.7; // 3:07.7
const rel = (absVslSeconds: number) => s(absVslSeconds - ABS_START);

const AROMATASE_SPEC: NodeGraphSpec = {
  nodes: [
    { id: "fat", icon: "molecule", label: "Fat tissue", xPct: 22, yPct: 68 },
    { id: "aromatase", icon: "factory", label: "Aromatase enzyme", xPct: 50, yPct: 30 },
    { id: "moreFat", icon: "molecule", label: "More fat stored", xPct: 78, yPct: 68 },
    { id: "brain", icon: "brain", label: "Signal to brain", xPct: 50, yPct: 85 },
  ],
  edges: [
    { from: "fat", to: "aromatase" },
    { from: "aromatase", to: "moreFat" },
    { from: "moreFat", to: "brain" },
    { from: "brain", to: "fat" },
  ],
  // Absolute VSL seconds, matching the cut-sheet's narration beats.
  focusSteps: [
    { at: 224, target: "fat" }, // "fat tissue has... an enzyme"
    { at: 233, target: "aromatase" }, // "called aromatase"
    { at: 241, target: "moreFat" }, // "more fat you're carrying"
    { at: 250, target: "brain" }, // "signal back to your brain"
    { at: 255, target: "__all__" }, // "loop closes" - hold on full loop, no single node singled out
  ],
};

export const Section03Cause1: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <>
      {/* 3:19-3:23 — "something I CAN help with" */}
      <KineticText
        frame={frame}
        startFrame={rel(199)}
        duration={rel(203) - rel(199)}
        text="something I CAN help with"
        size="medium"
        accent="actionable"
        position="lower-third"
      />

      {/* 3:29-3:35 — age contrast chip */}
      <LabelChip frame={frame} startFrame={rel(209)} duration={rel(215) - rel(209)} text="30s → 40s/50s" />

      {/* 3:44-4:29 — Aromatase loop Beat, internal focus-step choreography */}
      <Beat startFrame={rel(224)} durationInFrames={rel(269) - rel(224)}>
        <BeatBackground>
          <NodeGraph spec={AROMATASE_SPEC} absStartSeconds={ABS_START} />
        </BeatBackground>
      </Beat>

      {/* 4:29-4:33 — "calories in ≠ calories out" */}
      <KineticText
        frame={frame}
        startFrame={rel(269)}
        duration={rel(273) - rel(269)}
        text="calories in ≠ calories out"
        size="medium"
      />

      {/* 4:41-4:46 — "diet alone often doesn't break the cycle" */}
      <KineticText
        frame={frame}
        startFrame={rel(281)}
        duration={rel(286) - rel(281)}
        text="diet alone often doesn't break the cycle"
        size="medium"
        accent="mandatory"
      />
    </>
  );
};
