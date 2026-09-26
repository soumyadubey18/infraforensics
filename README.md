# 🔍 INFRAFORENSICS

### Infrastructure State Reconstruction & Incident Forensics Platform

> **Know what changed. Know when it changed. Know the infrastructure state.**

INFRAFORENSICS is a Python-based infrastructure forensics platform that captures system state over time, stores historical snapshots, generates Infrastructure DNA fingerprints, detects state changes, and classifies changes by severity.

The project is being built incrementally with a focus on:

- Infrastructure state history
- Change detection
- Infrastructure DNA
- Incident forensics
- Evidence-based investigation
- Explainable infrastructure analysis

---

# 🎯 Problem

When an infrastructure incident occurs, one of the most important questions is:

> **"What changed before the incident?"**

Traditional monitoring can show the current health of a system, but historical state reconstruction can be difficult.

INFRAFORENSICS aims to preserve infrastructure state over time so that changes can later be investigated.

---

# 🧠 Current Architecture

```text
                INFRAFORENSICS
                      │
                      ▼
              System Collector
                      │
                      ▼
             System Snapshot
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
       SQLite              Infrastructure DNA
          │                       │
          └───────────┬───────────┘
                      ▼
              Historical State
                      │
                      ▼
              DNA Comparison
                      │
              ┌───────┴───────┐
              ▼               ▼
           CHANGED         UNCHANGED
              │
              ▼
        Change Detection
              │
              ▼
       Severity Classification