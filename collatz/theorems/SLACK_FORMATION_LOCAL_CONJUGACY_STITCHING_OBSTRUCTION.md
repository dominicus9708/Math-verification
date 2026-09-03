# Slack/formation local conjugacy and stitching obstruction

Status: **EXACT local conjugacy / REJECTED as a general direct global identification**

## Purpose

The Route-B suffix-carry reduction and the established formation automaton contain a superficially identical one-step recurrence.  This note identifies the exact coordinate change, then audits whether that local coincidence can be promoted to one global formation rank path.

The answer is:

- **yes** for the local projective recurrence;
- **no in general** for direct gate-to-gate rank stitching.

This prevents an invalid shortcut in S10.

## 1. Suffix slack coordinates

Let equal-count target/candidate one positions be

\[
a_1<\cdots<a_q,
\qquad
b_1<\cdots<b_q,
\qquad
b_r\le a_r.
\]

Index from the right:

\[
A_t=a_{q-t},
\qquad
B_t=b_{q-t},
\qquad t=0,1,\ldots.
\]

Define

\[
b_t^{\rm base}=q-t-1,
\]

\[
D_t=A_t-b_t^{\rm base},
\qquad
s_t=B_t-b_t^{\rm base}.
\]

Then the dominance/ordering reduction gives

\[
0\le s_t\le D_t,
\qquad
s_{t+1}\le s_t.
\]

The target-relative suffix carry satisfies

\[
z_{t+1}
=
\frac{z_t+2^{A_t}-2^{B_t}}{3}
\]

whenever the corresponding ternary divisibility gate is passed.

## 2. Exact projective normalization

At remaining ternary precision

\[
m=q-t,
\]

powers of two are units modulo \(3^m\).  Define the projective coordinate

\[
\boxed{
c_t
=
2^{-b_t^{\rm base}}z_t
\pmod{3^m}.
}
\]

Because

\[
b_{t+1}^{\rm base}=b_t^{\rm base}-1,
\]

we obtain

\[
\begin{aligned}
c_{t+1}
&=
2^{-(b_t^{\rm base}-1)}
\frac{z_t+2^{b_t^{\rm base}+D_t}-2^{b_t^{\rm base}+s_t}}{3}\\
&=
\frac{2c_t+2(2^{D_t}-2^{s_t})}{3}
\pmod{3^{m-1}}.
\end{aligned}
\]

Hence

\[
\boxed{
c_{t+1}
=
\frac{2c_t+2(2^{D_t}-2^{s_t})}{3}.
}
\]

This is exactly the algebraic form of one established formation transition

\[
F_{a\to b}(c)
=
\frac{2c+2(2^a-2^b)}{3},
\qquad a\ge b\ge0,
\]

under the local identification

\[
(a,b)=(D_t,s_t).
\]

### Scope of the conjugacy

This is a **projective 3-adic one-gate conjugacy**.  It does not by itself identify the normalized suffix carry with an unrestricted integer formation carry satisfying every formation-side interval/sign condition.

## 3. Direct stitching criterion

A standard formation rank path is one sequence

\[
a_0\ge a_1\ge a_2\ge\cdots.
\]

If suffix gate \(t\) is identified with the formation transition

\[
D_t\to s_t,
\]

then gate \(t+1\) can be the immediately following formation transition only if its starting rank equals the previous ending rank:

\[
\boxed{
s_t=D_{t+1}.}
\]

In original one-position coordinates,

\[
\begin{aligned}
s_t=D_{t+1}
&\iff
B_t-(q-t-1)
=
A_{t+1}-(q-t-2)\\
&\iff
\boxed{B_t=A_{t+1}+1}.
\end{aligned}
\]

Therefore direct global rank-path stitching is equivalent to a strong interlacing condition that is **not** part of ordinary prefix dominance.

## 4. Failure already occurs for the target itself

Set candidate equal to target, \(B_t=A_t\).  Then the direct-stitch condition becomes

\[
A_t=A_{t+1}+1.
\]

Thus every target one-gap of size two violates direct stitching.

The characteristic Route-B target has one-gaps in \(\{1,2\}\), so even the target word itself does not generally turn the sequence of local pairs \((D_t,s_t)\) into one standard formation rank path.

This is a structural counterexample to the proposed unrestricted identification; it is not a Collatz counterexample.

## 5. Why rank reset is not free

When

\[
D_{t+1}>s_t,
\]

moving from the previous ending rank \(s_t\) to the next required starting rank \(D_{t+1}\) would require a rank increase, forbidden in the nonincreasing formation automaton.

When

\[
D_{t+1}<s_t,
\]

a descending connector is rank-legal, but it is not a free relabel.  A nonempty formation connector of length \(K\) has affine carry law

\[
3^K c_{out}=2^K c_{in}+D_P,
\]

with path-dependent \(D_P\).  Because \(2^K\ne3^K\) for \(K>0\), no nonempty connector is the identity on all incoming carry states.

Consequently any such connector requires an additional carry-dependent arithmetic condition.  It cannot be silently inserted to globalize the local recurrence.

## 6. DSD audit

### EXACT / CLOSED

- suffix slack coordinates \((D_t,s_t)\);
- projective normalization \(c_t=2^{-b_t^{\rm base}}z_t\);
- local recurrence conjugacy;
- direct stitching criterion
  \[
  s_t=D_{t+1}\iff B_t=A_{t+1}+1;
  \]
- impossibility of a free rank-increase reset;
- nonexistence of a state-independent nonempty identity connector.

### REJECTED shortcut

The implication

\[
\text{same one-step recurrence}
\Longrightarrow
\text{one global formation rank path}
\]

is rejected.

### CONDITIONAL future use

A global bridge remains possible only if a separate theorem explicitly supplies:

1. the boundary-rank transition between \(s_t\) and \(D_{t+1}\);
2. the induced carry transformation;
3. all required integrality/corridor conditions;
4. compatibility with the next suffix gate.

Such a theorem would be additional structure, not a consequence of the local conjugacy alone.

## 7. Consequence for S10

Do not use the slack/formation local recurrence coincidence as justification for:

- replacing the suffix carry DP by one ordinary formation rank path;
- importing bounded-drop polynomial path counts into the suffix family without a bridge theorem;
- merging source families on formation-rank labels alone.

The safe representations remain separate:

\[
\text{suffix side}: (z_t,S_{\max})\text{ or equivalent projective slack state},
\]

and

\[
\text{formation side}: \text{certified H/L or fixed-rank-path arithmetic cylinders}.
\]

Any later joining of those representations must carry an explicit certified interface.

## Regression certificate

`../src/A0_s1_routeB_slack_formation_local_conjugacy_stitching_certificate.py`

The finite audit through target length 8 checks 438,144 projective local gates and 19,273 consecutive-rank boundaries.  It observes 10,874 non-stitching boundaries, including 522 with candidate equal to target.  These counts are implementation evidence; the theorem itself is the algebra above.
