# Two-place backtrace-potential inequality for a minimal counterexample

Date: 2026-08-12

Status: **exact local-minimality inequality + min-plus reformulation**. This note unifies the repeated `3`-adic predecessor filters with the real/Christoffel skew coordinate. It is a necessary condition for a hypothetical minimal counterexample and provides a finite-resolution bridge between the `3`-adic endpoint channel and the real orbit-size channel. It does not prove Collatz.

## 1. Setup

Use the odd-only accelerated map

\[
x_{i+1}=\frac{3x_i+1}{2^{v_i}},
\qquad v_i=v_2(3x_i+1).
\]

Let `N=x_0` be a hypothetical **minimal positive counterexample**.

Every positive integer that merges into the forward orbit of `N` is then at least `N`. Otherwise a smaller positive integer would have the same nonconvergent tail and would itself be a counterexample.

On an R1 first-crossing renewal segment, write

\[
\gamma=\log_2 3,
\qquad
h_i=\lfloor i\gamma\rfloor-a_i\ge0,
\qquad
\theta_i=\{i\gamma\}.
\]

The exact odd-state formula is

\[
\boxed{
x_i=(N+c_i)2^{h_i+\theta_i}.}
\]

Therefore

\[
\boxed{
\log_2\frac{x_i}{N}
=h_i+\theta_i+
\log_2\left(1+\frac{c_i}{N}\right).
}
\]

## 2. Finite back-tracing codes

Take a positive odd-to-odd exponent code

\[
\mathbf a=(a_1,\ldots,a_q),
\qquad a_j\ge1,
\]

with total binary exponent

\[
K(\mathbf a)=\sum_{j=1}^{q}a_j.
\]

Its forward affine map is

\[
F_{\mathbf a}(m)
=\frac{3^q m+R_{\mathbf a}}{2^{K(\mathbf a)}},
\qquad R_{\mathbf a}>0.
\]

If the code is admissible as a positive back-tracing path from the endpoint `x`, then

\[
m
=\frac{2^{K(\mathbf a)}x-R_{\mathbf a}}{3^q}
\]

is a positive integer merging into `x` and

\[
\boxed{
m<\lambda(\mathbf a)x,}
\qquad
\lambda(\mathbf a)
:=\frac{2^{K(\mathbf a)}}{3^q}.
\]

The logarithmic multiplier is

\[
\boxed{
\log_2\lambda(\mathbf a)
=K(\mathbf a)-q\gamma.
}
\]

## 3. Finite-resolution 3-adic backtrace potential

Fix a reverse odd-depth cutoff `Q`.

For an odd endpoint `x`, define

\[
\boxed{
\mathcal B_Q(x)
:=
\min_{\substack{1\le q\le Q\\
\mathbf a\text{ positive backtrace-admissible at }x}}
\left(K(\mathbf a)-q\gamma\right).
}
\]

If there is no positive admissible code within the chosen cutoff, set the value to `+infinity`.

For fixed `Q`, the admissibility data are purely `3`-adic: a depth-`q` code is admissible on one endpoint residue class modulo `3^q`. Hence

\[
\boxed{
\mathcal B_Q(x)
\text{ depends only on }x\bmod3^Q.
}
\]

The quantity is monotone in resolution:

\[
\boxed{
\mathcal B_{Q+1}(x)\le\mathcal B_Q(x).
}
\]

Increasing reverse depth can only add possible smaller multipliers.

## 4. Exact minimality inequality

Let `x_i` be any odd state on the hypothetical minimal-counterexample orbit and let `a` be any positive admissible back-tracing code for `x_i`.

Its ancestor `m` merges into the same nonconvergent orbit, so minimality gives

\[
N\le m.
\]

But

\[
m<\lambda(\mathbf a)x_i.
\]

Therefore

\[
\boxed{
\lambda(\mathbf a)x_i>N.
}
\]

Taking base-two logarithms,

\[
K(\mathbf a)-q\gamma
+\log_2\frac{x_i}{N}>0.
\]

Minimizing over all admissible codes of reverse depth at most `Q` gives

\[
\boxed{
\mathcal B_Q(x_i)
+\log_2\frac{x_i}{N}>0.
}
\]

Substituting the R1 state formula yields the central two-place inequality

\[
\boxed{
\mathcal B_Q(x_i)
+h_i+\theta_i
+\log_2\left(1+\frac{c_i}{N}\right)
>0.
}
\]

This is exact.

## 5. Interpretation

The four terms have distinct roles:

- `B_Q(x_i)`: finite-resolution `3`-adic predecessor potential;
- `h_i`: integer Christoffel/skew displacement;
- `theta_i`: irrational rotation phase;
- `log2(1+c_i/N)`: small positive affine-correction term.

A violation means that the `3`-adic endpoint admits a sufficiently contracting predecessor compared with the actual real size of the orbit state, producing a positive ancestor below `N`.

Thus minimality is a compatibility condition between two places:

\[
\boxed{
3\text{-adic backtrace address}
\quad+\quad
\text{real orbit height}
>0.
}
\]

This is the conceptual form behind the repeated residue filters.

## 6. Min-plus Bellman form

For a residue `r mod 3^q`, define `D_q(r)` to be the minimum total binary exponent `K` among positive `q`-odd-step back-tracing codes admissible at `r`.

The last inverse odd step may use exponent `a>=1` only when

\[
2^a r\equiv1\pmod3.
\]

The predecessor residue is

\[
r'\equiv\frac{2^a r-1}{3}\pmod{3^{q-1}}.
\]

Therefore the exact min-plus recurrence is

\[
\boxed{
D_q(r)
=
\min_{\substack{a\ge1\\2^a r\equiv1\;(3)}}
\left[
 a+D_{q-1}\left(\frac{2^a r-1}{3}\right)
\right],
}
\]

with

\[
D_0=0.
\]

For a finite modulus the exponent search is finite because powers of two are periodic modulo `3^q`; practical threshold calculations can truncate even earlier once the candidate exponent already exceeds the best known cost.

The potential is then

\[
\boxed{
\mathcal B_Q(r)
=
\min_{1\le q\le Q}
\left(D_q(r\bmod3^q)-q\gamma\right).
}
\]

Thus the predecessor channel is itself a finite min-plus dynamic program, directly parallel to the existing forward/backward min-plus structures in the repository.

## 7. Relation to the q<=8 window filter

The previous repeated-backtrace certificates used only coarse sublevel sets of this potential.

At a zero-defect state,

\[
h_i=0,
\qquad
x_i<2\left(N+\frac H3\right).
\]

Selecting all residues whose `B_Q` is sufficiently negative to beat this worst-case factor reproduces the `q<=8` forbidden endpoint classes and the current defect floor

\[
r_*\ge26,381,334,316.
\]

The potential inequality is strictly stronger because it retains the actual phase `theta_i` rather than replacing it by the worst-case bound `theta_i<1`.

## 8. Phase-adaptive next step

For one admissible code with multiplier `lambda`, the exact sufficient condition for a forbidden state is

\[
\lambda (N+c_i)2^{h_i+\theta_i}<N.
\]

Using a lower bound `N>=V_0` and an upper bound on `c_i`, this produces an explicit phase cutoff

\[
\theta_i<\Theta(\lambda,h_i).
\]

Because the critical Sturmian factor cylinders are intervals in the rotation phase, these cutoffs can be inserted by refining the finite rotation partition rather than by inspecting the `H` individual orbit positions.

For example, at `h_i=0`:

- the two-step codes `(1,2)` and `(2,1)` have `lambda=8/9`, so they become forbidden on sufficiently low phase intervals even though they were absent from the worst-case `lambda<1/2` filter;
- the three-step one-extra-exponent codes have `lambda=16/27`, producing a much larger admissible phase range.

This is the next exact target: refine each length-47 Sturmian factor cylinder by the finitely many backtrace-potential phase thresholds and retain a local skew path only if at least one phase subinterval remains compatible with the two-place inequality.

## External background

The finite back-tracing-vector formalism and unique endpoint congruence modulo powers of three are classical. Monks, Monks, Monks & Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph* (Discrete Mathematics 313, 2013; arXiv:1204.3904) explicitly use Wirsching's feasible vectors and the unique `3^q` admissibility class. The two-place potential and its coupling to the R1 skew/rotation coordinate are project-derived here.
