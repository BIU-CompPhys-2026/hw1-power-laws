# Homework N: [Topic]

## Instructions

1. **Implement** all functions in `solution.py` — use any LLM to help you write the code
2. **Test locally** before pushing:
   ```bash
   pytest tests/ -v
   ```
3. **Push to GitHub** — grading runs automatically via GitHub Classroom (check the assignment page for results)
4. **Document** your physics reasoning and prompt history in `notebook.ipynb`

## Submission Checklist

- [ ] All functions in `solution.py` are implemented
- [ ] Public tests pass locally (`pytest tests/ -v`)
- [ ] Autograder passes (check GitHub Classroom)
- [ ] `notebook.ipynb` contains physics explanations in markdown cells
- [ ] Prompt history is included (link or pasted conversation)

## Grading

| Component | Weight |
|-----------|--------|
| Autograder (automated tests) | 60% |
| Physics explanation | 25% |
| Prompt history | 15% |

## Setup

```bash
pip install -r requirements.txt
```

## Tips

- The graded tests check **physical correctness**, not just code output
- If public tests pass but the autograder fails, your physics reasoning is likely wrong
- Think about edge cases, convergence, and known analytical results
