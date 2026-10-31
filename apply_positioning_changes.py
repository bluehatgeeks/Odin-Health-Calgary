#!/usr/bin/env python3
"""Apply all positioning v2 text changes from changes.md to the page.html files."""

import os
import re

SITE = "https://odinhealthlab.ca"

# Define all text replacements per page
CHANGES = {
    "andropause-vs-menopause": [
        # h2 change
        ("How Odin helps men with andropause symptoms", "How Odin Health Lab helps men with andropause symptoms"),
        # body paragraphs
        ("Odin Health Lab is telehealth for men in Canada and the USA with andropause and low testosterone symptoms. If your partner is going through menopause and you are wondering whether something similar is happening to you, this is a good place to start. On video or phone consults, we take your symptoms, go through your lab results with you in plain language (two early-morning total testosterone results, free T, SHBG, LH and the metabolic markers that affect energy and weight) and look for the causes above. Then we build a plan around the levers that move symptoms day to day: sleep, training, nutrition and stress, with follow-up check-ins and repeat labs so you can see what is changing. See how our health coaching works.",
         "Odin Health Lab is a natural health clinic offering natural alternatives to TRT, by video call, for men in Canada and the USA with andropause and low testosterone symptoms. We do not provide TRT. If your partner is going through menopause and you are wondering whether something similar is happening to you, this is a good place to start. On video or phone consults, we take your symptoms, go through your lab results with you in plain language (two early-morning total testosterone results, free T, SHBG, LH and the metabolic markers that affect energy and weight) and look for the causes above. Then we build a plan around the levers that move symptoms day to day: sleep, training, nutrition and stress, with follow-up check-ins and repeat labs so you can see what is changing. See how our health coaching works."),
    ],
    # Will add more pages...
}

def apply_changes(page_dir, changes):
    """Apply text replacements to a page.html file."""
    page_path = os.path.join("site/pages", page_dir, "page.html")
    if not os.path.exists(page_path):
        print(f"Skipping {page_dir}: page.html not found")
        return False
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old_text, new_text in changes:
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(f"  ✓ Applied change in {page_dir}")
        else:
            # Try to find partial matches for debugging
            if old_text[:50] in content:
                print(f"  ⚠ Partial match found for: {old_text[:60]}...")
            else:
                print(f"  ✗ Not found in {page_dir}: {old_text[:60]}...")
    
    if content != original:
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == "__main__":
    os.chdir("/workspace")
    
    for page_dir, changes in CHANGES.items():
        print(f"\nProcessing {page_dir}...")
        apply_changes(page_dir, changes)
    
    print("\n✓ All changes applied!")
