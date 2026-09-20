---
layout: page
title: "Anomal-E: Edge-Centric Graph Anomaly Detection (Implementation)"
description: Implementation of Anomal-E â€” an edge-centric GNN approach for anomaly detection in network traffic, treating each network flow as a graph edge with rich feature information.
img: assets/img/7.jpg
importance: 3
category: research
related_publications: false
---

## Overview

**Anomal-E** is a graph-based anomaly detection method designed for **network traffic analysis**. Unlike node-centric GNN methods, Anomal-E treats each **network flow as an edge**, with rich per-flow features (protocol, bytes, flags, etc.). The GNN then learns to detect edges (flows) that are anomalous given the neighborhood context.

**GitHub:** [Ilya-Jahed/Anomal-E-Implementation](https://github.com/Ilya-Jahed/Anomal-E-Implementation)

---

## Key Ideas

- **Edge-centric perspective**: Flows (not hosts) are the primary unit of analysis
- **Line graph transformation**: Converts the edge-centric problem into a node-centric one by building a *line graph* where each original edge becomes a node
- **GNN on line graph**: Standard message-passing is applied on this transformed graph
- **Unsupervised anomaly scoring**: Detects anomalies without requiring labeled attack data

---

## Relevance to My Research

Anomal-E offers a complementary perspective to NegSC: where NegSC focuses on *node* behavior in signed graphs, Anomal-E focuses on *edge* (flow) behavior. Comparing both provides insight into the design space for NIDS graph anomaly detection.

---

## Stack

- Python Â· PyTorch Â· PyTorch Geometric Â· PCAP processing tools


