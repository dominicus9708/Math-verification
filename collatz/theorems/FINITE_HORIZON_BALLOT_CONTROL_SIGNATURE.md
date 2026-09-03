# Finite-horizon ballot-control signature

Status: **EXACT / CLOSED for the pure-ballot control factor only**

## Control state

Under the source-payload/control factorization, the pure-ballot jump legality is controlled by

\[
C=(h,S),
\]

where `h` is absolute depth and

\[
S=q-Q(h)\ge0.
\]

For a proposed next zero-run length `a`, the jump `0^a1` is legal iff

\[
S\ge Q(h+a)-Q(h),
\]

and

\[
S+1\ge Q(h+a+1)-Q(h).
\]

The outgoing control is

\[
\tau_a(h,S)
=
\left(
 h+a+1,
 S+1-[Q(h+a+1)-Q(h)]
\right).
\]

This transition is independent of the source payload `(r,y,m_lo,m_hi)`.

## Finite-horizon signature

Define recursively

\[
\sigma_0(h,S)=\star,
\]

and

\[
\boxed{
\sigma_{d+1}(h,S)
=
\bigl((a,\sigma_d(\tau_a(h,S)))\bigr)_{a\in A(h,S)},
}
\]

where `A(h,S)` is the ordered set of ballot-legal jump lengths.

Then two control states have the same `d`-horizon signature iff their labeled pure-ballot control trees are identical through `d` future odd events.

This is an exact finite-horizon equivalence for the **control factor**.

## What it permits

If

\[
\sigma_d(h_1,S_1)=\sigma_d(h_2,S_2),
\]

then the same precomputed ballot-control transition skeleton may be reused for both states for `d` future jumps.

The source arithmetic still has to be applied separately to each payload.

Thus the correct computational form is

\[
\text{shared control template}
\;\otimes\;
\text{distinct source payloads}.
\]

## What it does not permit

Equality of control signatures does **not** imply that two source cylinders are the same family or have the same future source-sensitive realizability set.

In particular it does not justify merging distinct

\[
(r,y,m_{lo},m_{hi})
\]

payloads before H/L, C4F, checkpoint/debit, physical-score, or other source-sensitive predicates have been proven invariant under that merge.

## Current eight-jump frontier

At the certified eight-jump frontier there are

- `14,224` source cylinders;
- only `90` distinct exact control states `(h,S)`.

Among those 90 controls, the number of distinct finite-horizon signatures is:

| future odd-event horizon `d` | signature classes |
|---:|---:|
| 1 | 7 |
| 2 | 13 |
| 3 | 13 |
| 4 | 13 |
| 5 | 20 |
| 6 | 20 |
| 7 | 26 |
| 8 | 26 |
| 9 | 32 |
| 10 | 39 |
| 11 | 39 |
| 12 | 45 |

Thus a four-jump pure-ballot control template needs only 13 transition skeletons for the present frontier, even though the arithmetic payload count is 14,224.

## DSD audit

### EXACT

- control transition depends only on `(h,S,a)`;
- finite-horizon signature equality gives identical labeled ballot-control trees;
- transition skeleton sharing across equal signatures.

### CONDITIONAL

- any identification of source payloads requires a separate invariant/future-equivalence theorem for every remaining predicate.

### FORBIDDEN

- `same ballot signature -> same source family`;
- `same ballot signature -> same H/L/C4F/checkpoint behavior`;
- using finite-horizon signature equality as an infinite-horizon theorem.

## Certificate

- `../src/A0_s1_finite_horizon_ballot_control_signature_certificate.py`
