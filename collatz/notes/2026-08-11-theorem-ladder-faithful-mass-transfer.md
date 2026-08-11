# Collatz theorem ladder: faithful mass, local hazards, and attribute transfer

Date: 2026-08-11

Status: **proof architecture with several exact proved reductions and one explicit conditional global certificate**. This note does not claim a proof of the Collatz conjecture.

## 0. Map and first-descent target

Use the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Define

\[
\tau(n):=\min\{k\ge1:T^k(n)<n\},
\]

with \(\tau(n)=\infty\) if no such time exists.

For positive integers,

\[
\boxed{\text{Collatz}\iff \tau(n)<\infty\text{ for every }n>1.}
\]

The forward implication is immediate. The reverse implication follows by strong induction on the starting integer.

---

## 1. Unresolved sets

For \(k\ge0\), define

\[
\boxed{
U_k:=\{n\ge2:T^j(n)\ge n\text{ for all }1\le j\le k\}.
}
\]

Then

\[
U_{k+1}\subseteq U_k,
\]

and

\[
\boxed{
\bigcap_{k\ge0}U_k
=\{n\ge2:\tau(n)=\infty\}.
}
\]

Hence

\[
\boxed{
\text{Collatz}\iff\bigcap_{k\ge0}U_k=\varnothing.
}
\]

This is an exact reformulation, not yet a proof advance.

---

## 2. Exact channel representation

At depth \(k\), write

\[
n=r+2^k m.
\]

The exact prefix identity implies that within a fixed realizable residue channel, every no-first-descent constraint is affine in \(m\). Therefore the unresolved subset of the channel is an integer interval

\[
I_k(r)=[L_k(r),U_k(r)]\cap\mathbb Z,
\]

possibly empty or unbounded.

A channel state may therefore be represented as

\[
s=(k,r,y,q,[L,U]),
\]

with represented natural-number set

\[
\boxed{
\llbracket s\rrbracket
:=\{r+2^k m:m\in[L,U]\cap\mathbb Z\}.
}
\]

For the exact survivor channel family \(K_k\),

\[
\boxed{
U_k=\bigsqcup_{s\in K_k}\llbracket s\rrbracket.
}
\]

The exact binary refinement previously derived gives a closed state transition at arbitrary depth.

---

## 3. Full-support finite measure on the natural numbers

Assign the dyadic weight

\[
\boxed{w_n:=2^{1-n},\qquad n\ge2.}
\]

Then

\[
\sum_{n=2}^{\infty}w_n=1,
\]

and every singleton has strictly positive mass.

For \(A\subseteq\mathbb N_{\ge2}\), define

\[
\mu(A):=\sum_{n\in A}w_n.
\]

Because every \(w_n>0\),

\[
\boxed{\mu(A)=0\iff A=\varnothing.}
\]

This full-support property is the key difference from natural density: a finite or sparse counterexample set cannot disappear inside a zero-measure exceptional set.

Define the unresolved mass

\[
\boxed{M_k:=\mu(U_k).}
\]

Since \(U_k\) is decreasing and \(\mu(U_0)=1<\infty\), continuity from above gives

\[
\lim_{k\to\infty}M_k
=\mu\!\left(\bigcap_{k\ge0}U_k\right).
\]

Hence

\[
\boxed{
\text{Collatz}\iff M_k\to0.
}
\]

This is an exact integral-style reformulation.

---

## 4. Faithful-mass theorem

Let

\[
\nu(k):=\min U_k
\]

when \(U_k\neq\varnothing\).

Since \(\nu(k)\in U_k\),

\[
M_k\ge2^{1-\nu(k)}.
\]

Since \(U_k\subseteq\{n\ge\nu(k)\}\),

\[
M_k
\le\sum_{n=\nu(k)}^{\infty}2^{1-n}
=2^{2-\nu(k)}.
\]

Therefore

\[
\boxed{
2^{1-\nu(k)}\le M_k\le2^{2-\nu(k)}.
}
\]

Equivalently,

\[
\boxed{
\nu(k)-2
\le
-\log_2 M_k
\le
\nu(k)-1.
}
\]

Thus \(-\log_2 M_k\) tracks the unresolved frontier to within one unit. The mass aggregation does not average away sparse small survivors.

Consequently,

\[
\boxed{
M_k\to0\iff\nu(k)\to\infty.
}
\]

---

## 5. Exact channel mass

For a channel

\[
\llbracket s\rrbracket
=\{r+2^k m:L\le m\le U\},
\]

its mass is a geometric series.

If \(U<\infty\),

\[
\boxed{
\mu(s)
=
2^{1-r-2^kL}
\frac{1-2^{-2^k(U-L+1)}}{1-2^{-2^k}}.
}
\]

If \(U=+\infty\),

\[
\boxed{
\mu(s)
=
\frac{2^{1-r-2^kL}}{1-2^{-2^k}}.
}
\]

Hence an infinite residue interval can be integrated exactly from its state boundaries without enumerating its members.

Because the channel family partitions \(U_k\),

\[
\boxed{M_k=\sum_{s\in K_k}\mu(s).}
\]

---

## 6. Dissipation identity and stopping-time survival function

The unresolved mass is exactly the survival function of the first-descent time under the probability distribution \(w_n\):

\[
\boxed{
M_k
=
\sum_{n\ge2}w_n\mathbf1_{\{\tau(n)>k\}}.
}
\]

Define the newly resolved mass at step \(k+1\) by

\[
\boxed{
D_{k+1}:=M_k-M_{k+1}.
}
\]

Then

\[
\boxed{
D_{k+1}
=
\sum_{\tau(n)=k+1}w_n.
}
\]

Since \(M_0=1\),

\[
\boxed{
M_k=1-\sum_{j=1}^{k}D_j.
}
\]

Therefore

\[
\boxed{
\text{Collatz}\iff\sum_{j=1}^{\infty}D_j=1.
}
\]

The conjecture can thus be stated as complete dissipation of the initial full-support mass.

---

## 7. Local channel hazard

For a survivor channel \(s\in K_k\), let \(\mathrm{Ch}(s)\subseteq K_{k+1}\) be its exact surviving child channels after binary refinement and the new no-descent inequality.

Define its surviving child mass

\[
\mu^+(s):=\sum_{s'\in\mathrm{Ch}(s)}\mu(s').
\]

Since the surviving children represent a subset of the parent,

\[
0\le\mu^+(s)\le\mu(s).
\]

Define the local hazard

\[
\boxed{
\eta(s):=1-\frac{\mu^+(s)}{\mu(s)}\in[0,1].
}
\]

This is the exact fraction of the parent's dyadic mass that is resolved at the next refinement.

The global hazard is the mass-weighted average

\[
\boxed{
\bar\eta_k
:=
\sum_{s\in K_k}
\frac{\mu(s)}{M_k}\eta(s).
}
\]

Then exactly

\[
\boxed{
M_{k+1}=(1-\bar\eta_k)M_k.
}
\]

Therefore, while \(M_k>0\),

\[
\boxed{
M_k
=
\prod_{j=0}^{k-1}(1-\bar\eta_j).
}
\]

If no factor is exactly zero, the infinite product vanishes iff

\[
\boxed{
\sum_{j=0}^{\infty}\bar\eta_j=\infty.
}
\]

Thus another exact global target is divergence of cumulative unresolved-mass hazard.

---

## 8. Purpose of the attribute frame

Let an attribute map

\[
\Phi(s)=a
\]

assign each exact channel to an attribute class \(a\in\mathcal A\).

The purpose of the attributes is not descriptive richness. They should retain only information needed to establish one or more of:

1. formation soundness;
2. a lower bound on local hazard \(\eta(s)\);
3. a bound on child attribute classes;
4. a frontier increase when hazard is weak.

Candidate raw information from earlier work includes coefficient balance, correction/headroom, valuation, carry/wrap data, and 2-adic/3-adic alignment. These are not yet assumed to be minimal.

---

## 9. Attribute-mass vector

For each attribute class \(a\in\mathcal A\), define

\[
\boxed{
m_k(a):=
\sum_{\substack{s\in K_k\\\Phi(s)=a}}
\mu(s).
}
\]

Then

\[
M_k=\sum_{a\in\mathcal A}m_k(a).
\]

The desired abstraction should be dynamically closed: child classes must be determined or safely over-approximated from the parent class without inspecting individual natural numbers.

---

## 10. Conditional finite transfer certificate

Suppose \(\mathcal A=\{1,\dots,d\}\) is finite and there exists a fixed nonnegative matrix

\[
P\in\mathbb R_{\ge0}^{d\times d}
\]

such that for every depth \(k\),

\[
\boxed{
\mathbf m_{k+1}\le P\mathbf m_k
}
\]

componentwise.

Crucially, the entries of \(P\) must be proved worst-case bounds valid for every exact channel in each attribute class. They may not be empirical transition frequencies from a finite sample.

Assume there exists a vector \(v\in\mathbb R_{>0}^d\) and a constant \(0\le\lambda<1\) such that

\[
\boxed{
v^\top P\le\lambda v^\top.
}
\]

Then, with

\[
V_k:=v^\top\mathbf m_k,
\]

we have

\[
V_{k+1}\le\lambda V_k,
\]

so

\[
V_k\le\lambda^kV_0\to0.
\]

Because \(v_{\min}:=\min_i v_i>0\),

\[
M_k\le\frac{V_k}{v_{\min}}\to0.
\]

Hence

\[
\boxed{
\text{exact finite attribute abstraction}
+
\text{valid transfer majorant }P
+
v^\top P\le\lambda v^\top,\ \lambda<1
\Longrightarrow
\text{Collatz}.
}
\]

This is a complete conditional proof certificate. The unresolved task is to construct an attribute abstraction and symbolic transfer bounds satisfying its hypotheses.

For a finite fixed matrix, spectral radius \(\rho(P)<1\) is an equivalent contraction target; the positive-vector inequality is often a more explicit proof certificate.

---

## 11. Block and mixed certificates

One-step uniform contraction may be too strong. The same theorem applies to a fixed block operator \(P_B\) satisfying

\[
\mathbf m_{k+B}\le P_B\mathbf m_k
\]

and a contraction certificate

\[
v^\top P_B\le\lambda v^\top,
\qquad\lambda<1.
\]

If a finite abstraction cannot contract uniformly because of critical states, augment it with a well-founded rank or frontier coordinate. A mixed progress certificate can take the form

\[
\boxed{
\text{mass contraction}
\quad\lor\quad
\text{strict well-founded progress}.
}
\]

The critical states are exactly those attribute classes where the transfer operator fails to lose sufficient mass; they should be refined only until their persistence can be ruled out symbolically.

---

## 12. Proof ladder and status

### Exact / already established or elementary

1. First-descent equivalence.
2. Nested unresolved sets.
3. Exact residue-cylinder affine representation.
4. Exact interval aggregation.
5. Exact channel refinement.
6. Full-support dyadic measure.
7. Faithful-mass theorem.
8. Exact channel-mass formula.
9. Dissipation and hazard identities.

### Definition/construction task

10. Choose a minimal dynamically closed attribute frame \(\Phi\).
11. Prove exact or safe symbolic child-class bounds.

### Main unproved theorem target

12. Produce either:
   - a transfer contraction certificate;
   - a frontier escape theorem;
   - a mixed mass/rank progress theorem.

Any finite numerical audit is subordinate to steps 10--12: it may discover candidate classes or falsify candidate inequalities, but it is not part of the universal quantification of the final proof.

---

## 13. Anti-enumeration criterion

A proposed proof route is accepted as genuinely non-enumerative only if all four hold:

1. **Universality:** every \(n>1\) is represented by the exact state system.
2. **Closure:** the same fixed attribute rules apply at arbitrary depth.
3. **Soundness:** pruning and transfer bounds are proved for entire classes, not sampled members.
4. **Asymptotic termination:** \(M_k\to0\), \(\nu(k)\to\infty\), or an equivalent well-founded termination statement follows without any growing numerical cutoff \(n\le N\) or depth cutoff \(k\le K\).

This criterion is intended to prevent a disguised return from natural-number enumeration to attribute-class enumeration.
