# Terminal 28-gate target-dominance saturation

Status: **EXACT / CLOSED for target-dominance suffix existence at terminal precision 28**

## Setting

At the current right-H terminal window, keep only the final

\[
L=28
\]

ranked one-events.  Index them from the right by `t=0,...,27`.

Let

\[
A_t
\]

be the target ranked-one exponent,

\[
B_t=\operatorname{base}_t+s_t
\]

the candidate exponent, and

\[
0\le s_{t+1}\le s_t\le D_t
\]

the exact target-dominance ordering constraints.

The carry gate is

\[
z_t+2^{A_t}-2^{B_t}\equiv0\pmod3,
\]

with

\[
z_{t+1}
=\frac{z_t+2^{A_t}-2^{B_t}}3.
\]

## Local mod-3 obstruction

Because `2^n mod 3` depends only on parity, a fixed target exponent `A` admits exactly two incoming carry classes modulo 3:

\[
G(A)=
\begin{cases}
\{0,1\}, & A\text{ even},\\
\{0,2\}, & A\text{ odd}.
\end{cases}
\]

No choice of candidate exponent can pass the one-gate divisibility test outside `G(A)`.

## Lifting lemma

Suppose the remaining suffix from the next gate is guaranteed whenever its incoming slack cap is at least `T`.

Fix arbitrary residues

- `z_t mod 9` consistent with the local admissible mod-3 class;
- `A_t mod 6`;
- `base_t mod 6`;
- next target parity;
- `T mod 6`.

Among the four consecutive slack values

\[
T,T+1,T+2,T+3,
\]

there is always one `s_t` such that

1. the current numerator is divisible by 3; and
2. the successor carry lies in the next gate's local admissible set modulo 3.

This is a complete finite residue lemma modulo 6 and 9.

Hence the sufficient slack thresholds satisfy

\[
T_{27}=1,
\qquad
T_t=T_{t+1}+3.
\]

Therefore

\[
\boxed{T_0=82}.
\]

## Current capacity margin

The actual 28 target capacities satisfy

\[
D_t\ge232{,}565{,}502
\]

for every terminal rank.

In particular

\[
D_t\gg T_t.
\]

Thus every locally admissible incoming carry lifts through the entire 28-gate suffix.

Consequently the complete target-dominance acceptance set is exactly

\[
\boxed{z_H\bmod3\in G(A_0)}.
\]

The current rightmost target exponent is

\[
A_0=630{,}138{,}896,
\]

which is even. Hence

\[
\boxed{z_H\bmod3\in\{0,1\}}.
\]

Equivalently, exactly

\[
2\cdot3^{27}
\]

of the `3^28` terminal carry residues satisfy target-dominance suffix existence.

This is an exact cardinality statement, not a probability statement.

## Ordinary-checkpoint corollary

The synchronized right-H observation is

\[
z_H\equiv2^S Z-C(H_s^*)\pmod{3^{28}}.
\]

Since `S` is odd,

\[
2^S\equiv2\pmod3,
\]

and because the final target ranked-one exponent `A_0` is even,

\[
C(H_s^*)\equiv1\pmod3.
\]

Therefore

\[
z_H\equiv2Z-1\pmod3.
\]

The accepted carry classes `{0,1}` correspond exactly to

\[
\boxed{Z\bmod3\in\{1,2\}},
\]

or equivalently

\[
\boxed{3\nmid Z}.
\]

## DSD audit

### EXACT / CLOSED

- the one-gate mod-3 obstruction;
- the universal `+3` lifting lemma;
- the threshold `T_0=82` for 28 gates;
- saturation under the actual right-H capacities;
- exact dominance-only acceptance set `z_H mod 3 in {0,1}`;
- checkpoint corollary `3 does not divide Z`.

### Important consequence

For **target-dominance suffix existence alone**, the nominal 28-trit terminal predicate saturates after its first ternary digit.  Higher terminal trits do not further restrict existence because the enormous slack capacity can lift every locally admissible first digit through the remaining 27 gates.

### NOT CLOSED

- additional H/L grammar boundary or block-control labels;
- the exact long correction-language membership predicate;
- source/checkpoint same-orbit compatibility;
- Route-B closure.

Therefore the synchronized CRT singleton theorem remains a valid exact seam when a full `z_H mod 3^28` observation is supplied, but target-dominance existence by itself supplies only two residue cylinders modulo 3 and is not sufficient to expose an ordinary checkpoint singleton.

## Certificate

- `../src/A0_s1_routeB_terminal_28gate_dominance_saturation_certificate.py`
