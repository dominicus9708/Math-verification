# Source-payload / control factorization for valuation jumps

Status: **EXACT / CLOSED for the source-preserving pure-ballot jump interface**

## Setup

At absolute depth `h`, keep the exact source cylinder

\[
X=r+2^h m,
\qquad
m_{lo}\le m\le m_{hi},
\]

and the exact affine current state

\[
T^h(X)=y+3^q m.
\]

Let

\[
Q(h)=\lceil h\log_3 2\rceil
\]

in the exact integer sense used by the ballot certificates, and define the pure-ballot surplus

\[
S=q-Q(h)\ge0.
\]

Then

\[
\boxed{q=Q(h)+S}
\]

and therefore the affine coefficient

\[
\boxed{A=3^q=3^{Q(h)+S}}
\]

is a derived coordinate.  It need not be stored independently.

## Exact valuation child

Suppose the next odd event occurs after `a` zeros, i.e. the forced block is

`0^a 1`.

Since `A` is odd, the condition

\[
v_2(y+Am)=a
\]

selects the unique residue

\[
\boxed{
\rho_a
\equiv
(2^a-y)A^{-1}
\pmod{2^{a+1}}.
}
\]

Write

\[
m=\rho_a+2^{a+1}k.
\]

Then the exact source cylinder becomes

\[
\boxed{
X=r'+2^{h'}k,
}
\]

with

\[
\boxed{
r'=r+2^h\rho_a,
\qquad
h'=h+a+1.
}
\]

The current orbit state after the forced block is

\[
\boxed{
T^{h'}(X)=y'+3^{q+1}k,
}
\]

where

\[
\boxed{
y'=
\frac{3(y+A\rho_a)+2^a}{2^{a+1}}.
}
\]

The parameter interval is transformed exactly by

\[
\left\lceil\frac{m_{lo}-\rho_a}{2^{a+1}}\right\rceil
\le k\le
\left\lfloor\frac{m_{hi}-\rho_a}{2^{a+1}}\right\rfloor.
\]

## Ballot-control factor

The legality of the jump and outgoing surplus depend only on `(h,S,a)`:

\[
S\ge Q(h+a)-Q(h),
\]

\[
S+1\ge Q(h+a+1)-Q(h),
\]

and, when legal,

\[
S'=S+1-[Q(h+a+1)-Q(h)].
\]

Thus the transition separates exactly into:

1. a **control factor** `(h,S)` deciding which `a` are ballot-legal and the outgoing `(h',S')`;
2. a **source payload** `(r,y,m_lo,m_hi)` deciding the exact nonempty residue child and preserving the ordinary source cylinder.

## Reusable state

For source-sensitive downstream predicates, the minimal current structural state is therefore of the form

\[
\boxed{
(r,y,m_{lo},m_{hi},h,S;\ \text{future-predicate labels})
}
\]

rather than

\[
(y,A,m_{lo},m_{hi},h,S).
\]

`A` is redundant, while `r` is not: checkpoint/debit/source predicates may need the exact ordinary source relation

\[
X=r+2^h m.
\]

## DSD interpretation

This is an exact separation between a **control axis** and a **source payload axis**.

Predicate-relative compression is legal as follows:

- `A` may be forgotten because it is exactly recoverable from `(h,S)`;
- ballot transition logic may be shared by states with the same control state/signature;
- source payloads must remain distinct unless a separate theorem proves that every remaining predicate is invariant under the proposed payload identification.

## Scope restriction

This theorem does not merge different source cylinders.
It does not discharge H/L, C4F, checkpoint/debit, tail, or Route-B closure.
It supplies a source-preserving transition interface for the active S10 family computation.

## Certificate

- `../src/A0_s1_source_payload_control_factorization_certificate.py`
