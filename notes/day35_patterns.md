
# Day 35 – Specification Pattern (Monitoring & Alert Rules)

**Intent:** Encapsulate business or monitoring rules as objects that can be combined and reused.

**Why for AI Ops:**  
- Express drift alerts, SLA breaches, and release gating logic as composable specifications.  
- Make alert logic testable, auditable, and readable by product/ops teams.

## Example: Specification base + combinators

class Specification:
    def is_satisfied_by(self, candidate):
        raise NotImplementedError
    def __and__(self, other): return AndSpecification(self, other)
    def __or__(self, other): return OrSpecification(self, other)
    def __invert__(self): return NotSpecification(self)

class AndSpecification(Specification):
    def __init__(self, a, b): self.a, self.b = a, b
    def is_satisfied_by(self, candidate): return self.a.is_satisfied_by(candidate) and self.b.is_satisfied_by(candidate)

class OrSpecification(Specification):
    def __init__(self, a, b): self.a, self.b = a, b
    def is_satisfied_by(self, candidate): return self.a.is_satisfied_by(candidate) or self.b.is_satisfied_by(candidate)

class NotSpecification(Specification):
    def __init__(self, a): self.a = a
    def is_satisfied_by(self, candidate): return not self.a.is_satisfied_by(candidate)

# Concrete specs for ML monitoring
class FeatureDriftSpec(Specification):
    def __init__(self, feature_name, psi_threshold):
        self.feature_name = feature_name
        self.psi_threshold = psi_threshold
    def is_satisfied_by(self, candidate):  # candidate is a dict of metric values
        psi = candidate.get(f"psi_{self.feature_name}", 0.0)
        return psi > self.psi_threshold

class LatencySpec(Specification):
    def __init__(self, max_latency_ms):
        self.max_latency_ms = max_latency_ms
    def is_satisfied_by(self, candidate):
        return candidate.get("p95_latency_ms", 0) > self.max_latency_ms

class AccuracyDropSpec(Specification):
    def __init__(self, drop_pct):
        self.drop_pct = drop_pct
    def is_satisfied_by(self, candidate):
        return candidate.get("accuracy_drop_pct", 0) > self.drop_pct

# Usage
psi_spec = FeatureDriftSpec("age", 0.2)
lat_spec = LatencySpec(200)
acc_spec = AccuracyDropSpec(5.0)

# Composite rule: alert if (age drift OR accuracy drop) AND latency is OK (i.e., not a latency-only issue)
alert_rule = (psi_spec | acc_spec) & ~lat_spec

candidate_metrics = {
    "psi_age": 0.25,
    "p95_latency_ms": 150,
    "accuracy_drop_pct": 1.0
}

if alert_rule.is_satisfied_by(candidate_metrics):
    print("Trigger: Model-quality alert (not latency)")
else:
    print("No trigger")


