import numpy as np
import pandas as pd

def calculate_psi(expected, actual, bins=10):

    breakpoints = np.linspace(0, 100, bins + 1)

    expected_perc = np.percentile(expected, breakpoints)
    actual_perc = np.percentile(actual, breakpoints)

    psi_value = 0

    for i in range(len(expected_perc) - 1):

        expected_count = ((expected >= expected_perc[i]) &
                          (expected < expected_perc[i+1])).mean()

        actual_count = ((actual >= expected_perc[i]) &
                        (actual < expected_perc[i+1])).mean()
        
        epsilon = 1e-6

        expected_count = max(expected_count, epsilon)
        actual_count = max(actual_count, epsilon)

        psi = (actual_count - expected_count) * np.log(
            actual_count / expected_count
        )

        psi_value += psi

    return psi_value

#Example usage:

train_feature = [10, 12, 15, 20, 22, 25, 30]
prod_feature = [10,11,14,18,35,40,45]

psi_score = calculate_psi(train_feature, prod_feature)

if psi_score > 0.2:
    print("Significant drift detected")