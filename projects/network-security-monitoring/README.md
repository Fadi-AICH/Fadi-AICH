# Network Security Monitoring — SELKS / Suricata / Cisco

> Sanitized case study based on a 2025 network-security internship project. No employer-internal topology, credentials, private addresses or proprietary operational data are published here.

## Goal

Deploy a practical **Network Security Monitoring** environment capable of collecting mirrored network traffic, detecting suspicious activity, visualizing events and supporting investigation using open-source tooling.

## Architecture

```text
Production-like network traffic
          |
          v
   Cisco switch / SPAN
          |
          v
       SELKS host
   +----------------+
   | Suricata IDS   |
   | Zeek telemetry |
   | Elasticsearch  |
   | Logstash       |
   | Kibana         |
   | Scirius        |
   +----------------+
          |
          v
 Detection + indexing + dashboards
          |
          +--> controlled scan / brute-force / DoS validation
          |
          +--> honeypot telemetry for additional observations
```

## What was implemented

- SELKS deployment in a Dockerized Ubuntu environment
- Suricata-based IDS/IPS monitoring
- Elasticsearch / Logstash / Kibana pipeline for indexing and investigation
- Scirius for Suricata rule governance
- Cisco switch reset/configuration and SPAN-based traffic mirroring
- network-segmentation and monitoring-oriented configuration work
- custom Kibana dashboards for alert/log analysis
- controlled attack simulations to validate detection behavior
- honeypot extension after a comparison/selection phase

## Validation scenarios

The monitoring stack was tested with controlled traffic including:

- network scans
- brute-force attempts
- denial-of-service traffic

The resulting events were inspected in Suricata/Elastic/Kibana to verify visibility, alert generation and correlation.

## Investigation workflow

```text
Packet / flow visibility
      -> Suricata detection
      -> event indexing
      -> Kibana investigation
      -> rule tuning / correlation
      -> analyst interpretation
```

## Engineering lessons

- SPAN/mirroring design determines what the sensor can actually see.
- IDS/IPS value comes from both detection quality and usable investigation context.
- Dashboards should support analyst questions rather than simply display many charts.
- Rule governance and tuning are necessary to keep alerting useful over time.
- Honeypot data can enrich monitoring, but must be interpreted separately from ordinary production traffic.

## Technologies

`SELKS` · `Suricata` · `Zeek` · `Elasticsearch` · `Logstash` · `Kibana` · `Scirius` · `Docker` · `Cisco` · `SPAN` · `IDS/IPS` · `Linux`

## Public version scope

This page describes the project at a portfolio level. Detailed internal network information and employer-specific configuration have intentionally been excluded.

The complete internship report remains private.