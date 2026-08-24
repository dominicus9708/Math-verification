# Scope correction for L7 later-block residue maximality

Date: 2026-08-25

Status: **logical audit and scope correction.**  The finite L7 full-Hensel class arithmetic and its local-language entropy certificate remain exact.  What is withdrawn is the unconditional inference that every later aligned block of a hypothetical least counterexample must itself be the maximum-correction representative of its full-Hensel class.

This note does not prove the Collatz conjecture.

## 1. Exact local identity

Let a length-\(L\) actual binary Collatz block begin at an orbit state \(x\), with \(q\) odd symbols and correction \(R_w\):

\[
T^L(x)=\frac{3^q x+R_w}{2^L}.
\]

Let \(u\) be another length-\(L\), weight-\(q\) word in the same full-Hensel correction class,

\[
R_u\equiv R_w\pmod{3^q},
\qquad R_u>R_w.
\]

Then

\[
\Delta:=\frac{R_u-R_w}{3^q}\in\mathbb Z_{>0}
\]

and the alternate start

\[
\boxed{x'=x-\Delta}
\]

satisfies the exact same-endpoint identity

\[
\boxed{
3^q x'+R_u=3^q x+R_w.
}
\]

When the inverse branch is positive/admissible this gives an ordinary smaller predecessor of the **current block state**:

\[
\boxed{x'<x.}
\]

This local algebra is correct and is exactly what the L7/L8/H19 finite Hensel certificates measure.

## 2. Missing inequality in the previous globalization

Let \(N\) denote the original least-counterexample start.  Minimality can be contradicted only by an ordinary positive integer that is smaller than \(N\) and joins the same forward orbit.

For a later orbit state \(x=T^s(N)\), local residue nonmaximality gives

\[
x'=x-\Delta<x,
\]

but it does **not** by itself give

\[
\boxed{x'<N.}
\]

If \(x\) is much larger than \(N\), a bounded local credit \(\Delta\) can leave \(x'\) far above the original root.

Therefore the implication

\[
\text{later block nonmaximal}
\Longrightarrow
\text{contradiction to least-counterexample minimality}
\]

requires an additional root-pullback/headroom theorem.  It is not a consequence of the local Hensel-class identity alone.

## 3. Exact finite witness before the first descent of 27

The source

`collatz/src/l7_later_block_globality_counterexample_certificate.py`

provides a particularly clean logical witness.

Use the binary Collatz map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

The orbit of \(N=27\) first falls below 27 only at binary step 59.  At the aligned step

\[
s=35=5\cdot7
\]

we have

\[
\boxed{x=T^{35}(27)=719.}
\]

The next seven actual parity bits are, in chronological order,

\[
\boxed{w=1111001,}
\]

with

\[
q=5,
\qquad R_w=259.
\]

The full-Hensel class modulus is

\[
3^5=243,
\]

and

\[
259\equiv16\pmod{243}.
\]

The maximum-correction sibling in this class is

\[
\boxed{u=0111011,\qquad R_u=502,}
\]

with

\[
502\equiv16\pmod{243}.
\]

Hence

\[
\Delta=\frac{502-259}{243}=1
\]

and

\[
\boxed{x'=718.}
\]

Both words are realized by ordinary positive integer trajectories:

\[
719\to1079\to1619\to2429\to3644\to1822\to911\to1367,
\]

\[
718\to359\to539\to809\to1214\to607\to911\to1367.
\]

The affine equality is exact:

\[
3^5\cdot719+259
=
3^5\cdot718+502
=
2^7\cdot1367.
\]

But

\[
\boxed{27<718<719.}
\]

Thus the local predecessor is smaller than the later orbit state while still being much larger than the original root.  This occurs before the root orbit's first descent, so even the finite condition “all states seen so far are at least \(N\)” does not repair the inference.

This witness does not say anything negative about the local L7 arithmetic.  It pinpoints the missing global inequality.

## 4. Consequences for the L7 and L8 entropy certificates

The exact class counts remain valid:

\[
(c_0,\ldots,c_7)=(1,2,6,15,21,16,7,1)
\]

for L7, with local maximum credit 21, and the corresponding L8 counts and local maximum credit 42 remain valid.

The macro entropy inequalities also remain exact statements about the **locally residue-maximal sublanguages**.

However their exclusion rates

\[
\eta_{L7}>\frac7{50},
\qquad
\eta_{L8}>\frac2{15}
\]

must not be treated as unconditional deterministic exclusion rates for every later block of a hypothetical least counterexample unless a separate theorem proves that the actual later block is forced into the local-maximal language.

Accordingly, calculations such as the finite selector--L7 frontier remain exact conditional diagnostics for the intersection with that language, but they are not by themselves necessary-condition frontiers for all hypothetical counterexamples.

## 5. Why the repeated-backtrace rule survives this audit

The existing repeated-backtrace local-minimality theorem has the extra ingredient missing above.

At a zero-defect endpoint \(y\), a short inverse exponent code produces an ancestor

\[
m<\frac{2^K}{3^q}y.
\]

For the current m=44 R1 geometry the theorem also proves

\[
y<2\left(N+\frac H3\right),
\qquad
N>\frac{8H}{3},
\]

and for the selected contracting inverse codes

\[
\frac{2^K}{3^q}\le\frac49.
\]

Therefore

\[
m<\frac49\,2\left(N+\frac H3\right)<N.
\]

That final strict inequality is exactly what is absent from naive later-block L7 maximality.  Hence the repeated forbidden 3-adic endpoint classes at zero-defect states are genuine orbit-wide minimality conditions.

This gives the correct design principle:

\[
\boxed{
\text{local alternate relation}
+\text{quantitative root-headroom bound}
\Longrightarrow
\text{valid repeated minimality filter}.
}
\]

## 6. Correct role of L7 after the audit

L7 remains useful in three ways.

1. **Local information geometry.**  It exactly measures the size and correction structure of full-Hensel sibling classes.
2. **Conditional diagnostics.**  It gives strong finite selector intersections and exposes which parts of the hard language are particularly rigid.
3. **Input to a repair-budget theorem.**  Instead of demanding that every actual later block be locally maximal, one may charge local exclusion information against the cost of repairing/pulling back a nonmaximal block.

The third role matches the existing block-exclusion-credit identity

\[
\Gamma_{K:B}=I_{K:B}-R_{K:B}.
\]

The globalization target is then not “all blocks are maximal,” but rather

\[
\boxed{
\sum_j\Gamma_j=+\infty
}
\]

for a positive-density family of valid structural blocks.

## 7. Revised proof frontier

The unconditional proof program should therefore use only one of the following bridges:

### A. Headroom-globalized local predecessor

For a positive-density family of later blocks, prove that any nonmaximal local sibling produces an ordinary ancestor below the original root \(N\).

### B. Repeated backtrace/minimality language

Extend the already valid zero-defect forbidden-residue construction to enough local inverse codes and prove that the resulting repeated language has insufficient capacity.

### C. Net exclusion/repair budget

Retain the exact local L7 information loss, but allow nonmaximal blocks and prove that the total root-level repair amplification has asymptotic rate strictly smaller than the local exclusion rate.

The repository already contains substantial machinery for B and C.  No unconditional use of the L7 \(7/50\) rate should be made until one of these globalization bridges is closed.

## 8. Paper-level interpretation

For a DSD case-study paper this correction is itself useful evidence of the method's auditability:

\[
\text{local structural rule}
\to
\text{attempted globalization}
\to
\text{counter-witness}
\to
\text{scope correction}
\to
\text{stronger state/bridge requirement}.
\]

The mathematically defensible claim is structural reduction and exact certified pruning, together with explicit isolation of the remaining globalization obstruction.  It is not yet an unconditional proof of the Collatz conjecture.
