"""
Public tests — students can see and run these locally.

Run with:
    pytest tests/ -v
"""

import numpy as np
from solution import power_law_pdf, mle_alpha, log_histogram, ssr_zipf


# --- power_law_pdf ---

def test_pdf_at_xmin():
    """P(x_min) should equal (alpha - 1) / x_min."""
    # For alpha=2.5, x_min=1.0: C = 1.5 * 1^1.5 = 1.5, P(1) = 1.5 * 1^(-2.5) = 1.5
    assert abs(power_law_pdf(1.0, 2.5, 1.0) - 1.5) < 1e-10


def test_pdf_handles_array():
    """Should accept and return numpy arrays."""
    x = np.array([1.0, 2.0, 3.0])
    result = power_law_pdf(x, 2.5, 1.0)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3,)


# --- mle_alpha ---

def test_mle_returns_greater_than_one():
    """MLE estimate should always be > 1 for valid power-law data."""
    data = np.array([1.0, 2.0, 3.0, 5.0, 10.0])
    alpha = mle_alpha(data, 1.0)
    assert alpha > 1.0


# --- log_histogram ---

def test_log_histogram_shapes():
    """Output arrays should have correct lengths."""
    np.random.seed(0)
    data = np.random.pareto(1.5, size=1000) + 1
    densities, centers, edges = log_histogram(data, num_bins=20, x_range=(1, 1000))
    assert len(densities) == 20
    assert len(centers) == 20
    assert len(edges) == 21


# --- ssr_zipf ---

def test_ssr_returns_normalized():
    """Visit frequencies should sum to approximately 1."""
    freq = ssr_zipf(10, num_iterations=10000, seed=0)
    assert len(freq) == 10
    assert abs(sum(freq) - 1.0) < 0.01
