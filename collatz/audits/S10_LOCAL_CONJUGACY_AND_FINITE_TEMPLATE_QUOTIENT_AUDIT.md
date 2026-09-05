# S10 audit — local conjugacy vs finite source/ballot template quotient

Date: 2026-09-03

Status: **SAFE structural clarification / principal source-family contraction gate remains OPEN**

## Objects audited

1. suffix slack/carry recurrence;
2. fixed-rank formation recurrence;
3. direct gate-to-gate rank stitching;
4. finite-horizon source projective quotient;
5. finite-horizon pure-ballot control signature;
6. their product quotient at the certified 8-jump frontier.

## A. Local slack/formation conjugacy

With right-indexed target/candidate one positions and

\[
D_t=A_t-(q-t-1),
\qquad
s_t=B_t-(q-t-1),
\]

define the projective normalized suffix carry

\[
c_t=2^{-(q-t-1)}z_t\pmod{3^{q-t}}.
\]

Then the suffix gate becomes

\[
c_{t+1}
=
\frac{2c_t+2(2^{D_t}-2^{s_t})}{3},
\]

which is exactly the algebraic one-step formation transition with local ranks

\[
(D_t,s_t).
\]

### Audit status

**EXACT / CLOSED locally.**

The equality is projective and one-step.  It does not identify the full integer formation state or its corridor constraints.

## B. Direct global stitching

For consecutive local pairs to be consecutive edges of one ordinary nonincreasing formation rank path, the previous ending rank must equal the next starting rank:

\[
s_t=D_{t+1}.
\]

Equivalently,

\[
B_t=A_{t+1}+1.
\]

General target-dominance does not imply this condition.  It fails even for candidate=target whenever the target has a one-gap of size 2.

Finite regression through length 8:

- projective local gates checked: `438,144`;
- consecutive rank boundaries checked: `19,273`;
- direct stitches: `8,399`;
- non-stitches: `10,874`;
- non-stitches with candidate=target: `522`;
- reset would require rank increase: `7,904`;
- reset would require a descending connector: `2,970`.

### DSD ruling

**REJECTED**:

\[
\text{local recurrence equality}
\Rightarrow
\text{one global formation rank path}.
\]

A descending connector is not a free relabel because every nonempty formation block changes the carry by a nontrivial affine map.  A rank-increasing reset is outside the established formation automaton.

Therefore bounded-drop formation path counts must not be imported into the suffix slack family merely from the local recurrence coincidence.

## C. Finite source/ballot product quotient

For future raw-bit horizon `d`, retain

\[
Q_d^{src}=(y\bmod2^d,3^q\bmod2^d)
\]

and

\[
B_d=(S,\Delta_1,\ldots,\Delta_d),
\qquad
\Delta_i=Q(h+i)-Q(h+i-1).
\]

The product

\[
P_d=(B_d,Q_d^{src})
\]

is sufficient to determine, for every low parameter residue modulo `2^d`,

1. the emitted parity block;
2. all pure-ballot prefix verdicts through the horizon;
3. the outgoing surplus within that horizon.

### DSD ruling

**SAFE / EXACT finite-horizon control quotient.**

It permits transition-template sharing, not source-payload merging.

Exact payload coordinates such as source residue and parameter interval remain separate.

## D. Current 8-jump measurement

Certified frontier payload count:

`14,224` exact cylinders.

Distinct `P_d` templates:

| d | templates | payload instances saved from duplicate transition logic |
|---:|---:|---:|
| 1 | 18 | 14,206 |
| 4 | 583 | 13,641 |
| 8 | 8,372 | 5,852 |
| 12 | 13,923 | 301 |
| 16 | 14,209 | 15 |
| 17 | 14,213 | 11 |
| 18 | 14,224 | 0 |

Interpretation:

- low precision has strong control/transducer reuse;
- reuse decays rapidly with future precision;
- at `d=18`, this particular quotient completely separates the current payloads.

This is a finite frontier fact, not a theorem that all stronger quotients must fail.

## E. Describability audit

### D — domain

The local conjugacy lives in the projective ternary carry domain.  Formation integer/corridor semantics are a stricter domain and must not be silently imported.

### R — resolution

`P_d` is defined only at explicit finite horizon `d`.  Its precision is consumed as parameter bits are processed.

### S — state sufficiency

`P_d` is sufficient for next-`d`-bit source/parity/ballot transition logic.
It is insufficient for indefinite continuation or later source-sensitive predicates.

### E — equivalence

Equal `P_d` means equal finite-horizon transition problem, not equal source family.

### T — transition

Source quotient transition and ballot control transition are exact and composable over the selected horizon.

### C — closure

No horizon-independent bound follows.  Current 8-jump payloads are fully separated by `d=18` under this quotient.

### N — non-independence

Ballot control and source parity emission are joined as one product state.  Their survival effects must not be multiplied as independent densities.

### O — outstanding

1. find a stronger source-sensitive invariant/quotient whose width does not simply recover all payloads as horizon grows;
2. or find a certified large-block predicate that removes whole source payloads rather than merely sharing transition logic;
3. preserve late activation of checkpoint coordinates;
4. keep formation and suffix carry representations separate until an explicit bridge theorem exists.

## F. Principal conclusion

The current S10 strategy should use finite product templates as an implementation optimization while searching for a genuinely contracting source-sensitive invariant.

Do not spend further proof effort attempting to globalize the slack/formation one-step recurrence by direct rank identification; that route is structurally invalid in general.
