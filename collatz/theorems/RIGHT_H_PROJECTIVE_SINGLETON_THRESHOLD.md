# Right-H projective singleton threshold

Status: **EXACT / CLOSED for prescribed cylinders**

## Universal capacity lemma

For a binary block of length `h` with `q` one-events, let `A_t` be its one-positions indexed from the right and define

\[
D_t=A_t-(q-t-1).
\]

Because there must be `t` later one-events after `A_t`,

\[
A_t\le h-t-1.
\]

Therefore

\[
\boxed{0\le D_t\le h-q}.
\]

Every legal candidate slack satisfies

\[
0\le s_t\le D_t.
\]

At remaining ternary precision `m`, a prescribed projective transition fixes one slack residue class modulo

\[
\lambda_m=2\cdot3^{m-1}.
\]

Hence, whenever

\[
\lambda_m>h-q,
\]

the prescribed cylinder intersects the complete legal slack interval in at most one integer.

## Current right-H block

At the existing critical cut,

\[
h_R=630{,}138{,}897,
\qquad
q_R=397{,}573{,}380,
\]

so

\[
h_R-q_R=232{,}565{,}517.
\]

But

\[
\lambda_{17}=86{,}093{,}442
\le232{,}565{,}517,
\]

while

\[
\lambda_{18}=258{,}280{,}326
>232{,}565{,}517.
\]

Thus

\[
\boxed{m\ge18\Rightarrow\text{every prescribed right-H projective cylinder is empty or singleton}.}
\]

This sharpens the prior generic `m>=23` bound.

For the currently relevant terminal precisions this certifies high-precision empty/singleton ranges of at least:

- `L=24`: 7 one-event gates (`m=24,...,18`);
- `L=28`: 11 one-event gates;
- `L=47`: 30 one-event gates.

## Scope restriction

A singleton **prescribed cylinder** is not a singleton **carry path**.

The theorem does not bound how many distinct outgoing carry/cylinder states are present. Therefore raw carry-family compression remains an open part of G2.

## Certificate

- `../src/A0_s1_routeB_rightH_projective_singleton_threshold_certificate.py`

Its finite small-word and residue-spacing checks are regression guards only; the theorem is the capacity inequality plus residue spacing.
