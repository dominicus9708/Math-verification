# Defect-coordinate checkpoint join equivalence

## Scope

This theorem rewrites the CLOSED source-activation/checkpoint provenance join in
exact target-displacement defect coordinates.  It shows that the realized
prefix defect is already **derived from the exact source channel** and is
constant over its source parameter interval.

The reformulation is exact but is not counted as an independent pruning
predicate.

## 1. Ordered-one correction coordinates

Let the fixed target have length `t0`, total one-count `j0`, and ordered target
one positions

\[
t_0^{(1)}<t_1^{(1)}<\cdots<t_{j_0-1}^{(1)}.
\]

For the first `q` ordered one-events define the target correction

\[
C_T^{(q)}
=
\sum_{i=0}^{q-1}3^{q-1-i}2^{t_i^{(1)}}.
\]

For a candidate prefix with ordered one positions

\[
a_0<a_1<\cdots<a_{q-1},
\]

define

\[
C_W^{(q)}
=
\sum_{i=0}^{q-1}3^{q-1-i}2^{a_i},
\]

and realized prefix defect

\[
\boxed{N_q=C_T^{(q)}-C_W^{(q)}}.
\]

Under target dominance `a_i<=t_i^(1)`, `N_q>=0`; the algebra below does not
require that sign assumption.

## 2. Prefix defect is derived and source-parameter independent

Let the exact source channel at the activation seam be

\[
X=r+2^h k,
\qquad
T^h(X)=y+3^qk,
\qquad k\in[k_{lo},k_{hi}].
\]

The prefix affine identity is

\[
2^h(y+3^qk)=3^q(r+2^hk)+C_W^{(q)}.
\]

The parameter terms cancel, so

\[
C_W^{(q)}=2^hy-3^qr.
\]

Therefore

\[
\boxed{
N_q=3^qr+C_T^{(q)}-2^hy.
}
\]

Hence `N_q` is constant on the whole exact source cylinder and is derived from
`(r,y,h,q)` plus the fixed target.  It must not be added as a redundant
persistent S10 coordinate.

For the current late seam, `q=j0-28` and `q=Q(h)+S` remains derived from the
canonical source/control state.

## 3. Final 28-event defect

Let the remaining terminal suffix `B` have

\[
|B|=n=t_0-h,
\qquad q(B)=M=28,
\qquad C_B=C(B).
\]

Let the target correction of the final `M` ordered one-ranks, still using their
absolute bit positions, be

\[
C_{T,tail}^{(M)}
=
\sum_{i=0}^{M-1}3^{M-1-i}2^{t_{q+i}^{(1)}}.
\]

The candidate terminal contribution in full-word coordinates is `2^h C_B`.
Define

\[
\boxed{
F_M=C_{T,tail}^{(M)}-2^hC_B.
}
\]

Then the exact defect composition law is

\[
\boxed{
N_{j_0}=3^MN_q+F_M.
}
\]

For the current seam, `M=28`.

## 4. Full checkpoint defect identity

Let `C_T^{full}` denote the full fixed-target correction.  Since the candidate
full correction is

\[
C_W^{full}=C_T^{full}-N_{j_0},
\]

the ordinary checkpoint equation

\[
2^{t_0}Z=3^{j_0}X+C_W^{full}
\]

is equivalent to

\[
\boxed{
3^{28}N_q+F_{28}
=
3^{j_0}X+C_T^{full}-2^{t_0}Z.
}
\]

This identity can also solve for the unique source value associated with one
fixed `(activation channel, terminal defect record, Z)`:

\[
3^{j_0}X
=
2^{t_0}Z+3^{28}N_q+F_{28}-C_T^{full}.
\]

The resulting `X` must still lie in the exact source cylinder.

## 5. Equivalence with the activation-fiber join

The candidate prefix correction is

\[
C_W^{(q)}=C_T^{(q)}-N_q.
\]

The full target correction splits by ordered-one rank as

\[
C_T^{full}=3^{28}C_T^{(q)}+C_{T,tail}^{(28)}.
\]

Substituting the definitions into the defect-coordinate checkpoint identity
gives

\[
2^{t_0}Z
=
3^{28}\bigl(3^qX+C_W^{(q)}\bigr)+2^hC_B.
\]

Using the prefix channel

\[
3^qX+C_W^{(q)}=2^hY,
\]

and `t0=h+n`, divide by `2^h` to obtain

\[
\boxed{
2^nZ=3^{28}Y+C_B.
}
\]

This is exactly the terminal affine equation used by
`SOURCE_ACTIVATION_CHECKPOINT_PROVENANCE_JOIN.md`.

Therefore the defect-coordinate identity and the activation-fiber criterion are
**exactly equivalent descriptions of the same same-orbit provenance gate**.

## 6. State-minimization consequence

At the late activation seam:

- exact `N_q` is derived from `(r,y,h,S)` and the fixed target;
- `F_28` is derived from `(h,C_B)` and the fixed target tail once the terminal
  suffix descriptor is validated;
- neither quantity is an independent persistent state coordinate.

The defect formulation can nevertheless be useful for event/valuation
compression because it separates a source-constant prefix term from a
28-event terminal term.

## DSD audit

- **EXACT/CLOSED**: `N_q` is constant across one exact source channel.
- **EXACT/CLOSED**: `N_q=3^q r+C_T^(q)-2^h y`.
- **EXACT/CLOSED**: `N_full=3^28 N_q+F_28`.
- **EXACT/CLOSED**: defect-coordinate checkpoint identity.
- **EXACT/CLOSED**: equivalence to the existing activation-fiber same-orbit
  criterion.
- **REJECTED**: counting the defect-coordinate form as an independent pruning
  factor in addition to the activation-fiber form.
- **REJECTED**: storing exact `N_q` as a new persistent S10 coordinate when
  `(r,y,h,S)` is already present.
- **OPEN**: compressed source-preserving export of the final 28-event terminal
  record / ordinary checkpoint candidates.
- **OPEN**: Route-B and global Collatz closure.
