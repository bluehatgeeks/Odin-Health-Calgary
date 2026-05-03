# Odin Labs Calgary: Lead Intake Form Specification

## 🎯 Objective
Define the exact data fields required at the first point of contact to ensure precise patient segmentation and a frictionless transition to the clinical roadmap.

## 📋 Field Requirements

### 1. Core Contact Information
- **Full Name** (Required)
- **Email Address** (Required)
- **Phone Number** (Required)
- **Preferred Contact Method** (Dropdown: Email, Text, Phone)

### 2. Health Goals & Triage (Segmentation Logic)
- **Primary Health Goal** (Multi-select)
  - [ ] Weight Loss / Metabolic Health
  - [ ] Stress / Anxiety / Sleep
  - [ ] Chronic Inflammation / Pain
  - [ ] Digestive Health / Gut Wellness
  - [ ] General Longevity / Optimization
- **Current Knowledge of Ayurveda** (Scale 1-5)
- **Interest in Advanced Modalities** (Checkboxes)
  - [ ] PEMF Therapy
  - [ ] Hydrogen Inhalation
  - [ ] Marma Massage

### 3. Executive Profile (High-Net-Worth Filter)
- **Profession / Industry** (Open Text)
- **Weekly Working Hours** (Number)
- **Current Health Optimization Spend** (Dropdown: <<$$500, $500-$2k, $2k+)

## 🛠 GHL Implementation Note
Fields must be mapped to the GHL Custom Fields defined in `GHL_SHEETS_WEBHOOK_BLUEPRINT.md` to maintain the "Digital Glue" automation flow.
