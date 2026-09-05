# SOC Graph AI — Detection, Correlation & Automated Response

> Sanitized case study based on a controlled cybersecurity lab completed during a 2026 internship. No employer-internal infrastructure, credentials, private addresses or proprietary configurations are published here.

## Goal

Build a defensible SOC workflow that goes beyond raw alert collection and demonstrates the full chain from **controlled adversary activity** to **detection, enrichment, correlation, prioritization, analyst investigation and response orchestration**.

## Architecture

```text
Controlled attack activity
        |
        v
Windows / Linux endpoints + pfSense telemetry
        |
        v
      Wazuh
 SIEM / XDR layer
        |
        v
JSONL export + Python enrichment
        |
        +--> MITRE ATT&CK mapping
        +--> UEBA / ML scoring
        +--> normalization & risk features
        |
        v
      Neo4j
 graph investigation
        |
        v
    Streamlit
 analyst dashboard
        |
        v
 n8n / Shuffle SOAR
 triage + notification
```

## What was implemented

- Wazuh-based SOC lab with Windows and Linux endpoint telemetry
- custom/local detection logic and structured alert export
- Python pipeline for normalization, enrichment and analytic scoring
- MITRE ATT&CK mapping for adversary behavior
- Neo4j graph model linking alerts, hosts, users, processes, rules and ATT&CK techniques
- UEBA / ML-assisted prioritization to support analyst triage
- Streamlit views for graph exploration and analyst-oriented restitution
- n8n and Shuffle workflows for controlled SOAR orchestration
- pfSense firewall telemetry integrated into the monitoring chain

## Validation

The prototype was tested in an isolated lab with:

- **12 controlled attack scenarios**
- **Atomic Red Team** techniques
- **MITRE Caldera** adversary emulation
- more than **1,400 alerts** normalized and enriched during validation

Examples of validated behavior included reconnaissance, PowerShell/LOLBins activity, persistence, credential-access attempts, discovery, collection and scheduled-task activity.

## Why Graph AI?

Traditional alert views often isolate events from their context. The graph layer was used to connect entities such as:

```text
Host <-> User <-> Process <-> Alert <-> Rule <-> ATT&CK Technique
```

This made it possible to investigate relationships and prioritize evidence instead of treating each alert as an isolated record.

## Security engineering lessons

- Detection quality depends heavily on telemetry quality and normalization.
- ATT&CK coverage should be demonstrated with evidence, not assumed from rule names.
- ML/UEBA scores are decision-support signals, not automatic truth.
- SOAR workflows should remain controlled and auditable; destructive actions should not be automated without explicit approval.
- A useful SOC prototype must preserve evidence and help the analyst explain *why* an alert matters.

## Technologies

`Wazuh` · `Python` · `Neo4j` · `Streamlit` · `MITRE ATT&CK` · `Atomic Red Team` · `MITRE Caldera` · `n8n` · `Shuffle` · `pfSense` · `Windows` · `Linux`

## Public version scope

This repository intentionally documents the **engineering approach, architecture, validation method and lessons learned** rather than publishing raw employer material or sensitive lab configuration.

The full internship report remains private.