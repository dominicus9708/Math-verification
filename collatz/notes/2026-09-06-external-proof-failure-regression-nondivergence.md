# External Collatz proof failure as DSD regression tests: non-divergence quantifier errors

Date: 2026-09-06

Source audited: *Resolution of the Collatz Conjecture: A Rigorous Analysis of Collatz Sequences and their Unique Cycle*, Preprints.org manuscript `202406.0256`, v4.

Status: **D — GLOBAL NON-DIVERGENCE ARGUMENT FAILS.**  This note does not claim that every statement in the manuscript is false.  It isolates explicit logical failures in the displayed non-divergence proof and converts them into reusable DSD regression rules.

---

## 1. Claimed target

The manuscript attempts to prove that no positive Collatz trajectory is divergent.

It considers the standard map

\[
C(n)=\begin{cases}
n/2,&n\text{ even},\\
3n+1,&n\text{ odd}.
\end{cases}
\]

and defines divergence in the ordinary eventual sense:

\[
\forall M\ \exists K\ \forall k\ge K:\ a_k>M.
\]

Three displayed arguments are sufficient to reject the proof of non-divergence as written.

---

## 2. Failure A: no two consecutive increasing standard steps does not exclude divergence

The manuscript observes that if `a_N` is odd then

\[
a_{N+1}=3a_N+1
\]

is even. Therefore the next standard Collatz step is division by two; in particular one cannot have two consecutive odd `3n+1` steps.

This is correct locally.

The attempted conclusion is that an orbit therefore cannot grow without bound.

That conclusion does not follow.

A divergent sequence need not be eventually monotone and need not increase at every step.  It can have infinitely many local decreases while its long-term envelope tends to infinity.

For the Collatz map, an odd-even pair gives

\[
n\mapsto3n+1\mapsto\frac{3n+1}{2},
\]

and for every odd `n>1`,

\[
\frac{3n+1}{2}>n.
\]

Thus even the mandatory decrease from `3n+1` to `(3n+1)/2` does not erase the net growth of the two-step block.

DSD failure type:

\[
\boxed{
\text{local non-monotonicity}
\not\Rightarrow
\text{global boundedness/non-divergence}.
}
\]

Regression rule: never replace a cumulative/limsup growth question by a one-step sign pattern unless a genuine Lyapunov or telescoping estimate is supplied.

---

## 3. Failure B: well-ordering does not contradict eventual escape above the minimum

The manuscript next considers an infinite set of visited values

\[
S=\{a_k:k\ge0\}
\]

and notes that, by well-ordering, `S` has a least element `m`.

For a divergent trajectory, there is a `K` such that

\[
a_k>m\qquad(k\ge K).
\]

The manuscript treats this as a contradiction with the existence of the least element.

There is no contradiction.  The least value `m` may occur only once, or finitely many times, before time `K`.  Divergence explicitly permits all early values to lie below all sufficiently late values.

A simple unrelated example is

\[
a_k=k+1.
\]

Its value set has least element `1`, and nevertheless

\[
a_k>1
\]

for every `k>=1`; indeed it diverges to infinity.

DSD failure type: **quantifier/time-domain confusion**.

The statements

\[
\exists m\in S:\forall s\in S,\ m\le s
\]

and

\[
\exists K:\forall k\ge K,\ a_k>m
\]

are perfectly compatible.

Regression rule:

\[
\boxed{
\text{global minimum attained at finite time}
\not\Rightarrow
\text{minimum is revisited arbitrarily late}.
}
\]

---

## 4. Failure C: an n-dependent exponential upper bound does not contradict divergence

The manuscript proves the elementary one-step estimate

\[
a_{k+1}\le3a_k+1.
\]

It then derives an exponential upper bound depending on the iteration index, schematically

\[
a_n\le(3a_0+1)^n,
\]

and states that this contradicts divergence.

It does not.

A divergent sequence only requires that `a_n` exceed every **fixed** bound eventually.  An upper bound `B_n` that itself tends to infinity is fully compatible with divergence.

For example,

\[
a_n=n
\]

satisfies

\[
a_n\le2^n
\]

for all sufficiently large `n`, while still diverging.

DSD failure type: **nonuniform bound promoted to boundedness**.

The required conclusion would need

\[
\exists B<\infty:\forall n,\ a_n\le B,
\]

whereas the displayed estimate gives only

\[
\forall n,\ a_n\le B(n)
\]

with

\[
B(n)\to\infty.
\]

Regression rule:

\[
\boxed{
\forall n\;a_n\le B(n),\ B(n)\to\infty
\not\Rightarrow
\sup_n a_n<\infty.
}
\]

---

## 5. Consequence

Any one of the three failures is enough to leave non-divergence unproved.  Together they show that the manuscript's case exhaustion does not establish

\[
\forall n\in\mathbb N_{>0},\quad \sup_k C^k(n)<\infty.
\]

The global proof claim therefore does not follow from the displayed non-divergence section.

This verdict does not depend on computation or on any unresolved deep Collatz theorem; it is a direct audit of the logical implications used.

---

## 6. What can still be retained

The manuscript's elementary definitions and trivial local observations may of course be correct.  In particular:

- `3n+1` is even for odd `n`;
- the map has an elementary one-step growth bound;
- finite visited sets imply eventual cycling for deterministic iteration.

What cannot be retained is the jump from those local facts to universal non-divergence.

---

## 7. DSD anti-pattern library extracted from this failure

### AP-1 — local sign pattern to global trend

Forbidden upgrade:

\[
\text{no two consecutive growth steps}
\Rightarrow
\text{no divergence}.
\]

Required repair: cumulative log-growth, stopping-time, Lyapunov, or comparable global control.

### AP-2 — set minimum to recurrence

Forbidden upgrade:

\[
S\text{ has a least element}
\Rightarrow
\text{the orbit cannot eventually stay above it}.
\]

Required repair: a recurrence theorem or return mechanism, not well-ordering alone.

### AP-3 — moving upper bound to uniform boundedness

Forbidden upgrade:

\[
a_n\le B_n\quad\forall n
\Rightarrow
\sup a_n<\infty
\]

when `B_n` is unbounded.

Required repair: a uniform constant or a bound whose asymptotic behavior itself contradicts the hypothesized growth.

### AP-4 — case labels do not imply exhaustive proof

Naming cases such as monotone growth / oscillation / non-monotone unbounded growth is not enough.  Each case must be excluded by an implication matching the precise quantifiers in the definition of divergence.

---

## 8. Regression against the current internal program

The present DSD Collatz route passes these three tests so far:

1. `paradoxical first crossing` is defined by an exact endpoint inequality, not by a local sign heuristic;
2. the inverse-limit ghost criterion distinguishes finite-time minima from asymptotic stabilization;
3. `FINITE ONLY` bounds and growing envelopes are never called uniform boundedness;
4. almost-all or density decay is not promoted to emptiness without an atom/integer bridge.

These rules should remain permanent audit checks for every future external or internal closure argument.

---

## 9. Verdict

\[
\boxed{
\text{The audited non-divergence proof fails by explicit quantifier and uniformity errors.}
}
\]

The value of the failed proof to the DSD program is therefore negative but concrete: it supplies three reusable prohibited-upgrade rules.
