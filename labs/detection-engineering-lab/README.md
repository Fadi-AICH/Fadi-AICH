# Detection Engineering Lab

A compact defensive-security lab for building and documenting detections across **Sigma, Wazuh and Suricata**, with **MITRE ATT&CK** mappings and controlled validation notes.

> This repository content is designed for defensive research and lab validation only.

## Objectives

- write portable detection logic
- map detections to ATT&CK techniques
- document telemetry requirements
- reduce false positives through tuning notes
- validate rules against controlled test activity

## Structure

```text
labs/detection-engineering-lab/
├── README.md
├── sigma/
│   └── suspicious-powershell-download.yml
├── wazuh/
│   └── local_rules.xml
├── suricata/
│   └── suspicious-dns.rules
└── mitre/
    └── coverage.md
```

## Current detections

| Detection | Engine | ATT&CK | Purpose |
|---|---|---|---|
| Suspicious PowerShell download behavior | Sigma | T1059.001 / T1105 | Flag common download-and-execute behavior |
| Suspicious PowerShell execution | Wazuh | T1059.001 | Detect encoded/hidden PowerShell usage |
| Unusually long DNS queries | Suricata | T1071.004 | Surface potential DNS tunneling indicators |

## Validation approach

Each rule should be tested against:

1. expected benign activity
2. controlled suspicious activity
3. noisy edge cases
4. event fields actually available in telemetry
5. ATT&CK mapping consistency

## Roadmap

- add Windows persistence detections
- add credential-access detections
- add Linux privilege-escalation detections
- add rule test fixtures
- add false-positive notes and tuning guidance
- add a simple CI validation workflow for rule syntax
