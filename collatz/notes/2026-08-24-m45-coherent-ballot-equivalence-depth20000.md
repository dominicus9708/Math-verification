# m=45 coherent no-descent implies coefficient survival through depth 20,000

Date: 2026-08-24

Status: **exact finite theorem for the current m=45 layer.**  This corrects the earlier endpoint-only interpretation of the apparent `H=195,q=123` exception.  It is not a proof of the Collatz conjecture.

## 1. Setup

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

a length-\(j\) parity prefix with \(q\) odd symbols has

\[
2^jT^j(N)=3^qN+R_j.
\]

The current recursively sufficient m=45 roots satisfy

\[
N\ge N_{\min}:=4\cdot3^{45}+3
\]

and \(N\equiv3\pmod4\), so their first two accelerated parity symbols are forced `11`.

Define the coefficient barrier

\[
b_j:=\min\{q:3^q\ge2^j\}=\lceil j\log_3 2\rceil.
\]

## 2. Why the earlier q=123 exception was only endpoint-wise

If one fixes only the terminal pair `(H,q)` and maximizes the correction independently, then at

\[
H=195,\qquad q=123=b_{195}-1
\]

the unrestricted maximum correction is large enough that the crude endpoint inequality alone no longer proves descent uniformly over \(N\ge N_{\min}\).

That does **not** imply that one parity word can reach this terminal state while also satisfying

\[
T^i(N)\ge N
\qquad(1\le i<195).
\]

The missing condition is coherence of the entire prefix.

## 3. Mechanical minimum-q induction

Assume no coherent subcritical state has survived before depth \(j\).

Then every coherent no-descent prefix has odd count at least \(b_{j-1}\).  The unique prefix with the minimum possible odd count follows the mechanical Beatty boundary:

- if \(b_j=b_{j-1}\), its minimal child is even;
- if \(b_j=b_{j-1}+1\), its minimal coefficient-surviving child is odd.

No other previous state can produce a smaller odd count, because odd count never decreases.

Therefore a **first** coherent subcritical state can be born only at a barrier-rise depth

\[
b_j=b_{j-1}+1
\]

by taking the even child of the unique previous mechanical-boundary prefix.

Let that previous prefix have correction \(R_{j-1}^{\rm mech}\).  The even offshoot has

\[
q=b_j-1
\]

and the same correction.  Since it is subcritical, it remains unresolved only if

\[
R_{j-1}^{\rm mech}
\ge
N\left(2^j-3^{b_j-1}\right).
\]

The right side increases with \(N\), so it is enough to test \(N=N_{\min}\).

## 4. Exact finite result

The certificate evaluates the exact integer inequality

\[
\boxed{
R_{j-1}^{\rm mech}
<
N_{\min}\left(2^j-3^{b_j-1}\right)
}
\]

at every barrier-rise depth

\[
3\le j\le20{,}000.
\]

All \(12{,}617\) rise offshoots fail the no-descent condition.

Hence no first coherent subcritical state can be born in this range.  By induction,

\[
\boxed{
\left[T^i(N)\ge N\text{ for all }1\le i\le H\right]
\Longrightarrow
\left[3^{q_i}\ge2^i\text{ for all }1\le i\le H\right]
}
\]

for every current m=45 root and every

\[
\boxed{H\le20{,}000.}
\]

In particular,

\[
\boxed{H=195,q=123}
\]

cannot occur on a coherent no-descent trajectory.  The minimum coherent odd count at depth 195 is

\[
\boxed{q=124=b_{195}.}
\]

## 5. Safety margin

Among the tested rise depths, the largest exact ratio

\[
\frac{R_{j-1}^{\rm mech}}
{N_{\min}(2^j-3^{b_j-1})}
\]

occurs at

\[
\boxed{j=19{,}457,\qquad b_j-1=12{,}276,}
\]

and remains strictly below 1 by exact cross multiplication.

Thus depth 20,000 is not close to the first loss of the coherent inequality in this finite scan.

## 6. Role in Stage 4

This theorem is stronger for the current finite layer than the earlier endpoint-wise `uniform_subcritical_safe` audit.

It means that the H=900 selector/Fourier program may legitimately use the pure coefficient-surviving ballot language as an **outer language containing every actual m=45 no-descent candidate**.  Additive correction cannot create an extra coherent branch anywhere before depth 20,000.

The remaining m=45 problem is therefore the exact same-address intersection

\[
\boxed{
\text{45-bit ternary selector family}
\cap
\text{coefficient-surviving dyadic ballot residues}
}
\]

rather than a separate additive-headroom exception problem.

Certificate:

`collatz/src/m45_coherent_ballot_equivalence_depth20000_certificate.py`.
