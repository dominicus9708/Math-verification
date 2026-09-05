# Source-controlled residual correction recursion

Status: **EXACT / CLOSED as an algebraic recursion interface**

## Purpose

The active S10 problem is full correction-language inversion under exact source/control constraints.

A source prefix already carries the dyadic information of the required full correction, so `C_req mod 2^K` must not be added as an independent pruning coordinate.  The useful object is instead the **exact residual correction after the prefix has been discharged**.

## Setup

Let

\[
W=AB,
\qquad |A|=K,
\qquad |W|=t,
\]

with

\[
q(A)=p,
\qquad q(W)=Q,
\qquad q(B)=Q-p.
\]

Let the source be `X`, the state after the exact prefix `A` be

\[
Y=T^K(X),
\]

and let the proposed ordinary endpoint/checkpoint be `Z`.

The required full correction is

\[
C_{req}=2^t Z-3^QX.
\]

Exact correction composition gives

\[
C(W)=3^{Q-p}C(A)+2^K C(B).
\]

The exact prefix identity is

\[
2^K Y=3^pX+C(A),
\]

so

\[
C(A)=2^KY-3^pX.
\]

## Residual correction theorem

Define the prefix residual

\[
R_A
:=
\frac{C_{req}-3^{Q-p}C(A)}{2^K}.
\]

Substituting the endpoint requirement and the exact prefix identity,

\[
\begin{aligned}
C_{req}-3^{Q-p}C(A)
&=2^tZ-3^QX
  -3^{Q-p}(2^KY-3^pX)\\
&=2^tZ-2^K3^{Q-p}Y\\
&=2^K\left(2^{t-K}Z-3^{Q-p}Y\right).
\end{aligned}
\]

Hence the division by `2^K` is exact and

\[
\boxed{
R_A=2^{t-K}Z-3^{Q-p}Y.
}
\]

Therefore

\[
\boxed{
C(W)=C_{req}
\iff
C(B)=R_A,
}
\]

provided `A` is the exact realized source prefix and the total length/one-count split is the stated one.

Equivalently,

\[
\boxed{
C(B)=2^{|B|}Z-3^{q(B)}Y.
}
\]

This is exactly the same correction equation as the original problem, but restarted from the certified prefix state `Y` with only the remaining length and remaining one-count.

## Recursive state consequence

After an exact source/control prefix has been discharged, the historical correction value `C(A)` and the redundant dyadic observation `C_req mod 2^K` need not remain active state coordinates.

For full correction equality, it is sufficient to retain:

1. the exact current source/orbit state `Y` or an exact source cylinder representing it;
2. the remaining length `t-K`;
3. the remaining one-count `Q-p`;
4. the exact future formation/control class needed by the H/L or pre-bridge grammar;
5. the proposed endpoint/checkpoint `Z`, or an exact endpoint class only when the current predicate proves that class sufficient;
6. any predicate-relative nonredundant observation required by the next block.

The correction inversion problem is therefore **self-similar under exact prefix discharge**.

## Legal quotient / merge criterion

Two discharged histories may be merged for the correction-equality predicate only if they induce the same future problem:

\[
(Y,\,t_{rem},\,q_{rem},\,\Gamma_{future},\,Z_{state})
\]

with equality interpreted at the exact resolution actually required by the future predicates.

Equality of an old correction residue alone is not a legal merge criterion.
Equality of a physical score alone is not a legal merge criterion.
Histories with different future formation controls must not be merged merely because their current numerical residuals coincide.

Conversely, if the exact current state, remaining counters, future-control class, and endpoint state are identical, then the historical prefix correction has no further role in the correction-equality recursion; all future correction realizability is determined by the common suffix problem.

## DSD analysis

### Describability axes retained

- **source/state axis**: `Y`;
- **remaining-time/length axis**: `t_rem`;
- **remaining-one-count axis**: `q_rem`;
- **formation/control axis**: `Gamma_future`;
- **endpoint axis**: `Z_state`;
- **predicate-relative observation axis**: only information queried by the next exact gate.

### Information that may be forgotten after exact prefix discharge

- the explicit historical value `C(A)`;
- `C_req mod 2^K` when exact source-prefix control is already present;
- internal prefix details that provably do not alter `Y`, remaining counters, or future-control class.

This is predicate-relative forgetting, not global identification of histories.

## DSD audit

### EXACT / CLOSED

- correction composition;
- exact divisibility of the residual numerator by `2^K` for a realized prefix;
- residual identity
  \[
  R_A=2^{t-K}Z-3^{Q-p}Y;
  \]
- equivalence of full correction equality with suffix correction equality;
- algebraic self-similarity of the inversion problem after exact prefix discharge.

### CONDITIONAL

- merging histories that share a compressed `Y` representation is legal only when that representation is proven sufficient for every remaining source/formation predicate;
- compressing `Z` to a residue/interval is legal only at a predicate that observes no finer endpoint information.

### FORBIDDEN / REJECTED USE

- residual congruence mismatch as full membership rejection outside an active equality gate;
- dropping future H/L/pre-bridge control because the numerical residuals agree;
- treating the recursion theorem as proof that a suffix realization exists;
- treating a finite implementation regression as proof of universal language closure;
- using this S10 recursion to bypass S11 checkpoint/debit/tail obligations.

## Consequence for S10

The first inverse quotient should not store both an exact source prefix and a growing dyadic correction coordinate.

Instead, process an exact prefix block, replace the original problem by its exact residual suffix instance, and quotient only by states with identical certified future realization problems.

The next implementation milestone is a finite-block transducer that compares:

1. direct enumeration of legal suffix words `B`;
2. recursive residual instances produced after prefixes `A`;
3. future-realizability sets for states proposed for merging.

This theorem supplies the algebraic recursion interface only.  Exact finite-block quotient construction and its merge certificate remain ACTIVE.
