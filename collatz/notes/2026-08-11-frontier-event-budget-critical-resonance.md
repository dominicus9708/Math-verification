# Unresolved frontier, odd-event budget, and critical-resonance formulation

Date: 2026-08-11

Status: **exact set-theoretic reduction + exact odd-event resource identities + new critical-resonance theorem target**. This note does not claim a proof of the Collatz conjecture.

## 1. Global unresolved frontier

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

define

\[
U_k
=
\{n\ge2:T^j(n)\ge n\text{ for every }1\le j\le k\}.
\]

Then

\[
U_{k+1}\subseteq U_k.
\]

Define the actual unresolved frontier

\[
\boxed{\nu(k):=\min U_k}
\]

whenever \(U_k\neq\varnothing\).

Because the sets are nested, \(\nu(k)\) is nondecreasing. Moreover,

\[
\boxed{
\text{Collatz}
\Longleftrightarrow
\nu(k)\to\infty.
}
\]

Indeed, if \(\nu(k)\) were bounded, its integer monotonicity would force eventual stabilization at some finite \(n\), and that \(n\) would belong to every \(U_k\). Conversely, an integer with infinite first-descent time bounds \(\nu(k)\) from above for all \(k\).

Thus the earlier pathwise rank \(\rho\) can be compressed to one global frontier.

The frontier values are exactly stopping-time record holders: if \(\nu(k)=n\), then every smaller integer has already descended by time \(k\), whereas \(n\) has not.

---

## 2. Why a second time scale is useful

The accelerated-step clock is exact but counts every factor-of-two removal separately. For the plateau problem it is useful to aggregate each odd state together with the complete following run of powers of two.

For an odd state \(x_j\), define

\[
\boxed{a_j:=v_2(3x_j+1)}
\]

and the odd-to-odd Syracuse event map

\[
\boxed{
x_{j+1}=\frac{3x_j+1}{2^{a_j}}.}
\]

Let

\[
A_q:=\sum_{j=0}^{q-1}a_j,
\qquad A_0=0.
\]

The event index \(q\) counts odd events, while \(A_q\) records the total accelerated-time cost of those events.

This is a coarse-graining of the same trajectory, not a new Collatz map assumption.

---

## 3. Exact triangular event state

Define

\[
\boxed{\lambda_q:=\frac{2^{A_q}}{3^q}}
\]

and

\[
\boxed{
S_q:=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}}.
}
\]

Then the odd-event affine formula gives

\[
\boxed{
x_q=\frac{n+S_q}{\lambda_q}}
\]

for an odd initial integer \(x_0=n\).

The state update is triangular:

\[
\boxed{
\lambda_{q+1}=\lambda_q\frac{2^{a_q}}{3},
}
\]

\[
\boxed{
S_{q+1}=S_q+\frac{\lambda_q}{3}.
}
\]

Thus \(\lambda\) records the multiplicative balance between powers of two and powers of three, while \(S\) is the accumulated affine correction mass.

---

## 4. Exact headroom resource

Define

\[
\boxed{
H_q
:=
1+\frac{S_q}{n}-\lambda_q.
}
\]

Using the endpoint identity,

\[
\boxed{
H_q
=
\lambda_q\left(\frac{x_q}{n}-1\right).
}
\]

Hence

\[
H_q\ge0
\iff
x_q\ge n.
\]

For a trajectory that never descends below its start, every odd-event state satisfies \(H_q\ge0\).

The exact one-event change is

\[
\boxed{
H_{q+1}-H_q
=
\frac{\lambda_q}{3}
\left(3+\frac1n-2^{a_q}\right).
}
\]

For every \(n>1\):

- if \(a_q=1\), then
  \[
  H_{q+1}-H_q
  =
  \frac{\lambda_q}{3}\left(1+\frac1n\right)>0;
  \]
- if \(a_q\ge2\), then
  \[
  H_{q+1}-H_q<0.
  \]

Therefore

\[
\boxed{
\text{valuation }a=1\text{ is the unique local credit event,}
}
\]

whereas every \(a\ge2\) event spends the accumulated headroom.

This gives a precise dynamic meaning to the previously informal idea that a plateau must consume another property when the frontier itself does not move.

---

## 5. Credit runs are 2-adic alignment events

Suppose a maximal run beginning at an odd state \(x\) has

\[
a_0=a_1=\cdots=a_{\ell-1}=1,
\qquad
a_\ell\ge2.
\]

When \(a=1\),

\[
x_{t+1}+1
=
\frac32(x_t+1).
\]

Therefore the run length is not a free symbolic choice. Exactly

\[
\boxed{
\ell=v_2(x+1)-1.
}
\]

Equivalently,

\[
\boxed{
\ell\text{ consecutive credit events}
\iff
x\equiv-1\pmod{2^{\ell+1}}.
}
\]

Thus accumulation of positive headroom requires the current state to lie progressively deeper in the 2-adic neighborhood of \(-1\).

This couples a real-order resource \(H\) to a 2-adic alignment property.

---

## 6. Macroblock dynamics

Aggregate a maximal block consisting of \(\ell\) credit events \(a=1\), followed by one debit event \(b\ge2\).

Let \((\lambda,H)\) be the state at the beginning of the block. Then

\[
\boxed{
\lambda'
=
\lambda\frac{2^{\ell+b}}{3^{\ell+1}}.
}
\]

The exact headroom change is

\[
\boxed{
H'-H
=
\frac{\lambda}{3}
\left[
3\left(1+\frac1n\right)
-
\left(\frac23\right)^\ell
\left(2^b+\frac2n\right)
\right].
}
\]

Define the macroblock multiplier

\[
\boxed{
M_{\ell,b}:=\frac{2^{\ell+b}}{3^{\ell+1}}.
}
\]

A block can therefore do one of three structural things:

1. add headroom but shrink \(\lambda\);
2. spend headroom while increasing or decreasing \(\lambda\);
3. avoid both losses only at a near-resonance between powers of 2 and 3.

---

## 7. Critical-resonance lemma

Assume a macroblock is nonnegative in headroom,

\[
H'-H\ge0,
\]

and also noncontracting in the multiplier coordinate,

\[
M_{\ell,b}\ge1.
\]

Then the macroblock identity gives

\[
\left(\frac23\right)^\ell
\left(2^b+\frac2n\right)
\le
3\left(1+\frac1n\right).
\]

Since

\[
3M_{\ell,b}
=
\left(\frac23\right)^\ell2^b,
\]

we obtain

\[
0
\le
M_{\ell,b}-1
\le
\frac{3-2(2/3)^\ell}{3n}
<
\frac1n.
\]

Hence

\[
\boxed{
H'-H\ge0\text{ and }M_{\ell,b}\ge1
\Longrightarrow
1\le M_{\ell,b}<1+\frac1n.
}
\]

Equivalently,

\[
\boxed{
1
\le
\frac{2^{\ell+b}}{3^{\ell+1}}
<
1+\frac1n.
}
\]

Thus a macroblock that neither spends headroom nor contracts the multiplicative state must satisfy an increasingly sharp Diophantine resonance as \(n\) grows.

This is an exact theorem, not a finite observation.

---

## 8. Relation to the known 2-adic/parity framework

Bernstein and Lagarias constructed the 3x+1 conjugacy between the 2-adic shift and the Collatz map, so representing trajectories by parity information and 2-adic alignment is part of the established framework.

The present variables do not replace that conjugacy. They add a real-order resource \(H\) to the arithmetic/parity state and identify which local valuation events create or spend the resource.

A relevant external boundary result is the theorem of Lopez and Stoll (arXiv:2101.12747): if a rational 2-adic integer has a divergent, non-cyclic trajectory, then the lower limiting proportion of odd entries in its parity vector is exactly

\[
\frac{\log 2}{\log 3}.
\]

In odd-event coordinates this places any divergent rational counterexample on the critical asymptotic boundary between powers of 2 and 3, rather than uniformly inside either side.

Recent parity-vector work of Niu (arXiv:2605.13886), building on Rozier and Terracol (arXiv:2502.00948), likewise reports that the observed exceptional/paradoxical length-height ratios concentrate near continued-fraction approximants of the same critical logarithmic slope. Those results do not prove Collatz or the coefficient-stopping-time conjecture.

The critical-resonance lemma above is independent of that numerical observation, but it points to the same boundary from the headroom-resource side.

---

## 9. Counterexample modes in the new state

If an integer belongs to

\[
\bigcap_{k\ge0}U_k,
\]

its orbit never descends below its start.

There are two cases.

### Bounded orbit

A bounded deterministic integer orbit must eventually repeat. Therefore it gives a nontrivial positive periodic component whose minimum is at least the initial unresolved frontier.

### Unbounded orbit

The orbit is divergent. For a positive integer, hence a rational 2-adic integer, the known parity-density restriction forces the trajectory toward the critical powers-of-2/powers-of-3 boundary.

Thus both failure modes are naturally associated with critical arithmetic balance, although the precise constraints differ for cycles and divergent trajectories.

---

## 10. Revised theorem target: critical-resonance exclusion

The master target remains

\[
\boxed{\nu(k)\to\infty.}
\]

The event-budget calculation suggests a sharper auxiliary target.

### Critical-Resonance Exclusion Target

Prove that no finite positive integer can generate an infinite macroblock path satisfying simultaneously:

1. the exact 2-adic realization constraints of the Collatz map;
2. the no-descent resource constraint
   \[
   H_q\ge0\quad\text{for every event prefix};
   \]
3. the repeated critical-resonance requirements needed to avoid permanent loss of either \(H\) or \(\lambda\).

The point is not to enumerate all macroblocks. Ordinary blocks are structurally dissipative in at least one coordinate. The candidate infinite survivor must repeatedly return to a sparse near-resonant subset.

The next mathematical task is therefore to characterize the arithmetic transition between successive resonant macroblocks and determine whether an eventually finite natural-number residue can traverse that resonant set indefinitely.

---

## 11. Reproducibility audit

The exact algebraic identities are independently checked by

`collatz/src/event_budget_macroblock_audit.py`.

The reference audit output is

`collatz/results/event_budget_macroblock_audit.txt`.

The finite audit checks:

- odd starts 3 through 999 for 80 odd events each;
- 22,381 maximal macroblocks encountered for odd starts 3 through 499 over 100 odd events.

All endpoint, headroom-transition, run-alignment, and macroblock identities pass exactly using rational arithmetic.

These checks validate the implementation of the identities; they are not a convergence proof.
