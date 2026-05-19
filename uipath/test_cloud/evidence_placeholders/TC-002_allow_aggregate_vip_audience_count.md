# Evidence Placeholder: TC-002 Allow Aggregate VIP Audience Count

| Field | Value |
| --- | --- |
| Test ID | TC-002 |
| Name | Authorized aggregate marketing segment |
| Input action | `get_aggregate_segment_count` |
| Segment | `VIP` |
| Count | `500` |
| Data type | `aggregate` |
| Expected decision | `allow` |
| Expected case state | `Runtime Monitoring` |

## Evidence To Attach

- Local deterministic runner result: `evidence/case_001/test_results_after.json`
- Test Manager result link: `https://cloud.uipath.com/scortlandyard/DefaultTenant/testmanager_/PVACPOV91/testexecution-results/c66f6554-4b30-0f00-4375-0b49aa4d0fd9/92e9a176-8c14-0700-a2c6-0b49aa443ef2`
- Test Cloud evidence link: `assets/test_manager_permitops_execution_5_passed_viewport.png`
- License decision evidence: `evidence/case_001/license.json`
