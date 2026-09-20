---
layout: page
title: "NEGSC: Graph Anomaly Detection for NIDS — Reimplementation and Ongoing Work"
description: Modular reimplementation of the NEGSC (2024) paper on signed-graph convolutions for anomaly detection, serving as the foundation for ongoing private extension work on self-supervised NIDS.
img: assets/img/12.jpg
importance: 1
category: research
related_publications: false
---

## Overview

**NEGSC** is a graph neural network framework for anomaly detection published in 2024. It addresses how to model *negative* (absent or suppressed) interactions between nodes alongside positive ones, using **signed-graph convolutions**.

This repository contains a clean, modular reimplementation of the NEGSC framework, built as the foundation for ongoing research at the [Scalable Systems Lab](https://ssl.iust.ac.ir/) at IUST.

**GitHub:** [Ilya-Jahed/negsc-fraud-detection](https://github.com/Ilya-Jahed/negsc-fraud-detection)

---

## Research Journey

My work on graph-based NIDS has progressed through three stages:

1. **Anomal-E analysis and reimplementation** — I started by studying and modularising Anomal-E, an edge-centric self-supervised NIDS method. During this process I identified several implementation issues, including target-encoding leakage and preprocessing concerns, which informed my later work.

2. **SL-GAD study** — I then reimplemented SL-GAD, a node-centric self-supervised graph anomaly detection method. While this approach is less suitable for NIDS (which typically requires edge- or flow-level analysis), it provided useful insights into contrastive learning on graphs.

3. **NEGSC reimplementation and extension** — I analysed the NEGSC paper and built a modular reimplementation. Upon auditing the original approach, I identified several issues and began developing extensions. The active extension work is currently **private and incomplete**; only the modular reimplementation is public.

---

## Current Status

The public repository contains the audited and modularised NEGSC reimplementation. The extension work — including additional ideas and architectural modifications — is under active development in a private repository. The final method, experimental protocol, and results have **not yet been finalised or claimed**.

---

## Stack

- Python · PyTorch · PyTorch Geometric
- Datasets: benchmark NIDS / fraud graph datasets


