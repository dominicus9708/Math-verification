# Bounded-record density versus the López–Stoll periodicity claim: conditional bridge and audit

Date: 2026-08-22

Status: **external-result audit.** The internal bounded-record density theorem is exact. The López–Stoll implication recorded here is treated as conditional because the cited source is an arXiv preprint and its proof uses a cross-completion step that should not be silently imported into the present proof program. This note does not close the Collatz conjecture.

Let

\[
\alpha=\frac{\ln2}{\ln3}.
\]

The internal bounded-record theorem already proves that if a hypothetical infinite nonperiodic Collatz tail has an eventual record-length bound

\[
L_r\le M<\infty,
\]

then its parity-one count \(m_k\) satisfies

\[
\boxed{
\liminf_{k\to\infty}\frac{m_k}{k}
\ge
\alpha+\frac1M
>
\alpha.
}
\]

## 1. Peer-reviewed external input that is safe

Monks and Yazinski, *The autoconjugacy of the 3x+1 function*, Discrete Mathematics 275 (2004), prove for a rational 2-adic integer with divergent orbit the necessary lower bound

\[
\boxed{
\liminf_{k\to\infty}\frac{m_k}{k}\ge\alpha.
}
\]

This lower bound is compatible with the internal bounded-record inequality. By itself it does **not** rule out any finite \(M\), because \(\alpha+1/M\) also satisfies the Monks–Yazinski inequality.

Thus no bounded-record closure is claimed from the 2004 peer-reviewed theorem alone.

## 2. López–Stoll claim

López and Stoll, *The 3x+1 Periodicity Conjeture in R*, arXiv:2101.12747 (2021), state as Theorem 1 that if a rational 2-adic integer has a divergent trajectory, then

\[
\boxed{
\liminf_{k\to\infty}\frac{m_k}{k}=\alpha.
}
\]

If this theorem is accepted as stated, then the internal bounded-record theorem gives an immediate contradiction:

\[
\alpha+\frac1M
\le
\liminf\frac{m_k}{k}
=
\alpha.
\]

Hence:

\[
\boxed{
\text{Conditional on López–Stoll Theorem 1, every finite eventual record bound }M
\text{ is impossible.}
}
\]

This would close the entire bounded-record branch at once, including the first unresolved deterministic case \(M=5\).

## 3. Why this proof program does not import the claim unconditionally

The López–Stoll source remains an arXiv preprint rather than a peer-reviewed theorem used as a standard Collatz result.

More importantly for this project, the paper's argument explicitly evaluates the conjugacy series in the real completion while also drawing conclusions about eventual periodicity / rationality in the 2-adic completion. The present project has independently reduced its final obstruction to precisely this kind of real/2-adic cross-completion compatibility.

Therefore importing the López–Stoll equality as a black box would risk assuming a statement whose difficult step overlaps the theorem we are trying to establish.

The safe classification is:

- Monks–Yazinski lower bound: **peer-reviewed, usable, insufficient for closure**;
- López–Stoll equality claim: **strong enough for immediate bounded-record closure, but retained here only as a conditional external bridge pending independent proof audit**.

## 4. Consequence for the active proof front

The unconditional path remains:

1. unbounded record lengths: record-strip entropy/Fourier contraction;
2. bounded record lengths: strengthened parity entropy + terminal Haar + post-atomic integer/Hensel arithmetic;
3. first unresolved bounded case: M=5 valuation renewal / weighted matching language.

The López–Stoll result is useful as a diagnostic: it predicts that a true closure theorem should force the odd-density excess above \(\alpha\) to be impossible for a rational 2-adic starting point. But that prediction is not counted as a completed internal theorem.

## References

- K. G. Monks and J. Yazinski, *The autoconjugacy of the 3x+1 function*, Discrete Mathematics 275 (2004), 219–236, DOI 10.1016/S0012-365X(03)00125-0.
- J. López and P. Stoll, *The 3x+1 Periodicity Conjeture in R*, arXiv:2101.12747 (2021), Theorem 1.
