# Fixed-target remaining-counter derivation

Status: **EXACT / CLOSED**

## Setup

In the current A0 `s=1` Route-B pre-bridge, the total target length and total target one-count are fixed:

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701.
\]

At an active prefix depth `h`, let the realized one-count be `q` and let pure-ballot surplus be

\[
S=q-Q(h),
\qquad
Q(h)=\lceil h\log_3 2\rceil.
\]

Then

\[
\boxed{q=Q(h)+S.}
\]

## Remaining counters

Because `(t_0,j_0)` are fixed globally,

\[
\boxed{
n_{rem}=t_0-h,
}
\]

and

\[
\boxed{
q_{rem}=j_0-Q(h)-S.
}
\]

Thus neither remaining length nor remaining one-count is an independent persistent state coordinate once `(h,S)` is retained.

## Update across a valuation jump

Suppose the next forced block is `0^a1`. Then

\[
h'=h+a+1,
\qquad
q'=q+1.
\]

The ballot-control update gives

\[
S'=q'-Q(h').
\]

Hence

\[
Q(h')+S'=Q(h)+S+1,
\]

so

\[
q'_{rem}=q_{rem}-1.
\]

The remaining one-count therefore acts as an exact odd-event countdown derived from the normal state rather than a separately stored counter.

## Terminal checkpoint activation

For the current terminal ternary observation, `K=28` final one-events are required.

The terminal suffix becomes the complete remaining-one suffix exactly when

\[
\boxed{q_{rem}=28.}
\]

Equivalently,

\[
\boxed{Q(h)+S=j_0-28.}
\]

At that boundary the future pre-checkpoint word contains exactly the final 28 one-events, so the terminal locality theorem may activate

\[
Z\bmod3^{28}.
\]

No H/L history, checkpoint estimate, or extra countdown coordinate is needed merely to detect this activation boundary.

## DSD consequence

The early/middle persistent source state remains

\[
(r,y,[m_{lo},m_{hi}],h,S),
\]

while

\[
q,\;3^q,\;n_{rem},\;q_{rem}
\]

are derived exactly from fixed target constants and `(h,S)`.

This is a state-axis redundancy theorem only. It does not prove that a family reaches the terminal boundary or realizes a valid checkpoint.

## Certificate

- `../src/A0_s1_fixed_target_counter_derivation_certificate.py`
