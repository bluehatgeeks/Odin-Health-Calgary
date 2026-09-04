# Odin Labs Calgary: Clinic Inventory Management System (CIMS)

## 🎯 Objective
Implement a rigorous tracking system for all medical consumables and hardware to prevent stock-outs and ensure equipment longevity.

## 📊 Inventory Structure
The `Inventory` tab in the `Odin_Labs_Clinic_Dashboard` is categorized as follows:
- **Category A: High-Turnover Consumables** (Herbal oils, bandages, disposable electrodes).
- **Category B: Specialized Supplements** (Ayurvedic tonics, Functional Health vitamins).
- **Category C: Capital Hardware** (PEMF Mats, Hydrogen Inhalers, Marma tools).

## ⚙️ Management Logic
### 1. The Reorder Point (ROP)
- Each SKU has a defined `Min_Threshold`.
- **Trigger**: When `Current_Stock` $\le$ `Min_Threshold` $\rightarrow$ Automatic alert to Clinic Coordinator.
- **Action**: Reorder based on `Average_Monthly_Usage` $\times$ 1.5 (Safety Buffer).

### 2. Audit Cycle
- **Weekly Cycle**: Physical count of Category A items.
- **Monthly Cycle**: Comprehensive audit of Category B and C.
- **Discrepancy Log**: Any variance $>5\%$ must be documented in the `Inventory_Variance_Log`.

### 3. Hardware Lifecycle
- **Maintenance Log**: Every hardware session is logged.
- **Service Interval**: Hardware is flagged for calibration every 500 hours of use.
- **Depreciation**: Logged for quarterly financial review.
