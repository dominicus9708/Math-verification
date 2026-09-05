# Pure-ballot / contracting-ceiling redundancy

Status: **EXACT / CLOSED in the active pure-ballot S10 domain**

## Setup

At an accelerated parity prefix of absolute depth `h` with one-count `q`, define

\[
Q(h)=\min\{k:3^k>2^h\}=\lceil h\log_3 2\rceil
\]

in the exact integer-power sense used by the active A0 `s=1` certificates.

Pure-ballot admissibility is

\[
q\ge Q(h).
\]

The historical contracting-ceiling coordinates use

\[
\lambda=\frac{2^h}{3^q}.
\]

A finite endpoint survival ceiling is activated only at a contracting endpoint

\[
\lambda>1.
\]

## Theorem

For every positive-depth pure-ballot prefix,

\[
q\ge Q(h)
\]

implies

\[
3^q\ge3^{Q(h)}>2^h.
\]

Therefore

\[
\boxed{\lambda=2^h/3^q<1.}
\]

Hence no legal pure-ballot prefix lies in the contracting-ceiling domain `lambda>1`.

Conversely, if an extension reaches

\[
\lambda>1,
\]

then

\[
3^q<2^h,
\]

so necessarily

\[
q<Q(h),
\]

which is already a pure-ballot failure.

Since equality `3^q=2^h` is impossible for positive integers `h,q`, there is no nontrivial boundary equality case.

Thus

\[
\boxed{
\text{contracting-ceiling activation inside active S10}
\iff
\text{pure-ballot has already failed}.
}
\]

## Macroblock consequence

The historical contracting-ceiling macroblock trichotomy classifies resource changes across maximal odd-event macroblocks and is exact in its stated domain.

However, when the active Route-B search is already enforcing pure ballot at every prefix:

- a macroblock whose interior and endpoint remain pure-ballot legal never activates a finite contracting ceiling;
- a macroblock that first enters `lambda>1` has already crossed the pure-ballot boundary and is rejected by the existing ballot control;
- therefore the contracting-ceiling predicate contributes no independent pruning factor inside this S10 language.

The macroblock theorem may remain useful in other domains or as structural interpretation, but it should not be counted twice with pure-ballot rejection here.

## DSD interpretation

This is an active-predicate redundancy theorem.

Two descriptive coordinates

\[
S=q-Q(h)
\]

and

\[
\lambda=2^h/3^q
\]

encode the same sign boundary for the current question:

\[
S\ge0\Rightarrow\lambda<1,
\qquad
\lambda>1\Rightarrow S<0.
\]

The real-valued contracting ceiling contains additional information only after entering a domain that the active pure-ballot gate has already excluded.

## Scope restrictions

This does not say that contracting-ceiling/headroom methods are globally useless. It says only that they are not an **independent S10 pruning engine** while every active candidate is required to satisfy pure ballot at every prefix.

It does not address Route-A, non-pure-ballot sectors, post-checkpoint tail conditions, or Collatz globally.
