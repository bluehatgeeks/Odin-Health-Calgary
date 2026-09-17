import { useCurrentFrame } from "remotion";
import { s } from "../timeline";
import { C } from "../brand";
import { KineticText } from "../graphics/KineticText";
import { LabelChip, StatCard } from "../graphics/StatCard";
import { FullFrameInfographic } from "../graphics/FullFrameInfographic";
import { Beat } from "../graphics/beats/Beat";
import { BeatBackground } from "../graphics/beats/BeatBackground";
import { NodeGraph } from "../graphics/beats/NodeGraph";
import type { NodeGraphSpec } from "../graphics/beats/nodeGraphTypes";

// ── Section 4: Cause 2 — Stress/Energy/Illness Suppression (5:10.1 – 7:36.7) ──
// v4 (2026-09-17): cortisol-fork portion rebuilt on the Beat/NodeGraph
// engine per docs/superpowers/specs/2026-09-17-owen-lowt-beat-composition-design.md.
// Sleep timeline/stat-card portions unchanged — no per-element highlight
// needed there, so the prior FullFrameInfographic approach is still
// appropriate for that stretch.

const ABS_START = 310.1; // 5:10.1
const rel = (absVslSeconds: number) => s(absVslSeconds - ABS_START);

const REPRISE_WINDOW = { startFrame: rel(310.1), endFrame: rel(312) };

const CORTISOL_SPEC: NodeGraphSpec = {
  nodes: [
    { id: "raw", icon: "raw-material", label: "Raw material", xPct: 50, yPct: 22 },
    { id: "valve", icon: "valve", label: "One path", xPct: 50, yPct: 48 },
    { id: "cortisol", icon: "cortisol", label: "Cortisol", xPct: 26, yPct: 76 },
    { id: "testosterone", icon: "testosterone", label: "Testosterone", xPct: 74, yPct: 76 },
  ],
  edges: [
    { from: "raw", to: "valve" },
    { from: "valve", to: "cortisol" },
    { from: "valve", to: "testosterone" },
  ],
  // Absolute VSL seconds, matching the cut-sheet's narration beats.
  focusSteps: [
    { at: 337, target: "raw" }, // 5:37 "cortisol... main stress hormone"
    { at: 341, target: "raw" }, // 5:41 "same shared raw material"
    { at: 347, target: "valve" }, // 5:47 "can only turn into one or the other"
    { at: 350, target: "cortisol" }, // 5:50 "sustained high-stress mode"
    { at: 353, target: "testosterone" }, // 5:53 "testosterone production gets pushed down"
    { at: 356, target: ["cortisol", "testosterone"] }, // 5:56 "cortisol bar fills, testosterone drops"
    { at: 361, target: "__all__" }, // 6:01 hold on full diagram
  ],
  bars: {
    activeWhenTarget: ["cortisol", "testosterone"],
    falling: { label: "Testosterone", color: C.lime },
    rising: { label: "Cortisol", color: C.mandatory },
    xPct: 50,
    yPct: 76,
  },
};

const SLEEP_WINDOW = { startFrame: rel(375), endFrame: rel(382) };

export const Section04Cause2: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <>
      {/* 5:10.1-5:14 — checklist reprise, quick glimpse */}
      <FullFrameInfographic
        src="infographics/seven-causes-checklist.png"
        startFrame={REPRISE_WINDOW.startFrame}
        endFrame={REPRISE_WINDOW.endFrame}
        frame={frame}
      />

      {/* 5:14-5:20 — "EMERGENCY MODE" stamp */}
      <KineticText
        frame={frame}
        startFrame={rel(314)}
        duration={rel(320) - rel(314)}
        text="EMERGENCY MODE"
        size="medium"
        accent="mandatory"
        position="lower-third"
      />

      {/* 5:37-6:04 — Cortisol/Testosterone fork Beat, internal focus-step choreography */}
      <Beat startFrame={rel(337)} durationInFrames={rel(364) - rel(337)}>
        <BeatBackground>
          <NodeGraph spec={CORTISOL_SPEC} absStartSeconds={337} />
        </BeatBackground>
      </Beat>

      {/* 6:10-6:15 — "SLEEP" isolated word */}
      <KineticText
        frame={frame}
        startFrame={rel(370)}
        duration={rel(375) - rel(370)}
        text="SLEEP"
        size="large"
      />

      {/* 6:15-6:22 — sleep timeline */}
      <FullFrameInfographic
        src="infographics/sleep-timeline.png"
        startFrame={SLEEP_WINDOW.startFrame}
        endFrame={SLEEP_WINDOW.endFrame}
        frame={frame}
      />

      {/* 6:22-6:28 — first sleep stat card */}
      <StatCard
        frame={frame}
        startFrame={rel(382)}
        duration={rel(388) - rel(382)}
        value="5 hrs sleep"
        label="→ 10-15% less testosterone"
      />

      {/* 6:28-6:35 — second sleep stat card */}
      <StatCard
        frame={frame}
        startFrame={rel(388)}
        duration={rel(395) - rel(388)}
        value="≤6 hrs sleep"
        label="≈ +10 years, hormonally"
        accent="mandatory"
      />

      {/* 6:51-6:58 — "normal labs ≠ the full story" */}
      <KineticText
        frame={frame}
        startFrame={rel(411)}
        duration={rel(418) - rel(411)}
        text="normal labs ≠ the full story"
        size="medium"
      />

      {/* 7:12-7:19 — "30s & 40s" age chip reprise */}
      <LabelChip frame={frame} startFrame={rel(432)} duration={rel(439) - rel(432)} text="30s & 40s" />
    </>
  );
};
