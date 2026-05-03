# Odin Labs Calgary: GHL-to-Sheets Webhook Blueprint

## 🎯 Objective
Zero-loss automated transfer of patient leads from GHL to the `Odin_Labs_Clinic_Dashboard` for real-time clinic management.

## 🛠 Technical Architecture
`GHL Workflow` $\rightarrow$ `Webhook (JSON Payload)` $\rightarrow$ `Agent-Bridge (Python/API)` $\rightarrow$ `Google Sheets (Pipeline Tab)`

## 📋 Mapping Logic
| GHL Custom Field | Google Sheet Column | Data Type | Validation |
| :--- | :--- | :--- | :--- |
| `contact.first_name` | Column A (First Name) | String | Required |
| `contact.last_name` | Column B (Last Name) | String | Required |
| `contact.email` | Column C (Email) | Email | Required |
| `contact.phone` | Column D (Phone) | Phone | Required |
| `custom_field: patient_segment` | Column E (Segment) | Dropdown | Ayurveda/Functional/Treatment |
| `custom_field: lead_source` | Column F (Source) | String | LinkedIn/SEO/Referral |
| `workflow.trigger_date` | Column G (Date Added) | Date | ISO 8601 |

## 🚀 Execution Steps
- [ ] **GHL Side**: Create Workflow Trigger $\rightarrow$ "Customer Created" or "Tag Added" $\rightarrow$ Action: "Webhook".
- [ ] **Endpoint Setup**: Deploy listener endpoint to receive JSON payload.
- [ ] **Data Transformation**: Script to parse GHL JSON and map to Sheet row index.
- [ ] **Error Handling**: Implement retry logic for 5xx errors to prevent data loss.
- [ ] **Verification**: Send test lead from GHL $\rightarrow$ Confirm appearance in `Odin_Labs_Clinic_Dashboard`.
