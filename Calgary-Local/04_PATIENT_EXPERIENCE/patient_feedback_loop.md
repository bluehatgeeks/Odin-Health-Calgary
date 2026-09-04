# Odin Labs Calgary: Patient Feedback & SIS Loop Framework

## 🎯 Objective
Implement a quantitative and qualitative feedback loop to measure treatment efficacy and refine clinical roadmaps in real-time.

## 📊 The SIS (Subjective Improvement Score)
Patients rate their perceived improvement on a scale of 1-10 across four key vectors:
1. **Energy Levels** (Vitality/Ojas)
2. **Digestive Function** (Agni/Metabolism)
3. **Mental Clarity** (Sattva/Focus)
4. **Physical Comfort** (Pain/Inflammation)

## 🔄 The Feedback Loop
`Treatment Session` $\rightarrow$ `Post-Session Survey` $\rightarrow$ `Dashboard Update` $\rightarrow$ `Roadmap Adjustment`

### 1. Collection Method
- **Tool**: GHL automated survey sent 24 hours post-treatment.
- **Metric**: Average SIS across all vectors.

### 2. Trigger-Based Actions
- **SIS $\ge$ 7**: Maintain current protocol; move toward "Maintenance Phase."
- **SIS 4-6**: Trigger clinical review; adjust herbal dosage or modality frequency.
- **SIS $<$ 4**: Immediate "Red Flag" alert $\rightarrow$ Practitioner must perform an emergency roadmap audit within 48 hours.

## 🛠 Digital Glue Integration
- **GHL**: Survey response $\rightarrow$ Webhook $\rightarrow$ `Odin_Labs_Clinic_Dashboard` (Outcome Tab).
- **Dashboard**: Automated calculation of "Patient Progress Trend" using linear regression on SIS scores.
