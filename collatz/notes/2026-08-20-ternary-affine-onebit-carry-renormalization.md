# Ternary-affine one-bit carry renormalization

Date: 2026-08-20

Status: **exact state compression for repeated five-step sparse-tail renormalization.** This is not a proof of the Collatz conjecture.

## 1. Canonical endpoint box

For a fixed parity word of length \(k\), let

- \(r\) be its least positive canonical start representative,
- \(q\) its odd-step count,
- \(c=T^k(r)\) its canonical endpoint.

The canonical lift recurrence gives

\[
\boxed{1\le r\le2^k,\qquad1\le c\le3^q.}
\]

The endpoint bound follows inductively. Assume \(1\le y\le3^q\).

- For an even next bit, the canonical carry either leaves \(y\) unchanged or replaces it by \(y+3^q\), after which division by two gives a new endpoint at most \(3^q\).
- For an odd next bit, the adjusted preimage is at most \(2\cdot3^q\), so \((3y+1)/2\) after the canonical adjustment is at most \(3^{q+1}\).

Equality \(c=3^q\) is preserved only by the all-even continuation from the initial equality state; once an odd step occurs the endpoint inequality is strict.

## 2. Input affine ternary progression

Use the sparse-tail progression state

\[
\boxed{
x=A+3^a u,\qquad u\ge0.}
\]

After normalization, write

\[
\boxed{A=\rho+e3^a,\qquad0\le\rho<3^a.}
\]

The claim is that repeated five-step renormalization needs only

\[
\boxed{e\in\{0,1\}.}
\]

Thus the lower-floor information is a single carry bit.

## 3. Exact intersection with a five-step cylinder

Let a five-step parity word have canonical data \((r_w,q_w,c_w)\). Its start cylinder is

\[
x=r_w+32t.
\]

Put \(M=3^a\). The congruence intersection is determined by

\[
\boxed{
t_0=\left[(\rho-r_w)32^{-1}\right]_M.}
\]

The canonical CRT intersection point is

\[
x_{\rm res}=r_w+32t_0,
\qquad0\le t_0<M.
\]

Because the input floor satisfies \(A<2M\), while the common period is \(32M\), the least point in the actual half-infinite progression is

\[
\boxed{
x_0=x_{\rm res}+n32M,\qquad n\in\{0,1\},}
\]

where \(n=1\) only when \(x_{\rm res}<A\).

## 4. Endpoint progression and one-bit output carry

The five-step affine map gives

\[
T^5(x_0)=c_w+3^{q_w}(t_0+nM).
\]

Put

\[
M'=3^{a+q_w}.
\]

Since

\[
c_w\le3^{q_w},
\qquad0\le t_0\le M-1,
\]

we have

\[
c_w+3^{q_w}t_0\le M'.
\]

If the inequality is strict, then adding the possible pull-up term \(nM'\) gives an endpoint strictly below \(2M'\).

The equality case requires simultaneously

\[
c_w=3^{q_w}
\quad\text{and}\quad
t_0=M-1.
\]

The first condition is the all-even five-step word. In that case \(r_w=32,q_w=0,c_w=1\), and the second condition forces \(\rho=0\). Then

\[
x_{\rm res}=32M>A
\]

for every normalized input with \(e\in\{0,1\}\), so \(n=0\). Hence the endpoint is still at most \(M'\), not \(2M'\).

Therefore in all cases

\[
\boxed{0<T^5(x_0)<2M'.}
\]

Writing

\[
T^5(x_0)=\rho'+e'M',
\qquad0\le\rho'<M',
\]

gives the invariant

\[
\boxed{e'\in\{0,1\}.}
\]

## 5. Compressed exact sparse-tail state

The repeated five-block affine-progression state can therefore be written as

\[
\boxed{
(s,h,a,\rho,e),
\qquad
0\le\rho<3^a,
\qquad e\in\{0,1\}.
}
\]

The transition under a five-step word is explicit:

\[
\begin{aligned}
t_0&=\left[(\rho-r_w)32^{-1}\right]_{3^a},\\
n&=\mathbf 1_{\{r_w+32t_0<\rho+e3^a\}},\\
y_0&=c_w+3^{q_w}t_0+n3^{a+q_w},\\
a'&=a+q_w,\\
\rho'&=[y_0]_{3^{a'}},\\
e'&=\left\lfloor\frac{y_0}{3^{a'}}\right\rfloor\in\{0,1\},\\
h'&=h+q_w-(b_{s+5}-b_s),\\
s'&=s+5.
\end{aligned}
\]

Thus no unbounded integer floor variable is needed.

## 6. Finite exact certificate

`collatz/src/ternary_affine_fiveblock_carry_certificate.py` exhaustively checks

- all 32 five-bit parity words,
- every \(0\le a\le6\),
- every \(0\le\rho<3^a\),
- both input carry values \(e=0,1\),

for 69,728 exact state/word combinations.

It independently verifies

1. the CRT intersection,
2. minimality above the progression floor,
3. the requested five-bit trajectory,
4. the affine endpoint formula,
5. the output bound \(e'\in\{0,1\}\).

The maximum observed output carry is exactly one, as required by the theorem.

## 7. Consequence

The sparse-tail problem is now more sharply localized. The only growing arithmetic component of the repeated exact state is the ternary syndrome \(\rho\pmod{3^a}\); the phase, height update, and progression-floor correction are finite/small auxiliary channels.

The next target is therefore to quotient or renew the growing ternary syndrome without losing the exact min-plus ordering. A successful renewal/quotient theorem here would connect directly to the already established finite Hensel/formation renewal certificates and would provide the deterministic tail half of the corrected Stage-4 bulk/sparse program.
