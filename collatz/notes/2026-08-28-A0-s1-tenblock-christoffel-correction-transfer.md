# A0 s=1: ten-block Christoffel correction transfer and ballot-envelope pruning

Date: 2026-08-28

Status: **SAFE threshold compression / SAFE correction-DAG construction / SAFE necessary pruning / OPEN full correction-language membership.**

This note continues the `A0-s=1` Route B correction-language program.  It does **not** prove the Collatz conjecture and does **not** close `C6A`.

## 1. Constants and threshold word

Let

\[
\alpha=\log_3 2,
\qquad
J_0=10\,439\,860\,591,
\qquad
R_0=6\,586\,818\,670,
\]

and

\[
t_0=10J_0=104\,398\,605\,910,
\qquad
j_0=10R_0+1=65\,868\,186\,701.
\]

For the lower ballot boundary define

\[
b_n=\lceil \alpha(n+1)\rceil-\lceil\alpha n\rceil.
\]

Put

\[
\varepsilon=J_0\alpha-R_0.
\]

Directed rational logarithm bounds prove

\[
\boxed{
0<\varepsilon,
\qquad
10\varepsilon<\frac1{J_0}.
}
\]

Because \(\gcd(R_0,J_0)=1\), every nonzero fractional part of
\(R_0r/J_0\) is at least \(1/J_0\) from the next integer.  Hence the
phase drift through ten consecutive `J0` blocks cannot cross an integer
at any interior residue.

Therefore the full threshold word has the exact factorization

\[
\boxed{
W_{\rm th}=U\,L^9,
}
\]

where

\[
L_r=
\left\lfloor\frac{(r+1)R_0}{J_0}\right\rfloor
-
\left\lfloor\frac{rR_0}{J_0}\right\rfloor
\]

is the lower rational mechanical word of slope \(R_0/J_0\).

Writing the common interior as \(s\),

\[
\boxed{
U=1s1,
\qquad
L=0s1.
}
\]

Thus

\[
|L|=|U|=J_0,
\qquad
q(L)=R_0,
\qquad
q(U)=R_0+1.
\]

No \(104\,398\,605\,910\)-bit expansion is needed.

## 2. Exact correction transfer

For a parity word \(w\), let \(C(w)\) be its accelerated-Collatz affine
correction.  Concatenation obeys

\[
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
\]

Put

\[
K=C(L).
\]

Since \(U\) differs from \(L\) only by the added first odd event,

\[
\boxed{
C(U)=K+3^{R_0}.
}
\]

Repeated block composition gives

\[
\boxed{
C(W_{\rm th})
=
3^{10R_0}
+
A\,K,
}
\]

with

\[
\boxed{
A=
\sum_{i=0}^{9}
3^{(9-i)R_0}2^{iJ_0}.
}
\]

Equivalently,

\[
A=
\frac{2^{10J_0}-3^{10R_0}}
     {2^{J_0}-3^{R_0}}.
\]

The important point is representational: the giant correction is now an
exact arithmetic circuit depending on the single base-block correction
\(K\), rather than an expanded billion-step integer expression.

## 3. Stern-Brocot / Christoffel DAG for the base block

For Farey neighbours

\[
\frac ab<\frac cd,
\qquad
bc-ad=1,
\]

the lower mechanical word of the mediant satisfies

\[
\boxed{
L_{a+c,b+d}=L_{a,b}L_{c,d}.
}
\]

Starting from

\[
\frac01\mapsto 0,
\qquad
\frac11\mapsto 1,
\]

the exact Stern-Brocot path to

\[
\frac{R_0}{J_0}
=
\frac{6\,586\,818\,670}{10\,439\,860\,591}
\]

constructs \(L\) with only

\[
\boxed{127}
\]

mediant nodes, plus the two base nodes.

Therefore the \(J_0=10\,439\,860\,591\) parity bits of \(L\) admit an
exact `129`-node concatenation DAG.

Each node retains

\[
(\text{length},\text{odd count},\text{left child},\text{right child})
\]

and the correction transfer

\[
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
\]

The target word and target correction integer are deliberately **not**
materialized.

The companion certificate exhaustively checks all reduced slopes with
denominator at most `40` against direct mechanical-word generation and
direct correction computation before applying the same exact
Farey-mediant construction to the target slope.

## 4. Pure-ballot correction envelope

At fixed \(t_0,j_0\), correction is coordinatewise increasing in the odd
positions

\[
0\le a_1<\cdots<a_{j_0}<t_0.
\]

The lower ballot threshold delays each \(a_r\) as far as the ballot
constraint permits, so it is the correction maximum of the **pure ballot
language**.

Its odd positions are

\[
a_r^{\rm th}
=
\left\lfloor\frac{r-1}{\alpha}\right\rfloor.
\]

Since

\[
j_0-1<\alpha t_0,
\]

each normalized threshold atom satisfies

\[
3^{j_0-r}2^{a_r^{\rm th}-t_0}<1.
\]

Summing the \(j_0\) atoms gives the exact safe envelope

\[
\boxed{
0\le \frac{C}{2^{t_0}}<j_0
=
65\,868\,186\,701.
}
\]

### DSD scope correction

The statement

\[
C_{\max}=C(W_{\rm th})
\]

is exact for the **pure ballot language**.

It must **not** be promoted without proof to an exact maximum of the
full `W_pre` language, because `W_pre` also carries additional SAFE
`C4F` formation requirements.

However,

\[
W_{\rm pre}\subseteq W_{\rm ballot},
\]

so \(C(W_{\rm th})\), and in particular the simpler bound
\(C/2^{t_0}<j_0\), remains a SAFE upper envelope for every full admissible
bridge.

## 5. New physical-X pruning

For a genuine bridge,

\[
2^{t_0}Z=3^{j_0}X+C.
\]

Define

\[
\lambda=\frac{3^{j_0}}{2^{t_0}},
\qquad
\delta=3-\lambda.
\]

Because

\[
j_0=10R_0+1,
\qquad
t_0=10J_0,
\]

we have

\[
\lambda
=
3\left(\frac{3^{R_0}}{2^{J_0}}\right)^{10}.
\]

Let

\[
d=J_0\ln2-R_0\ln3>0.
\]

Then

\[
\delta=3(1-e^{-10d}).
\]

Directed rational logarithm bounds give a positive rational lower bound
\(d_{\rm lo}\).  From \(e^y\ge1+y\),

\[
1-e^{-y}\ge\frac{y}{1+y},
\]

hence

\[
\delta
\ge
\frac{30d_{\rm lo}}{1+10d_{\rm lo}}
=: \delta_{\rm lo}>0.
\]

Using

\[
L_-=3X-Z
\]

and

\[
\frac{C}{2^{t_0}}
=
Z-\lambda X
=
\delta X-L_-,
\]

the pure-ballot envelope gives

\[
\delta X-L_-<j_0.
\]

The already certified debit corridor has

\[
L_-\le934\,928\,480\,993.
\]

Therefore

\[
\delta_{\rm lo}X
<
934\,928\,480\,993+65\,868\,186\,701.
\]

Exact rational integer division yields

\[
\boxed{
X\le
3\,295\,414\,002\,074\,039\,191\,016.
}
\]

Previously the physical shell only required

\[
2^{71}<X<2^{72}.
\]

The new necessary condition leaves at most approximately

\[
\boxed{39.5662\%}
\]

of that shell.

This is a deterministic pruning theorem, not a probability estimate.

## 6. DSD audit

### SAFE

- directed-rational proof of
  \(0<\varepsilon\) and \(10\varepsilon<1/J_0\);
- exact threshold factorization \(W_{\rm th}=UL^9\);
- identification of \(L\) with the lower rational mechanical word of
  slope \(R_0/J_0\);
- exact correction transfer
  \(C(W_{\rm th})=3^{10R_0}+A\,C(L)\);
- exact `129`-node Stern-Brocot/Christoffel concatenation DAG for \(L\);
- pure-ballot correction maximum at the threshold word;
- safe normalized envelope \(0\le C/2^{t_0}<j_0\);
- deterministic physical pruning
  \(X\le3\,295\,414\,002\,074\,039\,191\,016\).

### REJECTED

- expanding the full `t0` parity word;
- materializing the giant correction integer merely to claim exactness;
- treating an interval between correction extrema as filled;
- treating the pure-ballot maximum as automatically the exact maximum
  after adding all `C4F` restrictions;
- interpreting the new `39.5662%` figure probabilistically;
- promoting this necessary pruning to same-orbit closure.

### OPEN

The full gate remains

\[
C_{\rm req}(X,Z)\in\mathcal C_{\rm pre}.
\]

The new DAG solves the **boundary threshold word** and its correction
transfer, but it does not yet represent every admissible interior
departure above the threshold.

## 7. Next gate

The next state object should augment the Christoffel DAG with **deviation
budget / ballot surplus** while preserving exact correction transfer.

A candidate node state must retain enough information to answer:

1. how much prefix ballot surplus enters and leaves the node;
2. which deviations from the lower mechanical boundary are realizable;
3. how those deviations transform the exact correction;
4. whether two states merged by the quotient remain distinguishable by a
   future start/end correction target.

The DSD admissibility test is therefore:

\[
\boxed{
\text{merge two block states only if every future correction-language
membership query gives the same answer for both.}
}
\]

This is stricter than residue equality or interval overlap and is the
next reverse-dependency attack.

## Companion certificates

- `collatz/src/A0_s1_threshold_tenblock_certificate.py`
- `collatz/src/A0_s1_christoffel_correction_dag_certificate.py`
- `collatz/src/A0_s1_ballot_correction_envelope_pruning_certificate.py`
- `collatz/src/A0_s1_correction_language_injective_decoder_certificate.py`
- `collatz/src/A0_s1_exact_ballot_renewal_certificate.py`
