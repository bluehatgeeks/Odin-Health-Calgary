export type FocusStep = { at: number; target: string };

export function getActiveTarget(
  steps: FocusStep[],
  absSeconds: number,
): string | null {
  let active: string | null = null;
  for (const step of steps) {
    if (absSeconds >= step.at) {
      active = step.target;
    }
  }
  return active;
}
