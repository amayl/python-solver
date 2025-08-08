\documentclass[11pt]{article}

\usepackage{amsmath}
\usepackage{geometry}
\geometry{margin=1in}

\title{\(n\)-Equations Solver (Matrix Inversion)}
\author{Your Name}
\date{}

\begin{document}
\maketitle

\section*{Overview}
This tool solves \(n\) linear equations in \(n\) unknowns:
\[
A \mathbf{x} = \mathbf{b}
\]
by computing:
\[
\mathbf{x} = A^{-1} \mathbf{b}
\]
where \(A\) is an \(n \times n\) coefficient matrix, \(\mathbf{b}\) is the constants vector, and \(A^{-1}\) is the inverse of \(A\).

\section*{Usage}
\begin{enumerate}
    \item Enter \(n\) (number of equations).
    \item Input \(A\) (\(n \times n\) matrix) and \(\mathbf{b}\) (\(n \times 1\) vector).
    \item Program outputs \(\mathbf{x}\) (solution vector).
\end{enumerate}

\section*{Requirements}
\begin{itemize}
    \item \(A\) must be invertible (\(\det(A) \neq 0\)).
    \item Environment with basic matrix operations.
\end{itemize}

\section*{Example}
For:
\[
\begin{cases}
2x + y = 5 \\
x - 3y = -4
\end{cases}
\]
\[
A =
\begin{bmatrix}
2 & 1 \\
1 & -3
\end{bmatrix},
\quad
\mathbf{b} =
\begin{bmatrix}
5 \\ -4
\end{bmatrix}
\]
Solution:
\[
\mathbf{x} =
\begin{bmatrix}
1 \\ 3
\end{bmatrix}
\]

\end{document}
