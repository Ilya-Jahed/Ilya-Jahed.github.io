---
layout: page
title: "Kernel to Provenance: Systems Security Notes"
description: Study notes tracing from OS kernel audit mechanisms to provenance graph construction and graph-based threat detection â€” covering audit systems, provenance-based NIDS, and threat hunting.
img: assets/img/11.jpg
importance: 2
category: notes
related_publications: false
---

## Overview

Notes documenting my study of the systems security literature, from **OS kernel audit mechanisms** to **provenance graph construction** and graph-based intrusion detection.

**GitHub:** [Ilya-Jahed/kernel-to-provenance-notes](https://github.com/Ilya-Jahed/kernel-to-provenance-notes)

---

## What is a Provenance Graph?

A **provenance graph** is a directed acyclic graph (DAG) recording the causal history of system events:
- **Nodes**: processes, files, network sockets, users
- **Edges**: system calls (read, write, connect, fork, exec, â€¦) with timestamps

Provenance graphs capture *what happened, to what, by whom, and when* â€” making them powerful for **threat hunting** and **APT detection**.

---

## Topics Covered

- **OS Audit Subsystems** â€” Linux Audit, ETW (Windows), DTrace, eBPF
- **Provenance Graph Construction** â€” parsing audit logs, handling noise
- **Graph-based Threat Detection** â€” anomaly detection on provenance graphs, attack pattern matching
- **Key Papers** â€” WATSON, MORSE, UNICORN, SHADEWATCHER, ProvDetector
- **Scalability Challenges** â€” provenance explosion, graph partitioning, streaming processing

---

## Motivation

Understanding provenance-based detection provides essential context for NIDS research â€” both domains build graphs from system/network events, and many architectural ideas transfer directly.


