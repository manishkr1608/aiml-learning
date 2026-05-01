# Model Performance Monitoring

# Overview

Model Performance Monitoring ensures that machine learning models continue to perform well after deployment. Unlike traditional software, ML models degrade over time due to:

* Data Drift
* Concept Drift
* Prediction Drift
* Feature Pipeline Issues
* Infrastructure Problems

Without monitoring, models silently fail and cause business impact.

---

# What Should Be Monitored

Model monitoring should be divided into 5 layers:

1. Data Monitoring
2. Prediction Monitoring
3. Performance Monitoring
4. Drift Monitoring
5. Business KPI Monitoring

---

# 1. Data Monitoring

Monitor incoming data quality.

## Metrics

### Missing Values

* % Missing per feature
* Sudden spike detection

Example:

| Feature | Yesterday | Today |
| ------- | --------- | ----- |
| income  | 1%        | 25%   |

Alert: Feature pipeline broken

---

### Feature Distribution

Compare training vs production

Methods:

* PSI (Population Stability Index)
* KL Divergence
* Histogram comparison

Example:

Age distribution changed from:

20–40 → 70%

To:

40–60 → 65%

Model may degrade.

---

### Data Range Validation

Example:

| Feature | Expected | Observed |
| ------- | -------- | -------- |
| Age     | 18–80    | 5–120    |

Alert: Bad input data

---

# 2. Prediction Monitoring

Monitor model outputs

## Metrics

### Prediction Distribution

Example:

Fraud Model

| Day | Fraud Rate |
| --- | ---------- |
| Mon | 2%         |
| Tue | 35%        |

Alert: Model malfunction

---

### Confidence Score Monitoring

Example:

Confidence suddenly drops:

0.85 → 0.52

Model uncertain about predictions

---

### Prediction Volume

Example:

Expected: 50k predictions

Actual: 5k predictions

Alert: Pipeline broken

---

# 3. Model Performance Monitoring

This requires Ground Truth (Actual Labels)

## Metrics

### Classification Models

Monitor:

* Accuracy
* Precision
* Recall
* F1 Score
* AUC

Example:

| Metric   | Training | Production |
| -------- | -------- | ---------- |
| Accuracy | 92%      | 78%        |

Alert: Model degradation

---

### Regression Models

Monitor:

* RMSE
* MAE
* MAPE

Example:

RMSE increased:

12 → 28

Alert: Model drift

---

# 4. Drift Monitoring

## Data Drift

Input data distribution changes

Example:

COVID period changed spending behavior

Model trained on old data fails

---

## Concept Drift

Relationship between input and output changes

Example:

Before:

High income → Low default

After:

High income → High default

Model becomes inaccurate

---

## Prediction Drift

Model output distribution changes

Example:

Fraud predictions:

2% → 18%

Alert triggered

---

# 5. Business KPI Monitoring

Most Important Layer

Example:

Recommendation Model

Monitor:

* Click Through Rate
* Conversion Rate
* Revenue

Example:

CTR dropped:

5% → 2%

Business impact detected

---

# Monitoring Architecture

Typical Architecture

```
Production Data
     ↓
Prediction Service
     ↓
Monitoring Collector
     ↓
Metrics Store
     ↓
Dashboard
     ↓
Alerting
```

---

# Tools for Monitoring

## Open Source

* Evidently AI
* WhyLabs
* Prometheus
* Grafana
* MLflow

---

## Cloud

AWS:

* SageMaker Model Monitor
* CloudWatch

Azure:

* Azure ML Monitoring

---

# Alerting Strategy

Example:

| Metric        | Threshold |
| ------------- | --------- |
| PSI           | >0.2      |
| Accuracy Drop | >5%       |
| Missing Data  | >10%      |

Trigger Alerts:

* Slack
* Email
* PagerDuty

---

# Monitoring Frequency

Real‑Time Models

* Fraud Detection
* Recommendation

Monitor: Real-time

Batch Models

* Credit scoring
* Forecasting

Monitor: Daily / Weekly

---

# Production Monitoring Dashboard

Typical Dashboard

* Model Accuracy Trend
* Drift Metrics
* Prediction Volume
* Business KPIs
* Data Quality Metrics

---

# Example: Fraud Model Monitoring

Monitor:

Data

* Transaction Amount
* Country

Prediction

* Fraud rate

Performance

* Recall

Business

* Fraud loss

---

# Best Practices

Always Monitor:

* Data
* Predictions
* Performance
* Business Metrics

Never rely on accuracy alone.

Monitor end‑to‑end.

---

# Production Readiness Checklist

Before Deploying Model

* Monitoring added
* Alerts configured
* Dashboard created
* Retraining strategy defined

---
