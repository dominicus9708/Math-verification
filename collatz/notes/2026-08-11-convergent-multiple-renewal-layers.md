# Convergent-multiple structure of economical renewal layers

Date: 2026-08-11

Status: **exact refinement of the two-sided continued-fraction filter**. It corrects the shorthand statement that the renewal odd-event count `H` itself must be a convergent denominator: only the reduced ratio `D/H` must be a convergent, so `(H,D)` may be a bounded positive multiple of a primitive convergent pair.

## 1. Setup

Let

\[
\alpha:=\log_2(3/2).
\]

Suppose an economical nearest-layer renewal has a ratio

\[
\frac DH
\]

whose reduced form is the continued-fraction convergent

\[
\frac pq.
\]

Then there exists an integer `s>=1` such that

\[
\boxed{H=sq,\qquad D=sp.}
\]

## 2. Lower convergent multiples

Assume

\[
\frac pq<\alpha.
\]

Then

\[
\alpha H-D
=s(\alpha q-p)>0.
\]

The pair `(H,D)` lies on the nearest lower critical layer exactly when

\[
D=\lfloor\alpha H\rfloor.
\]

Since `D` is an integer, this is equivalent to

\[
\boxed{
0<s(\alpha q-p)<1.
}
\]

Hence the allowed multipliers are precisely

\[
\boxed{
1\le s<\frac1{\alpha q-p}.
}
\]

## 3. Upper convergent multiples

Assume

\[
\frac pq>\alpha.
\]

Then

\[
D-\alpha H
=s(p-\alpha q)>0.
\]

The pair lies on the nearest upper critical layer exactly when

\[
D=\lceil\alpha H\rceil,
\]

which is equivalent to

\[
\boxed{
0<s(p-\alpha q)<1.
}
\]

Thus

\[
\boxed{
1\le s<\frac1{p-\alpha q}.
}
\]

## 4. Unified form

For either side, an economical CF-resonant renewal pair has the form

\[
\boxed{
(H,D)=(sq,sp)
}
\]

for a convergent `p/q` of `alpha`, with the finite multiplicity constraint

\[
\boxed{
1\le s<\frac1{|q\alpha-p|}.
}
\]

Thus each primitive convergent contributes only finitely many nearest-layer aggregate exponent pairs.

Standard continued-fraction estimates place `|q alpha-p|` on the scale of the reciprocal next convergent denominator, so the allowed multiplicity is controlled by the next Diophantine scale rather than being arbitrary.

## 5. Factorization of the aggregate cycle denominator

For a convergent multiple

\[
H=sq,
\qquad
D=sp,
\]

the accelerated length is

\[
A=H+D=s(p+q).
\]

The supercritical cycle-shadow denominator numerator is

\[
Z=2^A-3^H
=2^{s(p+q)}-3^{sq}.
\]

It factors as

\[
\boxed{
Z=
\left(2^{p+q}-3^q\right)
\sum_{j=0}^{s-1}
2^{(p+q)(s-1-j)}3^{qj}.
}
\]

Hence every upper CF-resonant renewal shadow carries the primitive resonance divisor

\[
\boxed{Z_0:=2^{p+q}-3^q.}
\]

The exact shadow denominator remains

\[
\operatorname{den}(C)=\frac{Z}{\gcd(Z,g)},
\]

so future arithmetic work can separate the primitive convergent divisor `Z_0` from the multiplicity factor.

## 6. Role

After excluding macroscopic-cost transitions, the residual renewal language is not indexed by all positive integers `H`. It is supported on a countable hierarchy

\[
\boxed{
\{(sq_k,sp_k):p_k/q_k\text{ a convergent of }\alpha,\ 1\le s<|q_k\alpha-p_k|^{-1}\}.
}
\]

This gives a substantially thinner exact target for the remaining mixed-place formation analysis.
