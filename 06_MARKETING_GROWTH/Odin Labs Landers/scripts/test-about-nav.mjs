/**
 * One-off: load local odinlabcalgary.html, click About Us, assert section visible + founder in view.
 * Run from repo root with: npx playwright test (or node after playwright install).
 */
import { chromium } from "playwright";

const base = process.env.BASE_URL || "http://127.0.0.1:8765";

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
await page.setViewportSize({ width: 1280, height: 800 });

try {
  await page.goto(`${base}/odinlabcalgary.html`, {
    waitUntil: "domcontentloaded",
    timeout: 60000,
  });

  await page.waitForSelector('a.nav-link[href*="#about-us-section"]', {
    timeout: 45000,
  });

  const aboutBefore = await page.locator("#about-us-section").evaluate((el) =>
    el.classList.contains("about-us-section--hidden")
  );
  console.log("About section hidden before click:", aboutBefore);

  await page.click('a.nav-link[href*="#about-us-section"]');
  await page.waitForFunction(
    () => {
      const el = document.getElementById("about-us-section");
      return el && !el.classList.contains("about-us-section--hidden");
    },
    { timeout: 10000 }
  );

  const vh = page.viewportSize().height;
  await page.waitForFunction(
    (height) => {
      const card = document.querySelector(".about-us-founder-card");
      if (!card) return false;
      const top = card.getBoundingClientRect().top;
      return top >= 40 && top < height * 0.9;
    },
    vh,
    { timeout: 8000 }
  );

  const hiddenAfter = await page.locator("#about-us-section").evaluate((el) =>
    el.classList.contains("about-us-section--hidden")
  );
  const founderRect = await page.locator(".about-us-founder-card").boundingBox();

  console.log("About section hidden after click:", hiddenAfter);
  console.log("Founder card bounding box:", founderRect);
  console.log("Viewport height:", vh);

  if (hiddenAfter) {
    throw new Error("About section should be visible after nav click");
  }
  if (!founderRect) {
    throw new Error("Founder card not found or not visible");
  }

  console.log("PASS: About Us nav reveals section and founder card is in view.");
} finally {
  await browser.close();
}
