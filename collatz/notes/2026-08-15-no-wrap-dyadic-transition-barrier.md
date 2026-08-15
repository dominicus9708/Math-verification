# No-wrap dyadic barrier for bounded-credit gate transition repair

Date: 2026-08-15

Status: **exact mixed 3-adic/2-adic nonrepair theorem for the enlarged first- and second-return gate transition sections**.  It combines a universal Sturmian prefix bound, the balanced-Hensel residual envelope, and an exact 2-adic valuation mismatch.  For every incoming integer credit `1<=delta<=397`, repair is impossible until the transition block absorbs all but `O(log F)` of the syndrome front.  The theorem applies to enlarged transition sections containing the explicit neutral/one-slack cubes; it is not a full-gate-fibre theorem and does not prove Collatz.

## 1. Enlarged transition section

Use a gate cube

\[
1^F(01/10)^J0,
\qquad q=F+J,
\qquad L=F+2J+1.
\]

For transition width `h`, put

\[
f:=F-h,
\qquad n:=J-h,
\]

and enlarge the section to

\[
\boxed{
1^f B(01/10)^n0,
\qquad |B|=3h,\quad |B|_1=2h.
}
\]

The boundary word `B` is allowed to vary far beyond the original pair cube.  We impose only a necessary coefficient-survival prefix bound, so the family remains an over-family of the corresponding neutral or one-slack gate section.

Let `s=0` for the neutral floor and `s=1` for the one-slack floor.

## 2. Universal prefix bound for the boundary correction

For every mechanical/Sturmian factor of slope

\[
\alpha=\log_3 2,
\]

the number of odd symbols in a prefix of length `t` is at least

\[
\lfloor t\alpha\rfloor.
\]

Hence an actual orientation with relative floor `-s` must satisfy

\[
q_{\rm act}(t)
\ge
\lfloor t\alpha\rfloor-s.
\]

Number the odd symbols of `B` by `j=1,...,2h`, and let the `j`-th odd occur at local zero-based position `p_j`.  At global prefix length

\[
t=f+p_j+1
\]

the actual odd count is `f+j`, so

\[
f+j
\ge
\lfloor t\alpha\rfloor-s.
\]

Since `t alpha` is irrational for `t>0`,

\[
t\alpha<f+j+s+1.
\]

Exponentiating in base three gives

\[
2^{f+p_j+1}<3^{f+j+s+1},
\]

and therefore

\[
\boxed{
2^{p_j}
<
\frac{3^{f+j+s+1}}{2^{f+1}}.
}
\]

The standalone boundary correction is

\[
R_B
=
\sum_{j=1}^{2h}3^{2h-j}2^{p_j}.
\]

Thus

\[
R_B
<
2h\frac{3^{f+2h+s+1}}{2^{f+1}}
=
\boxed{
\frac{h\,3^{F+h+s+1}}{2^f}.
}
\]

Consequently any difference of two allowed boundary corrections satisfies

\[
\boxed{
|D_B|
<
\frac{h\,3^{F+h+s+1}}{2^f}.
}
\]

A sufficient condition for the whole boundary-difference range to lie in the least signed interval modulo `3^(F+h)` is therefore

\[
\boxed{
2^f>2h\,3^{s+1}.
}
\]

## 3. Raw Hensel target remains unwrapped

Let an incoming integer predecessor credit be

\[
1\le\delta\le397.
\]

After the remaining `n=J-h` pair coordinates are balanced-Hensel lifted, write the signed residual as `U_n=-a_n`.  The exact recurrence gives

\[
a_0=8\delta,
\]

and

\[
a_n
<
(8\delta+4)\left(\frac43\right)^n.
\]

The required boundary target is

\[
\boxed{
T_h=2^{3h-2}U_n.
}
\]

Put

\[
\lambda:=\frac{3^q}{2^L}.
\]

Using

\[
\frac{3^F}{(4/3)^J}
=
2^{F+1}\lambda,
\]

a sufficient condition for

\[
2|T_h|<3^{F+h}
\]

is exactly

\[
\boxed{
2^f\lambda>2\delta+1.
}
\]

For the whole bounded range it is enough to check

\[
\boxed{
2^f3^q>795\,2^L.
}
\]

No floating-point approximation is needed.

## 4. Dyadic valuation mismatch

Assume `n>=1`.  One balanced-Hensel update has the form

\[
U_{k+1}=\frac{4(U_k-e_k)}3,
\qquad e_k\in\{-1,0,1\},
\]

so

\[
\boxed{4\mid U_n.}
\]

Therefore

\[
\boxed{2^{3h}\mid T_h.}
\]

Now take two distinct length-`3h`, weight-`2h` boundary words and let `p` be their earliest differing time position.  Their affine-correction terms before `p` agree.  At `p`, exactly one word contributes an odd coefficient times `2^p`, while every later term is divisible by `2^(p+1)`.  Hence

\[
\boxed{v_2(D_B)=p\le3h-1.}
\]

Suppose both no-wrap conditions from Sections 2 and 3 hold.  Then a congruence

\[
D_B\equiv T_h\pmod{3^{F+h}}
\]

between their least signed representatives is an ordinary integer equality

\[
D_B=T_h.
\]

But a nonzero equality is impossible because

\[
v_2(D_B)\le3h-1
<3h\le v_2(T_h).
\]

Thus:

\[
\boxed{
\begin{aligned}
&2^f>2h3^{s+1},\\
&2^f3^q>(2\delta+1)2^L,\\
&h<J
\end{aligned}
\quad\Longrightarrow\quad
\text{no bounded-credit transition repair}.}
\]

## 5. Exact current gate bounds

Apply the worst case `delta=397`, so `2 delta+1=795`.  Exact integer arithmetic gives

\[
\boxed{\begin{array}{c|r|r|r}
\text{gate/fibre}&F&\text{repair impossible for every }h\le&F-h_{\max}\\\hline
G_{81}\text{ neutral}&404&392&12\\
G_{81}\text{ one-slack}&402&389&13\\
G_{82}\text{ neutral}&409&397&12\\
G_{82}\text{ one-slack}&407&394&13\\
G_{13}\text{ neutral}&5245&5230&15\\
G_{13}\text{ one-slack}&5243&5226&17\\
G_{14}\text{ neutral}&5648&5632&16\\
G_{14}\text{ one-slack}&5646&5629&17
\end{array}}
\]

These are phase-uniform bounds: only the universal Sturmian prefix floor was used.

For example, in the `G_13` neutral enlarged section, every credit in `1..397` remains impossible even after the transition block is allowed to absorb

\[
\boxed{5230/5245>99.71\%}
\]

of the syndrome front.

## 6. Asymptotic interpretation

For a fixed bounded credit range, the target no-wrap inequality requires only

\[
f
>
\log_2\frac{2\delta+1}{\lambda},
\]

which is `O(1)` along critical Euclidean gates because `lambda` remains near one.

The boundary no-wrap condition requires

\[
2^f>2h3^{s+1},
\]

so

\[
f>\log_2 h+O(1).
\]

Since `h` is of order `F`, both are satisfied whenever

\[
\boxed{f\ge(1+o(1))\log_2 F.}
\]

Therefore in these enlarged transition sections a bounded-credit repair can occur only after

\[
\boxed{
h=F-O(\log F).}
\]

Equivalently,

\[
\boxed{
\frac{h_{\min}}F\longrightarrow1
}
\]

as the critical gate scale grows.

This is much stronger than the earlier magnitude-only lower bound `h/F >= log_3(3/2)-o(1) approximately 0.369`.

## 7. Meaning for the R1 program

The systematic low-Hensel cube is not separated from the full-fibre problem by a narrow transition layer.  For bounded predecessor credits, any repair inside the present enlarged sections must reorganize essentially the entire complementary syndrome front, leaving only logarithmically many forced-front coordinates untouched.

This strengthens the late-repair picture:

\[
\boxed{
\text{bounded credit}
+\text{same-state survival}
\Longrightarrow
\text{macroscopic, asymptotically full-front reorganization}.}
\]

The remaining limitation is important: the full same-state gate fibre need not admit a representation by one such front--boundary--pair decomposition.  The next theorem must show that every full-fibre repair can be normalized into an enlarged transition section of this kind, or otherwise derive an equivalent no-wrap dyadic mismatch directly from the full Euclidean state.

## Reproducibility

Exact inequality certificate:

`collatz/src/gate_transition_no_wrap_v2_barrier_certificate.py`
