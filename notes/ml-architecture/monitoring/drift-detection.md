# Drift Detection in Production ML Systems

## 1. Introduction

Machine learning models assume that **training data and production data follow the same statistical distribution**.

In real-world systems, this assumption breaks over time due to:

* Changing user behavior
* Seasonal patterns
* New fraud strategies
* Product feature changes
* Data pipeline bugs

This phenomenon is called **data drift** or **concept drift**.

Without detecting drift, model performance will gradually degrade.

Example:

A fraud detection model trained in 2024 may fail in 2025 when fraudsters adopt new attack patterns.

---

# 2. Types of Drift

## 2.1 Data Drift (Feature Drift)

Occurs when **input feature distributions change**.

Example:

| Feature               | Training Mean | Production Mean |
| --------------------- | ------------- | --------------- |
| transaction_amount    | 1200          | 4200            |
| transactions_per_hour | 2.1           | 6.7             |

This indicates **behavior change in users**.

Example causes:

* economic changes
* seasonal behavior
* new product features
* data pipeline errors

---

## 2.2 Prediction Drift

Occurs when **model output distribution changes**.

Example:

Training prediction distribution:

```
Fraud probability mean = 0.12
```

Production prediction distribution:

```
Fraud probability mean = 0.34
```

Possible reasons:

* real fraud patterns changing
* feature drift
* model degradation
* data pipeline bugs

---

## 2.3 Concept Drift

Occurs when **relationship between features and labels changes**.

Example:

Previously:

```
High transaction frequency → fraud
```

Now:

```
Fraudsters mimic normal behavior
```

The feature relationship changes, so the model becomes inaccurate.

Concept drift is the **hardest type of drift to detect** because labels often arrive **late**.

---

# 3. Drift Detection Metrics

## 3.1 Population Stability Index (PSI)

PSI measures the difference between **two distributions**.

Example:

| PSI Score | Interpretation    |
| --------- | ----------------- |
| < 0.1     | No drift          |
| 0.1 – 0.2 | Moderate drift    |
| > 0.2     | Significant drift |

Example calculation flow:

```
Training distribution → bucketized
Production distribution → bucketized
Compute PSI across bins
```

PSI is widely used in **banking and fraud systems**.

---

## 3.2 KL Divergence

Measures how one probability distribution diverges from another.

Formula:

```
KL(P || Q) = Σ P(x) log(P(x) / Q(x))
```

Where:

* P = training distribution
* Q = production distribution

Higher values indicate **stronger drift**.

Used in:

* recommendation systems
* NLP models
* deep learning pipelines

---

## 3.3 Kolmogorov-Smirnov Test (KS Test)

Measures the maximum difference between two cumulative distributions.

```
KS = max|F_train(x) − F_prod(x)|
```

Advantages:

* non-parametric
* works well for continuous features

Commonly used for **feature monitoring pipelines**.

---

# 4. Drift Detection Pipeline Architecture

A typical ML platform implements drift detection using **batch jobs over logged production data**.

Architecture:

```
Prediction Service
      |
      v
Feature + Prediction Logging
      |
      v
Streaming Pipeline (Kinesis / Kafka)
      |
      v
Data Lake (S3)
      |
      v
Drift Detection Job (Spark / Glue)
      |
      v
Drift Metrics Stored
      |
      v
Monitoring Dashboard
```

---

# 5. AWS Implementation Example

Example architecture for drift detection.

```
Transaction API
      |
      v
Fraud Model Endpoint (SageMaker)
      |
      +----------------------------+
      |                            |
      v                            v

Prediction Logs               Feature Logs
(Kinesis Stream)              (Kinesis Stream)

      |                            |
      v                            v

             S3 Data Lake

                   |
                   v

       Daily Drift Detection Job
           (AWS Glue / Spark)

                   |
                   v

          Drift Metrics Store
            (DynamoDB)

                   |
                   v

      Monitoring Dashboard
        (CloudWatch / Grafana)
```

---

# 6. Example Drift Detection Code

Check drift_detection.py in weeks/week9

---

# 7. Monitoring Dashboard Metrics

Drift dashboards typically track:

| Metric                  | Description                  |
| ----------------------- | ---------------------------- |
| Feature PSI             | Drift in individual features |
| Prediction distribution | Output drift                 |
| Feature missing rate    | Pipeline failures            |
| Feature freshness       | Stale data detection         |

Example visualization:

```
Feature Drift Dashboard

transaction_amount PSI = 0.28 ⚠
transactions_per_hour PSI = 0.05 ✓
device_count PSI = 0.19 ⚠
```

---

# 8. Drift Response Strategy

Detecting drift is only useful if the system **responds automatically**.

Common responses:

### 1. Alert Engineers

```
PSI > 0.2
→ Slack alert
→ investigate feature pipeline
```

---

### 2. Trigger Model Retraining

```
Drift detected
      |
      v
Training pipeline triggered
      |
      v
Train new model
      |
      v
Evaluate against baseline
```

---

### 3. Deploy Updated Model

```
Model Registry
      |
      v
Canary Deployment
      |
      v
Full rollout if stable
```

---

# 9. Best Practices

1. Log **every prediction with features used**.
2. Monitor **feature distributions daily**.
3. Track **prediction distribution drift**.
4. Monitor **training vs serving feature skew**.
5. Automate **alerts and retraining pipelines**.
6. Store drift metrics historically for trend analysis.

---

# 10. Key Takeaway

Drift detection ensures that ML models remain **reliable after deployment**.

Production ML systems must continuously monitor:

* feature distributions
* prediction distributions
* model performance
* business KPIs

Without drift monitoring, **models silently fail in production**.
