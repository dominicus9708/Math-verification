# A0 low-surplus sector: exact bridge to the Hensel min-plus cost

Date: 2026-08-27

Status: **SAFE STRUCTURAL BRIDGE + exact numeric budget certificate.** This does not prove the Collatz conjecture.

## 1. Why the s=1 sector is structurally special

At the tenth-J0 checkpoint

\[
t_0=10J_0,
\qquad j_0=10R_0+1,
\]

the mechanical A0 first-crossing word has exactly `j0` odd events.

The difficult low-surplus class has

\[
\boxed{s=1,\qquad q_{t_0}=j_0.}
\]

In ordered odd-event positions this is

\[
\boxed{
\tau_{j_0}\le t_0<\tau_{j_0+1}.
}
\]

Hence no odd ordinal is transported across the checkpoint boundary.

This gives the exact DSD sector interpretation

\[
\boxed{s=1\iff\text{no-cross-boundary transport sector}.}
\]

The word can still differ substantially from the mechanical envelope on either side of the checkpoint, but those defects are internal to the two blocks.

## 2. Ordered-position defect functional

Let

\[
n_j=\left\lfloor\frac{j-1}{\alpha}\right\rfloor+1,
\qquad \alpha=\log_3 2,
\]

be the mechanical odd-event positions and define the left displacement

\[
\boxed{d_j=n_j-\tau_j\ge0.}
\]

The mechanical normalized correction is

\[
S_{\rm mech}
=\sum_j\frac{2^{n_j-1}}{3^j},
\]

whereas the actual correction is

\[
S
=\sum_j\frac{2^{n_j-d_j-1}}{3^j}.
\]

Thus the exact correction defect is

\[
\boxed{
D:=S_{\rm mech}-S
=\sum_j a_j(1-2^{-d_j}),
\qquad
a_j:=\frac{2^{n_j-1}}{3^j}.
}
\]

No approximation is used.

## 3. Exact calibration to the existing Hensel min-plus cost

Consecutive mechanical odd positions satisfy

\[
g_j:=n_{j+1}-n_j\in\{1,2\}.
\]

Their correction weights obey

\[
\boxed{
a_j=a_{j+1}\frac{3}{2^{g_j}}.}
\]

The existing two-boundary Hensel operator uses right-to-left weights satisfying

\[
w_i=w_{i-1}\frac{3}{2^{g_i}}
\]

and local displacement cost

\[
\kappa_i(d)=2w_i(1-2^{-d}).
\]

Choose the right-boundary normalization so that

\[
\boxed{2w_i=a_j}
\]

for the corresponding odd ordinal.

Then the local Hensel cost becomes exactly

\[
\boxed{
\kappa_i(d_j)=a_j(1-2^{-d_j}),
}
\]

and therefore the total min-plus path cost is precisely the ordered-position correction defect `D` on that block.

So the previous Hensel cost is not merely analogous to the current Archimedean defect: after this normalization it is the same quantity.

## 4. Two-boundary composition is now the correct low-surplus language

Because `s=1` forbids transport across `t0`, the A0 defect splits into two boundary-preserving sectors:

\[
\boxed{
D=D_{\rm pre}+D_{\rm tail}.
}
\]

The Hensel state

\[
(K,p)
\]

must still be retained at the interface.

The exact weighted min-plus concatenation law from the earlier audit therefore applies without discarding boundary information:

\[
\boxed{
\mathcal T_{uv}(S,T)
=
\inf_R\left[
\mathcal T_u(S,R)+\lambda(u)\mathcal T_v(R,T)
\right].
}
\]

This is precisely the safe replacement for the rejected sign-only/local-pullback reduction.

## 5. Near-root survival gives an upper budget on Hensel cost

Let the local A0 block start at

\[
X=N+d
\]

and end at

\[
X'=N+d'\ge N.
\]

For the mechanical envelope, let `a_A` be the previously certified maximum gap credit.

Replacing the mechanical word by a word with defect `D` subtracts exactly `C_A D` from the endpoint, where

\[
C_A=3^{Q_0}/2^{A_0}<1.
\]

Hence

\[
d'
<d+a_A-C_A D.
\]

Since `d'>=0`, every admissible near-root A0 return must satisfy

\[
\boxed{
C_A D<d+a_A.
}
\]

Equivalently,

\[
\boxed{
D<\frac{d+a_A}{C_A}.
}
\]

Thus the near-root condition imposes a global **upper cost budget** on every Hensel-compatible displacement path.

## 6. Exact coarse budgets in the two important strips

The exact-rational companion certificate gives:

### Promoted strip

After the two-J0 promotion,

\[
d<2G,
\qquad G=2^{33}.
\]

Therefore

\[
\boxed{D<2.503G.}
\]

### After an A0,A0,J0 reset

The previous macro theorem gives

\[
d<0.478G.
\]

Therefore

\[
\boxed{D<0.981G.}
\]

These are safe coarse ceilings; sharper starting-gap information can be inserted directly into the same inequality.

## 7. DSD logical chain

The low-surplus branch is now represented as

\[
\boxed{
\text{s=1}
\to
\text{no boundary transport}
\to
\text{internal displacements }d_j
\to
\text{Hensel-compatible two-boundary path}
\to
\text{min-plus defect cost }D
\to
\text{near-root upper budget}.
}
\]

The next contradiction target is therefore exact and quantitative:

\[
\boxed{
\text{Hensel lower cost}
>
\text{near-root upper cost budget}.
}
\]

If this inequality can be proved uniformly for every admissible pair of boundary states in the `s=1` sector, that sector closes.

## 8. Structural audit

### SAFE

- `s=1` is exactly the no-cross-checkpoint-transport sector;
- ordered-position defect identity;
- exact calibration of the displacement defect to the existing Hensel min-plus local cost;
- boundary states `(K,p)` remain mandatory;
- near-root endpoint gives a global upper cost budget;
- promoted and reset numerical budgets.

### REJECTED

- projecting away the Hensel boundary state;
- using a local same-q credit as a root predecessor without the 3-adic pullback condition;
- treating low surplus as equivalent to the unique mechanical word.

### OPEN

- obtain a lower bound for the two-boundary Hensel operator strong enough to exceed the applicable budget;
- compress `(K,p)` without destroying the lower bound.

## 9. Next Gate

The exact Euclidean decomposition

\[
(A_0,Q_0)=10(J_0,R_0)+(U,P)
\]

and the continued-fraction/Christoffel hierarchy should now be used to evaluate or lower-bound the two-boundary operator recursively.

The required theorem is no longer an unrestricted parity statement. It is:

> In the `s=1` no-transport sector, certify a boundary-preserving Hensel min-plus lower cost above the current near-root budget, or identify the finite boundary-state classes that remain below it.

Companion certificate:

`collatz/src/A0_low_surplus_hensel_budget_bridge_certificate.py`
