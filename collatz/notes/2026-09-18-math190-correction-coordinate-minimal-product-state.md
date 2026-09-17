# MATH-190 — correction-coordinate reduction of the Hensel/address product state

Date: 2026-09-18

Status: `EXACT LOGICAL-STATE REDUCTION / HENSEL AS PREFIX PREDICATE / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-188 proposed a synchronized product state containing

\[
(k,q,\Sigma,c,\mathcal P,A,B,M,\mathcal H).
\]

MATH-189 shows that `Sigma`, normalized correction, Hensel class, and canonical source residue are all determined by the same integer correction `C`.

The next question is whether the Hensel witness subset `mathcal H` and affine intercepts `(A,B)` are mathematical state variables or only implementation devices.

Within the audited finite product range, they are implementation devices. A smaller exact logical state is available.

## 2. Hensel maximality is a predicate of `(k,q,C)`

Write

\[
C=h3^q+r,
\qquad
0\le r<3^q.
\]

MATH-040 defines the unrestricted one-sided class maximum

\[
\boxed{
M_k(q,r)
:=
\max_{u\in\mathcal L_{\rm arbitrary}(k,q,r)}
\left\lfloor\frac{C(u)}{3^q}\right\rfloor.
}
\]

A coefficient-valid candidate survives the one-sided root-Hensel test at this prefix exactly when

\[
\boxed{
h=M_k(q,r).}
\]

If

\[
h<M_k(q,r),
\]

then the positive credit

\[
t=M_k(q,r)-h
\]

gives the same `k`-step endpoint from the smaller ordinary start `N-t`.

By MATH-189, in the present first-cell range `k<=41` every positive such credit automatically has `0<t<N`.

Therefore define the exact prefix predicate

\[
\boxed{
\mathsf H(k,q,C)=1
\iff
\left\lfloor C/3^q\right\rfloor
=M_k\left(q,C\bmod3^q\right).
}
\]

A branch is deleted immediately when `mathsf H=0`.

## 3. Why no Hensel-history coordinate is needed

The nested Hensel condition means that every candidate prefix encountered along one ordinary-source lineage must pass its current one-sided test.

This is enforced by applying

\[
\mathsf H(k,q,C)
\]

after every one-step transition.

If a prefix fails, root minimality excludes the ordinary starts represented by that state and no descendant of that state is retained.

Hence previous Hensel decisions do not need to be encoded in a separate future state once the branch has survived them.

The MATH-051 bounded-carry / viable-witness subset is an exact and efficient way to evaluate many such Hensel comparisons in bulk. It remains valuable implementation machinery, but it is not an additional mathematical coordinate of a single surviving state.

Thus

\[
\boxed{\mathcal H\text{ is an oracle/cache state, not a proof-state coordinate.}}
\]

This does not weaken the requirement that Hensel maximality be checked at every prefix.

## 4. Canonical source and endpoint from `C`

For fixed `(k,q,C)`, let

\[
\boxed{
a\equiv-C(3^q)^{-1}\pmod{2^k},
\qquad0\le a<2^k.}
\]

Then every ordinary start with this parity prefix has the form

\[
\boxed{N=a+2^ks.}
\]

The corresponding endpoint is

\[
T^k(N)
=\frac{3^q(a+2^ks)+C}{2^k}
=b_0+3^qs,
\]

where

\[
\boxed{b_0:=\frac{3^qa+C}{2^k}.}
\]

So the MATH-188 affine intercepts `(A,B)` are derived from `(k,q,C)` plus the chosen lift interval.

They do not need to be stored separately when a canonical residue origin is used.

## 5. Exact lift-interval address state

To allow exact structural cuts that retain only part of one residue class, keep an integer lift interval

\[
\boxed{s\in[L_s,U_s].}
\]

Equivalently one may store `(s_0,M)` with

\[
M=U_s-L_s+1.
\]

For the untouched first-cell residue class this interval is derived by intersecting

\[
N=a+2^ks
\]

with the frozen ordinary-start window.

If MATH-183 or another exact monotone cut retains only an initial lift subinterval, `(L_s,U_s)` records that subfamily without enumerating its ordinary starts.

## 6. One-step interval recurrence without `(A,B)`

Let the next actual parity bit be

\[
b\in\{0,1\}.
\]

Since `3^q` is odd,

\[
T^k(N)\equiv b_0+s\pmod2.
\]

Thus compatibility with parity `b` requires

\[
\boxed{s\equiv\eta:=b-b_0\pmod2.}
\]

Write

\[
s=\eta+2t.
\]

Then the child lift interval is exactly

\[
\boxed{
L_t=\left\lceil\frac{L_s-\eta}{2}\right\rceil,
\qquad
U_t=\left\lfloor\frac{U_s-\eta}{2}\right\rfloor.
}
\]

The branch is empty iff `L_t>U_t`.

The common correction/depth transition is

\[
\boxed{
\begin{aligned}
k'&=k+1,\\
q'&=q+b,\\
C'&=3^bC+b2^k.
\end{aligned}
}
\]

The canonical child residue derived from `(k',q',C')` agrees exactly with the residue obtained by substituting `s=eta+2t` into the parent family.

Therefore exact same-integer address propagation needs only the lift interval in addition to `(k,q,C)`.

## 7. Other MATH-188 coordinates are derived

From `(k,q,C)`:

\[
\boxed{d=k-q,}
\]

\[
\boxed{u=m(q)-(k-q),}
\]

\[
\boxed{\rho=2^k/3^q,}
\]

\[
\boxed{S=C/3^q,}
\]

\[
\boxed{\Sigma=(C+2^k)/3^q-1.}
\]

The mechanical phase scale

\[
\Omega_q=2^{q+m(q)}/3^q
\]

depends only on `q`.

The cumulative paid penalty is also derived:

\[
\boxed{
\mathcal P=S_*(q)-C/3^q,
}
\]

where `S_*(q)` is the deterministic zero-slack mechanical envelope of MATH-057.

Thus `Sigma`, `S`, `rho`, `Omega`, slack `u`, and cumulative penalty do not require independent storage.

## 8. Reduced proof-facing state

For the common-origin, finite first-cell product calculation, a minimal exact logical state may therefore be written

\[
\boxed{
\mathscr V
=(k,q,C;\ c;\ L_s,U_s),
}
\]

where

- `(k,q,C)` carries the full parity/correction/Hensel/analytic information;
- `c` is the paid-event count within the currently active positive-slack excursion when the `r=1..21` layer label is needed;
- `[L_s,U_s]` is the exact ordinary-source lift interval after any structural address cuts.

At each step:

1. coefficient admissibility is checked from derived slack `u`;
2. exact parity/address compatibility updates the lift interval;
3. correction updates by `C'=3^bC+b2^k`;
4. one-sided Hensel maximality `mathsf H(k',q',C')` is checked;
5. paid count / first-return labels are updated from the derived slack;
6. Bellman/address terminal rules such as MATH-183/186 are applied when relevant.

No ordinary start is enumerated by this representation.

## 9. Relation to MATH-051

MATH-051 remains essential as evidence that the one-sided Hensel predicate can be evaluated exactly through depth 41 without unrestricted parity-word enumeration.

Its fixed-`d` signature and bounded-carry viable-witness subsets are a batch implementation of the same class-max predicate encoded here by `mathsf H(k,q,C)`.

MATH-189 additionally identifies its gap level with the same `q` clock used by this recurrence.

Therefore the intended product is not

\[
\text{MATH-188 state}\times\text{an independent Hensel state}.
\]

The sharper description is

\[
\boxed{
\text{one correction/address recurrence}
+\text{ an exact Hensel prefix predicate}.
}
\]

## 10. Remaining theorem target

MATH-186 has already shown that every possible nonpositive multi-paid boundary transfer is localized to a singleton overshoot.

The present reduction means that such a singleton is described by

\[
(k,q,C,c,s)
\]

with `L_s=U_s=s`, and its Hensel maximality is decided by the same `(k,q,C)`.

The next target is therefore narrower:

> prove that every Hensel-maximal, coefficient-valid singleton overshoot either has negative orbit defect / descends to a smaller ordinary value, or enters a structurally contracting transition already covered by MATH-183/186.

This is the remaining non-enumerative terminal theorem target.

## 11. Claim boundary

Established:

- Hensel maximality is an exact prefix predicate of `(k,q,C)`;
- applying that predicate at every transition enforces nested Hensel survival without an independent logical history coordinate;
- canonical source and endpoint intercepts are derived from `(k,q,C)`;
- exact partial source families are carried by one lift interval;
- the MATH-188 explicit numeric state reduces to `(k,q,C,c,L_s,U_s)` for the synchronized first-cell calculation.

Not established:

- a complexity bound showing this reduced state has uniformly bounded cardinality at arbitrary depth;
- the singleton terminal theorem;
- closure of a new paid-count layer;
- first-cell emptiness;
- the Collatz conjecture.
