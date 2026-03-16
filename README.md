# Homework 1: Power Laws & Distributions

## Instructions

1. **Implement** all four functions in `solution.py` — use any LLM to help you write the code
2. **Test locally** before pushing:
   ```bash
   pytest tests/ -v
   ```
3. **Push to GitHub** — grading runs automatically via GitHub Classroom (check the assignment page for results)
4. **Document** your physics reasoning and prompt history in `notebook.ipynb`

## Functions to Implement

| Function | Description |
|----------|-------------|
| `power_law_pdf(x, alpha, x_min)` | Normalized power-law PDF with correct domain handling |
| `mle_alpha(data, x_min)` | Maximum Likelihood Estimation of the power-law exponent |
| `log_histogram(data, num_bins, x_range)` | Histogram with logarithmic (geometric) binning |
| `ssr_zipf(N, num_iterations, seed)` | Sample Space Reducing process → Zipf's law |

## Notebook Exercises

In `notebook.ipynb`, complete the following (with plots and physics explanations):

1. **Visualize** the power-law PDF for α = 1.6, 2.2, 3.1 on a log-log plot
2. **Compare** MLE vs polynomial fitting on log-log data — which is more accurate and why?
3. **Compare** linear vs logarithmic binning — why does linear binning fail for power-law data?
4. **Simulate** the SSR process and verify Zipf's law by fitting the slope
5. **Reproduce Slide 9** — plot sample mean and variance vs sample size N for α = 1.6, 2.2, 3.1. Explain which moments converge, which diverge, and why

## Submission Checklist

- [ ] All functions in `solution.py` are implemented
- [ ] Public tests pass locally (`pytest tests/ -v`)
- [ ] Autograder passes (check GitHub Classroom)
- [ ] `notebook.ipynb` contains plots and physics explanations for all 5 exercises
- [ ] Prompt history is included (link or pasted conversation)

## Grading

| Component | Weight |
|-----------|--------|
| Autograder (automated tests) | 60% |
| Physics explanation (notebook) | 30% |
| Prompt history | 10% |

## Setup

```bash
pip install -r requirements.txt
```

## Tips

- The graded tests check **physical correctness**, not just code output
- If public tests pass but the autograder fails, check your physics:
  - Is your PDF correctly normalized? What happens for x < x_min?
  - Does your MLE recover the known exponent from synthetic data?
  - Are your histogram bins truly logarithmically spaced?
- Think about edge cases, normalization, and known analytical results
- Refer to Lecture 1 slides and the tutorial notebook for theory
