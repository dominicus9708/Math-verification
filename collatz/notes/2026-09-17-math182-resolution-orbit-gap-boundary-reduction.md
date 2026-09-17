# MATH-182 — resolution / orbit-gap boundary reduction for the low-paid frontier

Date: 2026-09-17

Status: `EXACT STRUCTURAL SYNTHESIS / NON-ENUMERATIVE REDUCTION / r=10 CLOSURE OPEN`

## 1. Purpose

The current objective is not to replace the `r=10` 128-shard computation by another exhaustive executor.

The objective is to extract from the already audited high-paid closures and the DSD audit a proof-facing recurrence that removes ordinary-source enumeration wherever an exact structural inequality is available.

This note combines four already established ingredients:

1. MATH-074 resolution-overshoot Bellman localization;
2. MATH-077 orbit-gap / first-descent threshold;
3. MATH-079 address-versus-correction separation;
4. MATH-080 master affine comparison defect.

No new paid layer is claimed closed here.

## 2. Multi-source symbolic edges are not the Bellman bottleneck

Let an exact same-integer source cylinder contain `M>=1` ordinary source anchors and set

\[
R=\lceil\log_2 M\rceil.
\]

For a legal macro edge of shortcut length `ell`, penalty `p>=0`, and compatible child resolution `R'`, MATH-074 gives

\[
R'\le\max(0,R-\ell)
\]

and with

\[
\lambda=\frac{19}{503},
\qquad H_R=-\lambda R,
\]

\[
\boxed{
p-\lambda\ell+H_{R'}-H_R
\ge p-\lambda(\ell-R)_+.
}
\]

Hence every edge with

\[
\ell\le R
\]

is automatically Bellman-safe:

\[
\boxed{
p-\lambda\ell+H_{R'}-H_R\ge p\ge0.}
\]

Therefore a large unresolved multiplicity is a computational burden, but it is not by itself a mathematical Bellman obstruction.

This corrects the naive interpretation that the increase of maximum multiplicity from `r=11` to `r=10` must worsen the proof inequality. A larger `R` can extend the region in which exact symbolic refinement is automatically paid for by resolution consumption.

## 3. Localize the only possible reduced-cost deficit

Define the exact overshoot deficit

\[
\boxed{
\eta_e:=\bigl[\lambda(\ell-R)-p\bigr]_+.
}
\]

Then:

- if `ell<=R`, `eta_e=0`;
- if `ell>R` but `p>=lambda(ell-R)`, again `eta_e=0`;
- only if `ell>R` and `p<lambda(ell-R)` can `eta_e>0`.

But `ell>R` forces the compatible child to contain at most one source anchor.

Thus every possible Bellman deficit is localized to a terminal same-integer handoff:

\[
\boxed{
\eta_e>0
\Longrightarrow
R'=0.
}
\]

This is the first structural reduction of the `r=10` frontier: the unresolved proof obligation is not the full set of AP sources, but the terminal handoff boundary produced after exact resolution has been consumed.

## 4. Exact orbit-gap threshold removes enumeration inside a fixed cylinder

For a fixed parity prefix, MATH-077 gives

\[
T^k(N)=\frac{N+S}{\rho},
\qquad
\rho=\frac{2^k}{3^q},
\]

and

\[
\boxed{
T^k(N)-N
=\frac{S-N(\rho-1)}{\rho}.
}
\]

If `rho<=1`, that prefix cannot yield strict descent.

If `rho>1`, define

\[
\boxed{
N_*:=\frac{S}{\rho-1}.
}
\]

Then

\[
\boxed{
T^k(N)<N
\iff
N>N_*.
}
\]

Now let an exact dyadic source cylinder be

\[
\boxed{
N(s)=a+2^H s,
\qquad 0\le s<M,
}
\]

with fixed `(S,rho)` on that parity cylinder.

Its master self-defect is

\[
\mathfrak D(s)
=S-(a+2^Hs)(\rho-1).
\]

For `rho>1`,

\[
\boxed{
\mathfrak D(s+1)-\mathfrak D(s)
=-2^H(\rho-1)<0.
}
\]

Therefore the non-descending members of the cylinder cannot form an arbitrary subset. They are exactly an initial parameter interval.

Define

\[
M_{bad}
:=\#\{0\le s<M:\mathfrak D(s)\ge0\}.
\]

Then

\[
\boxed{
M_{bad}
=
\max\!\left(
0,
\min\!\left(
M,
1+\left\lfloor
\frac{S-a(\rho-1)}{2^H(\rho-1)}
\right\rfloor
\right)
\right)
}
\]

when `rho>1`, with the understood exact-rational comparison at the endpoints.

Equivalently, the surviving non-descent set is

\[
\boxed{
0\le s<M_{bad}.
}
\]

No enumeration over the `M` ordinary anchors is required.

If

\[
S<a(\rho-1),
\]

then

\[
\boxed{M_{bad}=0}
\]

and the entire exact cylinder closes at once.

## 5. Resolution renews after the threshold cut

If `M_bad>0`, set

\[
\boxed{
R_{bad}=\lceil\log_2 M_{bad}\rceil.
}
\]

The new unresolved family is the exact prefix cylinder

\[
N(s)=a+2^Hs,
\qquad 0\le s<M_{bad},
\]

with a reduced resolution height `R_bad<=R`.

This creates a proof-facing recurrence:

\[
\boxed{
(M,R,a,S,\rho)
\longmapsto
\begin{cases}
\varnothing, & \rho>1\text{ and }M_{bad}=0,\\
(M_{bad},R_{bad},a,S,\rho), & \rho>1\text{ and }M_{bad}>0,\\
\text{next exact compatible macro state}, & \rho\le1.
\end{cases}
}
\]

The second branch does not mean that the same parity prefix is iterated again. It means that the next compatible macro needs to be constructed only for the exact bad prefix, not for the already closed suffix.

Thus MATH-074 and MATH-077 alternate naturally:

\[
\boxed{
\text{resolution-safe symbolic propagation}
\to
\text{orbit-gap threshold cut}
\to
\text{smaller exact bad prefix}
\to
\text{resolution-safe propagation}
\to\cdots
}
\]

This is a structural recurrence rather than ordinary-integer enumeration.

## 6. Address compatibility remains indispensable

The threshold cut above is valid only inside one exact same-parity / same-affine cylinder.

MATH-079 supplies the exact compatibility coordinate. For same-depth states with

\[
q_H=q_L+d,
\]

define

\[
A_d=r_L-3^dr_H,
\qquad
C_d=3^dS_H-S_L,
\qquad
D_d=A_d-C_d.
\]

Then

\[
\boxed{
\rho_L(y_L-y_H)=D_d
}
\]

and exact endpoint compatibility is

\[
\boxed{
y_L=y_H\iff A_d=C_d.}
\]

Therefore the recurrence may quotient or merge states only after exact compatibility has been proved. A scalar interval for `S`, `rho`, `R`, or penalty cannot replace the address channel.

The proof-facing state decomposition remains

\[
\boxed{
(\Omega,\rho,S,R,
\mathcal A_{compat},
\mathcal A_{dom})
}
\]

with `A_dom` required only where Hensel/dominance pruning is invoked.

## 7. Relation to the master affine defect

MATH-080 defines

\[
\mathfrak D(X_1,X_2)
=\rho_2(a_1+S_1)-\rho_1(a_2+S_2)
\]

and proves

\[
\mathfrak D(X_1,X_2)
=\rho_1\rho_2(y_1-y_2).
\]

For self-descent against the identity reference,

\[
\boxed{
\mathfrak D(X,X_0)
=S-N(\rho-1).
}
\]

Thus the new threshold cut is not a new dynamical criterion. It is the exact ordering of the MATH-080 master defect along an affine source cylinder.

This identifies the roles cleanly:

1. `mathfrak D` is the final sign target;
2. penalty lowers `S`;
3. resolution `R` pays for symbolic propagation before ordinary resolution;
4. exact address data decides which transitions exist;
5. the orbit-gap threshold removes a whole ordered suffix of source anchors at once.

## 8. DSD variable audit

### Essential

- `rho`: coefficient scale and descent-threshold sign;
- `S` or an exactly equivalent correction coordinate;
- `R`: unresolved source-resolution height;
- `A_compat`: exact same-integer compatibility/address lineage.

### Conditional

- `A_dom`: only where Hensel/dominance pruning is used;
- phase `Omega`: needed to update paid penalty / macro choice, but not an independent terminal descent coordinate once `(S,rho)` is fixed.

### Derived / do not duplicate

- `N_* = S/(rho-1)` when `rho>1`;
- historical occupancy `theta=N_*/N`;
- historical crossing margin `H`;
- slack `u` when already recoverable from the chosen `(Omega,rho)` coordinates;
- endpoint-merge credit after compatibility, since it is the common value `A_d=C_d`.

### Forbidden compression

- `(R,Omega,penalty)` without exact address compatibility;
- Hensel carry used as a replacement for dyadic compatibility;
- separate pruning credit for endpoint order and Hensel/correction order when they are the same affine relation.

## 9. What this says about r=11 -> r=10

The frozen exact classifications are:

\[
\begin{array}{c|r|r|r|r}
r & total & safe & singleton & critical\\
\hline
11&1013&119&414&480\\
10&994&91&396&507
\end{array}
\]

and the maximum source multiplicities are

\[
M_{max}(11)=51,905,193,085,
\]

\[
M_{max}(10)=830,483,089,363.
\]

Hence the worst-case resolution heights are

\[
R_{max}(11)=36,
\qquad
R_{max}(10)=40.
\]

The important DSD conclusion is **not** that the extra four bits create a four-bit proof deficit. MATH-074 shows the opposite structural role: while a family remains multi-source, resolution consumption can make the corresponding long symbolic edge Bellman-safe.

The meaningful deterioration from `r=11` to `r=10` is instead:

- fewer cells are immediately analytic-safe;
- more cells reach the critical exact-address branch;
- the representation remains symbolic longer before the terminal boundary;
- therefore more terminal handoff boundary states must be controlled by a non-enumerative address/defect theorem.

This isolates the `r=10` problem much more sharply than the 278,725-source AP workload.

## 10. Next theorem target

The next mainline target is a uniform **terminal handoff contraction theorem**.

For every legal low-paid critical state, after exact compatibility is imposed, prove that the recurrence above either

1. has `M_bad=0`, so the whole family descends at the current crossing; or
2. maps to an exact bad prefix with a strictly smaller well-founded structural measure.

A candidate lexicographic measure is

\[
\boxed{
\mathcal W
=
\bigl(R,\,M_{bad},\,\text{remaining first-cell depth}\bigr),
}
\]

but no well-founded decrease is claimed yet. It must be checked against the exact macro transition law before use.

An even stronger target would be a direct inequality of the form

\[
\boxed{
S<a(\rho-1)
}
\]

for every exact `r=10` critical compatibility class at its first `rho>1` crossing. If established symbolically, that single inequality would close the entire `r=10` layer without enumerating its ordinary source anchors.

## 11. Claim boundary

Established in this synthesis:

- MATH-074 localizes possible Bellman deficit to resolution overshoot / terminal handoff;
- MATH-077 implies exact monotonicity of the master defect along a fixed affine cylinder when `rho>1`;
- therefore the non-descending subset of a fixed exact cylinder is one computable prefix, not an arbitrary set;
- the prefix size can be calculated from a single exact threshold inequality without enumerating ordinary anchors;
- MATH-079 exact address compatibility remains necessary before applying/merging such cylinders.

Not established:

- that every `r=10` critical cylinder has `M_bad=0`;
- that the proposed lexicographic measure strictly decreases on every legal residual transition;
- `r=10` closure;
- first universal Farey-cell emptiness;
- universal Collatz closure.

The existing `r=10` shard/AP calculations remain valuable as regression and cross-audit data, not as the desired final proof mechanism.
