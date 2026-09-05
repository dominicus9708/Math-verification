# A0 `s=1` checkpoint: exact invariant/Minkowski factorization

Date: 2026-08-27

Status: **SAFE local factorization on the `s=1` A0 formation domain.** This is not an all-surplus theorem and not a proof of the Collatz conjecture.

## 1. Checkpoint arithmetic

Let

\[
(A_0,Q_0)=(114208327604,72057431991),
\]

\[
(J_0,R_0)=(10439860591,6586818670),
\]

and

\[
t_0=10J_0,
\qquad
j_0=10R_0+1.
\]

The exact decomposition

\[
(A_0,Q_0)=10(J_0,R_0)+(U,P)
\]

has

\[
(U,P)=(9809721694,6189245291).
\]

For the 1-based mechanical odd position

\[
n_j=\left\lfloor{(j-1)A_0\over Q_0}\right\rfloor+1,
\]

exact arithmetic gives

\[
\boxed{n_{j_0}=t_0},
\qquad
\boxed{n_{j_0+1}=t_0+2}.
\]

## 2. `s=1` fixes the first tail displacement to two values

The minimal checkpoint surplus sector is

\[
s=1
\iff
\tau_{j_0}\le t_0<\tau_{j_0+1}.
\]

Because the next mechanical position is `t0+2`, integrality gives

\[
\tau_{j_0+1}\in\{t_0+1,t_0+2\},
\]

and therefore

\[
\boxed{
d_{j_0+1}=n_{j_0+1}-\tau_{j_0+1}\in\{0,1\}.}
\]

This is obtained from the checkpoint combinatorics alone.  No near-root defect ceiling and no Hensel lower bound is used.

## 3. Cross-checkpoint ordering is automatic

Write

\[
d_{\rm pre}:=d_{j_0}\ge0,
\qquad
d_{\rm tail}:=d_{j_0+1}\in\{0,1\}.
\]

The actual odd positions are

\[
\tau_{j_0}=t_0-d_{\rm pre},
\]

\[
\tau_{j_0+1}=t_0+2-d_{\rm tail}.
\]

Strict ordering across the split requires

\[
t_0-d_{\rm pre}<t_0+2-d_{\rm tail},
\]

or equivalently

\[
d_{\rm tail}\le d_{\rm pre}+1.
\]

Since `d_pre>=0` and `d_tail in {0,1}`, this inequality is automatic.

Hence no additional ordering state must be matched across this particular `s=1` split.

## 4. Why the interface Hensel carry can also be eliminated at the full-block level

For a length-`h` Hensel block, define

\[
\Xi_h:=K_0-3^hK_h
=-\sum_{i=0}^{h-1}3^i2^{e_i-d_i}.
\]

The exact full-block Hensel condition is equivalent to this two-boundary invariant equation once the displacement controls and physical boundary carries are fixed.

Therefore an internal carry at the tenth-`J0` split is only a factorization variable.  It need not be retained as an independent compatibility coordinate if the pre and tail displacement words are assembled first and the exact full `Xi` equation is imposed at the physical boundaries.

This statement is specific to a **complete block check**.  It does not claim that internal carries are dispensable in every recursive algorithm or every partial-boundary problem.

## 5. Exact product language

Let

\[
\mathscr D_{\rm pre}
\]

be the ordered displacement language on the first ten-`J0` part satisfying the `s=1` checkpoint count, and let

\[
\mathscr D_{\rm tail}^{(\epsilon)},
\qquad\epsilon\in\{0,1\},
\]

be the ordered tail language with first tail displacement `epsilon`.

Since the cross-ordering condition is automatic,

\[
\boxed{
\mathscr D_{s=1}
=
\mathscr D_{\rm pre}
\times
\left(
\mathscr D_{\rm tail}^{(0)}
\sqcup
\mathscr D_{\rm tail}^{(1)}
\right).
}
\]

For any additive full-block defect coordinate `D`, this gives the exact Minkowski decomposition

\[
\boxed{
\mathcal D_{s=1}
=
\mathcal D_{\rm pre}
+
\left(
\mathcal D_{\rm tail}^{(0)}
\cup
\mathcal D_{\rm tail}^{(1)}
\right).
}
\]

For the unnormalized Hensel invariant one inserts the appropriate power-of-three scale at concatenation; the generic rule is documented separately in the reachable-`Xi` composition note.

## 6. DSD audit

### SAFE

\[
C4F(s=1)
\to
\{d_{j_0+1}=0,1\}
\to
\text{automatic cross-ordering}
\to
\text{product language}.
\]

No physical gap budget is used.

### REJECTED over-promotions

Do not infer

\[
s=1\text{ factorization}
\Longrightarrow
s\ge1\text{ all-surplus factorization}.
\]

Do not infer that a checkpoint carry is irrelevant in every partial-block DP.  It is eliminated here because the full two-boundary invariant equation is imposed after the independently ordered pre/tail controls are assembled.

## 7. Next gate

The remaining task is no longer to enumerate an internal checkpoint carry.  It is to compress the two reachable invariant/defect sets

\[
\mathcal D_{\rm pre},
\qquad
\mathcal D_{\rm tail}^{(0,1)}
\]

on the anchored Christoffel/Farey DAG, then intersect their exact sum with the physical two-boundary target.

Companion certificate:

`collatz/src/A0_s1_invariant_minkowski_factorization_certificate.py`.
