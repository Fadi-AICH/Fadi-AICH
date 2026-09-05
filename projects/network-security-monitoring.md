# Network Security Monitoring — SELKS / Suricata / Cisco

> Cybersecurity internship project carried out at Tanger Med Port Authority (2025). This public case study is intentionally sanitized and omits internal infrastructure details.

## Objective

Build and validate an open-source Network Security Monitoring environment capable of observing mirrored traffic, detecting suspicious activity and supporting investigation through structured dashboards.

## Architecture

```text
Production-like network traffic
          |
      Cisco SPAN
          |
       SELKS VM
  /        |        \
Suricata  Zeek   Elasticsearch
   |                 |
 IDS/IPS            Kibana
   |                 |
Scirius rules   SOC dashboards
          \
          Honeypot telemetry
```

## What I implemented

- Deployed SELKS in Docker on Ubuntu.
- Integrated Suricata, Elasticsearch/Logstash/Kibana and Scirius.
- Reset and configured a Cisco switch for traffic visibility.
- Configured SPAN/mirroring so the monitoring sensor could inspect traffic.
- Worked with VLAN/trunk concepts and management hardening in the lab context.
- Simulated network scans, brute-force attempts and denial-of-service scenarios.
- Built a custom Kibana dashboard for alerts, logs and event correlation.
- Added a honeypot after a comparison/selection phase and correlated its telemetry with SELKS data.

## Validation

The lab demonstrated end-to-end visibility from network traffic capture through IDS detection, indexing and investigation. Suricata successfully detected controlled suspicious activity, while Kibana dashboards supported faster event review and correlation.

## Technologies

`SELKS` `Suricata` `Zeek` `Elasticsearch` `Logstash` `Kibana` `Scirius` `Docker` `Cisco` `SPAN` `IDS/IPS` `Honeypot` `Network Security Monitoring`

## Security / disclosure note

No credentials, raw employer data, sensitive internal addresses, production topology, proprietary configuration or operational screenshots are published here. The content is a recruiter-facing technical summary of the work performed.
