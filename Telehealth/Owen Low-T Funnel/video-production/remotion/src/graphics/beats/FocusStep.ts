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
