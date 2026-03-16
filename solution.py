"""
Introduction to Computational Physics — Homework 1: Power Laws & Distributions
Bar-Ilan University, 2026

Instructions:
    1. Use any LLM to help you write the code.
    2. Implement all functions below — do NOT rename them or change their signatures.
    3. Run the public tests locally before pushing:
           pytest tests/ -v
    4. The autograder will run additional tests automatically on push.
    5. Document your physics reasoning in notebook.ipynb.

Remember: Code is cheap. Physical validation is expensive.
"""

import numpy as np


def power_law_pdf(x, alpha, x_min=1.0):
    """Compute the normalized power-law probability density function.

    P(x) = C * x^(-alpha)  for x >= x_min
    P(x) = 0               for x < x_min

    where C = (alpha - 1) * x_min^(alpha - 1) is the normalization constant.

    Parameters
    ----------
    x : float or np.ndarray
        Values at which to evaluate the PDF.
    alpha : float
        Power-law exponent (must be > 1).
    x_min : float
        Lower cutoff of the distribution (default 1.0).

    Returns
    -------
    pdf : float or np.ndarray
        Probability density values.
    """
    # TODO: implement this function
    pass


def mle_alpha(data, x_min=1.0):
    """Estimate the power-law exponent using Maximum Likelihood Estimation.

    The MLE estimator for the continuous power-law distribution is:

        alpha_hat = 1 + n / sum(ln(x_i / x_min))

    where n is the number of data points and x_i are the observed values.

    Parameters
    ----------
    data : np.ndarray
        Observed values (all must be >= x_min).
    x_min : float
        Lower cutoff of the distribution (default 1.0).

    Returns
    -------
    alpha_hat : float
        Estimated power-law exponent.
    """
    # TODO: implement this function
    pass


def log_histogram(data, num_bins=50, x_range=None):
    """Compute a histogram with logarithmic (geometric) binning.

    Bin edges are geometrically (logarithmically) spaced between
    x_range[0] and x_range[1]. Returns probability density values
    normalized so that the integral over all bins approximates 1.

    Parameters
    ----------
    data : np.ndarray
        Positive-valued data points.
    num_bins : int
        Number of bins (default 50).
    x_range : tuple of (float, float) or None
        (x_min, x_max) range for binning. If None, use (data.min(), data.max()).

    Returns
    -------
    densities : np.ndarray
        Probability density in each bin (length num_bins).
    bin_centers : np.ndarray
        Center of each bin (length num_bins).
    bin_edges : np.ndarray
        Bin edges, logarithmically spaced (length num_bins + 1).
    """
    # TODO: implement this function
    pass


def ssr_zipf(N, num_iterations=100000, seed=None):
    """Simulate the Sample Space Reducing (SSR) process.

    A ball starts at state N and jumps uniformly at random to any lower
    state (1 to current_state - 1) at each step. When it reaches state 1,
    the cascade restarts from state N. After many cascades, the visit
    frequency follows Zipf's law: P(i) ~ 1/i.

    Parameters
    ----------
    N : int
        Number of states (highest state).
    num_iterations : int
        Number of complete cascades to simulate (default 100000).
    seed : int or None
        Random seed for reproducibility (default None).

    Returns
    -------
    visit_freq : np.ndarray
        Normalized visit frequencies for states 1, 2, ..., N (length N).
        visit_freq[0] corresponds to state 1, visit_freq[N-1] to state N.
    """
    # TODO: implement this function
    pass
