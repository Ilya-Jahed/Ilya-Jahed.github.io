---
layout: post
title: "Starting Research on Extending NegSC for NIDS"
date: 2026-08-10 12:00:00+0330
inline: false
related_posts: false
---

I've started working on extending the **NegSC (2024)** graph neural network framework as part of my research at the [Scalable Systems Lab](https://ssl.iust.ac.ir/) at IUST.

---

## What is NegSC?

NegSC is a graph-based anomaly detection method that models **negative (absent) interactions** between nodes alongside positive ones using **signed-graph convolutions**. It was published in 2024 and applied to fraud detection and network intrusion detection scenarios.

## What I'm Working On

My current work focuses on addressing key limitations in the original NegSC framework:

- **Dynamic graph modeling**: Better handling of temporal edge structures in network traffic
- **Class imbalance**: More robust training under the severe imbalance present in NIDS datasets
- **Dual node representation**: Improving how nodes are represented as both *source* and *destination* in network flows
- **Edge/distributed computing constraints**: Adapting the method for resource-constrained environments

## Baseline Reimplementations

As part of this work, I've reimplemented:
- [NegSC (fraud detection variant)](https://github.com/Ilya-Jahed/negsc-fraud-detection)
- [SL-GAD](https://github.com/Ilya-Jahed/sl-gad-reimplementation) — self-supervised contrastive graph anomaly detection
- [Anomal-E](https://github.com/Ilya-Jahed/Anomal-E-Implementation) — edge-centric flow anomaly detection

These form my benchmarking suite for comparing proposed improvements.


