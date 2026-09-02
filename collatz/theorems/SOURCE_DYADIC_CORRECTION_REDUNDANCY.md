# Source-prefix dyadic correction redundancy

Status: **EXACT / CLOSED**

## Statement

Let a fixed-total-one-count word split as

\[
W=AB,
\qquad |A|=K,
\qquad q(A)=p,
\qquad q(B)=Q-p.
\]

Exact correction composition gives

\[
C(W)=3^{Q-p}C(A)+2^K C(B).
\]

Therefore

\[
C(W)\equiv3^{Q-p}C(A)\pmod{2^K}.
\]

Suppose a full word of total one-count `Q` is required to connect source `X` to some endpoint.  For every `K` not exceeding the total word length, its required full correction satisfies

\[
C_{req}\equiv-3^QX\pmod{2^K}.
\]

Since `3` is invertible modulo `2^K`, the equality

\[
C(W)\equiv C_{req}\pmod{2^K}
\]

is equivalent to

\[
\boxed{C(A)\equiv-3^pX\pmod{2^K}}.
\]

But the exact affine prefix identity is

\[
2^KT^K(X)=3^pX+C(A).
\]

Hence the boxed congruence is exactly the ordinary source-prefix parity-cylinder condition.

## State consequence

If the active state already carries the exact source parity prefix/control through depth `K`, then adding

\[
C_{req}\bmod2^K
\]

as a second purported membership/pruning coordinate carries no independent information.

The future factor `3^(Q-p)` is an odd unit and merely reweights the same dyadic prefix condition.

Conversely, for a supplied binary prefix `A`, the congruence

\[
3^pX+C(A)\equiv0\pmod{2^K}
\]

has exactly one source residue modulo `2^K`; this is the canonical prefix cylinder represented by the exact source-channel transducer.

Thus the full-correction dyadic observation may be used as an **alternate decoder** when the prefix is not already known, but it must not be counted as an independent pruning channel when the source prefix/control is already present.

## What remains nonredundant

This theorem does **not** make full correction membership redundant.

The following remain genuine obligations:

- future one-count and formation constraints;
- exact suffix correction realization;
- the ordinary endpoint/checkpoint `Z`;
- full equality `C(W)=C_req`;
- tail/renewal obligations;
- Route-B closure.

In particular,

\[
\text{dyadic prefix consistency}
\not\Rightarrow
\text{full correction-language membership}.
\]

## DSD audit

### EXACT / CLOSED

- correction block composition modulo `2^K`;
- cancellation of the future odd factor `3^(Q-p)`;
- equivalence with the source-prefix affine divisibility condition;
- state-axis redundancy conditional on exact source prefix/control.

### REJECTED USE

Treating source parity-prefix information and `C_req mod 2^K` as statistically or logically independent pruning factors.

### ALLOWED USE

Use the dyadic correction residue as a decoder/representation when the source prefix itself is not already part of the state.

## Certificate

- `../src/A0_s1_routeB_source_dyadic_correction_redundancy_certificate.py`
