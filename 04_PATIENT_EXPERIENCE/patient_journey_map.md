# Odin Labs Calgary: Patient Journey Map (End-to-End)

## 🎯 Objective
Define the seamless transition of a lead from first touchpoint to long-term health maintenance, ensuring the "Digital Glue" captures every data point.

## 🗺️ The Journey

### 1. Awareness & Acquisition (The Hook)
- **Touchpoints**: LinkedIn "Executive Metabolic Audit" Ad $\rightarrow$ Landing Page $\rightarrow$ GHL Lead Form.
- **Digital Glue**: Lead data captured in GHL $\rightarrow$ Webhook $\rightarrow$ `Odin_Labs_Clinic_Dashboard` (Pipeline Tab).

### 2. Onboarding & Triage (The Entry)
- **Touchpoints**: Lead $\rightarrow$ Discovery Call (Coordinator) $\rightarrow$ Initial Consultation (Ayurvedic Practitioner).
- **Process**: Triage into segments (Ayurveda, Functional, or Treatment).
- **Digital Glue**: Patient record created in Google Drive $\rightarrow$ `01_Patient_Templates` folder.

### 3. The Clinical Blueprint (The Strategy)
- **Touchpoints**: Consultation $\rightarrow$ Delivery of `Metabolic Roadmap` or `Functional Health Blueprint`.
- **Process**: Definition of Dosha, target metabolic markers, and treatment frequency.
- **Digital Glue**: Roadmap saved as PDF in Patient Drive folder $\rightarrow$ linked in Dashboard.

### 4. Active Treatment (The Execution)
- **Touchpoints**: Scheduled Sessions $\rightarrow$ PEMF/Hydrogen/Marma Therapy $\rightarrow$ Herbal Prescription.
- **Process**: Real-time tracking of each modality session.
- **Digital Glue**: Practitioner updates `Treatment Protocol Log` $\rightarrow$ Logic check against `CLINICAL_QA_FRAMEWORK`.

### 5. Review & Optimization (The Loop)
- **Touchpoints**: Bi-weekly Review $\rightarrow$ SIS (Subjective Improvement Score) Update.
- **Process**: Adjusting the roadmap based on patient response.
- **Digital Glue**: SIS data plotted in `Odin_Labs_Clinic_Dashboard` $\rightarrow$ Trigger for roadmap revision.

### 6. Maintenance & Advocacy (The Horizon)
- **Touchpoints**: Maintenance Plan $\rightarrow$ Referral Request $\rightarrow$ Long-term Wellness Tracking.
- **Process**: Transition to low-frequency maintenance.
- **Digital Glue**: Automated GHL review request $\rightarrow$ Testimonial captured for Growth Strategy.
