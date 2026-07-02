# Justfile for Large-Scale Sparse Computation website

# Build the HTML website
build:
	.venv/bin/jupyter-book build --html --force

# Export the website to PDF
pdf:
	.venv/bin/jupyter-book build --pdf --force

# Export the website to TeX/LaTeX
tex:
	.venv/bin/jupyter-book build --tex --force

# Execute all notebooks in the chapters directory in-place
execute:
	.venv/bin/jupyter nbconvert --execute --inplace chapters/*.ipynb

# Start a local development server for the website
serve:
	.venv/bin/myst start

# Auto-generate the table of contents (TOC) in myst.yml
toc:
	@.venv/bin/python scripts/generate_toc.py
	.venv/bin/myst init --write-toc
