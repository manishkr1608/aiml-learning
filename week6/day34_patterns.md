
# Day 34 – Circuit Breaker Pattern (Resilience for Model Serving)

**Intent:** Prevent repeated failed requests to an unstable downstream service by "opening" the circuit after failures, and then periodically testing the service to "half-open" and finally "close" when healthy.

**Why it matters for AI deployment**
- Model endpoints (FastAPI, SageMaker, etc.) can fail under load, during rolling deploys, or when dependent infra is degraded.
- Without a circuit breaker, clients keep retrying and amplify outages (thundering herd).
- Circuit Breaker improves overall system resilience and provides graceful degradation (e.g., fallback predictions, cached responses, or feature flagging).

## States
- **Closed:** normal operation, count failures.
- **Open:** short-circuit requests to avoid hitting failed service; return fallback.
- **Half-Open:** after cooldown, allow a limited number of requests to test recovery.


## Use with client libraries calling model endpoints (FastAPI, gRPC, HTTP).

## Combine with fallback strategies: return cached result, default prediction, degrade to simpler model, or enqueue request for async processing.

## Instrument with metrics (breaker state, fail_count, calls short-circuited) to expose in your monitoring dashboard.

import time
from functools import wraps

class CircuitBreaker:
    def __init__(self, fail_max=5, reset_timeout=10):
        self.fail_max = fail_max
        self.reset_timeout = reset_timeout
        self.fail_count = 0
        self.state = "CLOSED"
        self.opened_since = None

    def _open(self):
        self.state = "OPEN"
        self.opened_since = time.time()

    def _half_open(self):
        self.state = "HALF_OPEN"

    def _close(self):
        self.state = "CLOSED"
        self.fail_count = 0
        self.opened_since = None

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            # If open, check timeout to move to half-open
            if self.state == "OPEN":
                if time.time() - (self.opened_since or 0) > self.reset_timeout:
                    self._half_open()
                else:
                    # Short-circuit — return fallback
                    return {"error":"service_unavailable","fallback": True}

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                # On failure, increment and possibly open circuit
                self.fail_count += 1
                if self.fail_count >= self.fail_max:
                    self._open()
                raise

            # On success:
            if self.state == "HALF_OPEN":
                # success during half-open means close circuit
                self._close()
            else:
                self.fail_count = 0
            return result
        return wrapped

# Example usage with a model inference call
import random

breaker = CircuitBreaker(fail_max=3, reset_timeout=5)

@breaker
def call_model(x):
    # Simulate intermittent failures
    if random.random() < 0.4:
        raise RuntimeError("simulated endpoint failure")
    return {"prediction": 42}

if __name__ == "__main__":
    for i in range(15):
        try:
            r = call_model(i)
            print("OK:", r)
        except Exception as e:
            print("FAIL:", e)
        time.sleep(0.8)