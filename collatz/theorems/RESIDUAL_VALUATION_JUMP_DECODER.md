# Residual valuation jump decoder

Status: **EXACT / CLOSED for an exact fixed source-endpoint instance**

## Setup

Let a remaining accelerated-Collatz parity word `B` have

\[
|B|=n,
\qquad q(B)=q,
\]

start from the exact integer state `Y`, and end at the exact integer `Z`.

Define the required remaining correction

\[
\boxed{R=2^nZ-3^qY.}
\]

A realization exists exactly when `R=C(B)` for a legal length-`n`, one-count-`q` word `B` whose actual parity evolution starts from `Y`.

## First-one valuation theorem

Assume `q>0` and let the first 1 of a realizing word occur at position `a`.
Then

\[
C(B)=3^{q-1}2^a+\sum_{r=2}^{q}3^{q-r}2^{a_r},
\qquad a<a_2<\cdots<a_q.
\]

Factoring `2^a`, the first coefficient is odd and every later term contributes an additional factor of 2. Therefore

\[
\boxed{v_2(R)=a.}
\]

Hence an exact source-endpoint instance has no branching choice for the position of its next 1.

## Exact zero-run jump

Let

\[
a=v_2(R).
\]

If `a>=n`, no length-`n` realization with `q>0` exists.
Otherwise the forced prefix is

\[
0^a1.
\]

Because `n>a`, the endpoint term `2^nZ` vanishes modulo `2^{a+1}`. Since `3^q` is odd,

\[
v_2(Y)=a.
\]

Thus the forced prefix is also exactly the actual parity prefix of `Y`.
After the `a` zero steps and the following odd step,

\[
\boxed{Y'=\frac{3Y+2^a}{2^{a+1}}.}
\]

Set

\[
n'=n-a-1,
\qquad q'=q-1.
\]

Removing the first correction atom and the consumed binary scale gives

\[
\begin{aligned}
R'
&=\frac{R-3^{q-1}2^a}{2^{a+1}}\\
&=2^{n'}Z-3^{q'}Y'.
\end{aligned}
\]

Therefore the exact same problem restarts on the suffix.

## Decoder

Repeat:

1. compute `R=2^nZ-3^qY`;
2. if `q=0`, accept iff `2^nZ=Y`;
3. otherwise require `R>0` and set `a=v2(R)`;
4. require `a<n`;
5. discharge the forced prefix `0^a1`;
6. replace `(Y,n,q)` by
   \[
   \left(\frac{3Y+2^a}{2^{a+1}},\ n-a-1,\ q-1\right);
   \]
7. continue.

The procedure either rejects or reconstructs the unique possible parity word.

Hence

\[
\boxed{
\#\{B:\ |B|=n,\ q(B)=q,\ T^n(Y)=Z\}\le1.
}
\]

More strongly, acceptance of the decoder is an exact existence certificate for the fixed source-endpoint instance, because every forced prefix is verified against the actual parity of the current state.

## Relation to existing correction injectivity

Fixed-`(n,q)` correction injectivity proves uniqueness.
The valuation recursion above supplies an explicit inverse and connects it directly to the source/end-state equation.

This distinction matters for the active S10 frontier: exact pairwise inversion is no longer an open mathematical question.

## Computational scope

The theorem does **not** make the full A0 family computationally small.
The target values of `n` and `q` are enormous, and the current source/checkpoint data are represented by large families rather than one exact pair.

Thus the remaining computational task is to execute or quotient this forced decoder over an exact source/checkpoint family without enumerating every member or every one-event.

## DSD interpretation

For an exact pair `(Y,Z,n,q)`, the correction-language choice axis collapses:

\[
\text{many candidate words}
\longrightarrow
\text{zero-or-one forced word}.
\]

Therefore an exact-pair state does not need an independent correction-language branch coordinate.
Formation predicates should instead be checked against the unique word as it is forced by the decoder.

At family resolution, however, different members can have different valuations and therefore different forced prefixes. Merging them requires an exact cylinder/quotient theorem preserving those future valuation branches.

## Audit restrictions

This theorem does not prove:

- that a large source cylinder has one common decoded word;
- that a residue or interval determines `v2(R)` unless certified;
- H/L, C4F, tail, renewal, or Route-B membership for a decoded word;
- A0 `s=1` Route-B closure;
- the Collatz conjecture.

## Certificate

- `../src/A0_s1_residual_valuation_jump_decoder_certificate.py`
