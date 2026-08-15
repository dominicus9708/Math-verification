# G13 survival-conditioned transition and exact parent-credit bridge

Date: 2026-08-15

Status: **exact G13-neutral transition-section theorem + exact parent-credit identity**.  This strengthens the earlier unrestricted transition-band calculations by imposing the necessary mechanical prefix-survival condition on the replacement boundary word.  It proves that this particular same-state transition repair mechanism is unavailable through width `h=5232`, and it identifies the exact integer predecessor credit produced by any later CRT lift.  It does **not** prove the Collatz conjecture and does not exclude all orientations of the full gate fibre.

## 1. G13 neutral gate

Use the second-return expanding gate

\[
\boxed{(L,q)=(20026,12635)}
\]

with the gate-wide neutral cube parameters

\[
\boxed{F=5245,\qquad J=7390,}
\]

so

\[
L=F+2J+1,
\qquad
q=F+J.
\]

The G13 phase interval contains no interior mechanical discontinuity, so there is one full-parity mechanical factor type.  An interior phase may be chosen as the exact midpoint

\[
\boxed{
x=5832-\frac{18487}{2}\alpha,
\qquad \alpha=\log_3 2.}
\]

The prefix mechanical odd count is then

\[
\boxed{Q(t)=\lfloor x+t\alpha\rfloor.}
\]

Using the rational enclosure

\[
\frac{15601}{24727}<\alpha<\frac{31867}{50508},
\]

every floor through `t=20026` is decided exactly.  In particular,

\[
\boxed{Q(2028)=1279,}
\]

\[
\boxed{Q(5245)=3309,}
\]

\[
\boxed{Q(20026)=12635.}
\]

## 2. Survival-conditioned transition family

At transition width `h`, replace the last `h` fixed front ones and the first `h` pair coordinates by a binary word `B`:

\[
\boxed{
1^{F-h}\,B\,(01/10)^{J-h}0,
}
\]

where

\[
|B|=3h,
\qquad
|B|_1=2h.
\]

The earlier magnitude theorem deliberately allowed every such `B`, even those that violate the gate survival floor.  Here impose the necessary same-state prefix condition.

Put

\[
s:=F-h.
\]

If `c_B(t)` is the number of ones in the first `t` positions of `B`, then every neutral-surviving realization must satisfy

\[
\boxed{
s+c_B(t)\ge Q(s+t)
\qquad(0\le t\le3h).}
\]

Equivalently,

\[
\boxed{
c_B(t)\ge\ell_h(t):=\max(0,Q(s+t)-s).}
\]

This condition is only necessary for a full gate realization; therefore an exclusion derived from it is safe even though later pair-state constraints are not yet imposed.

## 3. Exact largest correction under the survival floor

Let

\[
0\le p_1<\cdots<p_{2h}<3h
\]

be the one positions of `B`.  The affine correction is

\[
R_B=\sum_{r=1}^{2h}2^{p_r}3^{2h-r}.
\]

For each `r`, let `tau_r` be the first local prefix time at which the survival floor requires `r` ones:

\[
\tau_r:=\min\{t:Q(s+t)-s\ge r\}.
\]

Two exact upper bounds apply to the `r`-th one:

\[
p_r\le h+r-1
\]

from the remaining-capacity constraint, and

\[
p_r\le\tau_r-1
\]

from survival.

Hence the simultaneously latest feasible one positions are

\[
\boxed{
p_r^{\max}
=\min(h+r-1,\tau_r-1).}
\]

They form an admissible increasing sequence and maximize every position coordinate simultaneously.  Therefore they give the exact maximum surviving correction

\[
\boxed{
R_{\max}^{\rm surv}(h)
=
\sum_{r=1}^{2h}
2^{p_r^{\max}}3^{2h-r}.}
\]

The minimum is achieved by the fully front-loaded word

\[
1^{2h}0^h,
\]

which automatically survives, so

\[
\boxed{
R_{\min}(h)=3^{2h}-2^{2h}.}
\]

Thus every two surviving transition words obey

\[
\boxed{
|D_B|\le S_h,
\qquad
S_h:=R_{\max}^{\rm surv}(h)-R_{\min}(h).}
\]

## 4. Hensel target and CRT lifts

The universal balanced-Hensel recurrence is

\[
x_0=8\delta,
\qquad
x_{n+1}=4\left\lfloor\frac{x_n+1}{3}\right\rfloor,
\]

where `delta>0` is an incoming integer predecessor credit and

\[
n=J-h.
\]

The boundary target magnitude is

\[
\boxed{
T_h(\delta)=2^{3h-2}x_{J-h}(\delta).}
\]

A boundary correction difference must satisfy

\[
\boxed{
D_B=-T_h(\delta)+k3^{F+h},
\qquad k\in\mathbb Z.}
\]

Because `x_n` is monotone in `delta`, the bounded recurrent-credit window `1<=delta<=397` is enclosed by the two endpoint targets.

## 5. Survival collapses the first wrapped layers again

The unrestricted transition calculation first admitted a second ternary representative around `h=3216`.  However those words need not survive the actual G13 mechanical floor.

For example at

\[
h=3217,
\qquad s=2028,
\]

the unrestricted positive-difference candidates force the higher-correction word to contain only a handful of ones in the first `h` transition positions.  Yet the actual gate requires

\[
Q(F)=Q(5245)=3309
\]

ones by the end of that subprefix, while the fixed front contributes only `2028`.  The unrestricted wrapped candidates therefore lie far outside the neutral survival language.

The exact survivor span makes this quantitative.  At `h=3217`,

\[
\log_{10}\frac{S_h}{3^{F+h}}
\approx-607.0903.
\]

Thus the apparent early CRT freedom of the unrestricted over-family disappears once the same-state prefix condition is restored.

## 6. Exact survivor/CRT threshold

For every width such that

\[
\boxed{
S_h+T_h(397)<3^{F+h},}
\]

no nonzero CRT lift can enter the complete surviving correction interval for any

\[
1\le\delta\le397.
\]

Therefore `k=0` is the only possible representative.

But for two distinct equal-weight transition words,

\[
v_2(D_B)\le3h-2,
\]

whereas

\[
v_2(T_h)\ge3h.
\]

Hence the `k=0` representative is impossible.

An exact integer scan gives

\[
\boxed{
1\le h\le5232:
\quad
\text{no survival-compatible transition repair in this section}.}
\]

The first width at which a nonzero ternary lift enters the surviving correction span is

\[
\boxed{h=5233.}
\]

At that first width the complete safe lift union over `1<=delta<=397` is only

\[
\boxed{k\in\{-1,0,1\}.}
\]

Thus the survival condition pushes the transition-section obstruction from the unrestricted scale near `3216` all the way to within thirteen coordinates of the end of the fixed front.

## 7. The remaining thirteen widths

For reference, the exact safe lift unions are

\[
\boxed{\begin{array}{c|c|c}
h&F-h&\text{possible }k\text{ interval}\\\hline
5233&12&[-1,1]\\
5234&11&[-3,3]\\
5235&10&[-6,6]\\
5236&9&[-12,13]\\
5237&8&[-25,26]\\
5238&7&[-50,53]\\
5239&6&[-100,107]\\
5240&5&[-201,214]\\
5241&4&[-403,428]\\
5242&3&[-807,856]\\
5243&2&[-1614,1713]\\
5244&1&[-3229,3428]\\
5245&0&[-6461,6859]
\end{array}}
\]

These are **range enclosures**, not existence statements.  A listed lift must still be realized by two words satisfying the same survival state and the exact correction equation.

## 8. Exact cancellation to the parent integer credit

The transition lift index has a much stronger meaning than a local ternary label.

Let

\[
n=J-h,
\qquad
x=x_n(\delta).
\]

The remaining pair cube satisfies the exact balanced-Hensel identity

\[
\boxed{
D_V+2^{2n+1}\delta
=\frac{3^n}{4}x.}
\]

A boundary CRT lift is

\[
\boxed{
D_B=-2^{3h-2}x+k3^{F+h}.}
\]

Restoring the common fixed front `1^(F-h)`, the full gate correction relation is

\[
\begin{aligned}
D_{\rm full}+2^L\delta
&=2^{F-h}
\left[
3^nD_B+2^{3h}
\left(D_V+2^{2n+1}\delta\right)
\right]\\
&=k2^{F-h}3^{F+J}.
\end{aligned}
\]

Since the full gate has odd count

\[
q=F+J,
\]

the parent ordinary predecessor credit is therefore exactly

\[
\boxed{
\Delta_{\rm gate}
=\frac{D_{\rm full}+2^L\delta}{3^q}
=k2^{F-h}.}
\]

This identity is independent of the incoming `delta` after `k` and `h` are fixed.

It is the clearest same-word bridge obtained so far:

\[
\boxed{
\text{ternary transition lift }k
\quad\Longleftrightarrow\quad
\text{ordinary parent credit }k2^{F-h}.}
\]

## 9. First remaining layer

At the first surviving CRT layer,

\[
h=5233,
\qquad
F-h=12.
\]

Therefore any positive nonzero lift must be

\[
k=1
\]

and would generate the exact parent credit

\[
\boxed{
\Delta_{\rm gate}=2^{12}=4096.}
\]

The negative lift gives the corresponding negative displacement and is not an ordinary smaller-predecessor witness in the chosen sign convention.

This does **not** by itself prove that the `k=1` transition word exists.  It states that if a surviving same-state solution exists at the first open layer, its parent integer relation is forced to be `4096`.

## 10. Why the old `397` ceiling is not immediately a contradiction

The existing length-19 quotient analysis found an over-approximated recurrent integer-credit set

\[
|\mathcal C_*|=234,
\qquad
\max\mathcal C_*=397.
\]

However that result is a quotient/state statement, not a universal monotone upper bound on every partial Euclidean macroblock.  The same correction note explicitly showed that scalar credit is not a well-founded global proof rank and that the correct state is set-valued and phase-sensitive.

Therefore

\[
4096>397
\]

must **not** be declared a contradiction without a theorem showing that the large-gate parent relation is forced through the same invariant quotient section.

The present result instead provides the correct handoff target: propagate the finite length-19 state monoid, including `(return phase,Sigma,M)` and the complete integer-relation set, across the G13 gate and test whether a `4096` parent relation can belong to the reachable state.

## 11. Strategic consequence

The transition-section problem has now changed qualitatively.

Previously it appeared to require searching thousands of free boundary bits.  After imposing survival and carrying the CRT lift through the full affine word:

1. all widths through `h=5232` are excluded for this repair mechanism;
2. only thirteen terminal widths remain;
3. every remaining lift `k` immediately determines the ordinary parent credit `k2^(F-h)`;
4. at the first open layer the only positive parent credit is exactly `4096`.

Thus the next object is no longer a raw boundary word.  It is the finite renormalized compatibility state

\[
\boxed{
(\text{G13 phase},\Sigma,M,
\delta_{\rm in},
k,\Delta_{\rm gate})
}
\]

coupled to the dyadic canonical-address and Hensel sibling-max channels.

This is directly aligned with the existing state-monoid/Euclidean-credit program and avoids another flat search over the `20026` time bits of the gate.

## Reproducibility

Exact certificate:

`collatz/src/g13_survival_transition_credit_bridge.py`

Use `--full-scan` to verify every survival-conditioned width from `3217` through `5232` with exact integers.
