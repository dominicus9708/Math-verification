# Two-boundary Hensel invariant and collapse of the full-block cost coordinate

Date: 2026-08-27

Status: **SAFE exact operator identity + proof-target correction.** This is an algebraic reorganization of the repaired binary/Hensel branch. It does not prove the Collatz conjecture.

## 1. Exact full-block Hensel invariant

Traverse a length-\(h\) odd-ordinal block from right to left. At step \(i\), let

\[
u_i(d_i)=2^{e_i-d_i}\in\mathbb Z_3^	imes
\]

and

\[
K_{i+1}=rac{K_i+u_i(d_i)}3.
\]

Unrolling gives

\[
3^hK_h
=K_0+\sum_{i=0}^{h-1}3^iu_i(d_i).
\]

Hence the two-boundary covariance invariant is not only formally conserved; for every concrete control word it is exactly

\[
\boxed{
\Xi_h:=K_0-3^hK_h
=-\sum_{i=0}^{h-1}3^i2^{e_i-d_i}.
}
\]

For the mechanical zero-displacement word,

\[
\boxed{
\Xi_h^{(0)}
=-\sum_{i=0}^{h-1}3^i2^{e_i}.
}
\]

Subtracting,

\[
\boxed{
\Xi_h-\Xi_h^{(0)}
=\sum_{i=0}^{h-1}3^i2^{e_i}(1-2^{-d_i}).
}
\]

The right-hand side is positive in the ordinary real embedding whenever some displacement is positive.

## 2. The local min-plus charge is the same invariant difference

The mechanical weights obey

\[
w_i=w_{i-1}rac3{2^{g_i}},
\]

while the mechanical exponents satisfy

\[
e_i=e_{i-1}-g_i.
\]

Therefore

\[
3^i2^{e_i}
\]
obeys exactly the same multiplicative recurrence. If the initial normalization is \(w_0\), then

\[
2w_i
=rac{2w_0}{2^{e_0}}\,3^i2^{e_i}.
\]

The block cost

\[
J_w=\sum_i2w_i(1-2^{-d_i})
\]
therefore satisfies

\[
\boxed{
J_w
=rac{2w_0}{2^{e_0}}
igl(\Xi_h-\Xi_h^{(0)}igr).
}
\]

Thus, once both exact boundary carries are fixed, **every feasible control path has the same total cost**.

The min-plus operator still has a nontrivial role as a feasibility/representation operator, but its full-block scalar cost is not an additional independent degree of freedom.

## 3. Exact A0 calibration

For the first A0 block, write the ordered mechanical odd positions as \(n_j\), and traverse them right to left with

\[
i=Q_0-j.
\]

Then the Hensel mechanical term is

\[
3^i2^{n_j-1-A_0}.
\]

The ordered-position defect weight is

\[
a_j=rac{2^{n_j-1}}{3^j}.
\]

Since

\[
C_A:=rac{3^{Q_0}}{2^{A_0}},
\]

we have term by term

\[
oxed{
3^{Q_0-j}2^{n_j-1-A_0}=C_Aa_j.
}
\]

Therefore for

\[
D=\sum_j a_j(1-2^{-d_j}),
\]

the full A0 invariant satisfies

\[
\boxed{
\Xi_{Q_0}-\Xi_{Q_0}^{(0)}=C_A D.
}
\]

This is the exact equality underlying the earlier Hensel/ordered-defect calibration.

## 4. Physical boundaries

For an accelerated Collatz block

\[
X\longmapsto Y
\]
of length \(A\) with \(q\) odd events,

\[
K_R=-Y,
\qquad
K_L=-2^{-A}X.
\]

Hence

\[
\boxed{
\Xi_q^{m phys}
=K_R-3^qK_L
=rac{3^q}{2^A}X-Y.
}
\]

The affine identity

\[
2^AY=3^qX+R
\]
gives the equivalent form

\[
\boxed{
\Xi_q^{m phys}=-rac{R}{2^A}.
}
\]

If \(R_{m mech}\) is the mechanical correction and

\[
E=R_{m mech}-R,
\qquad
D=rac{E}{3^q},
\]
then

\[
\boxed{
\Xi_q^{m phys}-\Xi_q^{(0)}
=rac{E}{2^A}
=rac{3^q}{2^A}D.
}
\]

So the physical boundary pair and the correction defect are two coordinate descriptions of the same scalar invariant.

## 5. Full Hensel divisibility is equivalent to the invariant equation

Fix a displacement/control word \(d_0,\ldots,d_{h-1}\) and two endpoint carries \(K_0,K_h\).

Suppose

\[
K_0-3^hK_h
=-\sum_{i=0}^{h-1}3^iu_i(d_i).
\]

Reducing modulo three gives

\[
K_0+u_0(d_0)\equiv0\pmod3.
\]

Define

\[
K_1=rac{K_0+u_0(d_0)}3.
\]

After division by three the same identity becomes the corresponding suffix identity. Induction therefore recovers every Hensel division.

At each preterminal stage the next suffix identity gives

\[
K_i\equiv-u_i(d_i)
ot\equiv0\pmod3,
\]
so the continuation-unit condition is automatic.

Therefore

\[
\boxed{
	ext{full Hensel path for a prescribed control word}
\iff
	ext{one exact two-boundary invariant equation}.
}
\]

The local carry recurrence is an exact algorithmic factorization of this equation; it is not an additional independent arithmetic constraint.

## 6. Completeness of Xi for a full fixed-boundary operator

The already-proved covariance is

\[
(K_0,K_h)\mapsto(K_0+3^ht,\,K_h+t).
\]

If two admissible boundary pairs have the same \(\Xi_h\), then with

\[
t=K_h'-K_h
\]
we have

\[
K_0'=K_0+3^ht.
\]

Hence they are on the same covariance orbit and have a path-by-path cost-preserving correspondence.

Thus, for a **full block with the ordering boundary coordinates also fixed**, the carry-pair dependence reduces exactly to

\[
oxed{\Xi_h}.
\]

Caveat: this does **not** mean that \(\Xi\) alone is sufficient as an interface state for arbitrary recursive subblock composition. Matching two subblocks still requires their shared intermediate carry to be compatible. The reduction is exact for the complete prescribed two-boundary problem, not automatically for every internal DAG interface.

## 7. Corrected proof target

The earlier language was

\[
	ext{Hensel lower cost}>	ext{near-root upper cost budget}.
\]

That remains a valid sufficient strategy if the lower bound is obtained independently and uniformly over the physical boundary family.

But the exact invariant identity reveals the more canonical formulation.

Define the ordered-control reachable set

\[
\mathcal R_w(p_R,p_L)
:=\left\{
\Xi_h(d):
 d	ext{ obeys the ordering constraints and the stated boundary }p	ext{-data}
ight\}.
\]

Define the physical invariant set

\[
\mathcal P_w
:=\left\{
K_R-3^hK_L:
(K_R,K_L)	ext{ arise from the allowed ordinary physical boundaries}
ight\}.
\]

Then the exact full-block existence question is

\[
\boxed{
\mathcal R_w(p_R,p_L)\cap\mathcal P_w
earnothing\ ?
}
\]

For the hard \(s=1\) sector the tenth-J0 ordering interface has only

\[
p_{m int}\in\{0,1\}.
\]

So the carry-state problem is better viewed as an **ordered invariant-representation problem** with two possible ordering interface states.

## 8. Circularity audit

### SAFE route A: cost separation

\[
	ext{ordering/Hensel language}
	o	ext{uniform lower }D
\]
independently, and

\[
	ext{physical near-root boundary}
	o	ext{upper }D
\]
independently, followed by comparison.

### SAFE route B: direct invariant intersection

\[
	ext{physical ordinary boundaries}
	o\mathcal P_w,
\]

\[
	ext{ordered control language}
	o\mathcal R_w,
\]
then prove the sets are disjoint.

In route B it is legitimate to use the physical target interval as a target-set restriction, because one is no longer claiming that the resulting pruned search independently proves a lower cost.

### REJECTED

Do not use the physical defect ceiling to manufacture a supposedly independent Bellman lower bound and then compare that lower bound back to the same ceiling.

Do not treat the Hensel carry and the global invariant as independent evidence; the former is a factorization of the latter.

## 9. DSD interpretation

The repaired descriptor chain is

\[
oxed{
	ext{ordered displacement controls}
	o
	ext{global correction/invariant }\Xi
\leftrightarrow
	ext{two physical boundaries}.
}
\]

The Hensel carry sequence is an exact internal decomposition channel:

\[
\Xi
	o
(K_0,K_1,\ldots,K_h),
\]
not a second independent constraint channel.

This removes one layer of apparent state complexity without discarding arithmetic information.

## 10. Next gate

The useful next object is a Christoffel-DAG-compatible representation of the **reachable invariant set** rather than a flat table of all carries.

For a block split \(w=uv\), the raw invariant decomposes as

\[
\boxed{
\Xi_{uv}=\Xi_u+3^{|u|}\Xi_v.
}

The difficulty is to retain exactly the additional interface information needed to make the shared ordering/carry boundary realizable, while exploiting that the final full-block target itself depends only on \(\Xi\).

Companion exact regression:

`collatz/src/hensel_two_boundary_invariant_cost_certificate.py`
