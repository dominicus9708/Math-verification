# Terminal 28-event locality is not 28-bit/time locality

## Purpose

The late terminal condition

\[
q_{rem}=28
\]

means that only 28 **future one-events** remain.  It does **not** imply that the
checkpoint lies within a bounded window of about 28--50 ordinary parity bits.
This distinction is required for a correct source-preserving late-activation
exporter.

## 1. Exact threshold one-position formula

Let

\[
Q(n)=\min\{q:3^q>2^n\}.
\]

Since `log_3(2)` is irrational for positive integer arguments,

\[
Q(n)=\lceil n\log_3 2\rceil.
\]

If `t_{r-1}` is the zero-based position of the `r`-th one in the threshold
word, then cumulative threshold ones through position `p` equal `Q(p+1)`.
Hence

\[
\boxed{t_{r-1}=\lfloor(r-1)\log_2 3\rfloor.}
\]

## 2. Current terminal activation rank

For the fixed target

\[
t_0=104{,}398{,}605{,}910,
\qquad
j_0=65{,}868{,}186{,}701,
\]

the ternary terminal observation activates when

\[
q=j_0-28=65{,}868{,}186{,}673.
\]

The corresponding threshold `q`-th one position is exactly

\[
\boxed{t_{q-1}=104{,}398{,}605{,}865.}
\]

If a candidate's `q`-th one occurs at zero-based position `a_{q-1}`, choose the
canonical activation seam immediately after that event:

\[
h_{act}=a_{q-1}+1.
\]

Strict target dominance gives

\[
a_{q-1}\le t_{q-1},
\]

while distinct ordered one positions give the trivial lower bound

\[
a_{q-1}\ge q-1.
\]

Therefore

\[
\boxed{
q\le h_{act}\le t_{q-1}+1
=104{,}398{,}605{,}866.
}
\]

Equivalently the remaining ordinary parity-bit length satisfies

\[
\boxed{
44
\le
t_0-h_{act}
\le
38{,}530{,}419{,}237.
}
\]

The lower endpoint `44` is the threshold-near case.  The upper endpoint shows
that event locality alone gives no short bit-time shell.

## 3. Consequence for the paired exporter

The exact terminal locality theorem remains valuable:

- no ternary observation coordinate is needed while at least 28 future
  one-events remain;
- after activation, only 28 one-events must be resolved for the `3^28`
  terminal observation.

But the zero-runs between those one-events may be very long.  Therefore a
correct exporter should work in an **event/valuation representation** such as

\[
0^{a_1}1\,0^{a_2}1\cdots0^{a_{28}}1
\]

with the `a_i` treated as integer gap variables, rather than enumerating every
ordinary parity bit between activation and checkpoint.

This is compatible with the already certified affine valuation jump and
terminal suffix-carry/projective recurrences.

## 4. DSD audit

- **EXACT/CLOSED**: `q_rem=28` means 28 future one-events.
- **EXACT/CLOSED**: `t_{r-1}=floor((r-1) log_2 3)`.
- **EXACT/CLOSED**: at the current activation rank,
  `t_{q-1}=104398605865`.
- **EXACT/CLOSED**: the canonical activation seam may have remaining ordinary
  bit length anywhere in `[44, 38530419237]` under only ordering/dominance.
- **REJECTED**: interpreting terminal 28-one locality as a universal ~43-bit
  time shell.
- **OPEN**: source-preserving compression of the 28 valuation gaps and their
  coupling to right-H/checkpoint provenance.
- **OPEN**: Route-B and global Collatz closure.
