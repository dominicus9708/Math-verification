# DSD-dynamics Collatz checkpoint and proposition reframing

Date: 2026-08-11

Status: **recorded computational checkpoint + methodological reframing**. This note does not claim a proof of the Collatz conjecture.

## 1. Computational checkpoint frozen at this stage

The following results are retained as the current exact finite record:

- exact DSD-style single-channel closure and transition audit through depth 32;
- exact prefix block identity `T^k(r + m 2^k) = y + 3^Q m` on the audited channel states;
- endpoint quotient and true-first-merge diagnostics using the actual lifted predecessor;
- corrected rejection of the stronger conjecture `G = r_L - 3 r_H > 0` by the exact depth-37 Type-B counterexample;
- replacement of the correction-order target by the Pareto-relevant start-order target `J = r_L - r_H > 0`;
- joint 3-adic carry / 2-adic wrap formulation with `G = 1 + c_0` and common endpoint iff `m = 0`;
- exact negative carry-root spectrum through q = 33: the only observed negative root is `c_0 = -3`, hence `G = -2`;
- full negative-path expansion through q = 31 with no start-order dominance failure;
- positional lower bound `G > L_q`, implying Delta-Q=1 start dominance for q <= 36 without endpoint enumeration;
- first presently unresolved dangerous layer: q = 37, c_0 = -7, G = -6.

These results are preserved as diagnostic evidence and theorem-building input. The project should not continue by merely extending q = 37, 38, 39, ... indefinitely.

## 2. Why the problem is dynamic

The Collatz rule is not a static classification of integers. A state is repeatedly transformed, and the truth of the conjecture depends on the entire ordered sequence of transformations. Therefore an explicit discrete time/order coordinate is intrinsic to the problem.

The DSD import is formal rather than physical. The intended architecture is:

1. **Formation layer** — determine which states/channels are admissibly formed and remove the complement;
2. **Static aggregation layer** — describe and quotient the admissible states on each fixed-time slice;
3. **Axis-property layer** — attach the properties needed to distinguish states and transitions (parity, odd-count, coefficient status, correction/carry/wrap attributes, etc.);
4. **Dynamics layer** — determine how an admissible state and its attributes change from slice k to slice k+1;
5. **global trajectory statement** — classify the possible long-time orbit types of the resulting discrete flow.

No physical propagation speed, wave equation, Laplacian, or continuum-time assumption is imported.

## 3. State-space viewpoint

Let `Sigma_k` denote the admissible static state slice at discrete time k. The full discrete spacetime/state history is

\[
\mathcal X = \bigsqcup_{k\ge0} (\Sigma_k \times \{k\}).
\]

The Collatz dynamics is a map or transition relation

\[
\mathcal D_k : \Sigma_k \to \Sigma_{k+1}.
\]

The static-aggregation and formation operations act within each slice; the dynamics connects successive slices.

For visualization one may project the internal state to a two-coordinate structural plane and use k as the third coordinate. The two structural coordinates need not be literal spatial coordinates. They may be chosen from sufficient state variables or quotient coordinates such as current endpoint, coefficient/slack, correction, residue class, or another closed pair. The coordinate choice must be derived from sufficiency, not imposed geometrically.

## 4. Reframed proposition direction

The correct global target should not be `G > 0`, nor should it be a sequence of finite depth checks. It should classify the invariant / recurrent / escaping subsets of the discrete state flow.

A useful target form is:

> Every admissible positive-integer trajectory either enters the known Collatz terminal component containing 1, or would have to remain forever in a nonterminal invariant/recurrent/escaping subset of the admissible state space. Prove that the latter subset is empty.

Equivalently, if `A` is the admissible state space and `C_1` is the known terminal component containing 1, define the nonterminal survivor set

\[
\mathcal S_\infty
= \bigcap_{K\ge0} \mathcal D^{-K}(A\setminus C_1).
\]

The Collatz conjecture is reduced to showing

\[
\boxed{\mathcal S_\infty = \varnothing}
\]

for positive integer initial states, while separately excluding nontrivial periodic components and unbounded escaping components if the quotient construction distinguishes them.

This is the new proposition-building direction: identify sufficient state variables and prove that no nonterminal invariant trajectory can remain admissible for all time.

## 5. Next mathematical task

The next task is not a larger finite scan. It is to choose a minimal sufficient state/quotient for which:

- formation/admissibility is exact;
- static equivalence is exact;
- the transition is closed;
- periodicity, merger, contraction, and escape are distinguishable;
- a monotone, well-founded, or recurrent-set exclusion argument can be formulated.

The computational results already obtained should be used only to discover and falsify candidate invariants for that global statement.
