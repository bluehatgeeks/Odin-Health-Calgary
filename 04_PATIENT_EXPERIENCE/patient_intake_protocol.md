# Odin Labs Calgary: Patient Intake & Triage Protocol

## 🎯 Objective
Standardize the transition from "Lead" to "Patient" to ensure accurate segmentation and alignment with clinical capabilities.

## 📋 Triage Workflow

### 1. Initial Lead Capture (GHL)
- **Trigger**: Lead submits "Executive Metabolic Audit" form.
- **Action**: Automated GHL sequence $\rightarrow$ Schedule Discovery Call.

### 2. The Discovery Call (Coordinator)
- **Goal**: Filter for intent, budget, and primary health concern.
- **Key Questions**:
    - "What is your primary health goal (e.g., energy, longevity, chronic pain)?"
    - "Have you used Ayurvedic or Functional medicine before?"
    - "Are you seeking a comprehensive program or a specific treatment (e.g., PEMF)?"

### 3. Clinical Segmentation (Practitioner)
Based on the Discovery Call, the patient is assigned to one of three tracks:
- **Track A: Ayurveda** $\rightarrow$ Focus on Dosha balance, Agni, and herbal protocols.
- **Track B: Functional Health** $\rightarrow$ Focus on metabolic markers, blood work, and habit coaching.
- **Track C: Treatment-Specific** $\rightarrow$ Focus on targeted modality (e.g., PEMF for injury recovery).

## 🛠 Digital Glue Integration
- **Status Change**: Lead $\rightarrow$ Patient in `Odin_Labs_Clinic_Dashboard`.
- **Folder Creation**: Trigger creation of patient folder in `01_Patient_Templates`.
- **Blueprint Initiation**: Assign the corresponding roadmap template (`AYURVEDA_ROADMAP` or `Functional Health Blueprint`).
