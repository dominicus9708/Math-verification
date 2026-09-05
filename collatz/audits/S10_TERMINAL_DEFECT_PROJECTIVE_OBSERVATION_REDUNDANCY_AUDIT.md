# S10 audit — terminal defect / projective-observation redundancy

Date: **2026-09-05**

Status: **AUDITED / exporter architecture narrowed**

## Question

The active Route-B frontier still treated the low-precision `m<=17` right-H
carry family as an important unresolved terminal export object.

After the exact defect-coordinate checkpoint equivalence was closed, the next
DSD question is whether the exact final-28 physical defect `F_28` and the
right-H projective observation `z_H mod 3^28` are genuinely independent state
coordinates.

## Result

They are not independent.

For the final `L` right-indexed one-events, define the local target-displacement
defect

\[
E_L=\sum_{i=0}^{L-1}3^i(2^{A_i}-2^{B_i}).
\]

The realized right-H observation satisfies exactly

\[
\boxed{z_H\equiv-E_L\pmod{3^L}}.
\]

If the right-H block starts at absolute offset `p_R`, the corresponding
full-word defect is

\[
F_L=2^{p_R}E_L,
\]

so

\[
\boxed{z_H\equiv-2^{-p_R}F_L\pmod{3^L}}.
\]

For the current checkpoint,

\[
L=28,
\qquad p_R=103{,}768{,}467{,}013,
\]

and

\[
2^{-p_R}\equiv1{,}051{,}701{,}240{,}047\pmod{3^{28}}.
\]

Therefore a validated terminal suffix descriptor `(n,C_B)` determines

\[
F_{28}=C_{T,tail}^{(28)}-2^{t_0-n}C_B
\]

and hence determines `z_H` exactly modulo `3^28`.

Canonical theorem:

- `../theorems/TERMINAL_DEFECT_PROJECTIVE_OBSERVATION_REDUNDANCY.md`.

Regression certificate:

- `../src/A0_s1_routeB_terminal_defect_projective_observation_redundancy_certificate.py`.

## DSD channel analysis

The previous representation mixed two levels:

1. exact physical information: integer terminal defect `F_28`;
2. projective observation: one residue `z_H mod 3^28`.

The second is a deterministic finite-resolution projection of the first.
Therefore the pair

```text
(F_28, z_H)
```

contains a redundant coordinate whenever `F_28` is exact.

Equivalently, once `(n,C_B)` is already validated, the state

```text
(n, C_B, z_H)
```

should be minimized to

```text
(n, C_B)
```

for storage, with `z_H` computed lazily when the right-H or synchronized
checkpoint predicate queries it.

This is the same DSD principle already used for:

- derived `q=Q(h)+S`;
- derived prefix defect `N_q` on one exact source channel;
- derived `(z_2,z_H)` after a provenanced ordinary checkpoint `Z` is exposed.

## Effect on the principal exporter

### Old interpretation

```text
source front
  -> late activation
  -> independently construct/export right-H z_H carry family
  -> independently construct dyadic z_2 family
  -> synchronize
  -> recover Z
  -> attempt source provenance
```

This invites a Cartesian-marginal pairing error and makes the low-precision
carry family look like an independent output space.

### Audited interpretation

```text
source front
  -> source-preserving late activation
  -> generate/validate exact final-28 suffix descriptor (n,C_B)
  -> derive exact F_28
  -> derive the only compatible z_H
  -> query right-H formation acceptance at that prescribed z_H
  -> synchronize with a provenance-compatible dyadic checkpoint condition
  -> expose Z
  -> apply the CLOSED activation/checkpoint provenance join
```

The difficult object is therefore the **source-preserving terminal descriptor
language**, not an unconstrained right-H residue family.

## Reclassification of `m<=17`

The existing high-precision theorem remains useful:

\[
m\ge18
\Rightarrow
\text{a prescribed projective cylinder has at most one legal slack}.
\]

For `m<=17`, several slack representatives of one prescribed cylinder may be
possible.  However, after this audit they should be handled only inside the
right-H **acceptance/membership test for a prescribed derived observation**.

They need not be exported as an independent checkpoint coordinate family.

Thus:

- **REJECTED as principal output task:** enumerate/export all low-precision
  carry residues merely to create checkpoint observations;
- **OPEN and still necessary:** determine whether a prescribed derived `z_H`
  admits a right-H formation-compatible terminal 28-gate realization, carrying
  every boundary/control predicate that is genuinely queried;
- **CLOSED:** pure target-dominance existence alone is already saturated to
  `3∤Z`, so rebuilding the low-precision tree for that predicate is redundant.

## Remaining minimal-state problem

At the terminal seam, the candidate persistent/export interface should aim for
something of the form

```text
source_parent_id
(r,y,k_lo,k_hi,h,S)
terminal descriptor: (n,C_B) or an exact equivalent valuation-gap quotient
right-H boundary/formation control not derivable from the descriptor
post-checkpoint/dyadic provenance information not derivable before Z exposure
```

with the following quantities derived rather than stored independently:

```text
q = j0-28
h = t0-n                    (when n is used at the seam)
N_q                         from source activation channel
F_28                        from (n,C_B) and fixed target
z_H mod 3^28               from F_28
```

Whether additional right-H boundary controls can also be derived from the exact
terminal descriptor is **OPEN** and must be proved before they are removed.

## Audit verdict

### EXACT / CLOSED

- `F_28 -> z_H` projection;
- `(n,C_B) -> F_28 -> z_H` at the fixed target;
- `z_H` is redundant as persistent state once exact `(n,C_B)` is retained;
- low-precision carry enumeration is not required merely to manufacture a
  checkpoint ternary observation.

### OPEN / principal

- compressed source-preserving generation of the admissible final-28
  `(n,C_B)` language from the current 14,224 cylinders;
- right-H formation/boundary membership for the prescribed derived `z_H`;
- provenance-compatible synchronization with the dyadic side;
- ordinary `Z` exposure and source-fiber join at scale.

### REJECTED

- treating `F_28` and `z_H` as independent filters;
- Cartesian pairing of independently generated source suffix and right-H
  residue marginals;
- using projective residue agreement as a replacement for formation membership;
- inferring exact physical defect from `z_H` alone;
- interpreting this state reduction as Route-B or Collatz closure.

## Next calculation

The next principal calculation should act on the **28-event terminal descriptor
itself**.  The preferred coordinate is an exact valuation-gap / ordered-one
representation whose source refinement can be compiled by
`VALUATION_MACROBLOCK_COMPILATION.md`, while all right-H observations are
computed lazily from the exact defect projection above.
