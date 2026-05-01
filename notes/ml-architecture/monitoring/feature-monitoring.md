# Feature Monitoring

# Overview

Feature monitoring is a critical component of production ML systems. Even when model performance metrics look stable, underlying input features may drift, degrade, or break — eventually leading to model failure.

Feature monitoring focuses on:

* Data Drift
* Feature Quality
* Feature Distribution Changes
* Feature Availability
* Feature Freshness
* Feature Correlation Changes

---

# Why Feature Monitoring Matters

Model Monitoring Alone is Not Enough

Example:

* Model accuracy looks stable
* But input feature distributions slowly change
* Model eventually starts failing silently

This is called **Silent Model Degradation**

Feature monitoring helps detect problems **before** model performance degrades.

---

# Types of Feature Monitoring

# 1. Data Drift Monitoring

Detects when feature distributions change between:

* Training data
* Production data

Common Causes:

* Seasonality
* User behavior change
* Product changes
* Upstream pipeline bugs

Example:

Fraud Model Feature:

Training:

Average transaction amount = 2,000 INR

Production:

Average transaction amount = 12,000 INR

This indicates potential drift.

---

# Drift Detection Techniques

## Population Stability Index (PSI)

PSI measures distribution shift between two datasets.

Typical Thresholds:

* PSI < 0.1 → No Drift
* 0.1 – 0.25 → Moderate Drift
* > 0.25 → Significant Drift

Use PSI For:

* Numerical features
* Score monitoring

---

## Kolmogorov‑Smirnov Test (KS Test)

Measures maximum distance between two distributions.

Used For:

* Continuous features

---

## Jensen‑Shannon Divergence

Measures similarity between probability distributions.

Used For:

* Feature drift detection

---

# 2. Feature Quality Monitoring

Monitor feature quality issues:

## Missing Values

Example:

User Age Feature

Training:

Missing = 2%

Production:

Missing = 35%

Indicates pipeline issue.

---

## Outliers

Example:

Transaction Amount

Normal Range:

0 - 50,000

Production Suddenly:

Max = 10,000,000

Indicates bug or fraud.

---

## Data Type Changes

Example:

Training:

Age = Integer

Production:

Age = String

This breaks model inference.

---

# 3. Feature Freshness Monitoring

Important for:

* Real‑time models
* Streaming systems

Example:

Feature: Last Login Time

Expected:

Updated every 5 minutes

Actual:

Last updated 3 hours ago

Model predictions become stale.

---

# 4. Feature Availability Monitoring

Checks whether features are arriving on time.

Example:

Feature Store Expected:

100 Features

Received:

87 Features

Model may still run but accuracy degrades.

---

# 5. Feature Correlation Monitoring

Feature relationships change over time.

Example:

Training:

Income ↔ Spending (Strong Correlation)

Production:

Income ↔ Spending (Weak Correlation)

Indicates behavioral shift.

---

# 6. Feature Importance Monitoring

Monitor top features over time.

If important features change suddenly:

* Model may be learning noise
* Data pipeline issue

Example:

Training Top Feature:

Transaction Frequency

Production Top Feature:

Random ID column

This is a red flag.

---

# Feature Monitoring Architecture

Data Flow:

```
Production Data
     |
Feature Extractor
     |
Feature Monitoring Service
     |
Drift Detection
     |
Alerting System
     |
Dashboard
```

---

# What to Monitor Per Feature

For Each Feature:

* Mean
* Median
* Std Dev
* Min
* Max
* Missing %
* Distribution
* Drift Score

---

# Example Monitoring Table

| Feature           | Mean | Missing % | Drift Score | Status |
| ----------------- | ---- | --------- | ----------- | ------ |
| Age               | 35   | 2%        | 0.05        | OK     |
| Income            | 85K  | 15%       | 0.28        | ALERT  |
| Transaction Count | 5    | 1%        | 0.03        | OK     |

---

# Monitoring Frequency

Depends on Use Case

Real‑time Fraud Model

* Every 5 minutes

Recommendation Model

* Hourly

Batch Model

* Daily

---

# Feature Monitoring Tools

Open Source

* Evidently AI
* WhyLabs
* Great Expectations
* Prometheus

Cloud Tools

* AWS SageMaker Model Monitor
* Azure ML Monitoring
* GCP Vertex AI Monitoring

---

# Example Python Feature Drift Monitoring

```python
import numpy as np
import pandas as pd

def calculate_psi(expected, actual, bins=10):
    breakpoints = np.linspace(0, 100, bins + 1)

    expected_perc = np.percentile(expected, breakpoints)
    actual_perc = np.percentile(actual, breakpoints)

    psi = np.sum((actual_perc - expected_perc) * np.log(actual_perc / expected_perc))

    return psi
```

---

# Alerting Strategy

When Drift Detected:

* Send Slack Alert
* Create PagerDuty Alert
* Trigger Retraining Pipeline

Example:

```
ALERT: Feature Drift Detected
Feature: Transaction Amount
PSI: 0.31
Severity: High
```

---

# Best Practices

Monitor:

* All input features
* Model predictions
* Feature importance

Start With:

* Top 10 important features

Then expand.

---

# Common Mistakes

Monitoring Only Model Accuracy

Ignoring:

* Feature Drift
* Data Quality
* Missing Values

This leads to production failures.

---

# Production Example

Fraud Detection System

Features:

* Transaction Amount
* Device Type
* Location
* Transaction Frequency

Monitoring Detects:

Device Type Distribution Changed

Cause:

New Mobile App Released

Action:

Retrain Model

---

# Final Production Architecture

```
Data Pipeline
     |
Feature Store
     |
Feature Monitoring
     |
Model Inference
     |
Model Monitoring
     |
Alerting
```

---

# Next Step

Next File:

model-performance-monitoring.md

---

# Summary

Feature Monitoring Detects:

* Data Drift
* Feature Quality Issues
* Pipeline Failures
* Behavioral Changes

This prevents:

Silent Model Failures

---

# End
