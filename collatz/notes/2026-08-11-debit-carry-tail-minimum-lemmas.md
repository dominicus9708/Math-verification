# Debit carry and tail-minimum lemmas

Date: 2026-08-11

Status: **exact structural reductions for the nonperiodic first-descent hard core**. These lemmas do not prove the Collatz conjecture.

## 1. Odd-event and debit notation

Let

\[
x_{j+1}=\frac{3x_j+1}{2^{v_j}},\qquad v_j:=v_2(3x_j+1)\ge1,
\]

and

\[
A_j:=\sum_{i=0}^{j-1}v_i,
\qquad
E_j:=A_j-j.
\]

A **debit event** is an index `j` with `v_j>=2`. Write

\[
d_j:=v_j-1\ge1.
\]

The debit-only summation-by-parts term attached to this event is

\[
\boxed{
D_j
=
2^{E_j}(2^{d_j}-1)\left(\frac23\right)^{j+1}
=
\frac{2^{A_j+1}(2^{d_j}-1)}{3^{j+1}}.
}
\]

For a fixed positive starting integer `n`, the infinite debit series satisfies

\[
\boxed{
-(n+1)=\sum_{j:\,v_j\ge2}D_j
\quad\text{in }\mathbb Z_2.
}
\]

The nonzero debit terms have strictly increasing 2-adic valuations `A_j+1`.

---

## 2. Debit carry equals the next macroblock odd core

Let

\[
t_1<t_2<\cdots
\]

be the debit-event indices. Let

\[
P_r:=\sum_{s=1}^{r}D_{t_s}
\]

be the real partial debit sum through the `r`th debit.

Let the next debit occur at `t_{r+1}` and set

\[
g_r:=t_{r+1}-t_r-1,
\]

so exactly `g_r` credit events `v=1` occur between the two debits.

Because the next nonzero debit term has 2-adic valuation

\[
A_{t_{r+1}}+1,
\]

the residual identity implies

\[
\boxed{
v_2(n+1+P_r)=A_{t_{r+1}}+1.}
\]

Using the finite summation-by-parts identity just before the next debit gives the stronger exact equality

\[
\boxed{
n+1+P_r
=
\frac{2^{A_{t_{r+1}}}}{3^{t_{r+1}}}
\bigl(x_{t_{r+1}}+1\bigr).
}
\]

At a debit state `x`, one has `x\equiv1 (mod 4)`, hence

\[
v_2(x+1)=1.
\]

The intervening `g_r` credit events satisfy

\[
x_{j+1}+1=\frac32(x_j+1),
\]

so there is a unique odd integer `K_r>=1` such that

\[
\boxed{
x_{t_{r+1}}+1=2\cdot3^{g_r}K_r.}
\]

Consequently

\[
\boxed{
K_r
=
\frac{3^{t_r+1}(n+1+P_r)}{2^{A_{t_{r+1}}+1}}
\in2\mathbb Z+1.
}
\]

Thus the 2-adic carry obtained from the debit partial sum is exactly the odd core of the next macroblock.

---

## 3. Closed block-to-block recurrence

Write a maximal macroblock start as

\[
\boxed{x=2^hK-1,}
\]

where `h=v_2(x+1)>=1` and `K` is odd. The block consists of `h-1` credit events followed by one debit event. Let

\[
d:=v_{\rm debit}-1\ge1.
\]

After the block,

\[
\boxed{x'=\frac{3^hK-1}{2^d}.}
\]

Write the next block start in the same form,

\[
\boxed{x'=2^{h'}K'-1,}
\]

with `h'>=1` and `K'` odd. Then

\[
\boxed{
3^hK+2^d-1
=
2^{d+h'}K'.
}
\]

This is an exact integer recurrence on the debit/macroblock state `(h,d,K)`.

It shows that the following descriptions are not independent filters but equivalent encodings of the same transition:

1. the debit-only 2-adic carry;
2. the `v=1` credit-run alignment;
3. the macroblock CRT/residue bridge.

---

## 4. Cross-debit size inequality

Because `P_r` has denominator dividing `3^{t_r+1}` and `n+1+P_r>0`, the integer `K_r>=1` gives

\[
\boxed{
2^{A_{t_{r+1}}+1}
\le
3^{t_r+1}(n+1+P_r).
}
\]

For a hypothetical nonperiodic no-first-descent survivor, the harmonic debit bound gives

\[
P_r=O_n(t_r^{1/9}).
\]

Hence

\[
\boxed{
A_{t_{r+1}}+1
\le
(t_r+1)\log_2 3
+\frac19\log_2 t_r
+O_n(1).
}
\]

Since `A_j>=j`, this implies

\[
\boxed{
t_{r+1}
\le
(\log_2 3)t_r+O_n(\log t_r).}
\]

Therefore debit events cannot become supermultiplicatively sparse. In particular, their counting function is bounded below on a logarithmic scale.

This is distinct from the much sparser set of **contracting checkpoints** `lambda_j>1`, whose count is `O_n(q^{1/9})` under the harmonic corridor.

---

## 5. Tail-minimum strict-expansion lemma

Assume the odd-event orbit is nonperiodic and divergent. Then it tends to infinity and has infinitely many **tail minima**: odd states `N` such that every later odd-event state is at least `N`.

Let such a tail minimum be the start of one maximal macroblock:

\[
N=2^hK-1,
\qquad
N'=\frac{3^hK-1}{2^d}.
\]

Define the block multiplier of the odd-event `lambda` coordinate by

\[
\boxed{M:=\frac{2^{h+d}}{3^h}.}
\]

Because `N` is a tail minimum,

\[
N'\ge N.
\]

Suppose `M>1`. Put

\[
\Delta:=2^{h+d}-3^h>0.
\]

Then

\[
N'-N
=
\frac{2^d-1-\Delta K}{2^d}.
\]

Since `N' >= N`, the numerator is nonnegative. Since `\Delta K>=1`, it is at most `2^d-2`, hence strictly smaller than `2^d`. But `N'-N` is an integer, so the numerator must be divisible by `2^d`. The only possibility is

\[
\boxed{N'-N=0.}
\]

Thus

\[
\boxed{
M>1\text{ and }N'\ge N
\Longrightarrow
N'=N.
}
\]

Returning to the same odd state makes the deterministic orbit periodic. Therefore a **nonperiodic** divergent orbit cannot satisfy `M>1` at a tail minimum.

Equality `M=1` is impossible because no positive powers of 2 and 3 are equal. Consequently every tail-minimum first block satisfies

\[
\boxed{M<1.}
\]

Equivalently,

\[
\boxed{
d<h\log_2\frac32,}
\]

so, since `d` is an integer,

\[
\boxed{
d\le\left\lfloor h\log_2\frac32\right\rfloor.}
\]

In particular `h=1` is impossible, because then the right-hand side is zero while every debit has `d>=1`. Hence every tail minimum of a hypothetical nonperiodic divergent odd orbit satisfies

\[
\boxed{v_2(N+1)=h\ge2,}
\]

or equivalently

\[
\boxed{N\equiv3\pmod4.}
\]

---

## 6. Tail-minimum expansion factor

Let

\[
\alpha:=\log_2\frac32.
\]

At a tail minimum, `d<=floor(alpha h)`, hence

\[
M
\le
2^{-\{\alpha h\}},
\]

where `{.}` denotes fractional part. From the exact block map,

\[
\frac{N'+1}{N+1}
=
\frac{3^hK+2^d-1}{2^{h+d}K}
>
\frac{3^h}{2^{h+d}}
=
\frac1M.
\]

Therefore

\[
\boxed{
\frac{N'+1}{N+1}
>
2^{\{\alpha h\}}.
}
\]

Thus a tail-minimum first block can have only very small relative growth when `alpha h` lies very close to an integer from above. This isolates a lower-side Diophantine near-resonance condition, distinct from the contracting critical resonance studied earlier.

---

## 7. Current role

The new hard-core structure is now:

- debit events are encoded by the closed integer recurrence `(h,d,K)->(h',d',K')`;
- debit events cannot become too sparse multiplicatively;
- contracting checkpoints are nevertheless density-zero under the harmonic corridor;
- every tail minimum begins with a strictly expanding (`M<1`) macroblock;
- slowly expanding tail minima require lower-side Diophantine resonance in `h log_2(3/2)`.

The remaining task is to couple these tail-minimum constraints to the harmonic/mixed-place conditions strongly enough to rule out an infinite sequence of rising tail minima.