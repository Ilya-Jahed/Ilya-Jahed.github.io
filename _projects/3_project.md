---
layout: page
title: "Anomal-E: Edge-Centric Graph Anomaly Detection (Analysis and Reimplementation)"
description: Analysis and modular reimplementation of Anomal-E, an edge-centric self-supervised GNN method for anomaly detection in network traffic.
img: assets/img/Anomal-E.jpg
importance: 3
category: research
related_publications: false
---

## Overview

**Anomal-E** is a self-supervised graph neural network approach for network anomaly detection. It treats network flows as graph edges with rich flow-level features, rather than reducing the problem to node-level detection.

**GitHub:** [Ilya-Jahed/Anomal-E-Implementation](https://github.com/Ilya-Jahed/Anomal-E-Implementation)

## What I Did

I began my graph-based NIDS research by analysing the paper and reimplementing its source code. I then reorganised the implementation into modular components so that the data pipeline, graph construction, encoder, self-supervised objective, anomaly detectors, and evaluation could be inspected independently.

During the audit, I identified implementation and preprocessing concerns, including issues around **target encoding** and the separation between training-time information and evaluation labels. These observations helped shape my later approach to auditing and extending other graph-based NIDS methods.

## Technical Perspective

- **Edge-centric modelling:** network flows are represented as graph edges
- **Self-supervised training:** the encoder is trained without attack labels
- **DGI-style representation learning:** real and corrupted graph views are contrasted
- **Unsupervised scoring:** learned embeddings are passed to anomaly detectors
- **Modular research code:** preprocessing, graph construction, modelling, training, and evaluation are separated

## Role in My Research Path

Anomal-E established my initial flow-level perspective on graph-based NIDS. It also made clear how strongly conclusions depend on preprocessing choices, information leakage controls, and a careful separation between unsupervised training and labelled evaluation. These lessons informed my subsequent study of SL-GAD and NEGSC.

This repository documents an implementation and research-training project. It is not presented as a new published method or as a claim that the original paper has been fully reproduced under every experimental condition.

## Stack

- Python · PyTorch · DGL
- NetFlow data · graph neural networks · self-supervised learning


