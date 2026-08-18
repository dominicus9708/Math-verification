# Static transversality budget identity

Date: 2026-08-18

Status: **exact algebraic decomposition of the remaining globalization bridge**.

This note continues the rule extraction from the exact E=13--21 closures.
It does not prove the Collatz conjecture.  Its purpose is to replace the vague
request for equidistribution by two explicit static-aggregation bias terms whose
cumulative size is the only remaining issue in the formation-overlap channel.

---

## 1. Formation tree and candidate mass

For formation depth K let

\[
T_K\subset \mathbb Z/3^K\mathbb Z
\]

be the allowed formation target residues and put

\[
A_K=|T_K|.
\]

The reduction map modulo \(3^K\) sends \(T_{K+1}\) into \(T_K\).  Thus each
formation parent \(r\in T_K\) has three ternary lifts

\[
r+j3^K,\qquad j\in\{0,1,2\}.
\]

Let

\[
\varepsilon_{r,j}\in\{0,1\}
\]

indicate whether that lift belongs to \(T_{K+1}\), and define its formation
child multiplicity

\[
m_r=\sum_{j=0}^2\varepsilon_{r,j}\in\{0,1,2,3\}.
\]

Then exactly

\[
A_{K+1}=\sum_{r\in T_K}m_r.
\]

Now take any finite candidate multiset before the formation filter.  For a
formation parent r, let \(c_{r,j}\) be the candidate mass in its j-th ternary
lift and

\[
C_r=\sum_{j=0}^2 c_{r,j}.
\]

After imposing formation through depth K, let

\[
C_K=\sum_{r\in T_K}C_r.
\]

The next-depth survivor mass is

\[
C_{K+1}=\sum_{r\in T_K}\sum_{j=0}^2
\varepsilon_{r,j}c_{r,j}.
\]

---

## 2. Exact one-step transversality decomposition

Define the candidate parent weight and the uniform formation-parent weight by

\[
w_K(r)=\frac{C_r}{C_K},
\qquad
u_K(r)=\frac1{A_K}.
\]

The uniform formation extension ratio is

\[
\boxed{
 u_K=\frac{A_{K+1}}{3A_K}
     =\frac13\mathbb E_{\nu_K}[m_r].
}
\]

The actual candidate survival ratio is

\[
 r_K=\frac{C_{K+1}}{C_K}.
\]

Write each child mass as

\[
c_{r,j}=\frac{C_r}{3}
       +\left(c_{r,j}-\frac{C_r}{3}\right).
\]

Substitution gives the exact identity

\[
\boxed{
 r_K=u_K+\rho_K+\kappa_K,
}
\]

where

\[
\boxed{
\rho_K
=\frac13\left(
\mathbb E_{w_K}[m_r]-\mathbb E_{\nu_K}[m_r]
\right)
}
\]

is the **parent multiplicity bias**, and

\[
\boxed{
\kappa_K
=\frac1{C_K}
\sum_{r\in T_K}\sum_{j=0}^2
\varepsilon_{r,j}
\left(c_{r,j}-\frac{C_r}{3}\right)
}
\]

is the **within-parent lift bias**.

The two terms have distinct meanings.

1. \(\rho_K>0\): candidate mass has concentrated on formation parents having
   more admissible children than a uniformly chosen formation parent.
2. \(\kappa_K>0\): inside those parents, candidate mass has concentrated on the
   specific ternary lifts which formation keeps.

No other bias term exists in the one-step overlap.

---

## 3. Static-aggregation bounds for the two biases

For the child-lift term define

\[
\eta_K
:=\frac1{2C_K}
\sum_{r\in T_K}\sum_{j=0}^2
\left|c_{r,j}-\frac{C_r}{3}\right|.
\]

Because the three child deviations of every parent sum to zero, the sum over
any selected subset is at most half their \(\ell^1\) norm.  Therefore

\[
\boxed{|κ_K|\le\eta_K.}
\]

For the parent term let

\[
\operatorname{TV}(w_K,\nu_K)
=\frac12\sum_{r\in T_K}|w_K(r)-\nu_K(r)|.
\]

Since \(0\le m_r\le3\),

\[
\boxed{|ρ_K|\le\operatorname{TV}(w_K,\nu_K).}
\]

These are sufficient but generally not sharp.  The exact quantities
\(\rho_K,\kappa_K\), rather than total variation itself, are the natural targets
because only correlation with the formation extension multiplicity and the
chosen child lifts matters.

---

## 4. Exact product identity for the global correlation factor

Let the initial candidate mass be

\[
C_0=N>0.
\]

Since \(T_0\) consists of the unique residue modulo 1, \(A_0=1\).  Iterating the
candidate and uniform formation ratios gives

\[
\frac{C_K}{N}=\prod_{j=0}^{K-1}r_j,
\qquad
\frac{A_K}{3^K}=\prod_{j=0}^{K-1}u_j.
\]

Hence the relative overlap factor

\[
\Xi_K
:=
\frac{C_K/N}{A_K/3^K}
\]

satisfies the exact factorization

\[
\boxed{
\Xi_K
=\prod_{j=0}^{K-1}\frac{r_j}{u_j}
=\prod_{j=0}^{K-1}
\left(
1+\frac{\rho_j+\kappa_j}{u_j}
\right).
}
\]

Taking base-2 logarithms defines the cumulative **bias-repair budget**

\[
\boxed{
B_K:=\log_2\Xi_K
=\sum_{j=0}^{K-1}
\log_2\left(
1+\frac{\rho_j+\kappa_j}{u_j}
\right).
}
\]

If a step has \(r_j=0\), the candidate set is already empty and no later budget
is needed.

This identity shows that proving full equidistribution is unnecessary.  All
nonuniformity is permitted as long as its cumulative positive repair budget is
smaller than the formation exclusion budget.

---

## 5. Exact exclusion-bits identity

Define the formation information/exclusion budget

\[
I_K:=-\log_2\left(\frac{A_K}{3^K}\right).
\]

Then the definition of \(\Xi_K\) gives the exact identity

\[
\boxed{
\log_2 C_K
=\log_2 N-I_K+B_K.
}
\]

Therefore a nonempty finite candidate layer, for which \(C_K\ge1\), must obey

\[
\boxed{
B_K\ge I_K-\log_2 N.
}
\]

Conversely,

\[
\boxed{
I_K>\log_2N+B_K
\quad\Longrightarrow\quad
C_K=0.
}
\]

This is a finite extinction criterion; no limiting argument is required once the
inequality becomes strict.

---

## 6. Insert the coefficient-survival formation entropy gap

At a variable accelerated cut H, let k be the even-event count and q=H-k the
odd-event count.  The coefficient-surviving branch requires

\[
3^q\ge2^H.
\]

At the natural formation depth K=q, the previously proved path-count lemma and
binary entropy estimate imply

\[
I_q
\ge
\delta H,
\]

with

\[
\boxed{
\delta
=1-H_2(1-\log_3 2)
\approx0.05004447281.
}
\]

Thus every nonempty coefficient-surviving layer necessarily pays

\[
\boxed{
B_q\ge\delta H-\log_2N.
}
\]

The global problem is therefore reduced to showing that the two static bias
channels cannot supply that many repair bits.

---

## 7. Recursive ternary-selector core

For ternary selector depth m, before additional filters there are at most

\[
N\le2^m
\]

candidate selectors.  Therefore nonemptiness at a cut H requires

\[
\boxed{
B_q\ge\delta H-m.
}
\]

Suppose one proves, uniformly on the reduced coefficient-surviving core,

\[
B_q\le\lambda H+o(H)
\]

for some

\[
\lambda<\delta.
\]

Then for every

\[
C>\frac1{\delta-\lambda}
\]

and all sufficiently large m, choosing \(H=Cm\) gives

\[
\delta H-m-B_q>0,
\]

so the survivor mass is zero.  Consequently

\[
\boxed{M_F(m)=O(m).}
\]

In the stronger subexponential-bias case \(B_q=o(H)\), any

\[
C>\frac1\delta\approx19.98223
\]

suffices.

This recovers the earlier approximately 19.98 scale from a rigorous formation
entropy budget.  The remaining conditional part is only the bias-budget bound.

---

## 8. Relation to the project axiom systems

### Formation Axiom System

The sets \(T_K\) are the surviving simultaneous formation channels.  A missing
child lift is channel absence, not a numerical zero.

### Axis Property Axiom System

The passage

\[
r\pmod{3^K}\longrightarrow r+j3^K\pmod{3^{K+1}}
\]

is the ternary extension axis.  The parent multiplicity \(m_r\) measures how
many axial continuations remain compatible with formation.  The candidate mass
\(c_{r,j}\) measures how much of the independent candidate channel enters each
continuation.

### Static Aggregation

The decomposition

\[
r_K=u_K+\rho_K+\kappa_K
\]

is a channel-indexed static aggregation identity.  It separates the intrinsic
formation survival rate from cross-channel concentration at the parent and child
levels.

Thus the desired global proof no longer asks that candidate addresses be
uniform.  It asks only that the cumulative cross-channel repair budget

\[
B_q
\]

grow more slowly than the intrinsic formation exclusion budget

\[
I_q\ge\delta H.
\]

---

## 9. Next theorem target

The remaining globalization theorem can be stated narrowly as follows.

> **Static transversality theorem (target).**  On the recursively sufficient,
> coefficient-surviving core, the cumulative parent-multiplicity and child-lift
> bias satisfies
> \[
> \limsup_{H\to\infty}\frac{B_q}{H}<\delta.
> \]

A stronger but simpler sufficient target is

\[
B_q=o(H).
\]

A block version is also sufficient: find a fixed or slowly growing block size B
for which the accumulated positive bias over each B formation levels is bounded
strictly below the formation exclusion information gained over the same block.

This is the next rule to attack.  It is strictly weaker than a full uniform
spectral-gap or equidistribution theorem.
