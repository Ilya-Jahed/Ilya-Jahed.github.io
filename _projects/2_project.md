---
layout: page
title: "SL-GAD: Self-supervised Graph Anomaly Detection (Reimplementation)"
description: Reimplementation of SL-GAD â€” a self-supervised, contrastive-learning-based method for detecting anomalous nodes in attributed graphs.
img: assets/img/3.jpg
importance: 2
category: research
related_publications: false
---

## Overview

**SL-GAD** (Self-supervised Learning for Graph Anomaly Detection) uses **contrastive learning** â€” learning representations by contrasting augmented views of a graph â€” to detect nodes that are anomalous with respect to their local neighborhood structure.

This is a clean reimplementation with documented experiments, built for benchmarking against other methods in my research.

**GitHub:** [Ilya-Jahed/sl-gad-reimplementation](https://github.com/Ilya-Jahed/sl-gad-reimplementation)

---

## Key Ideas

- **Self-supervised pre-training**: No anomaly labels needed at training time
- **Contrastive objective**: Maximizes agreement between differently augmented views of the same node's neighborhood
- **Anomaly scoring**: Nodes whose representations are *inconsistent* across views are flagged as anomalies
- **Attributed graphs**: Works on graphs with both structural (edge) and feature (attribute) information

---

## Why Reimplementation?

Reimplementing published methods is essential for:
1. **Verifying reproducibility** of published results
2. Building a **clean, modular baseline** to extend and compare against
3. Deeply understanding the method's assumptions and failure modes

This reimplementation closely follows the original paper and includes ablation experiments.

---

## Stack

- Python Â· PyTorch Â· PyTorch Geometric Â· NetworkX


