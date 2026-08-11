# Unified terminal architecture via renewal floors

Date: 2026-08-11

Status: **proof-architecture consolidation**. This note does not prove either terminal exclusion.

## 1. Previous terminal split

The maximal-block sign theorem produced three qualitative terminal branches:

1. periodic exact returns;
2. Mode I — eventual monotone block expansion;
3. Mode II — infinitely many increasing/decreasing excursions.

The Mode I/Mode II split remains useful for local analysis but is not necessary as the final proof decomposition.

## 2. Renewal-floor recombination

Every nonperiodic positive-integer block orbit tends to infinity and therefore has an infinite increasing sequence of suffix minima

\[
N_0<N_1<N_2<\cdots\to\infty.
\]

Each consecutive pair is connected by one exact renewal-floor aggregate transition

\[
N_{j+1}
=
\frac{3^{H_j}N_j+B_j}{2^{H_j+D_j}},
\]

with positive correction `B_j` and aggregate multiplier

\[
P_j
=\frac{2^{H_j+D_j}}{3^{H_j}}
=2^{D_j-\alpha H_j},
\qquad
\alpha=\log_2(3/2).
\]

Mode I corresponds to the eventual one-block/subcritical renewal case. Mode II corresponds to multi-block renewal segments containing excursions.

## 3. Aggregate classification

Every renewal segment is exactly one of:

### A. Aggregate subcritical

\[
\boxed{P_j<1.}
\]

The higher next floor is then automatic.

### B. Aggregate supercritical

\[
\boxed{P_j>1.}
\]

Because the next renewal floor is nevertheless higher, accumulated affine correction must compensate for the coefficient contraction. The renewal-resonance theorem forces

\[
0<D_j-\alpha H_j
\le
\frac{1}{3\ln2}
\log\left(1+\frac{3(m_j-1)}{N_{j+1}}\right)
+O(1/N_{j+1}).
\]

Thus every aggregate-supercritical segment is exceptional.

The continued-fraction dichotomy further says that sufficiently late such segments must either

1. use a convergent `D_j/H_j` of `alpha`, or
2. pay a combinatorial-overload cost `m_jH_j \gtrsim N_{j+1}`.

## 4. Final nonperiodic theorem target

A complete aperiodic exclusion theorem may now be stated without the Mode I/Mode II split:

### Renewal-Floor Exclusion Target

Prove that no positive ordinary integer can generate an infinite exact renewal-floor chain

\[
\boxed{N_0<N_1<N_2<\cdots}
\]

whose segments all satisfy the exact Collatz aggregate transition and in which every aggregate-supercritical segment obeys the forced renewal resonance constraints.

Equivalently: every positive-integer nonperiodic Collatz orbit must eventually fail the no-first-descent condition.

## 5. Two terminal tasks for a complete first-descent proof

The full proof architecture can therefore be reduced again to two terminal exclusions:

\[
\boxed{
\begin{array}{ll}
\text{Periodic branch:}&\text{exclude every nontrivial exact return cycle},\\[1mm]
\text{Aperiodic branch:}&\text{prove Renewal-Floor Exclusion.}
\end{array}
}
\]

Once both are proved, no infinite first-descent counterexample remains. Strong induction then yields the Collatz conjecture.

## 6. Role of the older Mode I/II results

They are not discarded.

- Mode I provides a particularly thin one-block renewal sublanguage with exponential Haar contraction, diffuse long near-critical block necessity, and exact 3-adic core addresses.
- Mode II motivated the multi-block renewal aggregation and the resonance bound.

They now serve as diagnostic subclasses and potential lemmas inside the unified renewal proof rather than separate mandatory terminal theorems.

## 7. Current missing arithmetic engine

The remaining aperiodic obstruction is not local parity formation. Every finite renewal/block word remains arithmetically realizable in a thin residue class.

A successful theorem must use at least one genuinely global ingredient, such as:

- formation-floor growth across renewal segments;
- a well-founded discrete renewal budget;
- incompatibility between repeated continued-fraction resonance and the exact mixed 2-adic/3-adic formation addresses;
- or an aggregate mass/progress inequality that survives the renewal quotient.

The principal gain is that this global ingredient now needs to be formulated only once for the renewal-floor chain rather than separately for Mode I and Mode II.