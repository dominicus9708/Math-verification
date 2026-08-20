# Mechanical phase one-slack sandwich

Date: 2026-08-20

Status: **exact ceiling lemma for the coefficient barrier.** This is not a proof of the Collatz conjecture.

Let

\[
\alpha=\log_3 2,
\qquad
b_n=\lceil n\alpha\rceil.
\]

Because \(\alpha\) is irrational, \(s\alpha\) and \(j\alpha\) are never integers for positive integers \(s,j\).  For arbitrary nonintegral real numbers \(x,y\),

\[
\lceil x+y\rceil-\lceil x\rceil
\in
\{\lfloor y\rfloor,\lceil y\rceil\}.
\]

Taking \(x=s\alpha\) and \(y=j\alpha\) gives

\[
\boxed{
 b_{s+j}-b_s
 \in
 \{b_j-1,b_j\}.
}
\]

Equivalently,

\[
\boxed{
 b_j-1
 \le
 b_{s+j}-b_s
 \le
 b_j.
}
\]

For the generalized phase-height survivor language

\[
\mathcal S_{s,h}(J)
=
\{x\ge1:q_j(x)\ge b_{s+j}-b_s-h\ \forall j\le J\},
\]

this immediately yields the set sandwich

\[
\boxed{
\mathcal S_{0,h}(J)
\subseteq
\mathcal S_{s,h}(J)
\subseteq
\mathcal S_{0,h+1}(J).
}
\]

Therefore the corresponding minima satisfy

\[
\boxed{
\mu_{0,h}(J)
\ge
\mu_{s,h}(J)
\ge
\mu_{0,h+1}(J).
}
\]

The mechanical phase can therefore be removed from any *lower-bound* argument at the cost of at most one unit of slack.  This does not mean that the exact phase state is irrelevant to equality or to renewal conjugacy; it means that the infinite phase family is sandwiched between two phase-zero slack profiles.

For the ordinary depth-five decomposition, the first three branches enter at phase 5 with h=0 and the 31 mod 32 branch enters with h=1.  Hence

\[
\mu_{0,0}(J)\ge\mu_{5,0}(J)\ge\mu_{0,1}(J),
\]

and

\[
\mu_{0,1}(J)\ge\mu_{5,1}(J)\ge\mu_{0,2}(J).
\]

This is useful in the sparse-tail min-plus program because the mechanical phase need not be added as an unbounded independent lower-bound state.  The remaining nontrivial state is height/slack together with the ternary formation/Hensel syndrome.

Finite exact regression over s<=500 and j<=1000 is in

`collatz/src/mechanical_phase_one_slack_certificate.py`.
