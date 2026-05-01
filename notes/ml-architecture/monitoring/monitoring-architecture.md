# Monitoring Architecture for Production ML Systems

## 1. Why Monitoring is Critical

Deploying a model is not the end of the ML lifecycle.
Once in production, models can degrade due to:

* **Data drift** – input data distribution changes
* **Prediction drift** – model outputs change
* **Concept drift** – relationship between features and labels changes
* **Infrastructure failures** – latency, outages
* **Feature pipeline failures**

Without monitoring, these problems remain invisible until **business KPIs drop**.

Example:
A fraud detection model that initially detects 95% of fraud may degrade to 70% detection due to new fraud patterns.

---

# 2. Monitoring Layers in an ML System

Production ML systems require **five layers of monitoring**.

```
                +-----------------------+
                |   Business Metrics    |
                | (Fraud rate, churn)   |
                +-----------+-----------+
                            |
                +-----------v-----------+
                |   Model Performance   |
                | (Accuracy, Recall)    |
                +-----------+-----------+
                            |
                +-----------v-----------+
                |   Prediction Drift    |
                | (Output distribution) |
                +-----------+-----------+
                            |
                +-----------v-----------+
                |     Data Drift        |
                | (Feature distribution)|
                +-----------+-----------+
                            |
                +-----------v-----------+
                | Infrastructure Health |
                | (Latency, errors)     |
                +-----------------------+
```

---

# 3. Infrastructure Monitoring

This monitors **system reliability**.

### Key Metrics

| Metric               | Description          |
| -------------------- | -------------------- |
| API latency          | Model inference time |
| Error rate           | Failed predictions   |
| Throughput           | Requests per second  |
| Resource utilization | CPU, memory          |

### AWS Example

```
Client → API Gateway → Lambda / Model Endpoint → Feature Store
```

Monitoring tools:

* **CloudWatch**
* **Prometheus**
* **Grafana**

Example alerts:

```
Alert if:
p95 latency > 200ms
error rate > 2%
```

---

# 4. Data Drift Monitoring

Data drift occurs when **feature distributions change over time**.

Example:

| Feature               | Training Mean | Production Mean |
| --------------------- | ------------- | --------------- |
| transaction_amount    | 1200          | 3500            |
| transactions_per_hour | 2.1           | 6.5             |

This indicates **behavior shift**.

### Detection Methods

Common techniques:

* Population Stability Index (PSI)
* KL Divergence
* Kolmogorov-Smirnov Test

Example:

```
PSI < 0.1 → Stable
PSI 0.1–0.2 → Moderate drift
PSI > 0.2 → Significant drift
```

### Implementation

```
Prediction Service
      |
      v
Feature Logging (Kinesis)
      |
      v
S3 Data Lake
      |
      v
Daily Drift Job (Spark / Lambda)
```

Outputs:

```
Drift Report
Alert if PSI > threshold
```

---

# 5. Prediction Drift Monitoring

Prediction drift monitors **model output distribution**.

Example:

Fraud model predictions.

Training:

```
Fraud probability mean = 0.12
```

Production:

```
Fraud probability mean = 0.35
```

Possible causes:

* Fraud patterns changing
* Feature pipeline bug
* Model degradation

Implementation:

```
Predictions → Kinesis Stream
             ↓
         S3 Data Lake
             ↓
      Drift Detection Job
```

Metrics monitored:

* Prediction probability histogram
* Positive prediction rate
* Confidence scores

---

# 6. Model Performance Monitoring

This is the **most important monitoring layer**.

However labels are **delayed**.

Example:

Fraud labels arrive after **30 days**.

```
Prediction → Stored
Label arrives later
→ Join prediction + label
→ Compute metrics
```

Metrics:

| Metric    | Use                  |
| --------- | -------------------- |
| Precision | Fraud correctness    |
| Recall    | Fraud detection rate |
| F1 Score  | Balanced performance |
| ROC-AUC   | Model discrimination |

Example alert:

```
Recall < 85% → retrain model
```

---

# 7. Feature Pipeline Monitoring

Feature pipelines break frequently.

Common issues:

* Missing features
* Feature skew
* Feature freshness problems

Example:

Training feature:

```
avg_transactions_24h
```

Production feature:

```
avg_transactions_12h
```

This causes **training-serving skew**.

Monitoring checks:

```
Feature completeness
Feature freshness
Feature schema validation
```

---

# 8. Business KPI Monitoring

Ultimately the business cares about **business outcomes**.

Example metrics:

| Use Case         | KPI                 |
| ---------------- | ------------------- |
| Fraud detection  | Fraud loss          |
| Churn prediction | Customer churn rate |
| Recommendations  | CTR                 |

Example alert:

```
Fraud losses increase by 20%
→ investigate model performance
```

---

# 9. End-to-End Monitoring Architecture (AWS Example)

```
                   +-------------------+
                   |   API Gateway     |
                   +---------+---------+
                             |
                             v
                   +-------------------+
                   | Fraud Model API   |
                   | (SageMaker)       |
                   +---------+---------+
                             |
         +-------------------+-------------------+
         |                                       |
         v                                       v

Prediction Logs                         Feature Logs
(Kinesis Stream)                        (Kinesis Stream)

         |                                       |
         v                                       v

       S3 Data Lake ----------------------+
                |                         |
                v                         v

       Drift Detection Job          Label Join Job
       (Spark / Glue)               (Batch)

                |                         |
                v                         v

        Drift Metrics                Model Metrics
                |                         |
                +-----------+-------------+
                            |
                            v

                    Monitoring Dashboard
                    (Grafana / CloudWatch)

                            |
                            v

                         Alerts
                  (Slack / PagerDuty)


---

# 10. Automated Retraining Pipeline

Monitoring should trigger retraining.

Example flow:

```
Drift detected
       |
       v
Trigger training pipeline
       |
       v
Train new model
       |
       v
Evaluate
       |
       v
Deploy if performance improved
```

AWS example:

```
CloudWatch Alert
      ↓
Step Functions
      ↓
SageMaker Training
      ↓
Model Registry
      ↓
Deployment
```

---

# 11. Best Practices

1. Log **every prediction**.
2. Store **feature values used for prediction**.
3. Monitor **data drift and prediction drift separately**.
4. Track **training vs production feature distributions**.
5. Automate **retraining triggers**.
6. Build **central monitoring dashboards**.

---

# 12. Key Takeaway

A production ML system is **not just a model**.

It is an **observability system** that continuously monitors:

* data
* predictions
* model performance
* infrastructure
* business outcomes

Monitoring is what makes ML **reliable in production**.



1. Precision — Fraud Correctness

Definition:
Precision measures how many of the transactions predicted as fraud are actually fraud.

Formula:

Precision=True Positives/(False Positives+True Positives)
	​


True Positive (TP): Fraud correctly predicted as fraud

False Positive (FP): Legitimate transaction wrongly predicted as fraud

Interpretation in Fraud Detection:

If precision = 0.90, it means:

90% of transactions flagged as fraud were actually fraud

10% were false alarms

Why it matters:

High precision → fewer legitimate customers blocked unnecessarily

Example:

Model flagged 100 transactions as fraud

80 were actually fraud

20 were legitimate

Precision = 80 / 100 = 0.80

2. Recall — Fraud Detection Rate

Definition:
Recall measures how many of the actual fraud cases the model successfully catches.

Formula:


Recall=True Positives/(False Negatives+True Positives)
	​


False Negative (FN): Fraud transaction missed by the model

Interpretation in Fraud Detection:

If recall = 0.85, it means:

The model catches 85% of all fraud cases

15% fraud slips through

Why it matters:

High recall → less fraud escaping detection

Example:

Actual fraud transactions = 200

Model detected = 150

Recall = 150 / 200 = 0.75

3. F1 Score — Balanced Performance

Definition:
F1 Score is the harmonic mean of precision and recall, balancing both.

Formula:


F1=2×(Precision+Recall)/Precision×Recall
	

Why harmonic mean?
Because it penalizes imbalance between precision and recall.



Why it matters in fraud detection:

You want:

high recall → catch fraud

high precision → avoid false alarms

High precision but low recall → fraud goes undetected

High recall but low precision → too many false fraud alerts

F1 gives one number that balances both.

The F1 score ensures:

If precision is high but recall is low → F1 becomes low

If recall is high but precision is low → F1 becomes low

Only when both are good → F1 becomes high

So it forces a balance.

4. ROC-AUC — Model Discrimination Ability

ROC-AUC measures how well the model separates fraud vs legitimate transactions.

ROC Curve

ROC = Receiver Operating Characteristic

It plots:

True Positive Rate (Recall)
vs

False Positive Rate

FPR = False Positives/(True Negatives+False Positives)
	​


AUC

AUC = Area Under the Curve

Range:

AUC	Meaning
0.5	Random guessing
0.6–0.7	Poor
0.7–0.8	Fair
0.8–0.9	Good
0.9+	Excellent

Interpretation:

If ROC-AUC = 0.92

→ The model has a 92% chance of ranking a fraud transaction higher than a legitimate one.

Quick Summary
| Metric        | What it Measures                       | Key Goal in Fraud Detection      |
| ------------- | -------------------------------------- | -------------------------------- |
| **Precision** | Correctness of fraud predictions       | Avoid false alerts               |
| **Recall**    | How many frauds are caught             | Catch as many frauds as possible |
| **F1 Score**  | Balance of precision & recall          | Overall balanced model           |
| **ROC-AUC**   | Ability to separate fraud vs non-fraud | Overall discrimination quality   |

