---
layout: page
title: "NegSC: Graph Anomaly Detection for Fraud & NIDS"
description: Reimplementation of the NegSC (2024) paper â€” GNN-based anomaly detection using negative sampling and signed-graph convolutions, applied to network intrusion detection and fraud detection.
img: assets/img/12.jpg
importance: 1
category: research
related_publications: false
---

## Overview

**NegSC** is a graph neural network framework for anomaly detection that was published in 2024. It addresses a core challenge in graph-based NIDS and fraud detection: how to model *negative* (absent or suppressed) interactions between nodes alongside positive ones, using **signed-graph convolutions**.

This repository contains my clean, documented reimplementation of the NegSC framework, built as the foundation for my ongoing research at the [Scalable Systems Lab](https://ssl.iust.ac.ir/) at IUST.

**GitHub:** [Ilya-Jahed/negsc-fraud-detection](https://github.com/Ilya-Jahed/negsc-fraud-detection)

---

## Why NegSC?

Traditional GNN-based anomaly detectors aggregate neighbor features through positive edges only. NegSC argues that **the absence or negation of an edge carries information** â€” two nodes that *don't* interact in a normally well-connected neighborhood become a signal. The method introduces:

- **Negative sampling** during graph construction to explicitly model non-edges
- **Signed convolutions** that treat positive and negative edges with separate learnable parameters
- A **dual-view representation** capturing both source-side and destination-side node behaviors

---

## Research Context

This reimplementation serves as the foundation for my extension work, which targets key limitations of NegSC:

- Better representation of **dynamic** graph topologies (temporal edges)
- Improved handling of **class imbalance** in NIDS datasets
- Adaptation to **edge and distributed computing** constraints (lightweight inference)

---

## Stack

- Python Â· PyTorch Â· PyTorch Geometric
- Datasets: benchmark NIDS / fraud graph datasets


