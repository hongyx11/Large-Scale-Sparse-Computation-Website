# Large-scale Sparse Computation

Example Jupyter Book 2 source for notes on large scale sparse computation.

## Build

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/jupyter nbconvert --execute --inplace chapters/*.ipynb
.venv/bin/jupyter-book build --html --force
.venv/bin/jupyter-book build --pdf --tex --force
```

The website is written to `_build/html/`, and the PDF/LaTeX exports are written
to `_build/exports/`.
