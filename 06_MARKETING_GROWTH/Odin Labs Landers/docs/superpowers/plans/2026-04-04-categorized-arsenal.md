# Categorized Arsenal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the simple compound badge list with a high-end, categorized grid of "Clinical Toolkits" grouped by biological system.
**Architecture:** CSS Grid layout using cards. Each card represents a biological system and contains a list of associated compounds as styled "pills".
**Tech Stack:** HTML5, CSS3 (Custom Properties)

---

### Task 1: Define Arsenal Styles
**Files:**
- Modify: `nutritional-supplementation.css`

- [ ] **Step 1: Add CSS variables and base styles for the arsenal grid**
```css
/* Arsenal Section Variables */
:root {
    --ns-arsenal-bg: #1f1f1f;
    --ns-arsenal-border: rgba(196, 255, 73, 0.2);
    --ns-pill-bg: #333333;
}

.ns-arsenal-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 24px;
    margin-top: 30px;
}

.ns-arsenal-card {
    background: var(--ns-arsenal-bg);
    border: 1px solid var(--ns-arsenal-border);
    border-radius: 16px;
    padding: 30px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.ns-arsenal-card:hover {
    border-color: var(--lime-green);
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(196, 255, 73, 0.1);
}

.ns-arsenal-card h3 {
    font-family: 'Poppins', sans-serif;
    color: var(--lime-green);
    font-size: 1.25rem;
    margin: 0 0 20px 0;
    font-weight: 600;
}

.ns-arsenal-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.ns-arsenal-pill {
    background: var(--ns-pill-bg);
    color: #f5f5f5;
    font-size: 0.85rem;
    padding: 6px 14px;
    border-radius: 100px;
    border: 1px solid rgba(255,255,255,0.1);
    transition: all 0.2s ease;
    cursor: default;
}

.ns-arsenal-pill:hover {
    background: var(--lime-green);
    color: #0a0a0a;
    border-color: var(--lime-green);
}
```
- [ ] **Step 2: Commit styles**
```bash
git add nutritional-supplementation.css
git commit -m "feat: add styles for categorized compound arsenal"
```

### Task 2: Implement Arsenal HTML Structure
**Files:**
- Modify: `nutritional-supplementation.html`

- [ ] **Step 1: Replace the existing `.ns-badges-section` content**
Replace the content inside `<<divdiv class="ns-badges-inner">` (starting from the label to the end of the `.ns-badges-row` div) with:
```html
<<spanspan class="ns-badges-label">The Clinical Toolkit</span>
<<divdiv class="ns-arsenal-grid">
    <!-- Neuro-Cognitive -->
    <<divdiv class="ns-arsenal-card">
        <h3>Neuro-Cognitive</h3>
        <<divdiv class="ns-arsenal-pills">
            <<spanspan class="ns-arsenal-pill">Lion's Mane</span>
            <<spanspan class="ns-arsenal-pill">Rhodiola</span>
            <<spanspan class="ns-arsenal-pill">Methylfolate</span>
            <<spanspan class="ns-arsenal-pill">Methylcobalamin</span>
        </div>
    </div>
    <!-- Metabolic & Glycemic -->
    <<divdiv class="ns-arsenal-card">
        <h3>Metabolic & Glycemic</h3>
        <<divdiv class="ns-arsenal-pills">
            <<spanspan class="ns-arsenal-pill">Berberine</span>
            <<spanspan class="ns-arsenal-pill">Chromium</span>
            <<spanspan class="ns-arsenal-pill">ALA</span>
        </div>
    </div>
    <!-- Mitochondrial & Energy -->
    <<divdiv class="ns-arsenal-card">
        <h3>Mitochondrial & Energy</h3>
        <<divdiv class="ns-arsenal-pills">
            <<spanspan class="ns-arsenal-pill">CoQ10</span>
            <<spanspan class="ns-arsenal-pill">PQQ</span>
            <<spanspan class="ns-arsenal-pill">Magnesium</span>
        </div>
    </div>
    <!-- Immune & Inflammatory -->
    <<divdiv class="ns-arsenal-card">
        <h3>Immune & Inflammatory</h3>
        <<divdiv class="ns-arsenal-pills">
            <<spanspan class="ns-arsenal-pill">Omega-3</span>
            <<spanspan class="ns-arsenal-pill">Vitamin D3/K2</span>
            <<spanspan class="ns-arsenal-pill">Zinc</span>
            <<spanspan class="ns-arsenal-pill">Ashwagandha</span>
        </div>
    </div>
</div>
```
- [ ] **Step 2: Commit HTML changes**
```bash
git add nutritional-supplementation.html
git commit -m "feat: replace compound list with categorized arsenal grid"
```
