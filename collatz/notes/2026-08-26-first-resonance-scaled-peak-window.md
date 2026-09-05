# First resonance: mechanical-scaled state and exact root peak window

Date: 2026-08-26

Status: **exact structural lemma + exact rational first-resonance root window.** This does not prove the Collatz conjecture. It is a boundary-preserving reduction inside the repaired first-global-resonance branch.

## 1. Mechanical-scaled state

Let `x_j` be the actual odd state at odd ordinal `j`. Let `b_j` be the corresponding mechanical odd position and let

\[
d_j=b_j-a_j\ge0
\]

be the left displacement of the actual odd position `a_j` from the mechanical position.

Let

\[
g_j=b_{j+1}-b_j\in\{1,2\}
\]

with the final boundary included so that the block mechanical times add correctly. The actual odd valuation satisfies

\[
v_j=g_j+d_j-d_{j+1}.
\]

The actual odd map is

\[
x_{j+1}={3x_j+1\over2^{v_j}}.
\]

Define the mechanical-scaled real state

\[
\boxed{z_j={x_j\over2^{d_j}}.}
\]

Then the displacement terms cancel exactly:

\[
\boxed{
{z_{j+1}\over z_j}
={3+1/x_j\over2^{g_j}}.
}
\]

This identity is not a new dynamical assumption. It is an exact algebraic quotient which removes the explicit displacement control from the multiplicative block ratio while retaining the actual-state correction `1/x_j`.

## 2. Uniform block envelope on a minimal-counterexample prefix

The repaired first-resonance branch uses the external finite base

\[
B=2^{71}.
\]

Every state on a minimal-counterexample non-descent prefix is larger than `B`. Hence

\[
3<3+{1\over x_j}<3+{1\over B}.
\]

For any mechanical block containing `q` odd ordinals and total mechanical time `A_b`, multiplication gives

\[
\boxed{
{3^q\over2^{A_b}}
<
{z_{\rm out}\over z_{\rm in}}
\le
{(3+1/B)^q\over2^{A_b}}.
}
\]

Therefore:

- a block with `q/A_b > log_3 2` is strictly expanding in `z` for every admissible control;
- a block with `q/A_b < log_{3+1/B} 2` is strictly contracting in `z` for every admissible control.

This gives a dynamical meaning to the previously certified `U/S` coloring of the Christoffel DAG.

## 3. Root split

The first-resonance root is

\[
(A,Q)=(114208327604,72057431991).
\]

Its ordered anchored Christoffel split is

\[
\boxed{
U=(103768467013,65470613321),
\qquad
S=(10439860591,6586818670).
}
\]

The left block `U` is coefficient-supercritical and the right block `S` is finite-base RS-safe.

Thus every admissible first-resonance path has

\[
\boxed{z_{\rm mid}>z_{\rm start},\qquad z_{\rm mid}>z_{\rm end}.}
\]

The interface is a forced peak independently of how the internal displacement controls are chosen.

## 4. Exact absolute window above the endpoint

At the exposed boundaries,

\[
z_{\rm start}=N,
\qquad
z_{\rm end}=y=N+g.
\]

The already certified near-return bounds give

\[
2^{71}<y<{4\over3}2^{71}+2^{33}.
\]

Use the safe suffix `S`. Since

\[
{z_{\rm end}\over z_{\rm mid}}
\le
{(3+1/B)^{Q_S}\over2^{A_S}}<1,
\]

we obtain a lower peak excess. Conversely the true-3 lower coefficient on `S` gives an upper peak excess.

The companion exact-rational certificate proves

\[
\boxed{
21,706,947,634
<
z_{\rm mid}-y
<
31,870,071,812.
}
\]

Thus the root interface peak is not merely qualitative. It lies in an absolute window of width less than

\[
10,163,124,178.
\]

## 5. DSD interpretation

The useful DSD chain is now

\[
\boxed{
\text{mechanical block type}
\to
\text{uniform scaled-state direction}
\to
\text{forced interface peak}
\to
\text{two-boundary numeric window}.
}
\]

No orbit is enumerated in this step. The theorem applies to every admissible displacement control inside the block.

This is exactly the sort of reduction sought in the proof program: replace trajectory substitution by a boundary-preserving structural statement.

## 6. Next target

Every proper internal Christoffel node has already been certified to split in the ordered form

\[
U\cdot S.
\]

Therefore every internal interface is a scaled-state peak of the same qualitative type.

The next proof-level target is to convert this recursive peak hierarchy into a Bellman lower potential. In particular, one wants a node functional `Phi` such that the required rise into a `U` child and fall through the following `S` child forces either

1. a positive displacement-debt excursion with certified reserve cost, or
2. a Hensel repair consuming a bounded alignment credit,

and these node costs compose under the 21-run / 138-node Christoffel grammar.

Companion certificate:

`collatz/src/first_resonance_scaled_peak_window_certificate.py`.
