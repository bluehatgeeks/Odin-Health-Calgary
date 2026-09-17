export type FocusStep = { at: number; target: string | string[] };

export function getActiveTarget(
  steps: FocusStep[],
  absSeconds: number,
): string | string[] | null {
  let active: string | string[] | null = null;
  for (const step of steps) {
    if (absSeconds >= step.at) {
      active = step.target;
    }
  }
  return active;
}

export function matchesTarget(
  activeTarget: string | string[] | null,
  id: string,
): boolean {
  if (activeTarget === null) return true;
  if (activeTarget === "__all__") return true;
  if (Array.isArray(activeTarget)) return activeTarget.includes(id);
  return activeTarget === id;
}

/**
 * Order-independent set equality for two string arrays: same length, and
 * every element of one appears in the other. Used to check whether the
 * currently-active (possibly multi-node) focus target is exactly a given
 * target set — e.g. "is the bars overlay's activeWhenTarget currently
 * active?" — and to locate the specific FocusStep that activates it.
 */
export function sameTargetSet(a: string[], b: string[]): boolean {
  if (a.length !== b.length) return false;
  return a.every((id) => b.includes(id));
}
