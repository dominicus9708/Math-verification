# First global resonance: terminal-46 triangular 3-adic defect theorem

Date: 2026-08-26

Status: **exact finite theorem** in the repaired first-global-resonance binary branch. It uses the already-certified two-ended endpoint exposure and near-return congruence. It does not use the disputed ternary recursively-sufficient selector, repeated L7/L14 pullback, or an independence assumption. It does not prove the Collatz conjecture.

> Audit correction, 2026-08-26: the endpoint printed for class `(14,41,1,1)` in the first draft had a transcription error. The correct value is `2697452540596458587755`. The class count, survivor count, and theorem were unchanged. The companion certificate was corrected in commit `00823665...`.

## 1. Terminal address

At

\[
(A_0,Q_0)=(114208327604,72057431991),
\]

the final 46 odd ordinals determine the ordinary endpoint because

\[
y\equiv2^{-A_0}\sum_{\ell=0}^{45}3^\ell2^{a_{Q_0-\ell}}
\pmod{3^{46}},
\qquad y<2^{72}<3^{46}.
\]

Let

\[
B_t=b_{Q_0-45+t},\qquad
\delta_t=B_t-a_{Q_0-45+t}\ge0,\qquad0\le t\le45.
\]

Then

\[
\boxed{
y(\delta)=2^{-A_0}\sum_{t=0}^{45}
3^{45-t}2^{B_t-\delta_t}\pmod{3^{46}}.}
\]

The t-th displacement is visible only modulo

\[
\boxed{2\cdot3^t}
\]

because

\[
\operatorname{ord}_{3^{t+1}}(2)=2\cdot3^t.
\]

This is the triangular 3-adic terminal address.

## 2. Ordering

For the mechanical gap

\[
g_t=B_t-B_{t-1}\in\{1,2\},
\]

strict ordering of actual odd positions gives

\[
\boxed{\delta_t\le\delta_{t-1}+g_t-1.}
\]

In particular, if \(\delta_{t-1}=0\) and \(\delta_t>0\), then

\[
g_t=2,\qquad\delta_t=1.
\]

## 3. Endpoint channel

Every hypothetical first-resonance minimal counterexample satisfies

\[
2^{71}<y,
\qquad
3y<4\cdot2^{71}+3\cdot2^{33},
\qquad
y\equiv3\pmod4.
\]

The exact mechanical endpoint is

\[
4699104266570964686821,
\]

which is outside this band.

Define

\[
D_{\rm tail,46}=\#\{t:0\le t\le45,\delta_t>0\}.
\]

Exact enumeration gives:

- support 0: impossible;
- support 1: 28 finite classes, none admissible;
- support 2: 414 finite classes, 9 admissible classes, 8 distinct endpoints.

Hence

\[
\boxed{D_{\rm tail,46}\ge2.}
\]

The nine equality classes are

\[
\begin{array}{c|r}
(0,1,0,3)&2729562462203742221059\\
(0,1,1,5)&2729562462203742221059\\
(2,24,1,1)&3059622251880574799467\\
(5,26,1,1)&2390750338045521993103\\
(7,26,1,1)&2768988818993959778023\\
(9,11,1,1)&2463461351003862446095\\
(12,19,1,1)&3104589732879008787067\\
(14,41,1,1)&2697452540596458587755\\
(33,38,1,1)&2556248067081360242587
\end{array}
\]

For `(0,1,*,*)`, the final entries are the residue classes of \(\delta_0\bmod2\) and \(\delta_1\bmod6\); the other rows have the two support indices and forced unit displacements.

## 4. Relation to the early boundary

The independently certified start-boundary theorem gives

\[
D_{72}\ge11.
\]

The terminal odd ordinals have enormous ordinal index, so their actual positions are far beyond the first 72 steps. The supports are disjoint. At the 46-ordinal stage this already gave

\[
r_*\ge13.
\]

A stronger terminal ladder has now superseded this numerical lower bound:

\[
D_{\rm tail,50}\ge3,
\quad
D_{\rm tail,52}\ge4,
\quad
D_{\rm tail,56}\ge5,
\quad
D_{\rm tail,58}\ge6,
\]

hence

\[
\boxed{r_*\ge17.}
\]

See:

- `collatz/src/first_resonance_terminal_low_support_ladder_certificate.py`
- `collatz/notes/2026-08-26-first-resonance-terminal-low-support-ladder.md`

Companion terminal-46 certificate:

- `collatz/src/first_resonance_terminal46_triangular_defect_certificate.py`
