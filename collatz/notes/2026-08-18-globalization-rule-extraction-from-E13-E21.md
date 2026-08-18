# Globalization rule extraction from the E=13--21 layer closures

Date: 2026-08-18

Status: **structural theorem extraction / globalization program**.

The finite current-R1 certificates have already closed every layer

\[
E=13,14,\ldots,21.
\]

The purpose of this note is no longer to extend the brute finite ladder to E=22,
but to identify which parts of the observed mechanism can be promoted to
propositions that scale with a variable cut length.  Nothing below by itself is
a global proof of the Collatz conjecture.  Proven lemmas, finite diagnostics,
and remaining conditional bridges are separated explicitly.

---

## 1. Variable-cut notation

Let H be a variable accelerated-prefix length.  Let

\[
k=e_H
\]

be the number of even events and

\[
q=H-k
\]

be the number of odd events in that prefix.

For the coefficient-surviving branch one necessarily has

\[
3^q\ge 2^H.
\]

Set

\[
\alpha=\log_3 2,\qquad \beta=1-\alpha.
\]

Then

\[
\frac qH\ge\alpha\approx0.6309297536,
\qquad
\frac kH\le\beta\approx0.3690702464.
\]

The finite first-73 formation automata used in E=13--21 are the H=73 instances
of the same variable-cut object.

---

## 2. Proven formation-path cardinality lemma

Let \(\mathcal T_{k,K}\subset \mathbb Z/3^K\mathbb Z\) denote the set of target
residues which survive K levels of the formation subtraction automaton started
at rank k.

A surviving path has a nonincreasing rank sequence

\[
k=a_0\ge a_1\ge\cdots\ge a_K\ge0.
\]

For a fixed rank sequence, the reverse carry recurrence determines at most one
target residue modulo \(3^K\), because 2 is invertible modulo every power of 3.
The number of weakly decreasing length-K rank sequences with values in
\(\{0,\ldots,k\}\) is the multiset coefficient

\[
\binom{K+k}{k}.
\]

Therefore

\[
\boxed{
|\mathcal T_{k,K}|\le\binom{K+k}{k}.
}
\]

In particular, for fixed k,

\[
\boxed{
\frac{|\mathcal T_{k,K}|}{3^K}
\le
\frac{\binom{K+k}{k}}{3^K}
\longrightarrow0.
}
\]

Thus the formation language has polynomial path growth at fixed rank while the
ternary residue space grows exponentially.

---

## 3. Proven coefficient-survival entropy gap

At the natural full formation depth \(K=q=H-k\), the previous lemma gives

\[
|\mathcal T_{k,q}|\le\binom Hk.
\]

Since coefficient survival requires \(3^q\ge2^H\), and since
\(k/H\le\beta<1/2\), the binary-entropy bound gives

\[
\binom Hk
\le
2^{H H_2(k/H)}
\le
2^{H H_2(\beta)}.
\]

Hence

\[
\boxed{
\frac{|\mathcal T_{k,q}|}{3^q}
\le
2^{-\delta H},
}
\]

where

\[
\boxed{
\delta
=1-H_2(1-\log_3 2)
=1-H_2(\log_3 2)
\approx0.05004447281.
}
\]

Equivalently the coefficient-surviving branch supplies at least
\(\delta H\) bits of formation exclusion information.

The related proportional-rank threshold follows from Stirling asymptotics.  If
\(K=ck\), the path-density exponent changes sign at

\[
c_*\approx1.5581320670.
\]

The coefficient-survival boundary has

\[
\frac qk\ge\frac{\log_3 2}{1-\log_3 2}
\approx1.7095112914>c_*.
\]

Thus there is a genuine positive exponential gap; this is not merely the
fixed-k polynomial-vs-exponential observation.

---

## 4. Exact zero-carry attractor lemma for the formation automaton

Write a nonpositive carry as \(c=-x\), \(x\ge0\).  A rank transition
\(a\to b\le a\) becomes

\[
x'=
\frac23\left(x-(2^a-2^b)\right).
\]

If a path ever enters positive carry, all later carries stay positive.  Hence a
path that eventually reaches carry zero remains in the nonpositive-carry sector
until zero.

### Lemma

If a positive integer x at rank a can reach carry zero in finitely many valid
formation transitions, then, with \(t=v_2(x)\),

\[
\boxed{
0\le t\le a-1,
\qquad
x\le2^t3^{a-t-1}\le3^{a-1}.
}
\]

The final bound is sharp.

### Proof sketch

Induct on the rank a.  Before the first strict rank drop, suppose there are m
same-rank steps.  They replace x by \((2/3)^m x\), so the reverse reconstruction
multiplies by \((3/2)^m\) and requires enough 2-adic valuation.

At the first strict drop \(a\to b<a\), write the next nonnegative value as y:

\[
x_m=2^a-2^b+\frac32y.
\]

If \(y=0\), then \(v_2(x_m)=b\), and the required estimate reduces to

\[
2^d-1\le3^{d-1},\qquad d=a-b\ge1.
\]

If \(y>0\), the reverse transition forces y to be even.  Applying the induction
hypothesis at rank b, and writing \(s=v_2(y)\), gives

\[
y\le2^s3^{b-s-1},\qquad1\le s\le b-1.
\]

Now \(v_2(3y/2)=s-1<b=v_2(2^a-2^b)\), so the valuation of \(x_m\) is exactly
\(s-1\).  After cancelling the initial same-rank factors, the desired estimate
reduces to

\[
2^{d+1}(2^A-1)+3^d\le3^{A+d},
\qquad A=a-b\ge1,\ d=b-s\ge1,
\]

which follows from

\[
2(2/3)^d(2^A-1)\le 3^A-1.
\]

Sharpness is attained by \(x=3^{a-1}\): after \(a-2\) same-rank steps it becomes
\(3\,2^{a-2}\), and the drop \(a\to a-2\) has exactly the same subtraction
\(2^a-2^{a-2}=3\,2^{a-2}\), reaching zero.

Consequently an infinite formation path at fixed initial rank k can occur only
for a finite zero-attractor target set contained in

\[
1\le x\le3^{k-1}.
\]

This fact is stronger than density decay, but a global Collatz application still
requires compatibility with a variable cut H, because the target itself changes
with H.

---

## 5. Proven axis-split static aggregation identity

The static-mass identity already used in the m=44 certificates is a special case
of a general branch-axis statement.

For one parent state p, let an axis extension have b children with nonnegative
masses

\[
c_{p,0},\ldots,c_{p,b-1},
\qquad
C_p=\sum_i c_{p,i},
\qquad
\bar c_p=C_p/b.
\]

Let \(\varepsilon_{p,i}\in\{0,1\}\) indicate whether child i survives the next
constraint and let

\[
m_p=\sum_i\varepsilon_{p,i}.
\]

Then the surviving child mass is exactly

\[
\sum_i\varepsilon_{p,i}c_{p,i}
=
C_p-\frac{b-m_p}{b}C_p
+
\sum_i\varepsilon_{p,i}(c_{p,i}-\bar c_p).
\]

Summing over parents gives

\[
\boxed{
C'=C-\frac{D}{b}+K,
}
\]

with

\[
D=\sum_p(b-m_p)C_p,
\qquad
K=\sum_{p,i}\varepsilon_{p,i}(c_{p,i}-\bar c_p).
\]

Because the child deviations sum to zero for each parent,

\[
|K|
\le
U,
\qquad
U:=\frac12\sum_{p,i}|c_{p,i}-\bar c_p|.
\]

Therefore

\[
\boxed{
C'\le C\left(1-\gamma\right),
\qquad
\gamma=rac{D/b-U}{C}.
}
\]

For b=2 this reduces to the existing m=44 identity

\[
2C'=2C-D+K_{\rm bin},
\qquad |K_{\rm bin}|\le U_{\rm bin}.
\]

This supplies the precise static-aggregation meaning of "exclusion strengthening":
D is the balanced exclusion capacity and U is the amount by which address-mass
imbalance can repair that exclusion.

---

## 6. Proven cumulative-exclusion criterion

Suppose successive finite layers have nonnegative integer mass \(C_L\), and the
previous identity gives

\[
C_{L+1}\le C_L(1-\gamma_L),
\qquad 0\le\gamma_L<1.
\]

Then

\[
C_n
\le
C_{L_0}\prod_{L=L_0}^{n-1}(1-\gamma_L)
\le
C_{L_0}\exp\!\left(-\sum_{L=L_0}^{n-1}\gamma_L\right).
\]

Hence the uniform bound \(\gamma_L\ge\gamma_0>0\) is sufficient but not
necessary.  The weaker condition

\[
\boxed{
\sum_{L\ge L_0}\gamma_L=\infty
}
\]

already implies \(C_n\to0\).  Since the mass is integer-valued, some finite layer
must then satisfy

\[
\boxed{C_n=0}.
\]

This is the desired finite extinction theorem obtained from an exclusion-strengthening
limit without enumerating individual candidates.

---

## 7. Static overlap formulation of the remaining global bridge

For a candidate layer at cut H and odd count q, aggregate its target addresses
modulo \(3^q\):

\[
n_r=\#\{\text{candidate targets congruent to }r\pmod{3^q}\}.
\]

The exact formation survivor mass is the static inner product

\[
\boxed{
S_{H,q}
=
\sum_{r\bmod3^q}
 n_r\,\mathbf 1_{\mathcal T_{H-q,q}}(r).
}
\]

Define the relative overlap/correlation factor

\[
\Xi_{H,q}
:=
\frac{S_{H,q}/N_{H,q}}
{|\mathcal T_{H-q,q}|/3^q},
\]

when \(N_{H,q}>0\).  Exact equidistribution would give \(\Xi=1\), but that is
far stronger than necessary.

By the entropy-gap lemma,

\[
\frac{S_{H,q}}{N_{H,q}}
\le
\Xi_{H,q}\,2^{-\delta H}.
\]

Therefore it is enough to prove the weaker correlation-growth bound

\[
\boxed{
\limsup_{H\to\infty}
\frac{\log_2\Xi_{H,q}}{H}
<\delta
\approx0.05004447281
}
\]

uniformly over the coefficient-surviving q-layers relevant to the reduced core.
A subexponential bound \(\Xi_{H,q}=2^{o(H)}\) would be more than enough.

This is weaker than proving a uniform spectral gap or full equidistribution.
The existing Fourier-transfer diagnostics can therefore be redirected toward
this narrower correlation inequality.

---

## 8. Calibration supplied by the E=13--21 closures

For the repeated worst first-73 rank k=9, the exact formation target densities
are

\[
\begin{array}{c|c}
K&|\mathcal T_{9,K}|/3^K\\\hline
15&0.0450310257081\\
18&0.00706080622391\\
21&0.000882302807648
\end{array}
\]

For E=19,20,21 the measured overlap factors are already very close to one:

\[
\begin{array}{c|ccc}
E&\Xi_{K=15}&\Xi_{K=18}&\Xi_{K=21}\\\hline
19&1.000249&1.000818&1.003202\\
20&0.999502&0.999193&1.004375\\
21&0.999547&0.999083&0.999549
\end{array}
\]

These finite values do **not** prove an asymptotic correlation bound, but they
show that the E=13--21 data are calibrating exactly the quantity now identified
as the missing globalization bridge.

---

## 9. Event-position rule: useful but not the global engine

The exact relaxed event-position vectors exhibit a low-dimensional tail over the
range that produced the E=13--21 certificates.  Extending the exact optimizer
without enumerating Collatz starts gives

\[
\begin{array}{c|c}
E&\text{nontrivial tail dimension}\\\hline
16\ldots40&6\\
41\ldots55&7\\
56\ldots64&8
\end{array}
\]

and the tail dimension continues to grow later.  Thus the observed six-tail
shape is a genuine finite structural regularity, but not a global invariant.
For sufficiently large E at the fixed R1 horizon, the dense prefix itself
saturates and the tail grows again.

The event-position machinery should therefore be retained as an **axis/budget
upper-bound channel**, not used as the sole globalization theorem.

---

## 10. Axiom-system interpretation

The three project tools have distinct roles.

### Formation Axiom System

Use it to define the candidate as an intersection of simultaneously required
channels.  A missing channel removes a state from the candidate set; it is not
merely a numerical zero.

### Axis Property Axiom System

Use it to formalize extension along independent coordinates: event rank, event
position, remaining budget, dyadic lift, ternary lift, and formation carry.
Monotone rank is the key axis property behind the formation path bound.

### Static Aggregation

Aggregate whole address classes rather than individual starts.  The mass identity

\[
C'=C-D/b+K
\]

separates structural exclusion capacity D from concentration/imbalance repair K.
The cumulative criterion turns repeated local exclusions into finite global
extinction.

---

## 11. Current globalization target

The brute E=22 calculation is no longer the principal target.  The central
remaining theorem is now:

> **Correlation / imbalance theorem.**  Along the reduced coefficient-surviving
> core, candidate address mass cannot concentrate on the formation target
> language at exponential rate \(\delta\) or faster.

Equivalent sufficient forms include either

\[
\limsup_H H^{-1}\log_2\Xi_H<\delta,
\]

or a static-transport statement giving a divergent cumulative exclusion credit

\[
\sum_L\gamma_L=\infty.
\]

If this theorem is established uniformly under the already proved reduction
steps, the layer-by-layer computations are replaced by a genuine inductive / mass
transport argument.

The existing E=13--21 closures then become finite calibration certificates rather
than the proof itself.
