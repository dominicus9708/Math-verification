# Resonance promotion after two J0 gap debits

Date: 2026-08-27

Status: **SAFE LEMMA + exact Worley-Dujella certificate inside the repaired multi-boundary branch.** No ternary Cantor-core entry and no repeated-local pullback is used. This is not a proof of the Collatz conjecture.

## 1. Input from the local repetition theorem

Let

\[
G:=2^{33}.
\]

The repaired second-resonance annulus gives an endpoint gap below

\[
7G.
\]

The first admissible local lower resonance is

\[
(J_0,R_0)
=(10439860591,6586818670),
\]

and every realization of that resonance consumes more than

\[
\frac52G
\]

of additive gap to the same minimal root `N`.

Therefore after two consecutive `J0/R0` returns, the new endpoint has the form

\[
X=N+d,
\qquad
0\le d<2G.
\]

The third `J0/R0` return is already impossible by the gap-debit theorem.  We now determine the first later Diophantine scale at which a coefficient-subcritical prefix can reappear.

## 2. Near-survival inequality at gap below 2G

Suppose `(j,q)` is the first coefficient-subcritical prefix from `X`:

\[
3^q<2^j.
\]

Every proper prefix is coefficient-surviving, hence

\[
R\le q3^{q-1}.
\]

Writing

\[
C=\frac{3^q}{2^j}<1,
\]

minimal-counterexample no-descent gives the necessary inequality

\[
\boxed{
1-C
<
\frac{2G+q/3}{2^{71}}.
}
\]

Put

\[
\alpha=\log_3 2,
\qquad
\delta=j\ln2-q\ln3>0.
\]

For

\[
j<A_0:=114208327604,
\]

we have

\[
q\le Q_0:=72057431991.
\]

The exact rational log enclosure then yields

\[
\left|\alpha-\frac qj\right|
<\frac{K}{j^2}
\]

with

\[
\boxed{K<1.814.}
\]

Hence

\[
2K<3.628.
\]

By the Worley-Dujella adjacent-convergent theorem, every reduced primitive candidate lies in the finite family with

\[
rs<2K,
\]

so, integrally,

\[
\boxed{rs\le3.}
\]

## 3. Complete primitive candidate audit

The exact certificate enumerates every adjacent-convergent combination with

\[
rs\le3,
\]

retains only primitive fractions below `alpha` and below denominator `A0`, and applies the necessary approximation prefilter.

Exactly

\[
\boxed{27}
\]

primitive candidate fractions remain.

As before, an actual pair may be a positive multiple

\[
(q,j)=m(a,b)
\]

of a primitive candidate.

For each candidate put

\[
D_0=b\ln2-a\ln3>0.
\]

Using

\[
1-e^{-mD_0}
\ge
\frac{mD_0}{1+mD_0}
\]

and subtracting

\[
\frac{2G+ma/3}{2^{71}},
\]

gives a concave function of real `m`.  Exact positivity at

\[
m=1
\]

and at

\[
m=\left\lfloor\frac{A_0-1}{b}\right\rfloor
\]

therefore excludes the entire multiplicity interval.

All 27 primitive ranges fail.

Thus

\[
\boxed{
\text{no coefficient-subcritical prefix occurs for }1\le j<A_0.
}
\]

## 4. The promoted first possible scale

At

\[
(A_0,Q_0)
=(114208327604,72057431991),
\]

the same necessary near-survival inequality is no longer contradictory.

Therefore, once the two `J0` gap debits have reduced the endpoint gap below `2G`, the earliest possible coefficient-subcritical scale jumps from `J0` to

\[
\boxed{A_0.}
\]

This is a genuine resonance promotion:

\[
\boxed{
J_0
\xrightarrow{\text{two strict gap debits}}
A_0.
}
\]

Numerically,

\[
\frac{A_0}{J_0}\approx10.94,
\]

so the next admissible subcritical horizon is more than an order of magnitude farther away.

## 5. Relation among the Farey/continued-fraction vectors

The promotion is structurally consistent with the neighboring vectors already identified in the repaired phase geometry:

\[
(A_0,Q_0)
=(J_0,R_0)+(K_1,P_1),
\]

where

\[
(K_1,P_1)
=(103768467013,65470613321)
\]

is the opposite-sided convergent used in the first-to-second resonance bridge.

Thus the local lower resonance `J0` is not unrelated to the global first resonance.  The first global resonance is exactly the Farey sum of that lower scale and the intervening upper scale.

The gap dynamics have now recovered this arithmetic hierarchy dynamically:

\[
\text{large gap}
\Rightarrow
J_0\text{ allowed},
\]

\[
\text{two }J_0\text{ debits}
\Rightarrow
J_0\text{ forbidden},
\]

\[
\text{next admissible scale}
=A_0=J_0+K_1.
\]

## 6. DSD interpretation

This supplies the first explicit **state-dependent scale escalation** in the repaired branch.

The relevant state is no longer only the parity/Beatty phase.  It is the pair

\[
\boxed{
(\text{continued-fraction scale},\ \text{remaining additive gap budget}).
}
\]

A lower resonance consumes gap; once the remaining gap crosses a threshold, that resonance disappears from the describable candidate set and the next Farey scale becomes mandatory.

Symbolically,

\[
\boxed{
\text{gap depletion}
\Longrightarrow
\text{resonance pruning}
\Longrightarrow
\text{scale promotion}.
}
\]

This is stronger than a finite candidate-count reduction because it gives a deterministic transition rule between arithmetic scales.

## 7. Current branch after promotion

After the repaired first and second global boundaries, there are now two deterministic possibilities in the repeated-local branch:

1. the orbit avoids using `J0/R0` twice and must escape earlier into a later coefficient-surviving regime; or
2. it uses `J0/R0` twice, reducing the gap below `2G`, after which **every** proper prefix through `A0-1` is coefficient-surviving and the first possible new crossing is exactly the `A0/Q0` scale.

The next proof-level target is therefore to analyze an `A0/Q0` local return from a gap below `2G`, including its new endpoint gap and whether repeated `A0` use can force another scale escalation.

## 8. Audit classification

- **SAFE:** gap `<2G` after two `J0` debits.
- **SAFE:** uniform near-survival inequality at this gap.
- **SAFE:** exact Worley constant `K<1.814`, hence `rs<=3`.
- **SAFE:** exhaustive primitive/multiplicity exclusion below `A0`.
- **SAFE:** `A0/Q0` is the first nonexcluded promoted pair.
- **OPEN:** endpoint transport across one or more local `A0/Q0` blocks.

Companion certificate:

`collatz/src/post_two_J0_next_scale_A0_certificate.py`
