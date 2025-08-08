# n-Equations Solver via Matrix Inversion

## Overview
This project solves a system of \( n \) linear equations in \( n \) unknowns:

\[
A \mathbf{x} = \mathbf{b}
\]

by computing the inverse of the coefficient matrix:

\[
\mathbf{x} = A^{-1} \mathbf{b}
\]

The core logic is implemented in [`matrix_utils.py`](matrix_utils.py), with execution handled by [`main.py`](main.py).

---

## Repository Structure
- **`main.py`** – Application entry point. Handles input parsing, solver invocation, and output display.
- **`matrix_utils.py`** – Functions for matrix inversion, determinant calculation, and related operations.
- **`README.md`** – Project documentation.

---

## Requirements
- Python 3.x
- No external libraries required
- Input matrix \( A \) must be square and satisfy \( \det(A) \neq 0 \) for the inverse to exist.

---

## Usage
1. Clone the repository and navigate into the folder:
   ```bash
   git clone https://github.com/amayl/python-solver.git
   cd python-solver
