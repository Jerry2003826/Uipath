# Evidence Placeholder: TC-001 Deny Raw VIP Email Export

| Field | Value |
| --- | --- |
| Test ID | TC-001 |
| Name | Deny raw VIP email export |
| Input action | `export_raw_customer_emails` |
| Segment | `VIP` |
| Count | `500` |
| Data type | `raw_email` |
| Expected decision | `deny` |
| Expected case state | `Test Cloud Evidence` |

## Evidence To Attach

- Local deterministic runner result: `evidence/case_001/test_results_after.json`
- Test Manager result link: `https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/testexecution-results/c66f6554-4b30-0f00-4375-0b49aa4d0fd9/cb8464ba-8b14-0700-3328-0b49aa443162`
- Test Cloud evidence link: `assets/test_manager_permitops_execution_5_passed_viewport.png`
- Runtime proxy denial screenshot/link: `assets/uipath_api_workflow_success_deny_suspend.png`
