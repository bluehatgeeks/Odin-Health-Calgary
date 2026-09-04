# Odin Labs Calgary: Clinical Modality Integration Guide

## 🎯 Objective
Standardize the technical and clinical hand-off between different treatment modalities to ensure a seamless patient experience.

## 🔄 Integration Workflows

### 1. Ayurveda $\rightarrow$ PEMF/Hydrogen
- **Trigger**: Practitioner identifies "Systemic Inflammation" or "Deep Tissue Blockage" in the Ayurvedic Roadmap.
- **Action**: Add "PEMF session (30 min)" to the Treatment Protocol Log.
- **Hand-off**: Practitioner brief $\rightarrow$ Treatment Technician (focus area: lower back/inflammation).

### 2. Functional Coaching $\rightarrow$ Treatment
- **Trigger**: Coach identifies "Low Energy/Cognitive Fog" during a metabolic audit.
- **Action**: Prescribe "Hydrogen Inhalation Therapy" as a cognitive catalyst.
- **Hand-off**: Coach $\rightarrow$ Treatment Technician (session duration: 60 min).

### 3. Treatment $\rightarrow$ Ayurveda (Feedback Loop)
- **Trigger**: Technician observes significant physical release or acute reaction during Marma therapy.
- **Action**: Log observation in `Treatment Protocol Log` $\rightarrow$ Trigger "Roadmap Review" for Practitioner.
- **Hand-off**: Technician $\rightarrow$ Practitioner (clinical note update).

## 📉 Success Metrics
- **Cross-Modality Rate**: % of patients utilizing 2+ services.
- **Synergy Score**: Patient-reported improvement when modalities are combined vs. single-use.
- **Friction Rate**: Time delay between "Prescription" and "Session Execution".
