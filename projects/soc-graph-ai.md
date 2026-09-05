# SOC Graph AI — Detection, Correlation & Automated Response

> Final-year engineering project completed in a controlled lab environment during a cybersecurity internship at NearSecure, Rabat (2026).

## Objective

Design and validate an end-to-end SOC workflow that turns raw security telemetry into analyst-ready evidence by combining SIEM detection, enrichment, graph-based investigation, ML/UEBA prioritization, adversary emulation and SOAR workflows.

## Architecture

```text
Windows / Linux / pfSense telemetry
            |
          Wazuh
            |
      JSONL alert export
            |
      Python enrichment
       /            \
MITRE mapping     UEBA / ML scoring
       \            /
          Neo4j graph
              |
       Streamlit analyst view
              |
        n8n / Shuffle SOAR
              |
      triage + notification
```

## What I implemented

- Wazuh SIEM/XDR lab with Windows, Linux and firewall telemetry.
- Custom detection rules and structured alert export.
- Python enrichment pipeline for normalized security events.
- MITRE ATT&CK mapping and adversary-emulation validation.
- Neo4j investigation graph linking alerts, hosts, users, processes, rules and techniques.
- UEBA / ML scoring to help prioritize analyst attention.
- Streamlit dashboard for investigation and attack-story visualization.
- n8n and Shuffle workflows for controlled triage and notification.
- pfSense log ingestion and firewall-event validation.

## Validation

The prototype was tested through **12 controlled attack scenarios** and additional adversary emulation using **Atomic Red Team** and **MITRE Caldera**. The resulting workflow produced and processed **1,400+ normalized/enriched alerts** in the project validation environment.

## Technologies

`Wazuh` `Python` `Neo4j` `MITRE ATT&CK` `Atomic Red Team` `Caldera` `Streamlit` `n8n` `Shuffle` `pfSense` `Sysmon` `UEBA` `Machine Learning`

## Security / disclosure note

This public case study intentionally omits credentials, raw internal data, employer-sensitive configuration, exact private infrastructure details and non-public screenshots. It summarizes the engineering work and validated results without exposing operational information.
