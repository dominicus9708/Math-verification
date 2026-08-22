# Packed-terminal s=1 predecessor rule at coefficient plateaus

Date: 2026-08-20

Status: **deterministic original-start elimination lemma plus exact finite state-count calibration.** This is not a proof of the Collatz conjecture.

## 1. Context

The corrected Stage 3C does not permit a later local decrease \(x-\Delta<x\) to be called a minimality contradiction unless it is pulled back to an integer start smaller than the original minimal counterexample N.

The alternate-predecessor integerization theorem supplies one safe pullback mechanism. This note isolates a particularly simple infinite family of such pullbacks.

## 2. Coefficient plateau

Let

\[
q_{\min}(L):=\min\{q:3^q\ge2^L\}.
\]

Call L a coefficient plateau when

\[
\boxed{q_{\min}(L)=q_{\min}(L-1)=q.}
\]

Then a coefficient-surviving word can arrive at length L with exactly q odd symbols by appending an even bit to a boundary word of length \(L-1\).

The plateau identity also implies

\[
\boxed{3^{q-1}<2^{L-1}.}
\]

## 3. Packed-terminal alternate

Among all length-L binary words with exactly q odd symbols, put all odd symbols as far to the right as possible:

\[
\boxed{u^*_{L,q}=0^{L-q}1^q.}
\]

If the odd positions of a q-word are

\[
p_1<\cdots<p_q,
\]

its correction is

\[
R=\sum_{j=1}^q3^{q-j}2^{p_j}.
\]

Since

\[
p_j\le L-q+j-1
\]

and every coefficient is positive, \(u^*\) maximizes R for fixed L,q.

Its correction has the closed form

\[
\boxed{
R^*_{L,q}
=2^{L-q}(3^q-2^q).
}
\]

## 4. The s=1 pullback

Let w be a coefficient-surviving length-L word with exactly q odd symbols and final bit zero. Suppose

\[
\boxed{v_3(R^*_{L,q}-R_w)=1.}
\]

Write

\[
R^*_{L,q}-R_w=3C_0.
\]

In the integerization notation,

\[
s=1,
\qquad
d=q-1.
\]

For \(u^*\), the \((q-1)\)-th odd occurs at zero-indexed position \(L-2\), hence at time

\[
\boxed{t_d=L-1.}
\]

The plateau inequality gives

\[
2^{t_d}=2^{L-1}>3^{q-1}=3^d.
\]

Thus the prefix is contracting. The exact alternate-predecessor integerization theorem then constructs a genuine integer predecessor in the original-start coordinate.

In the current large-start regime

\[
N\ge N_{\min}=4(3^{44}+3^{32})+3
\]

and \(L\le44\), the positivity and size inequalities are automatic because every length-L correction is less than \(3^L<N_{\min}\).

Therefore:

> **Packed-terminal s=1 elimination lemma.** At a coefficient plateau, any coefficient-surviving boundary-even word w satisfying \(v_3(R^*_{L,q}-R_w)=1\) cannot be the corresponding prefix of a minimal counterexample in the stated large-start regime.

This is an original-start predecessor construction, not the withdrawn repeated local residue-maximality argument.

## 5. Terminal mod-9 form

Only the last two odd positions of w are needed.

Let

\[
p_{q-1}<p_q
\]

be its last two zero-indexed odd positions. Then

\[
\boxed{
R_w
\equiv
3\,2^{p_{q-1}}+2^{p_q}
\pmod9.
}
\]

For the packed-terminal alternate,

\[
\boxed{
R^*_{L,q}
\equiv
3\,2^{L-2}+2^{L-1}
\pmod9.
}
\]

Hence

\[
v_3(R^*-R_w)=1
\]

is exactly

\[
R_w\equiv R^*\pmod3,
\qquad
R_w\not\equiv R^*\pmod9.
\]

Because powers of two modulo 9 have period six, this rule is a finite terminal-state condition on

\[
\boxed{(p_{q-1},p_q,L)\pmod6.}
\]

No full correction integer is required to test it.

## 6. Exact finite counts

The certificate tracks only

- total odd count q;
- the last two odd positions modulo six;
- coefficient survival.

Selected exact plateau counts are

\[
\begin{array}{c|r|r|r}
L&|\mathcal B_L|&\text{boundary-even q layer}&s=1\text{ eliminated}\\\hline
6&8&3&1\\
9&38&12&4\\
11&128&30&13\\
14&734&173&61\\
17&4,228&961&337\\
19&14,990&2,652&1,101\\
22&93,222&17,637&6,199\\
25&573,162&108,950&38,119\\
28&3,524,586&663,535&231,515\\
30&12,771,274&1,900,470&775,398\\
38&1,934,757,182&257,978,502&104,198,298\\
49&1,991,314,765,702&248,369,601,964&100,037,865,953
\end{array}
\]

The eliminated share of the boundary layer is already roughly 0.35--0.43 across these examples. The eliminated share of the complete coefficient language decreases much more slowly, for example

\[
\frac{6199}{93222}\approx0.06650
\]

at L=22 and

\[
\frac{100037865953}{1991314765702}\approx0.05024
\]

at L=49.

These are finite scaling observations, not an asymptotic lower bound.

Certificate:

`collatz/src/packed_terminal_s1_predecessor_certificate.py`.

## 7. Interpretation

This lemma provides a safe deterministic operator concentrated exactly at the coefficient boundary:

\[
\text{boundary even child}
\quad\longrightarrow\quad
\text{terminal mod-9 test}
\quad\longrightarrow\quad
\text{smaller original predecessor}.
\]

It is therefore naturally compatible with the existing mass-transport identity

\[
2C_{\rm next}=2C-D+K.
\]

A promising next step is to split the boundary mass D by the finite terminal mod-6 state and quantify how much of D is deterministically removed by the packed-terminal predecessor before any probabilistic/transversality estimate is used.

This may improve the safe coefficient-only transport theorem without reintroducing the invalid repeated residue-maximality assumption.
