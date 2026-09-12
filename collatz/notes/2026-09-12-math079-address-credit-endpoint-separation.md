# MATH-079 — address contrast minus correction credit as the endpoint-separation coordinate

Date: 2026-09-12

Status: `EXACT ALGEBRAIC IDENTITY / ADDRESS-HENSEL ROLE SEPARATION / GLOBAL ORDER OPEN`

## 1. Motivation

MATH-076 considered pairs that had already merged and showed that their address contrast equals their normalized-correction credit. The depth-72--81 boundary audits, however, concern pairs that generally do **not** merge. To place both cases in one equation, keep the two sides separate before imposing endpoint equality.

The Collatz conjecture and first universal Farey cell remain `OPEN`.

## 2. General same-depth pair

Take two canonical states at the same shortcut depth `k`, ordered so

\[
q_H=q_L+d,
\qquad d\ge0.
\]

Let

\[
\rho_L=\frac{2^k}{3^{q_L}},
\qquad
\rho_H=\frac{\rho_L}{3^d}.
\]

Use the common-coordinate endpoint law

\[
y=\frac{r+S}{\rho}.
\]

Define the **address contrast**

\[
\boxed{
A_d:=r_L-3^dr_H
}
\]

and the **correction credit**

\[
\boxed{
C_d:=3^dS_H-S_L.
}
\]

Then

\[
\rho_Ly_L=r_L+S_L,
\]

while

\[
\rho_Ly_H=3^d(r_H+S_H).
\]

Subtracting gives the universal endpoint-separation identity

\[
\boxed{
\rho_L(y_L-y_H)=A_d-C_d.
}
\]

Define the separation mismatch

\[
\boxed{D_d:=A_d-C_d.}
\]

Then the sign of `D_d` is exactly the sign of the endpoint order after multiplication by the positive factor `rho_L`.

## 3. Compatibility is equality of two different channels

The exact endpoint-merge condition is now

\[
\boxed{
y_L=y_H\iff A_d=C_d.}
\]

MATH-076's merge credit `G_d` is therefore the common value

\[
G_d=A_d=C_d
\]

**after** compatibility has been imposed.

This clarifies the role of the two channels:

- `A_d` belongs to exact dyadic/source-address lineage;
- `C_d` belongs to normalized correction and, at fixed `q`, to the Hensel `Sigma` credit;
- endpoint compatibility is the equation that matches them.

Therefore a bounded-carry/Hensel state can compress the correction-credit side without replacing exact address information. The earlier DSD decision to keep compatibility and dominance separate is not merely conservative bookkeeping; it follows from the exact separation equation.

## 4. Fixed-q specialization

For `d=0`,

\[
A_0=r_L-r_H,
\qquad
C_0=S_H-S_L=\Sigma_H-\Sigma_L,
\]

and

\[
\boxed{
\rho(y_L-y_H)
=(r_L-r_H)-(S_H-S_L).
}
\]

Thus:

- Hensel/correction credit proposes an integer displacement that could be matched;
- the actual dyadic addresses supply the realized displacement;
- a same-`q` endpoint collision occurs exactly when those displacements agree.

This is the exact reason that `Delta Sigma` integrality is not, by itself, a same-integer endpoint collision theorem.

## 5. Relation to depth-72 and depth-75 collision halos

The historical internal-boundary certificates first used an analytic bound on possible same-endpoint start displacement,

\[
|r_L-r_H|<2^{k-q}\left(1-(2/3)^q\right).
\]

MATH-078 identifies the right-hand side as an `S` envelope. At fixed `q`, an actual collision would require

\[
r_L-r_H=S_H-S_L.
\]

Therefore the envelope proves that only a finite address halo around each large block boundary can possibly satisfy compatibility. The subsequent exact low-address endpoint scan decides whether equality actually occurs inside that halo.

At depth 72, coefficient survival gives `q>=46`, producing the complete finite halo below `2^26`; the exact scan found no cross-boundary endpoint collision. At depth 75, `q>=48` gives the corresponding halo below `2^27`; again the exact scan found no collision.

This is a clean DSD division of labor:

\[
\boxed{
S\text{-envelope narrows the domain}
\quad+\quad
\text{exact address scan decides compatibility}.
}
\]

## 6. Relation to ordered separation at depths 79--81

The later range audits found, in every common-`Q` boundary cell,

\[
E_L<E_R
\]

through depths 79, 80, and 81, with audited minimum endpoint gaps

\[
837,\quad1253,\quad1880.
\]

For same `Q` this is exactly a uniform sign statement for the `d=0` separation mismatch:

\[
\rho(E_R-E_L)
=(r_R-r_L)+(S_R-S_L).
\]

Equivalently, after orienting the pair consistently,

\[
D_0=A_0-C_0
\]

has a strict common sign throughout every audited cell.

The historical statement that a scalar interval is not a complete recursive state also fits the present decomposition: to propagate the sign of `D_0`, one needs enough endpoint residue/address information to update `A_0`, not merely an interval bound on `C_0`.

## 7. Finite regression

The companion certificate regenerates all coefficient-surviving canonical states through depth 14 and checks every unordered state pair.

Total pair checks:

\[
\boxed{372,731}.
\]

Results:

- separation-identity failures: `0`;
- merge-equivalence failures: `0`.

The identity is algebraic; the regression is an implementation check only.

## 8. Candidate use in the Bellman architecture

The new quantity

\[
D_d=A_d-C_d
\]

is not yet a Bellman potential. It is an exact compatibility/separation coordinate.

However it suggests a smaller future-complete decomposition than storing an opaque address object:

\[
\boxed{
\text{state}
=\text{analytic correction coordinates}
+\text{exact address contrast/residue data}
+\text{resolution height}.
}
\]

The next question is whether a residue-refined quotient can update the sign or a lower bound of `D_d` without materializing all ordinary starts.

## 9. Claim boundary

Established:

- universal separation identity `rho_L(y_L-y_H)=A_d-C_d`;
- exact compatibility criterion `A_d=C_d`;
- fixed-q identification of correction credit with `Delta S=Delta Sigma`;
- finite pairwise regression through depth 14;
- exact reinterpretation of existing depth-72--81 collision/separation audits.

Not established:

- arbitrary-depth ordered separation;
- monotonic growth of the depth-79--81 minimum gaps;
- a finite complete residue quotient for `D_d`;
- a Bellman lower bound at `19/503`;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math079_address_credit_separation_certificate.py`
