# Finite-horizon source/ballot product-template quotient

Status: **EXACT for a fixed future bit horizon / not a global source-payload merge**

## Purpose

The 8-jump Route-B frontier contains many exact affine source cylinders.  Pure-ballot control is highly reusable, but equal ballot control alone does not justify merging different source payloads.

This theorem identifies a stronger, exact finite-horizon equivalence by combining:

1. the source-channel projective quotient; and
2. the finite future pure-ballot control signature.

It is useful for sharing transition DAGs without identifying distinct source families.

## 1. Source projective state

Let

\[
T^h(X)=y+3^q m.
\]

For a requested future raw-bit horizon \(d\), define

\[
\boxed{
Q_d^{src}(y,q)
=
\left(y\bmod2^d,\;3^q\bmod2^d\right).
}
\]

The certified source-channel projective theorem implies that for every low parameter residue

\[
m\bmod2^d,
\]

this state determines the complete emitted parity prefix of length \(d\).  Equivalently, the online triangular parameter/parity transducer can be run using only this finite precision.

## 2. Ballot future signature

Let

\[
Q(n)=\lceil n\log_3 2\rceil
\]

and current surplus

\[
S=q-Q(h)\ge0.
\]

For a future bit horizon \(d\), define

\[
\boxed{
B_d(h,S)
=
\left(
S,
\Delta_1,\ldots,\Delta_d
\right),
}
\]

where

\[
\Delta_i=Q(h+i)-Q(h+i-1)\in\{0,1\}.
\]

For any proposed future parity word \(w_1\cdots w_d\), the prefix ballot inequalities are obtained by comparing

\[
S+\sum_{j=1}^i w_j
\]

with

\[
\sum_{j=1}^i\Delta_j.
\]

Hence \(B_d\) determines all pure-ballot accept/reject decisions through the next \(d\) bits and the outgoing surplus for every accepted word.

## 3. Product-template theorem

Define

\[
\boxed{
P_d
=
\left(
B_d(h,S),
Q_d^{src}(y,q)
\right).
}
\]

If two exact source cylinders have the same \(P_d\), then for every low parameter residue

\[
e\in\mathbb Z/2^d\mathbb Z,
\]

they:

1. emit the same parity word of length \(d\);
2. receive the same pure-ballot accept/reject verdict at every intermediate prefix;
3. have the same outgoing surplus relative to their corresponding end-of-horizon threshold phase.

Thus \(P_d\) is an exact **finite-horizon transition template**.

## 4. What is shared and what is not

Two source cylinders sharing \(P_d\) may reuse:

- parameter-bit to parity-bit transition code;
- ballot decision logic;
- the accepted low-residue mask modulo \(2^d\);
- any computation whose predicate is proven to observe only these \(d\)-horizon coordinates.

They may **not** be identified as the same source family.

The following remain payload data:

\[
r,\quad[m_{lo},m_{hi}],
\]

and any finer exact state needed after the selected horizon.

After \(d\) bits have been consumed, \(Q_d^{src}\) has spent its precision.  Continuing beyond the horizon requires fresh exact source information.  Therefore

\[
\boxed{
P_d\text{ is not claimed to be a horizon-independent right congruence.}
}
\]

## 5. Current 8-jump measurement

At the certified 8-jump frontier there are

\[
14{,}224
\]

exact source cylinders.

The number of distinct product templates is:

| future raw bits \(d\) | distinct templates | reused payload instances |
|---:|---:|---:|
| 1 | 18 | 14,206 |
| 2 | 88 | 14,136 |
| 3 | 203 | 14,021 |
| 4 | 583 | 13,641 |
| 5 | 1,964 | 12,260 |
| 6 | 3,453 | 10,771 |
| 7 | 5,715 | 8,509 |
| 8 | 8,372 | 5,852 |
| 9 | 10,888 | 3,336 |
| 10 | 12,582 | 1,642 |
| 11 | 13,443 | 781 |
| 12 | 13,923 | 301 |
| 13 | 14,102 | 122 |
| 14 | 14,148 | 76 |
| 15 | 14,178 | 46 |
| 16 | 14,209 | 15 |
| 17 | 14,213 | 11 |
| 18 | **14,224** | **0** |

Thus at \(d=4\) the transition logic can be shared across about

\[
95.90\%
\]

of payload instances, and at \(d=8\) across about

\[
41.14\%
\]

relative to one-template-per-cylinder execution.

But by \(d=18\), all current payloads have distinct product templates.

## 6. DSD interpretation

This separates three levels that must not be conflated.

### Control reuse

\[
\boxed{
\text{same }P_d
\Rightarrow
\text{same next-}d\text{-bit transition problem}
}
\]

is exact.

### Payload identity

\[
\text{same }P_d
\not\Rightarrow
\text{same source family}.
\]

### Global future equivalence

The observed loss of collisions as \(d\) increases shows that this particular quotient does not currently provide a stable horizon-independent compression of the 8-jump source payloads.

The finite result does not prove that no stronger global quotient exists.

## 7. Consequence for S10

Use \(P_d\) as an **execution/DAG-sharing quotient**, not as a proof-level source merge.

The 8-jump state explosion can therefore be reduced computationally over short horizons without duplicating transition logic, while preserving every exact source payload.  However a new structural invariant is still required to make source-family complexity contract or remain bounded as the horizon grows.

## Certificate

`../src/A0_s1_routeB_8jump_source_ballot_product_template_quotient_certificate.py`
