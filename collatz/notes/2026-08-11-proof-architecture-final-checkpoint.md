# Collatz proof architecture: final checkpoint before computation

Date: 2026-08-11

Status: **proof-design checkpoint only**. This document does **not** claim a proof of the Collatz conjecture. It freezes the non-enumerative logical architecture and identifies the single remaining universal theorem task that any later computation must serve.

## 0. Governing principle

The target is not to verify increasingly large finite ranges of starting integers, parity words, residues, or depths. A valid final proof must cover all positive integers by a fixed exact representation and a fixed universal transition rule.

The accepted proof route must satisfy four anti-enumeration requirements:

1. **Universality** — every integer \(n>1\) belongs to the exact state system;
2. **Closure** — the same finite kind of state/attribute data suffices at arbitrary depth;
3. **Soundness** — every pruning or transfer inequality is proved for an entire state class, not inferred from finite samples;
4. **Asymptotic termination** — convergence follows without a growing cutoff \(n\le N\), \(k\le K\), \(q\le Q\), or analogous exhaustive frontier.

Any route that requires increasing one of those cutoffs is evidence-generating only and is not part of the final universal proof.

---

## 1. First-descent reduction

Use the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Define the first-descent time

\[
\tau(n):=\min\{k\ge1:T^k(n)<n\},
\]

with \(\tau(n)=\infty\) if no descent occurs.

Then

\[
\boxed{\text{Collatz}\iff \tau(n)<\infty\text{ for every }n>1.}
\]

The reverse implication is by strong induction on the starting integer.

This formulation absorbs both possible failure modes — nontrivial cycles and noncyclic divergent orbits — into the single condition \(\tau(n)=\infty\).

---

## 2. Unresolved sets

For each depth \(k\ge0\), define

\[
\boxed{U_k:=\{n\ge2:T^j(n)\ge n\text{ for all }1\le j\le k\}.}
\]

Then

\[
U_{k+1}\subseteq U_k
\]

and

\[
\boxed{\bigcap_{k\ge0}U_k=\{n\ge2:\tau(n)=\infty\}.}
\]

Hence

\[
\boxed{\text{Collatz}\iff\bigcap_{k\ge0}U_k=\varnothing.}
\]

This is the master set formulation.

---

## 3. Exact interval-channel representation

At depth \(k\), write

\[
n=r+2^k m,
\qquad 0\le r<2^k.
\]

For a fixed realizable residue prefix, the exact affine identity gives

\[
T^j(r+2^k m)- (r+2^k m)
=A_{j,k}(r)+B_{j,k}(r)m
\]

for every \(j\le k\).

Therefore the unresolved lift values form an exact integer interval

\[
I_k(r)=[L,U]\cap\mathbb Z,
\]

possibly empty or unbounded.

The current exact reduced state is

\[
\boxed{s=(k,r,d,u,[L,U]),}
\]

where

\[
d:=T^k(r)-r,
\qquad
u:=3^{q_k(r)}.
\]

Then the whole channel endpoint is

\[
\boxed{T^k(r+2^k m)=r+d+u m.}
\]

The represented starting-number set is

\[
\boxed{\llbracket s\rrbracket=\{r+2^k m:m\in[L,U]\cap\mathbb Z\}.}
\]

For the exact survivor family \(K_k\),

\[
\boxed{U_k=\bigsqcup_{s\in K_k}\llbracket s\rrbracket.}
\]

No integer is omitted and no integer outside \(U_k\) is represented as an unresolved state.

---

## 4. Exact closed transition

Choose the next lift bit \(c\in\{0,1\}\) and write

\[
m=c+2m'.
\]

Then

\[
r'=r+c2^k.
\]

Because \(u\) is odd, the next parity is

\[
\boxed{p=(r+d+c)\bmod2.}
\]

The new multiplier is

\[
\boxed{u'=3^p u,}
\]

and the new endpoint displacement is

\[
\boxed{
d'=\frac{3^p(r+d+cu)+p}{2}-r-c2^k.}
\]

The new no-descent half-line is

\[
\boxed{d'+(u'-2^{k+1})m'\ge0.}
\]

Intersecting this with the inherited interval gives the exact child interval.

Thus the state type

\[
(k,r,d,u,[L,U])
\]

is exactly closed at arbitrary depth.

This proves that later work need not introduce new state kinds merely because \(k\) grows.

---

## 5. Formation and filtering contract

Let \(\operatorname{Form}(s)\) denote exact realizability of a candidate state.

Any state removed by a formation or property filter must satisfy

\[
\boxed{\llbracket s\rrbracket\cap U_k=\varnothing.}
\]

Filtering is therefore allowed only when it is **sound**. The retained kernel must preserve

\[
\boxed{U_k=\bigsqcup_{s\in K_k}\llbracket s\rrbracket.}
\]

Candidate filter attributes include:

- multiplicative balance between powers of \(2\) and \(3\);
- affine correction/headroom;
- parity and valuation information;
- carry/wrap data;
- \(2\)-adic and \(3\)-adic alignment.

These attributes are not ends in themselves. An attribute is retained only if it helps prove a universal pruning, surviving-mass bound, child-class bound, or well-founded progress inequality.

---

## 6. Full-support generating measure

Fix any \(z\in(0,1)\) and assign

\[
\boxed{w_n(z):=(1-z)z^{n-2},\qquad n\ge2.}
\]

Then

\[
\sum_{n=2}^{\infty}w_n(z)=1
\]

and every singleton has strictly positive mass.

Define

\[
\mu_z(A):=\sum_{n\in A}w_n(z)
\]

and unresolved mass

\[
\boxed{M_k(z):=\mu_z(U_k).}
\]

Because the sets \(U_k\) decrease and the measure is finite,

\[
\lim_{k\to\infty}M_k(z)
=\mu_z\!\left(\bigcap_{k\ge0}U_k\right).
\]

Since every singleton has positive mass,

\[
\boxed{\mu_z(A)=0\iff A=\varnothing.}
\]

Therefore, for every fixed \(z\in(0,1)\),

\[
\boxed{\text{Collatz}\iff M_k(z)\to0.}
\]

This is the exact integral-style global formulation: the infinite integer set is aggregated without allowing even one finite counterexample to disappear into a null exceptional set.

---

## 7. Exact channel mass

For

\[
\llbracket s\rrbracket
=\{r+2^k m:L\le m\le U\},
\]

the entire channel mass is a geometric sum.

If \(U<\infty\),

\[
\boxed{
\mu_z(s)
=(1-z)z^{r+2^kL-2}
\frac{1-z^{2^k(U-L+1)}}{1-z^{2^k}}.
}
\]

If \(U=+\infty\),

\[
\boxed{
\mu_z(s)
=\frac{(1-z)z^{r+2^kL-2}}{1-z^{2^k}}.
}
\]

Hence infinitely many represented integers are integrated exactly from finite channel boundary data.

---

## 8. Frontier–mass faithfulness

Let

\[
\nu(k):=\min U_k
\]

when \(U_k\neq\varnothing\).

For the special choice \(z=1/2\),

\[
\boxed{2^{1-\nu(k)}\le M_k\le2^{2-\nu(k)}.}
\]

Equivalently,

\[
\boxed{\nu(k)-2\le-\log_2 M_k\le\nu(k)-1.}
\]

Thus the generating mass is faithful to the smallest unresolved integer to within one binary unit. The aggregation does not hide a sparse low-lying survivor.

Consequently,

\[
\boxed{M_k\to0\iff\nu(k)\to\infty.}
\]

---

## 9. Dissipation and local hazard

Define newly resolved mass

\[
D_{k+1}:=M_k-M_{k+1}.
\]

Then

\[
\boxed{D_{k+1}=\sum_{\tau(n)=k+1}w_n.}
\]

Hence

\[
\boxed{\text{Collatz}\iff\sum_{j=1}^{\infty}D_j=1.}
\]

For a survivor channel \(s\in K_k\), let \(\mathrm{Ch}(s)\) denote its exact surviving children and define

\[
\mu_z^+(s):=\sum_{s'\in\mathrm{Ch}(s)}\mu_z(s').
\]

The exact local hazard is

\[
\boxed{\eta_z(s):=1-\frac{\mu_z^+(s)}{\mu_z(s)}.}
\]

The global hazard is the mass-weighted mean

\[
\boxed{\bar\eta_k
=\sum_{s\in K_k}\frac{\mu_z(s)}{M_k(z)}\eta_z(s),}
\]

and

\[
\boxed{M_{k+1}(z)=(1-\bar\eta_k)M_k(z).}
\]

The purpose of the attribute frame is therefore sharpened: retain only information required to control surviving child mass, local hazard, potential, or frontier progress.

---

## 10. Universal survivor-potential certificate

Let

\[
V(s)>0
\]

be a state potential with a uniform lower bound

\[
\boxed{V(s)\ge v_*>0.}
\]

Suppose there exist fixed \(z\in(0,1)\) and \(\lambda<1\) such that **every** exact survivor state satisfies

\[
\boxed{
\sum_{s'\in\mathrm{Ch}(s)}
\mu_z(s')V(s')
\le
\lambda\,\mu_z(s)V(s).
}
\tag{UC}
\]

Define

\[
\mathcal E_k(z)
:=\sum_{s\in K_k}\mu_z(s)V(s).
\]

Summing (UC) over all parents gives

\[
\mathcal E_{k+1}(z)\le\lambda\mathcal E_k(z),
\]

hence

\[
\mathcal E_k(z)\le\lambda^k\mathcal E_0(z)\to0.
\]

Since \(V\ge v_*>0\),

\[
M_k(z)\le\mathcal E_k(z)/v_*\to0.
\]

Therefore

\[
\boxed{
\text{exact state system}
+\text{full-support mass}
+\text{positive potential}
+\text{universal contraction (UC)}
\Longrightarrow\text{Collatz}.
}
\]

This is the main conditional proof certificate.

---

## 11. Fixed-block and finite-attribute versions

One-step contraction is not required. It is enough that some fixed universal block length \(B\ge1\) satisfy

\[
\boxed{
\sum_{s'\in\mathrm{Ch}^{(B)}(s)}
\mu_z(s')V(s')
\le
\lambda\mu_z(s)V(s),
\qquad\lambda<1
}
\]

for every survivor state.

The block length must be fixed independently of depth and starting value.

If the exact state space is quotiented into finitely many attribute classes and the class-mass vector satisfies

\[
\mathbf m_{k+B}\le P_B\mathbf m_k,
\]

then a positive vector \(v\) with

\[
\boxed{v^\top P_B\le\lambda v^\top,\qquad\lambda<1}
\]

is a finite-dimensional special case of the same certificate.

The entries of \(P_B\) must be symbolic worst-case class bounds, not empirical frequencies.

---

## 12. Mixed certificate if uniform contraction fails

If critical states prevent uniform mass contraction, augment the potential with a well-founded rank \(R(s)\).

A sufficient mixed progress statement is:

for every survivor state, within a fixed universal block,

\[
\boxed{
\text{potential-weighted mass contracts}
\quad\text{or}\quad
R\text{ makes strict well-founded progress}.
}
\]

This allows resonant or low-hazard states to be retained without treating them by endless enumeration. Their persistence must instead consume a well-founded resource or force frontier escape.

---

## 13. Final theorem ladder

The proof architecture is now:

\[
\boxed{
\begin{array}{c}
\text{accelerated Collatz map}\\
\downarrow\\
\text{first-descent target}\\
\downarrow\\
U_k\text{ unresolved sets}\\
\downarrow\\
\text{exact interval-channel partition}\\
\downarrow\\
\text{closed endpoint-affine transition}\\
\downarrow\\
\text{sound formation/property filters}\\
\downarrow\\
\text{full-support generating mass }M_k(z)\\
\downarrow\\
\text{attribute/potential transfer inequality}\\
\downarrow\\
M_k(z)\to0\\
\downarrow\\
\bigcap_kU_k=\varnothing\\
\downarrow\\
\forall n>1\ \exists j:T^j(n)<n\\
\downarrow\\
\text{Collatz by strong induction.}
\end{array}
}
\]

---

## 14. What is proved and what is not

### Exact / established within the current program

- first-descent equivalence;
- nested unresolved sets;
- residue-cylinder affine identity;
- interval aggregation;
- exact binary channel refinement;
- endpoint-affine reduced normal form;
- full-support generating measure;
- exact channel-mass formula;
- frontier–mass faithfulness for dyadic mass;
- dissipation identity;
- local/global hazard identity;
- conditional survivor-potential contraction theorem.

### Still unproved and decisive

The remaining core problem is constructive:

\[
\boxed{
\textbf{Find a fixed closed attribute frame and a positive potential }V
\textbf{ for which a universal fixed-step or fixed-block contraction/progress theorem holds.}
}
\]

This is the first point at which genuinely new Collatz mathematics is still required.

---

## 15. Rule for all subsequent computation

No future computation is allowed to function as a substitute for the universal theorem above.

A computation is useful only if it does one of the following:

1. falsifies a proposed universal inequality;
2. discovers which exact state information is necessary for closure;
3. suggests a candidate attribute quotient;
4. suggests a candidate potential \(V\), block length \(B\), or transfer majorant;
5. verifies an already-symbolic derivation against finite examples.

Increasing depth, starting-value cutoff, parity count, or residue range without strengthening the universal theorem is not progress toward proof.

This checkpoint therefore ends the exploratory enumeration phase and begins the attribute/potential construction phase.
