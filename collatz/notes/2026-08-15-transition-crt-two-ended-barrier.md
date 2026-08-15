# Transition CRT lift and two-ended dyadic/ternary barrier

Date: 2026-08-15

Status: **exact two-ended valuation theorem + strengthened no-wrap exclusion + first wrapped-layer exact interval certificate for `G13` neutral**.  This improves the scalar transition-band magnitude theorem by using the same correction difference simultaneously as a 2-adic and 3-adic object.  It is still a theorem for the enlarged transition sections, not for the entire gate fibre, and it does not prove Collatz.

## 1. General two-ended valuation law for equal-weight parity words

Let `u,v` be distinct binary words of the same time length `N` and the same odd count `q`.  Write

\[
D:=R_u-R_v.
\]

Let `p` be their earliest differing time position.  Before `p` their odd ranks agree.  At position `p`, exactly one word contributes one term

\[
\pm3^s2^p
\]

with odd coefficient, while every later contribution is divisible by `2^(p+1)`.  Hence

\[
\boxed{v_2(D)=p.}
\]

Now let `ell` be their latest differing position and let `r` be the number of common odd symbols strictly after `ell`.  At the latest differing odd event exactly one correction term has 3-adic valuation `r`, while every earlier differing contribution has strictly larger 3-adic valuation.  Therefore

\[
\boxed{v_3(D)=r.}
\]

Thus every equal-weight correction difference has an exact two-ended factorization

\[
\boxed{
D=2^p3^r U,
\qquad \gcd(U,6)=1,
}
\]

where the first differing time position controls the dyadic endpoint and the common odd suffix after the last difference controls the ternary endpoint.

This generalizes the earlier conjugacy-specific two-ended valuation laws to arbitrary equal-weight binary words.

## 2. Specialization to a length-`3h`, weight-`2h` transition block

The enlarged transition section uses a binary boundary block `B` of length

\[
N=3h
\]

with exactly

\[
q=2h
\]

odd symbols.

Two distinct equal-weight blocks must differ in at least two positions.  Therefore their first difference satisfies

\[
p\le N-2=3h-2.
\]

Consequently every nonzero boundary correction difference satisfies

\[
\boxed{v_2(D)\le3h-2.}
\]

## 3. The required Hensel target has too much dyadic divisibility

From the universal Hensel recurrence,

\[
x_0=8\delta,
\qquad
x_{n+1}=4\left\lfloor\frac{x_n+1}{3}\right\rfloor.
\]

For every `n>=1`, `x_n` is divisible by four, and `x_0` is divisible by eight.

At transition width `h`, with `n=J-h`, the required raw boundary correction is

\[
\boxed{
T_h(\delta)=2^{3h-2}x_{J-h}(\delta).
}
\]

Hence throughout the relevant range

\[
\boxed{v_2(T_h)\ge3h.}
\]

Therefore an exact equality

\[
D=T_h
\]

between a nonzero equal-weight boundary difference and the raw Hensel target is impossible:

\[
\boxed{
 v_2(D)\le3h-2
 <3h\le v_2(T_h).
}
\]

The only way to escape this obstruction is through a nonzero ternary CRT lift.

## 4. Unique-congruence-representative barrier

The exact boundary-difference range is

\[
|D|\le M_h,
\qquad
M_h=(2^h-1)(9^h-4^h).
\]

The Hensel congruence is modulo

\[
m_h:=3^{F+h}.
\]

Every candidate has the form

\[
\boxed{
D=-T_h(\delta)+k m_h,
\qquad k\in\mathbb Z.
}
\]

If

\[
\boxed{
M_h+T_h(397)<m_h,
}
\]

then for every `1<=delta<=397`, any nonzero `k` gives

\[
|D|\ge m_h-T_h(\delta)>M_h.
\]

Thus `k=0` is the only congruence representative inside the full correction range, and Section 3 excludes it by 2-adic valuation.

This is strictly stronger than the earlier scalar condition `M_h<T_h`, because it remains valid after the target itself has entered the correction magnitude range.

## 5. Exact strengthened exclusion widths

Let `h_CRT` be the first width where

\[
M_h+T_h(397)\ge3^{F+h}.
\]

Exact integer arithmetic gives

\[
\boxed{\begin{array}{c|c|c}
\text{gate/fibre}&\text{2-adic/unique-CRT exclusion through}&h_{CRT}\\\hline
G_{81}\text{ neutral}&247&248\\
G_{81}\text{ one-slack}&246&247\\
G_{82}\text{ neutral}&250&251\\
G_{82}\text{ one-slack}&249&250\\
G_{13}\text{ neutral}&3215&3216\\
G_{13}\text{ one-slack}&3214&3215\\
G_{14}\text{ neutral}&3463&3464\\
G_{14}\text{ one-slack}&3461&3462
\end{array}}
\]

Compare this with the earlier scalar-magnitude onset:

\[
150,150,151,152,1936,1937,2085,2085.
\]

The two-ended valuation theorem therefore pushes the explicit transition-section exclusion much farther than scalar magnitude alone.

For the second-return neutral gates, for example,

\[
G_{13}:\quad1935\to3215,
\]

\[
G_{14}:\quad2084\to3463.
\]

## 6. Second universal transition ratio

Ignoring exponentially small finite corrections, the unique-representative boundary is determined by

\[
M_h\sim18^h,
\qquad
m_h=3^{F+h}.
\]

Thus

\[
18^h\sim3^{F+h}
\]

or

\[
6^h\sim3^F.
\]

Hence

\[
\boxed{
\frac{h_{CRT}}F\to\log_6 3
=0.6131471927654585\ldots
}
\]

This is a distinct scale from the first scalar-magnitude threshold

\[
\frac{h_*}{F}\to\log_3\frac32
=0.3690702464\ldots.
\]

The transition section therefore has two natural renormalized widths:

1. near `0.369 F`, the boundary first becomes large enough in ordinary magnitude;
2. near `0.613 F`, a second ternary congruence representative first enters the entire boundary correction range.

Between these scales the target is large enough but still **arithmetically impossible** because its dyadic valuation exceeds that of every nonzero equal-weight boundary difference.

## 7. CRT lift index becomes the dyadic endpoint coordinate

After the unique-representative barrier fails, write

\[
D=-T_h+k3^{F+h},
\qquad k\ne0.
\]

Since

\[
v_2(T_h)\ge3h
\]

and the ternary modulus is odd, while the relevant lift indices satisfy `|k|<2^(3h)`, one has

\[
\boxed{
v_2(D)=v_2(k).}
\]

By the general two-ended theorem,

\[
\boxed{
\text{earliest differing boundary bit}=v_2(k).
}
\]

At the opposite end, because the added CRT term is divisible by `3^(F+h)`, while the raw target has much smaller 3-adic valuation,

\[
\boxed{
v_3(D)=v_3(T_h)=v_3(x_{J-h}).}
\]

Therefore

\[
\boxed{
\#\text{ common odd events after the latest difference}
=v_3(x_{J-h}).
}
\]

The same integer lift `k` and the universal Hensel state now determine the two endpoints of any candidate repair.

This is the sought same-word mixed-place bridge in an explicit form.

## 8. Credit disappears from the low dyadic block

Because `x_{J-h}` is divisible by four,

\[
T_h=2^{3h}\,y_h,
\qquad
 y_h:=x_{J-h}/4\in\mathbb Z.
\]

Thus for `N=3h`,

\[
D=-2^N y_h+k3^{F+h}.
\]

Modulo the full local dyadic block,

\[
\boxed{
D\equiv k3^{F+h}\pmod{2^{3h}}.
}
\]

Hence **all dependence on the bounded positive credit disappears from the low `3h` dyadic bits**.  The credit changes only the high integer quotient `y_h`; the low dyadic correction address is controlled solely by `k`.

Equivalently, for the local canonical-start difference of two weight-`2h` blocks,

\[
\Delta\rho
\equiv-3^{-2h}D
\equiv-k3^{F-h}\pmod{2^{3h}}.
\]

This gives a direct deterministic map

\[
\boxed{
\text{ternary CRT lift }k
\longrightarrow
\text{local dyadic start displacement }-k3^{F-h}.
}
\]

## 9. Exact first wrapped layer of `G13` neutral

For

\[
(F,J)=(5245,7390),
\]

the first nonunique width is

\[
\boxed{h=3216.}
\]

At this width the scalar correction range allows only

\[
\boxed{k=-1,0,1}
\]

for every `1<=delta<=397`.  The `k=0` branch is already impossible by the dyadic valuation theorem.

To test `k=+-1` without enumerating 397 credits, write

\[
y(\delta)=x_{J-h}(\delta)/4.
\]

Monotonicity gives

\[
y(1)\le y(\delta)\le y(397).
\]

An exact branch-and-bound recursion for correction differences was run on the entire **continuous integer over-interval**

\[
[y(1),y(397)].
\]

The correction recursion uses

\[
R(0w)=2R(w),
\]

\[
R(1w)=3^{q-1}+2R(w),
\]

with the exact remaining correction bounds

\[
R_{\min}(N,q)=3^q-2^q,
\]

\[
R_{\max}(N,q)=2^{N-q}(3^q-2^q).
\]

For both `k=-1` and `k=+1`, the over-interval state space becomes empty after exactly

\[
\boxed{3216}
\]

prefix steps, with maximum frontier size one.

Therefore

\[
\boxed{
G_{13}\text{ neutral enlarged transition section is excluded through }h=3216
}
\]

for **all** bounded credits `1..397`.

## 10. Next wrapped width `h=3217`

At

\[
\boxed{h=3217}
\]

the scalar range permits

\[
\boxed{k=-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6.}
\]

Again `k=0` is impossible by valuation.

The same exact interval recursion over all credits simultaneously excludes the four near-extreme lifts

\[
\boxed{k=\pm5,\ \pm6.}
\]

The current unresolved lift indices in this transition section are therefore

\[
\boxed{
k=\pm1,\pm2,\pm3,\pm4.}
\]

This is now the first explicit computational bottleneck in the enlarged `G13` neutral transition section.

## 11. Temporal-span consequence at the first wrap

At `h=3216`, every nonzero candidate lift has `|k|=1`, so

\[
p=v_2(k)=0.
\]

Thus any surviving pair would have to differ at the **first transition bit**.

For all bounded credits at this layer, the universal states have only small `v_3(x_{J-h})`; the maximum is five.  If `r=v_3(x_{J-h})`, the latest differing odd event has odd rank `2h-r`, so its time position is at least

\[
2h-r-1.
\]

Therefore a candidate repair would have to span at least

\[
2h-r-1-p
\]

transition positions.  In the worst bounded-credit case at `G13` neutral this is at least

\[
\boxed{6426}
\]

positions inside a block of length `9648`.

Thus the first wrapped candidate, even before its exact elimination in Section 9, is forced to be a genuinely global reorganization of the transition block rather than a local boundary repair.

## 12. Strategic consequence

The transition-section hierarchy is now:

\[
\boxed{
\begin{array}{c|c}
\text{regime}&\text{status}\\\hline
h<h_*\approx0.369F&\text{insufficient ordinary magnitude}\\
h_*\le h<h_{CRT}\approx0.613F&\text{magnitude sufficient but exact 2-adic valuation impossible}\\
h=h_{CRT}&\text{finite small CRT-lift set with exact two-ended coordinates}\\
h>h_{CRT}&\text{growing but structured CRT-lift cone}
\end{array}}
\]

For `G13` neutral the first wrapped layer is fully removed and the next layer has already been reduced to `|k|<=4`.

The remaining task is no longer an unconstrained search over thousands of transition bits.  It is a finite-lift mixed-place problem:

> for each small lift index `k`, determine whether the exact dyadic displacement `-k3^(F-h)` and the fixed Hensel quotient interval can be realized by two same-state weight-`2h` boundary words.

This is much closer to the fixed-Hensel dyadic-kernel object identified by the earlier `H_19` prototype.

## Reproducibility

Exact certificate:

`collatz/src/transition_crt_two_ended_certificate.py`
