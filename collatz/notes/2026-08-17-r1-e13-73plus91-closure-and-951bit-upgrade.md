# R1 E=13 closure by the 73+91 formation obstruction

Date: 2026-08-17

Status: **exact current-R1/current-core closure of the E=13 pre-G13 layer, using a finite set/composition obstruction modulo `3^21`**.  Combined with the previously certified first-73 `<=8` layer closure, this proves `e_1539>=14` for the current isolated R1 core and sharpens the natural G13 entrance bound to `x_1539<2^951`.  It does **not** prove the Collatz conjecture globally.

## 1. Prior E=13 first-73 reduction

The exact relaxed run-cover theorem already gives

\[
E=13\Longrightarrow e_{73}\le9.
\]

The first-73 layers containing at most eight even events were closed by the earlier exact sparse-even / Cantor certificates.  Therefore any still-unresolved current-core E=13 start would have to satisfy

\[
\boxed{e_{73}=9.}
\]

Write the nine even-event positions in the first 73 accelerated steps as

\[
0\le p_0<\cdots<p_8\le72.
\]

## 2. The tenth-even future-cover lower bound

Recompute the exact relaxed future-cover optimizer from the current numerical ceiling

\[
N\le N_{\max}=5,908,625,413,101,667,397,287.
\]

For total E=13 the necessary lower bounds on even-event positions are

\[
\boxed{
(0,1,2,3,4,5,6,7,66,164,317,558,938).
}
\]

In particular the tenth even event, zero-based rank 9, obeys

\[
\boxed{p_9\ge164.}
\]

Since the first 73 steps are positions `0,...,72`, steps `73,...,163` are therefore all odd.  There are exactly

\[
164-73=91
\]

such steps.

## 3. Natural formation consequence at depth 73

Put

\[
U=x+1.
\]

An odd accelerated step is exactly

\[
U\mapsto\frac{3U}{2}.
\]

A run of 91 consecutive odd steps from time 73 requires

\[
\boxed{2^{91}\mid U_{73}.}
\]

Hence write

\[
\boxed{U_{73}=2^{91}v,\qquad v\in\mathbb N_{>0}.}
\]

This is a finite-natural / zero-lift condition: the ordinary state at time 73 must already contain the 91 binary factors needed by the forced future odd run.

## 4. Exact first-73 formation equation

With nine evens and therefore 64 odd steps in the first 73 positions,

\[
\boxed{
2^{73}U_{73}
=
3^{64}U_0
+
\sum_{j=0}^{8}
2^{p_j}3^{64-p_j+j}.
}
\tag{1}
\]

Equivalently,

\[
\frac{2^{73}U_{73}}{3^{64}}
=
U_0+
\sum_{j=0}^{8}
3^j\left(\frac23\right)^{p_j}.
\]

Because `p_j>=j`,

\[
0<\epsilon_9
:=\sum_{j=0}^{8}3^j(2/3)^{p_j}
\le\sum_{j=0}^{8}2^j
=511.
\]

Substituting `U_73=2^91 v` into (1) gives

\[
2^{164}v=3^{64}(U_0+\epsilon_9).
\]

The current numerical interval

\[
N_0\le N\le N_{\max}
\]

therefore forces the finite exact window

\[
\boxed{579\le v\le867.}
\]

Only 289 integer values remain before any parity word is constructed.

## 5. Ternary formation coordinates

Define

\[
\boxed{e_j:=64-p_j+j.}
\]

Because the even positions are strictly increasing and all lie in the first 73 steps,

\[
\boxed{e_0\ge e_1\ge\cdots\ge e_8\ge0.}
\]

The correction term in (1) becomes

\[
2^{p_j}3^{64-p_j+j}
=2^{64}\,2^{j-e_j}3^{e_j}.
\]

Reducing (1) modulo `3^64` and dividing by the unit `2^64` gives the necessary formation congruence

\[
\boxed{
\sum_{j=0}^{8}2^{j-e_j}3^{e_j}
\equiv
2^{100}v
\pmod{3^{64}}.
}
\tag{2}
\]

This is the central set/composition representation.  The nine event positions are replaced by one ordered exponent-formation object.

## 6. Finite digit automaton

At ternary level `t`, let `a` be the number of event ranks not yet assigned an exponent below `t`, and let `c` be the scaled residual carry.

If the suffix ranks

\[
a',a'+1,\ldots,a-1
\]

are assigned exponent `t`, their coefficient contribution after normalization is

\[
\boxed{2^a-2^{a'}.}
\]

The next formation state exists exactly when

\[
\boxed{
c+2^a-2^{a'}\equiv0\pmod3,}
\]

with carry transition

\[
\boxed{
c'=rac23\left(c+2^a-2^{a'}\right).}
\]

Start from

\[
\boxed{(a,c)=(9,-2^{100}v).}
\]

If after `K` ternary levels some ranks remain unassigned, they are deliberately allowed to have `e_j>=K`.  Thus the finite automaton is an **over-family** of all physical first-73 event sets.  A rejection is therefore safe.

## 7. Exact `3^21` obstruction

Run the formation automaton only through `K=21`.

The exact surviving `v` sets are

\[
\boxed{
\begin{array}{c|c}
K&\text{surviving }v\\\hline
18&\{591\}\\
19&\{591\}\\
20&\{591\}\\
21&\varnothing
\end{array}}
\]

Hence none of the 289 numerically possible values can satisfy even the necessary congruence modulo `3^21`.

The complete death-depth histogram over `579<=v<=867` is

\[
\boxed{
\begin{array}{c|r}
K&\#\text{first deaths}\\\hline
1&96\\
6&1\\
7&9\\
8&16\\
9&20\\
10&33\\
11&33\\
12&20\\
13&20\\
14&12\\
15&15\\
16&5\\
17&4\\
18&4\\
21&1
\end{array}}
\]

The final survivor before closure is `v=591`.

A separate direct enumeration of the finite normalized exponent family at `K=6` reproduces the automaton residue set exactly, serving as an independent recurrence audit.

## 8. E=13 closure

Suppose an unresolved current R1 start had total pre-G13 even count `E=13`.

Then:

1. the run-cover theorem and the already-closed `e_73<=8` layers force `e_73=9`;
2. future-cover forces `p_9>=164`;
3. therefore `2^91|U_73`;
4. the numerical interval forces `579<=v<=867`;
5. but the required first-73 formation congruence has no solution even modulo `3^21`.

Contradiction.

Therefore

\[
\boxed{e_{1539}\ne13.}
\]

Together with the previous theorem `e_1539>=13`,

\[
\boxed{e_{1539}\ge14.}
\]

This is a current-core exact theorem/certificate, not a statistical or beam result.

## 9. G13 entrance upgrade

Now

\[
q_{1539}=1539-e_{1539}\le1525,
\]

so relative to the mechanical count `972`,

\[
\boxed{s_0\le553.}
\]

The exact relaxed endpoint optimizer gives

\[
\lfloor\log_2 U_{1539}^{\max}\rfloor=950
\]

at `E=14`, with smaller maxima for every larger even count.  Therefore

\[
\boxed{x_{1539}<2^{951}.}
\]

Since

\[
951=50\cdot19+1,
\]

the internal G13 natural lift chunks obey

\[
\boxed{t_{50}<2,}
\]

and

\[
\boxed{t_b=0\qquad(b\ge51).}
\]

The number of forced high zero G13 address bits increases to

\[
\boxed{20026-951=19075.}
\]

## 10. Structural significance

The E=13 layer was initially exposed as a potential `97,082,021,465`-word first-73 nine-zero enumeration problem.

The final closure does not enumerate that layer.  It uses the chain

\[
\boxed{
\text{E=13 set}
\to
\text{first-73 event count}=9
\to
\text{forced 91-odd future formation}
\to
v\in[579,867]
\to
\text{nine-event ternary formation automaton}
\to
\varnothing\pmod{3^{21}}.
}
\]

Thus the decisive proof object is a finite composition state, not a list of ordinary integers or parity words.  This is substantially closer to the intended Formation-Axiom-style set subtraction architecture.

## Reproducibility

Main exact obstruction:

`collatz/src/r1_e13_73plus91_formation_obstruction.py`

Entrance upgrade:

`collatz/src/r1_g13_entry_e14_951bit_upgrade_certificate.py`

Supporting first-73 / Hensel refinement work remains in:

`collatz/src/r1_e13_depth27_to73_formation_certificate.cpp`

The latter is now supplementary for E=13 closure, but its channel results remain exact and useful for later E>=14 layers.
