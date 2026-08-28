# A0 s=1: exposure versus pruning and the exact correction-language gate

Date: 2026-08-28

Status: **SAFE local exposure / SAFE algebraic reduction / OPEN middle-language membership.**  This note does not prove the Collatz conjecture.

## 1. Scope

Work only inside the already isolated `C6A` local `s=1` formation sector.  No `C4R` near-root budget is used as an input to a Hensel lower bound, and no result here is promoted to `C6B` all-surplus coverage.

At the ten-`J0` renewal point write

\[
t_0=10J_0,
\qquad
j_0=10R_0+1,
\]

and

\[
X\xrightarrow{(t_0,j_0)}Z.
\]

On the current reset corridor the companion certificates give

\[
2^{71}<X<2^{72},
\qquad
2^{72}<Z<2^{73},
\]

and, with `G=2^33`,

\[
\boxed{
{7581\over100}G<L_-=3X-Z<{2721\over25}G<2^{40}.
}
\]

The purpose of this note is to separate three logically different notions:

1. **address exposure** — a short local descriptor determines a bounded ordinary integer;
2. **local corridor compatibility** — two exposed addresses satisfy a necessary short congruence/carry relation;
3. **full extension** — one and the same `t0`-step parity word actually connects `X` to `Z`.

Only the third item is the long middle problem.

## 2. Dyadic parity-address bijection

For the accelerated Collatz map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

let a length-`h` parity word be

\[
w=(\epsilon_0,\ldots,\epsilon_{h-1}),
\qquad
\epsilon_i\in\{0,1\},
\]

with

\[
q_h=\sum_{i=0}^{h-1}\epsilon_i,
\qquad
q_{i+1}=\sum_{r=0}^{i}\epsilon_r.
\]

Define its affine correction

\[
\boxed{
C_h(w)=
\sum_{i=0}^{h-1}
\epsilon_i2^i3^{q_h-q_{i+1}}.
}
\]

Then

\[
\boxed{
2^hT^h(x)=3^{q_h}x+C_h(w).
}
\]

Hence the parity word requires

\[
\boxed{
x\equiv-3^{-q_h}C_h(w)\pmod{2^h}.}
\]

Conversely this residue realizes the prescribed word: reduction modulo every `2^k` gives the corresponding prefix residue, so the required parity at each step is forced.  Thus

\[
\boxed{
\{0,1\}^h\longleftrightarrow\mathbb Z/2^h\mathbb Z
}
\]

is a bijection.

Consequently the first 72 parity bits expose the ordinary `X`, and the first 73 parity bits beginning at `Z` expose the ordinary `Z`.

## 3. Exact marginal ballot counts

Directed rational logarithm bounds and exact integer dynamic programming give the necessary local ballot-language counts

\[
\boxed{
|\mathcal X_{72}^{\rm ballot}|
=4\,650\,657\,914\,809\,371\,340,
}
\]

\[
\boxed{
|\mathcal Z_{73}^{\rm tail}|
=42\,553\,228\,731\,364\,551\,533.
}
\]

with sharp integer reciprocal brackets

\[
507|\mathcal X_{72}^{\rm ballot}|<2^{71}
<508|\mathcal X_{72}^{\rm ballot}|,
\]

\[
110|\mathcal Z_{73}^{\rm tail}|<2^{72}
<111|\mathcal Z_{73}^{\rm tail}|.
\]

At depth 40,

\[
\boxed{|\mathcal X_{40}^{\rm ballot}|=6\,402\,835\,000,}
\]

\[
\boxed{|\mathcal Z_{40}^{\rm tail}|=31\,654\,570\,714,}
\]

with

\[
171|\mathcal X_{40}^{\rm ballot}|<2^{40}
<172|\mathcal X_{40}^{\rm ballot}|,
\]

and

\[
34|\mathcal Z_{40}^{\rm tail}|<2^{40}
<35|\mathcal Z_{40}^{\rm tail}|.
\]

These are **marginal** counts only.  Their densities must not be multiplied as though the two address languages were independent.

## 4. Forty-bit dyadic--dyadic corridor meet

Because

\[
0<L_-=3X-Z<2^{40},
\]

reduction modulo `2^40` already exposes the complete ordinary debit:

\[
\boxed{
L_-=
\bigl(3(X\bmod2^{40})-(Z\bmod2^{40})\bigr)
\bmod2^{40},
}
\]

where the right side is the least nonnegative residue.

The strict rational corridor is the exact integer interval

\[
\boxed{
651\,202\,941\,420
\le L_-
\le
934\,928\,480\,993.
}
\]

Writing

\[
3X=H_X2^{40}+r_X,
\qquad
0\le r_X<2^{40},
\]

gives the exact one-borrow law

\[
\boxed{
\left\lfloor{Z\over2^{40}}\right\rfloor
\in\{H_X,H_X-1\}.
}
\]

Thus the first 40 pre bits and first 40 tail bits already form a finite **local** carry meet.

This is not a full `t0`-step extension theorem.

## 5. Why the terminal ternary window cannot be counted as another pruning factor

The companion saturation theorem proves, for `m=26,28,47`,

\[
\boxed{
\mathcal Z_{\rm pre,term}^{(m)}
=(\mathbb Z/3^m\mathbb Z)^\times.
}
\]

Since

\[
3^{47}>2^{73},
\]

the terminal `0->0` ballot projection itself permits every ordinary checkpoint `Z` in the physical shell with `3\nmid Z`.

Therefore the ternary terminal window is an **exposure coordinate**, not an independent sparse filter.

In particular the following promotion is rejected:

\[
\text{40-bit dyadic sparsity}
\times
\text{terminal ternary sparsity}
\Longrightarrow
\text{joint scarcity}.
\]

The second alleged sparsity is absent, and even two genuinely sparse marginals would still require a correlation theorem.

## 6. Two-sided modular locality barrier

For the full pre block write

\[
\boxed{
2^{t_0}Z=3^{j_0}X+C_{t_0}(w).
}
\]

### Start-side reduction

For any `h<=t0`, reduce modulo `2^h`.  The left side vanishes, and correction atoms whose odd positions are at least `h` vanish.  Because the total odd count `j0` is fixed in the `s=1` sector, the resulting congruence depends only on the first `h` parity bits and `X mod 2^h`.

Thus a bounded dyadic window sees the **start address**, not the ordinary distant endpoint.

### Endpoint-side reduction

For any `k<=j0`, reduce modulo `3^k`.  The term `3^j0 X` vanishes, while only the final `k` odd correction atoms survive.  Since `2` is a unit modulo `3^k`, this determines an endpoint residue from the terminal odd positions.

Thus a bounded ternary window sees the **endpoint address**, not the ordinary distant start.

Therefore separate fixed-depth windows can expose both ends without certifying that the same billion-step interior joins them.

This is the exact structural reason the earlier four-window singleton/exposure theorem was not yet a same-orbit theorem.

## 7. Exact correction-language formulation of the middle gate

For a candidate ordinary pair `(X,Z)` define

\[
\boxed{
C_{\rm req}(X,Z)
:=2^{t_0}Z-3^{j_0}X.
}
\]

Let `W_pre` be the full admissible `s=1` pre language: length `t0`, exactly `j0` odd events, the `0->0` ballot bridge, and every other currently SAFE local `C4F` formation requirement.

Define the correction language

\[
\boxed{
\mathcal C_{\rm pre}
:=\{C_{t_0}(w):w\in W_{\rm pre}\}.
}
\]

Then the full same-address problem is exactly

\[
\boxed{
C_{\rm req}(X,Z)\in\mathcal C_{\rm pre}.
}
\]

Necessity is the affine Collatz identity.

For sufficiency, if a word `w` has

\[
C_{t_0}(w)=C_{\rm req}(X,Z),
\]

then reduction modulo `2^t0` gives the unique parity address of `w`.  Hence `X` realizes `w`, and the full affine identity gives endpoint `Z`.

So no extra hidden extension assumption is present in this formulation.

## 8. The correction language is injective at fixed `(t0,j0)`

Write the odd positions of a word as

\[
0\le a_1<\cdots<a_{j_0}<t_0.
\]

Then

\[
C=\sum_{r=1}^{j_0}3^{j_0-r}2^{a_r}.
\]

Because the coefficient of the first atom is odd and every later atom has strictly larger `2`-adic valuation,

\[
\boxed{a_1=v_2(C).}
\]

Subtract that atom:

\[
C_1=C-3^{j_0-1}2^{a_1}.
\]

If another odd event remains, then

\[
\boxed{a_2=v_2(C_1).}
\]

Continuing,

\[
\boxed{
\begin{aligned}
C_0&=C,\\
a_r&=v_2(C_{r-1}),\\
C_r&=C_{r-1}-3^{j_0-r}2^{a_r}.
\end{aligned}}
\]

A genuine correction terminates at `C_j0=0` and reconstructs the complete strictly increasing odd-position sequence.

Hence at fixed length and odd count the correction map is injective.  In fact `C mod 2^t0` is already injective, because it is equivalent to the unique dyadic parity address.

This removes one possible source of combinatorial ambiguity: the OPEN problem is not collision between many words with the same correction.  It is membership of one required correction in a huge injective language.

## 9. Exact block composition

For concatenated parity blocks `w=uv`, with lengths `|u|,|v|` and odd counts `q(u),q(v)`, the corrections satisfy

\[
\boxed{
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
}
\]

This is the affine counterpart of the weighted min-plus block composition already used in the Hensel operator.

It supplies the correct algebraic object for a Christoffel/Euclidean middle DAG: a node must preserve enough boundary ballot data and enough correction information that this exact affine composition remains valid.

A fixed small modulus alone cannot close the gate, because it falls back into the two-sided locality barrier.

## 10. DSD audit

### SAFE

- dyadic parity-word/address bijection;
- ordinary `X` exposure from 72 pre bits;
- ordinary `Z` exposure from 73 checkpoint/tail bits;
- exact 40-bit debit corridor meet;
- pre terminal ternary unit saturation;
- two-sided modular locality barrier;
- fixed-`(h,q)` correction injectivity and valuation decoder;
- exact correction concatenation law;
- equivalence between full same-address extension and correction-language membership.

### REJECTED

- multiplying marginal address densities as independent probabilities;
- treating terminal `3`-adic depth as a new sparse pruning factor;
- treating the 40-bit local carry meet as a full `t0`-step extension theorem;
- treating four-window singleton exposure as same-orbit closure;
- deepening the terminal ternary trie in expectation of sparsity.

### OPEN

Construct a boundary-preserving compressed representation of

\[
\mathcal C_{\rm pre}
\]

that can decide or bound membership of `C_req(X,Z)` without enumerating `t0` individual steps or projecting away the start/end correlation.

`C6A` therefore remains **OPEN**.

## 11. Next gate

The next object should be a **correction-language block transfer** rather than another marginal residue scan.

For each block retain at least:

\[
(\text{length},\text{odd count},\text{ballot interface state},\text{correction transfer data}),
\]

and compose with

\[
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
\]

The mechanical/Christoffel continued-fraction hierarchy can compress the boundary geometry, but a proposed state quotient is admissible only if it survives the DSD state-loss and reverse-dependency attacks.

Companion certificates:

- `collatz/src/A0_s1_72_73bit_ballot_address_cardinality_certificate.py`;
- `collatz/src/A0_s1_dyadic_bi_address_corridor_certificate.py`;
- `collatz/src/A0_s1_pre_terminal_unit_saturation_certificate.py`;
- `collatz/src/A0_s1_pre_terminal_47trit_saturation_certificate.py`;
- `collatz/src/A0_s1_correction_language_injective_decoder_certificate.py`.
