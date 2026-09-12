# MATH-085 — exact one-paid current-phase replay through macro depth 6

Date: 2026-09-12

Status: `FINITE EXACT DEPTH-4/5/6 BELLMAN TERMINAL REPLAY / ORDINARY HANDOFF RESIDUAL = 0 THROUGH DEPTH 6`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-084 separately proves that a multi-source one-paid chain can persist for at most 23 macros in the current source window.

## 1. Exact current-phase state

MATH-083 rewrites the phase/penalty history in current-anchor coordinates. Store

\[
J=(\Omega^-_{\rm cur},\Omega^+_{\rm cur})
\]

and

\[
\mathcal P=\alpha\Omega_{\rm cur}.
\]

For a one-paid edge with source-phase domain \(I_e\), phase multiplier \(\rho_e\), and

\[
c_e=\frac{\beta_e}{\rho_e}\in\left\{\frac14,\frac18\right\},
\]

exact composition is

\[
\boxed{J'=\rho_e(J\cap I_e)},
\]

\[
\boxed{\alpha'=\frac{\alpha}{\rho_e}+c_e}.
\]

The dyadic source/target compatibility condition of MATH-061 is unchanged.

## 2. Bellman terminal tests

With

\[
\lambda=\frac{19}{503},
\]

MATH-082 gives the phase-free sufficient wedge

\[
H\le73
\]

or, for \(H>73\),

\[
\boxed{503t\ge228(H-73)}.
\]

When that coarse bound is insufficient, the exact current-phase infimum gives

\[
\boxed{\alpha\Omega^-_{\rm cur}-\lambda(H-73)\ge0}.
\]

A terminal that passes either test is removed only from the low-cost Bellman candidate search. This is not the same claim as ordinary Collatz descent.

## 3. Depth 4

Exact composition from the canonical depth-3 multi-source states gives

\[
\boxed{76,585\text{ terminal singleton handoffs}}
\]

and

\[
\boxed{442,957\text{ multi-source survivors}}.
\]

Of the terminal handoffs,

\[
\boxed{76,564}
\]

pass the universal wedge directly. All remaining 21 pass the exact current-phase penalty-infimum test.

Therefore

\[
\boxed{76,585/76,585\text{ are Bellman-safe}},
\]

with

\[
\boxed{0\text{ ordinary-continuation residuals}}.
\]

Every depth-4 multi-source survivor satisfies

\[
H\le71.
\]

## 4. Depth 5

Exact continuation of all 442,957 depth-4 multi-source states gives

\[
\boxed{372,841\text{ terminal singleton handoffs}}
\]

and

\[
\boxed{1,689,024\text{ multi-source survivors}}.
\]

The phase-free wedge certifies

\[
\boxed{372,834}
\]

terminals. Only seven require the exact phase-infimum strengthening. Those seven also pass.

Hence

\[
\boxed{372,841/372,841\text{ are Bellman-safe}},
\]

again with

\[
\boxed{0\text{ ordinary-continuation residuals}}.
\]

Every multi-source survivor again has

\[
H\le71.
\]

## 5. Depth 6

Depth 6 was evaluated by streaming every depth-5 multi-source child immediately from exact disjoint depth-4 source shards. Sharding changes only memory scheduling; it is an exact partition of the source list and has no pruning meaning.

The aggregate result is

\[
\boxed{1,358,935\text{ terminal singleton handoffs}}
\]

and

\[
\boxed{4,943,810\text{ multi-source survivors}}.
\]

The universal wedge certifies

\[
\boxed{1,358,914}
\]

terminals. The remaining 21 all pass the exact current-phase infimum test.

Thus

\[
\boxed{1,358,935/1,358,935\text{ are Bellman-safe}},
\]

with

\[
\boxed{0\text{ ordinary-continuation residuals}}.
\]

The largest terminal accumulated modulus depth observed is

\[
\boxed{H=90},
\]

while every multi-source survivor again satisfies

\[
\boxed{H\le71}.
\]

MATH-084 proves that the latter inequality is structural, not merely a finite-depth observation.

## 6. Computational representation audit

The replay uses three exact reductions only:

1. cache the set of phase-compatible one-paid edges for identical current intervals \(J\);
2. cache \((3^Q)^{-1}\bmod2^h\) for repeated dyadic compatibility tests;
3. stream depth-5 states into depth 6 instead of storing the complete depth-5 table.

No candidate is removed by these representation choices.

The historical source anchor `source_A` of a composed state is not needed for future Bellman continuation once the exact current family

\[
B+3^Q s,\qquad 0\le s<M
\]

is known. However, each next edge's exact source congruence remains necessary, so dyadic compatibility is not discarded.

## 7. Current conclusion

Through macro depth 6, every newly singleton-resolved one-paid chain is certified Bellman-safe by

\[
\text{universal resolution wedge}
\quad\text{or}\quad
\text{exact current-phase penalty infimum}.
\]

Thus ordinary singleton continuation, which was needed for two depth-3 exceptions in MATH-082, is no longer needed at depths 4, 5, or 6.

This is strong finite evidence for a general terminal Bellman rule, but it is not yet a proof for all macro depths through the MATH-084 horizon.

## 8. Prohibited upgrades

Do not infer:

- depth-4/5/6 Bellman safety `=>` all one-paid depths are safe;
- Bellman-safe terminal `=>` ordinary descent theorem;
- `H<=71` for multi-source `=>` all terminal penalties are sufficient;
- finite-depth replay `=>` first-cell emptiness;
- current-phase compression `=>` dyadic address information can be removed.

## Reproducibility

`collatz/src/2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py`

The script supports exact disjoint depth-4 source slices via `--start` and `--stop`. Summing a partition of `[0,442957)` reproduces the full depth-5/6 aggregate without changing the represented set.
