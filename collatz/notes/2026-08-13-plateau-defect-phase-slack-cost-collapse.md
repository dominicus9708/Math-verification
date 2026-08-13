# Plateau defect cost collapse to rotation phase and slack

Date: 2026-08-13

Status: **exact identity**. It collapses the Archimedean cost of a deterministic plateau `01 -> 10` defect to a function of only the Beatty rotation phase and the local coefficient-survival slack. This sharpens the plateau two-place coordinate theorem; it is not a Collatz proof.

## 1. Setup

Put

\[
\alpha:=\log_3 2,
\qquad
b_t:=\lceil\alpha t\rceil,
\qquad
\delta_t:=b_t-\alpha t\in(0,1).
\]

Let `w` be a length-`L` coefficient-survival boundary word, so

\[
q_t(w)\ge b_t,
\qquad
q_L(w)=b_L.
\]

Fix a deterministic plateau start `j`,

\[
b_{j+1}=b_j,
\]

at which `w` has a mixed pair. Define the slack entering the pair by

\[
\boxed{s_j:=q_j(w)-b_j\ge0.}
\]

The one in that pair has ordinal

\[
\boxed{\ell_j=q_j+1=b_j+s_j+1.}
\]

## 2. Exact local real defect cost

From the adjacent-move formula, changing the mechanically preferred orientation `01` to `10` decreases the real remainder by

\[
d_j
:=
2^{j-L}3^{b_L-\ell_j}.
\]

Substitute

\[
b_L-\ell_j
=
\alpha(L-j)+\delta_L-\delta_j-1-s_j.
\]

Since

\[
3^{\alpha}=2,
\]

we obtain

\[
\begin{aligned}
d_j
&=2^{j-L}
3^{\alpha(L-j)}
3^{\delta_L-\delta_j-1-s_j}\\
&=
\boxed{3^{\delta_L-\delta_j-1-s_j}}.
\end{aligned}
\]

Thus the huge absolute depth `L` and position `j` cancel completely.

## 3. Uniform slack-layer bounds

Because

\[
-1<\delta_L-\delta_j<1,
\]

we have

\[
-2-s_j
<
\delta_L-\delta_j-1-s_j
<
-s_j.
\]

Therefore

\[
\boxed{
3^{-s_j-2}
<d_j<
3^{-s_j}.
}
\]

Equivalently,

\[
\boxed{
\frac19\,3^{-s_j}
<d_j<3^{-s_j}.
}
\]

Hence all plateau defects on the same slack level have Archimedean costs within a factor of nine, uniformly in the global resonance depth.

## 4. Level-set lower bound

Let

\[
N_s^{\rm plat,-}
:=
\#\{j:\ j\text{ deterministic plateau start},\ w_jw_{j+1}=10,\ s_j=s\}.
\]

The exact independent plateau-defect sum gives

\[
E(w_{chr})-E(w)
\ge
\sum_s\sum_{j:s_j=s}d_j.
\]

Therefore

\[
\boxed{
E(w_{chr})-E(w)
>
\frac19
\sum_{s\ge0}3^{-s}N_s^{\rm plat,-}.
}
\]

This is a phase-insensitive but slack-sensitive lower bound. The exact phase-aware expression is

\[
\boxed{
\sum_{j\in J_-(w)}
3^{\delta_L-\delta_j-1-s_j}.
}
\]

## 5. Dyadic partner coordinate

The same plateau defect moves the canonical dyadic address by

\[
\Delta r_j
\equiv
2^j3^{-\ell_j}
=
\boxed{2^j3^{-(b_j+s_j+1)}}
\pmod{2^L}.
\]

Thus at slack level `s`, the two-place coordinate is

\[
\boxed{
\left(
3^{\delta_L-\delta_j-1-s},
\quad
2^j3^{-(b_j+s+1)}\bmod2^L
\right).
}
\]

The real coordinate decays geometrically as `3^{-s}`, while the dyadic coordinate retains exact valuation `j` at every slack level.

This is important structurally: high-slack defects may be cheap in the real shadow but they still create nontrivial high-resolution dyadic lift bits.

## 6. Relation to previous defect-density limits

Earlier density arguments compressed all positive skew locations to one count and then recovered only a coarse average correction loss.

The present identity shows why that compression can lose decisive information:

- low-slack plateau defects have order-one real cost;
- high-slack plateau defects may have exponentially smaller real cost;
- both nevertheless move independent dyadic formation levels.

Therefore the correct object is not just a defect count but the joint level profile

\[
\boxed{
\{(j,s_j):j\in J_-(w)\}.
}
\]

This is the natural input for a coupled Archimedean-budget / dyadic-address argument.
