# Exact small-residue first-crossing scan through q <= 50,000

Date: 2026-08-10

Status: **EXACT FINITE COMPUTATIONAL CHECK / NOT AN ASYMPTOTIC THEOREM**

This note extends the diagnostic in `sparse-defect-residue-gap-target.md` without enumerating first-crossing parity words.

## 1. Target condition

For a first coefficient crossing with final odd count `q`, consider ordinary canonical starts satisfying

\[
\boxed{0<x<2q^2.}
\]

The previous parity-word exhaustive table only reached small `q` because the number of admissible odd-position vectors grows rapidly.

Instead, for a chosen `Q`, every possible hit with `q<=Q` lies in the ordinary start interval

\[
1\le x<2Q^2.
\]

Thus one may scan each ordinary start in this interval exactly once, compute its unique first coefficient crossing, and assign it to its resulting odd-count layer.

## 2. Exact scan

`collatz/src/small_residue_first_cross_scan.cpp` uses:

- exact big-integer construction of
  \[
  \kappa_i=\lfloor i\log_2 3\rfloor
  \]
  from the bit length of `3^i`;
- exact big-integer coefficient thresholds
  \[
  a_k=\min\{q:3^q\ge2^k\};
  \]
- guarded unsigned 64-bit trajectory arithmetic;
- direct defect counting from
  \[
  z_i=\kappa_i-d_i.
  \]

The `Q=50,000` run scans

\[
1\le x\le5,000,000,000
\]

and reports zero arithmetic overflows.

## 3. Complete hit layers in the certified range

The odd-count layers admitting at least one start `x<2q^2` are exactly

\[
\boxed{
1,2,3,4,5,9,12,13,15,17,18,19,22,23,24,25,26,28,
32,34,35,36,37,38,49,50,51.
}
\]

No additional hit layer occurs for

\[
\boxed{52\le q\le50,000.}
\]

Selected minima are:

| q | minimum defects among `x<2q^2` | example start |
|---:|---:|---:|
| 24 | 20 | 671 |
| 25 | 18 | 155 |
| 26 | 22 | 103 |
| 28 | 22 | 91 |
| 32 | 26 | 71 |
| 34 | 30 | 47 |
| 35 | 32 | 31 |
| 36 | 31 | 2047 |
| 37 | 33 | 27 |
| 38 | 32 | 1819 |
| 49 | 45 | 1583 |
| 50 | 44 | 2111 |
| 51 | 48 | 1407 |

The earlier exhaustive parity-word values through `q=23` are reproduced exactly on the overlap.

An independent Python start-scan through `q<=500` reproduces all 27 hit layers and the same minimum-defect/example-start pairs.

## 4. Interpretation

This finite result is much stronger numerically than the original small-q parity enumeration, but it does **not** prove

\[
q\ge52\Longrightarrow r_{\min}(q)\ge2q^2.
\]

The next unresolved resonance has

\[
q=137,528,045,312,
\]

far outside the certified range.

The computation nevertheless supports the more focused project target:

> obtain a deterministic lower bound on the canonical first-crossing residue in terms of `q`, or at minimum exclude polynomially small residues on the near-resonant layers relevant to a hypothetical minimal counterexample.

No extrapolation from `q<=50,000` is used as a proof step.