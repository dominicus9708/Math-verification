# Cycle-branch compatibility at the isolated first-crossing scale

Date: 2026-08-10

Status: **EXTERNAL-RESULT COMPARISON + PROJECT SCOPE CLARIFICATION**

This note clarifies how the project’s paradoxical first-coefficient-crossing branch relates to the second possible failure mode of the Collatz conjecture: a nontrivial positive cycle.  It does not derive a new cycle lower bound.

## 1. Two failure modes

For the deterministic Collatz map on positive integers, a counterexample can be:

1. an unbounded orbit;
2. a nontrivial periodic orbit.

A bounded infinite nonperiodic orbit is impossible because a bounded positive-integer orbit has only finitely many states, and a repeated state forces periodicity.

## 2. Why a nontrivial cycle enters the project’s first-crossing branch

For one period of a nontrivial cycle, let `h` be the period length and `q` the number of odd steps.  The affine identity is

\[
2^h n=3^q n+R,
\qquad R>0.
\]

Hence

\[
\boxed{2^h>3^q.}
\]

So the coefficient must cross below one somewhere within a period.

Choose the least ordinary integer `n_min` on the cycle.  At the first coefficient crossing along the orbit beginning at `n_min`, the numerical endpoint cannot be below `n_min`, by minimality.  Therefore that first crossing is paradoxical in the project’s sense:

\[
3^{q_\sigma}<2^\sigma,
\qquad
T^\sigma(n_{\min})\ge n_{\min}.
\]

Thus an eventual theorem eliminating every paradoxical first coefficient crossing would remove nontrivial cycles as well as the finite-crossing obstruction relevant to unbounded trajectories.

## 3. External cycle lower-bound scale

Christian Hercher, *There are no Collatz-m-Cycles with m<=91*, Journal of Integer Sequences 26 (2023), Article 23.3.5 (arXiv:2201.00406v3), proves `m>=92` for a nontrivial cycle and studies the next lower bound on the total number `K` of odd members/odd steps in a cycle.

Hercher states that verifying ordinary convergence through

\[
X_0\ge1536\cdot2^{60}=3\cdot2^{69}
\]

is sufficient to reach the next cycle lower-bound scale

\[
K\ge1.375\cdot10^{11}.
\]

David Barina’s public verification project reports convergence for every start below `2^71` as of 2025-01-15.  Since

\[
2^{71}>3\cdot2^{69},
\]

Hercher’s stated verification-range prerequisite is satisfied by the current verified range.

This note treats the exact numerical cycle bound only at the precision stated by Hercher (`1.375e11`); it does not replace his computation with a project-derived exact integer threshold.

## 4. Comparison with the isolated project resonance

The project has independently isolated, for its current first-crossing floor, the sole remaining pair in the interval above the previously eliminated resonance:

\[
\boxed{
(q,\sigma)=
(137,528,045,312,
217,976,794,617).
}
\]

Its odd-count scale is

\[
q=1.37528045312\cdot10^{11},
\]

which lies just above the external rounded cycle lower-bound scale `1.375e11`.

This numerical proximity should not be stated as an identity of the two results.  Both analyses are driven by the same `2^h` versus `3^q` Diophantine tension and continued-fraction structure, so the proximity is structurally unsurprising, but the project’s `q` is a first-coefficient-crossing count whereas Hercher’s `K` is a whole-cycle odd-step count.

## 5. Proof-program consequence

The current isolated resonance is therefore relevant to both possible global counterexample types:

- for an unbounded orbit it is a possible finite first crossing that still fails to descend;
- for a nontrivial cycle, choosing the cycle minimum likewise produces a paradoxical first crossing.

The project should continue to state the sufficient global descent target as

\[
\boxed{
\forall n>1\;\exists k\ge1:\ T^k(n)<n.
}
\]

If proved, strong induction sends every positive integer to `1`; a nontrivial cycle is impossible because its least element could not have a smaller future iterate.

The separate infinite-coefficient-survival branch must still be excluded: the first-crossing analysis alone does not cover an orbit for which `3^{q_k}>=2^k` forever.

## References

- C. Hercher, *There are no Collatz-m-Cycles with m<=91*, Journal of Integer Sequences 26 (2023), Article 23.3.5; arXiv:2201.00406.
- D. Barina, *Convergence verification of the Collatz problem*, J. Supercomput. 77 (2021), 2681-2688, with the associated public verification project reporting the later `2^71` milestone.
