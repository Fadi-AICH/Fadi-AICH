# MITRE ATT&CK Coverage

| Technique | Name | Detection | Telemetry |
|---|---|---|---|
| T1059.001 | PowerShell | Sigma + Wazuh | Windows process creation / Sysmon |
| T1105 | Ingress Tool Transfer | Sigma | Windows process creation |
| T1071.004 | DNS | Suricata | DNS network traffic |

## Notes

This matrix tracks what each rule is intended to surface, not guaranteed prevention or complete ATT&CK coverage. Every detection should be validated with controlled telemetry before use in production.
