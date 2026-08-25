# First global resonance: terminal-46 triangular 3-adic defect theorem

Date: 2026-08-26

Status: **exact finite theorem** in the repaired first-global-resonance binary branch. It uses the already-certified two-ended endpoint exposure and near-return congruence. It does not use the disputed ternary recursively-sufficient selector, repeated L7/L14 pullback, or an independence assumption. It does not prove the Collatz conjecture.

## 1. Fixed first-resonance endpoint address

At

\[
(A_0,Q_0)=(114208327604,72057431991),
\]

the last 46 odd ordinals determine the complete ordinary endpoint because

\[
y\equiv 2^{-A_0}\sum_{\ell=0}^{45}3^\ell 2^{a_{Q_0-\ell}}\pmod{3^{46}},
\qquad y<2^{72}<3^{46}.
\]

Let the exact mechanical tail, in increasing ordinal order, be

\[
B_t=b_{Q_0-45+t},\qquad 0\le t\le45,
\]

and define the terminal displacement

\[
\delta_t:=B_t-a_{Q_0-45+t}\ge0.
\]

Then the endpoint is

\[
\boxed{
y(\delta)=
2^{-A_0}\sum_{t=0}^{45}
3^{45-t}2^{B_t-\delta_t}\pmod{3^{46}}.}
\]

The least nonnegative residue is the ordinary endpoint itself.

## 2. Triangular 3-adic periodicity

The term with index \(t\) carries the factor \(3^{45-t}\). Hence modulo \(3^{46}\) it only needs

\[
2^{-\delta_t}\pmod{3^{t+1}}.
\]

Since

\[
\operatorname{ord}_{3^{t+1}}(2)=2\cdot3^t,
\]

the endpoint sees the \(t\)-th displacement only through

\[
\boxed{\delta_t\pmod{2\cdot3^t}.}
\]

This is the exact triangular terminal-address recursion: the earliest terminal ordinal contributes one ternary digit and only needs displacement parity; each later ordinal exposes one additional ternary digit.

## 3. Ordering recurrence

The actual odd positions are strictly increasing. If

\[
g_t:=B_t-B_{t-1}\in\{1,2\},
\]

then

\[
B_t-\delta_t>B_{t-1}-\delta_{t-1}
\]

is equivalent to

\[
\boxed{\delta_t\le\delta_{t-1}+g_t-1.}
\]

Consequently, whenever \(\delta_{t-1}=0\) and \(\delta_t>0\), one must have

\[
g_t=2,\qquad\delta_t=1.
\]

This makes small terminal-support classes finite even though \(\delta_0\) itself may be large.

## 4. Mechanical endpoint and the admissible endpoint channel

The exact mechanical endpoint is

\[
\boxed{y_{\rm mech}=4699104266570964686821,}
\]

which lies above the allowed near-return endpoint band.

For every hypothetical minimal counterexample in this cell,

\[
2^{71}<y,
\qquad
3y<4\cdot2^{71}+3\cdot2^{33},
\qquad
y\equiv3\pmod4.
\]

The last congruence follows from

\[
N\equiv3\pmod4,
\qquad y=N+g,
\qquad4\mid g.
\]

## 5. Exact exclusion of terminal support 0 and 1

Define

\[
D_{\rm tail}:=\#\{t:0\le t\le45,\ \delta_t>0\}.
\]

The case \(D_{\rm tail}=0\) is the already-excluded mechanical endpoint.

For \(D_{\rm tail}=1\):

- if the unique defect is at \(t=0\), only the two parity classes \(\delta_0\bmod2\) matter;
- if it is at \(t>0\), the preceding displacement is zero, so the ordering recurrence forces a mechanical gap 2 and \(\delta_t=1\).

There are therefore exactly

\[
\boxed{28}
\]

finite singleton endpoint classes.

Exact enumeration shows that only one singleton class even enters the broad numerical endpoint interval:

\[
t=9,\qquad\delta_9=1,
\]

with

\[
\boxed{y=2994179304232351671382.}
\]

But this value satisfies

\[
y\equiv2\pmod4,
\]

so it cannot be a near-return endpoint.

Hence

\[
\boxed{D_{\rm tail}\ge2.}
\]

This is a proof-level finite consequence of the terminal 3-adic address and the near-return channel.

## 6. Exact two-defect reduction

If \(D_{\rm tail}=2\), the triangular periods and the ordering recurrence reduce all possible displacement values to exactly

\[
\boxed{414}
\]

finite residue classes.

Of these, only

\[
\boxed{9}
\]

classes satisfy both the endpoint interval and \(y\equiv3\pmod4\), producing only

\[
\boxed{8}
\]

distinct ordinary endpoints.

Using the certificate's class notation, the surviving classes and endpoints are

\[
\begin{array}{c|r}
\text{terminal class}&y\\\hline
(0,1,0,3)&2729562462203742221059\\
(0,1,1,5)&2729562462203742221059\\
(2,24,1,1)&3059622251880574799467\\
(5,26,1,1)&2390750338045521993103\\
(7,26,1,1)&2768988818993959778023\\
(9,11,1,1)&2463461351003862446095\\
(12,19,1,1)&3104589732879008787067\\
(14,41,1,1)&2697452540596458807755\\
(33,38,1,1)&2556248067081360242587
\end{array}
\]

For the \((0,1,\cdot,\cdot)\) classes the final two entries are the relevant residue classes

\[
\delta_0\bmod2,
\qquad
\delta_1\bmod6.
\]

For the remaining entries they record the two terminal support indices and their forced small displacements.

Thus the tail boundary has been reduced from an a priori unbounded displacement problem to:

\[
\boxed{
D_{\rm tail}\ge3
\quad\text{or}\quad
D_{\rm tail}=2\text{ in one of nine explicit classes}.}
\]

## 7. Combination with the 72-bit start boundary

The independently certified prefix theorem gives

\[
D_{72}\ge11.
\]

The terminal odd ordinals have indices at least \(Q_0-45\), so their actual positions satisfy

\[
a_{Q_0-45}\ge Q_0-46>72.
\]

Therefore the early \(D_{72}\) displacement channels and the terminal \(D_{\rm tail}\) channels are disjoint.

Hence every remaining first-resonance candidate satisfies the new two-ended lower bound

\[
\boxed{r_*\ge13.}
\]

Using the coarse correction charge of more than \(1/12\) per displaced ordinal also gives

\[
\boxed{E/3^{Q_0}>13/12.}
\]

The structural two-ended statement is more important than this small numerical correction improvement.

## 8. DSD audit interpretation

The first-resonance bridge now has forced nonmechanical formation at both ends:

\[
\boxed{
D_{72}\ge11
\;\big|\;
\text{long Beatty transport bridge}
\;\big|\;
D_{\rm tail}\ge2.
}
\]

The terminal displacement is not a new independent descriptor. It is the late projection of the same global ordinal-transport vector \(s_j\) whose real projection gives the correction defect and whose early dyadic projection fixes the start address.

This is exactly the DSD-style bookkeeping gain: the two boundary conditions now constrain disjoint coordinates of one common transport state.

## 9. Next target

The most economical next attack is the exceptional equality case

\[
D_{\rm tail}=2.
\]

It has only eight possible endpoint integers. For each such endpoint,

\[
N=y-g,
\qquad
0<g<2^{33},
\qquad4\mid g.
\]

After fixing \(y\), a 33-bit dyadic start prefix already fixes the entire gap \(g\): because \(N\bmod2^{33}\) is known and \(g\) is the unique positive multiple of four below \(2^{33}\) satisfying \(N=y-g\).

Thus the next finite reduction can enumerate coefficient-surviving 33-bit formation prefixes rather than the full \(2^{31}\) gap range, then test the resulting exact ordinary starts. If all eight endpoint values are excluded, the terminal theorem strengthens to

\[
D_{\rm tail}\ge3.
\]

Companion exact certificate:

`collatz/src/first_resonance_terminal46_triangular_defect_certificate.py`.
