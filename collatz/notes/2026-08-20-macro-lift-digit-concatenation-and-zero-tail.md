# Macro lift-digit concatenation and the eventual-zero tail

Date: 2026-08-20

Status: **exact structural reduction of the sparse-tail lift process.** This is not a coefficient-stopping theorem and not a proof of the Collatz conjecture.

## 1. Actual prefix state has one redundant coordinate

Let

\[
b_s:=\min\{q:3^q\ge2^s\}=\lceil s\log_3 2\rceil.
\]

For an actual coefficient-surviving prefix of length \(s\), let \(a\) be its cumulative odd-step count and let the phase-height surplus be

\[
h:=a-b_s.
\]

Hence

\[
\boxed{a=b_s+h.}
\]

Under a length-\(B\) macro block containing \(Q\) odd steps,

\[
\begin{aligned}
a'&=a+Q,\\
h'&=h+Q-(b_{s+B}-b_s).
\end{aligned}
\]

Therefore

\[
a'=b_{s+B}+h'
\]

exactly. The affine exponent \(a\) is not an independent sparse-tail coordinate. For actual prefixes the state may be written as

\[
\boxed{(s,h,\rho)}
\]

with \(a=b_s+h\) reconstructed when needed.

## 2. Affine progression and the next macro lift digit

At one sparse-tail state write the exact candidate progression as

\[
\boxed{x=\rho+3^a t,\qquad t\in\mathbb Z_{\ge0}.}
\]

Fix a length-\(B\) parity block \(W\). Let \(r_W\) be its canonical start residue modulo \(2^B\), represented in \(\{1,\ldots,2^B\}\).

Compatibility with the block means

\[
\rho+3^a t\equiv r_W\pmod{2^B}.
\]

Since \(3^a\) is invertible modulo \(2^B\), the unique least lift digit is

\[
\boxed{
J_W=
\left[(r_W-\rho)3^{-a}\right]_{2^B},
\qquad0\le J_W<2^B.
}
\]

For the actual block followed by \(x\), this is simply

\[
\boxed{J_W=t\bmod2^B.}
\]

Thus

\[
\boxed{t=J_W+2^B t'}
\]

with

\[
t'=\frac{t-J_W}{2^B}\in\mathbb Z_{\ge0}.
\]

## 3. Exact transport of the remaining lift parameter

Let the block contain \(Q\) odd steps and have affine correction \(R_W\):

\[
T^B(z)=\frac{3^Qz+R_W}{2^B}.
\]

Define the minimal compatible seed

\[
x_0:=\rho+3^aJ_W
\]

and its endpoint

\[
\rho':=T^B(x_0).
\]

Substituting \(t=J_W+2^Bt'\) gives

\[
\begin{aligned}
T^B(x)
&=T^B\!\left(\rho+3^aJ_W+3^a2^Bt'\right)\\
&=\rho'+3^{a+Q}t'.
\end{aligned}
\]

Hence the affine progression reproduces itself exactly with

\[
\boxed{
(s,h,a,\rho,t)
\longmapsto
(s+B,h',a+Q,\rho',t').
}
\]

No information is lost.

## 4. Macro digits concatenate exactly

Iterate the preceding identity. After \(n\) macro blocks,

\[
\boxed{
 t
 =J_0
 +2^BJ_1
 +2^{2B}J_2
 +\cdots
 +2^{(n-1)B}J_{n-1}
 +2^{nB}t_n.
}
\]

Therefore the sequence

\[
J_0,J_1,J_2,\ldots
\]

is not a sequence of independent min-plus costs. It is exactly the base-\(2^B\) digit expansion of the original nonnegative progression parameter \(t\), read from low to high digits.

This corrects the proof target: proving a positive average lower bound for the \(J_n\) would be much stronger than necessary.

## 5. Eventual-zero equivalence for an ordinary integer

For every fixed finite integer \(t\), its base-\(2^B\) expansion is finite. Hence there is an \(N\) such that

\[
J_n=0
\qquad(n\ge N),
\]

and at that stage

\[
\boxed{t_N=0.}
\]

Conversely, if an infinite compatible path has

\[
J_n=0
\qquad(n\ge N),
\]

then \(t_N\) is divisible by \(2^{kB}\) for every \(k\). For an ordinary finite nonnegative integer this forces

\[
\boxed{t_N=0.}
\]

Thus an ordinary integer infinite-survivor path is necessarily an **eventually zero-lift path**.

Equivalently, to exclude ordinary-integer infinite coefficient survivors within this lift model, it is sufficient to prove **late macro-lift forcing**:

> every infinite coefficient-surviving compatible path must have \(J_n\ne0\) infinitely often.

This is a structural equivalence only. Proving the required forcing remains open.

## 6. Exact zero-run / minimal-survivor bridge

Suppose the remaining lift parameter has already reached zero at a state \((s,h,\rho)\). Then the next \(n\) macro digits are all zero if and only if the actual integer \(\rho\) itself follows a coefficient-surviving path for the next \(nB\) ordinary steps.

In the notation

\[
\mathcal S_{s,h}(J)
=\{x\ge1:q_j(x)\ge b_{s+j}-b_s-h\text{ for }1\le j\le J\},
\]

this is

\[
\boxed{
J_0=\cdots=J_{n-1}=0
\quad\Longrightarrow\quad
\rho\in\mathcal S_{s,h}(nB).
}
\]

Hence, with

\[
\mu_{s,h}(J)=\min\mathcal S_{s,h}(J),
\]

we obtain the deterministic late-lift criterion

\[
\boxed{
\rho<\mu_{s,h}(nB)
\quad\Longrightarrow\quad
\text{at least one of the next }n\text{ macro lift digits is nonzero.}
}
\]

The converse does not follow from the minimum alone; \(\rho\ge\mu_{s,h}(nB)\) is only a necessary condition for a zero run.

This is the exact bridge between the generalized minimal-survivor solver and late-lift forcing.

## 7. First-five-step branch calibration

The four ordinary coefficient-surviving depth-five branches enter the next phase as

\[
(\rho,s,h)
\in
\{(20,5,0),(40,5,0),(71,5,0),(242,5,1)\}.
\]

Direct exact trajectory checks give the maximum coefficient-surviving zero-lift prefix lengths

\[
\begin{array}{c|c|c}
\rho&\text{ordinary steps before barrier failure}&\text{complete zero 5-blocks}\\\hline
20&1&0\\
40&1&0\\
71&53&10\\
242&50&10
\end{array}
\]

Therefore:

- the `20` and `40` branches require a nonzero new macro lift already in the first subsequent five-step block;
- the `71` and `242` branches cannot continue with zero lifts beyond ten complete subsequent five-step blocks.

These are finite exact statements, not uniform asymptotic bounds.

## 8. What this does and does not solve

The result removes one misleading possible target. Long-term control of the sum or average of \(J_n\) is unnecessary: a fixed ordinary integer automatically has only finitely many nonzero macro digits.

The real obstruction is the opposite one:

\[
\boxed{
\text{can coefficient survival support an infinite eventually-zero lift tail?}
}
\]

Once \(t_N=0\), the future is the ordinary deterministic trajectory of \(\rho_N\). Excluding such a tail for every reachable state is therefore essentially the coefficient-stopping obstruction itself; the digit identity does not solve it.

The useful gain is that the remaining sparse-tail proof task is now localized exactly:

1. use the generalized min-plus function \(\mu_{s,h}\) to force future nonzero macro digits whenever the current base is below the relevant survivor minimum;
2. use Hensel/renewal information to control the reachable bases \(\rho\), rather than trying to bound arbitrary \(J_n\) averages;
3. combine this deterministic late-lift mechanism with the existing Haar-controlled bulk stage.

Certificate:

`collatz/src/macro_lift_digit_concatenation_certificate.py`.
