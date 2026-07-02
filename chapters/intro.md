---
title: Large-Scale Sparse Computation
subtitle: From Kernels to Applications
date: 2026-07-01
authors:
  - name: Yuxi Hong
    email: yuxi.hong.research@gmail.com
    orcid: 0000-0002-0741-6602
    url: https://luddy.iu.edu/people/hong-yuxi.html
    github: hongyx11
    affiliation: ISE, Indiana University Bloomington
---

```{figure} ../assets/cats-paw-16-2.jpg
:alt: Cat's Paw Nebula
:class: intro-top-image

[Cat's Paw Nebula](https://science.nasa.gov/image-detail/cats-paw-16-2/). This image from NASA's Spitzer Space Telescope shows the Cat's Paw Nebula, so named for the large, round features that create the impression of a feline footprint. Image Credit: NASA/JPL-Caltech.
```

## Overview

These example notes show how to build a computational textbook with
Jupyter Book. The topic is large scale sparse computation: representing
sparse matrices, understanding sparse matrix-vector multiplication, and
solving sparse linear systems with iterative methods. The solver material
starts from classical conjugate-gradient ideas {cite}`hestenes1952methods`
and connects them to modern sparse computation.

## How to Read This Book

Start with the reading guide if you want the shortest path through the
material. Then read each computational chapter with the code cells visible:
the examples are meant to connect the mathematical idea to the storage layout,
operation count, and solver behavior.

## Tools Used

The examples use:

- `numpy` for dense arrays and numerical checks
- `scipy.sparse` for sparse matrix formats
- `scipy.sparse.linalg` for Krylov solvers

## Why Sparsity Matters

The main idea behind sparse computation is simple: store and operate only on
the nonzero entries. The engineering challenge is that performance depends on
memory traffic, indexing, locality, and numerical stability as much as on the
number of floating point operations.

## Chapters

```{tableofcontents}
```
