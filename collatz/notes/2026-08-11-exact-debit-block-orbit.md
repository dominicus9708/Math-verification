# Exact debit-block orbit and block product

Date: 2026-08-11

Status: **exact coarse-graining of the odd-event first-descent problem**. Credit events are eliminated from the survival state without loss.

## 1. Maximal debit blocks

Let

\[
x_{j+1}=\frac{3x_j+1}{2^{v_j}},\qquad v_j=v_2(3x_j+1)\ge1.
\]

Partition the odd-event orbit into maximal blocks consisting of zero or more credit events `v=1` followed by one debit event `v>=2`.

Write the start of block `r` as

\[
\boxed{X_r=2^{h_r}K_r-1,}
\]

where

\[
h_r=v_2(X_r+1)\ge1,
\qquad K_r\text{ is odd}.
\]

Then the block contains `h_r-1` credit events and one debit event. Put

\[
\boxed{d_r:=v_{\rm debit}-1\ge1.}
\]

The next block start is

\[
\boxed{
X_{r+1}=\frac{3^{h_r}K_r-1}{2^{d_r}}.
}
\]

Writing

\[
X_{r+1}=2^{h_{r+1}}K_{r+1}-1
\]

gives the exact integer recurrence

\[
\boxed{
3^{h_r}K_r+2^{d_r}-1
=2^{d_r+h_{r+1}}K_{r+1}.
}
\]

---

## 2. Exact preservation of first-descent information

Inside one block, before the final debit, the credit states satisfy

\[
x_{t+1}+1=\frac32(x_t+1).
\]

Hence they are strictly increasing.

Therefore the minimum odd state attained during block `r` is one of its two endpoints:

\[
\min\{X_r,X_{r+1}\}.
\]

Consequently, for an odd initial integer `n`,

\[
\boxed{
\text{all odd-event states are }\ge n
\iff
X_r\ge n\text{ for every block start }r.
}
\]

Since every accelerated iterate between successive odd states is obtained by powers-of-two division and is at least the final odd endpoint, this is also equivalent to no first descent in the original accelerated map.

Thus the full nonperiodic first-descent hard core may be studied on the debit-block orbit `(X_r)` alone.

---

## 3. Block multiplier

Define

\[
\boxed{
M_r:=\frac{2^{h_r+d_r}}{3^{h_r}}.
}
\]

This is the exact multiplier of the odd-event `lambda` coordinate across block `r`.

From the block endpoint formula,

\[
\begin{aligned}
M_r\frac{X_{r+1}}{X_r}
&=\frac{2^{h_r+d_r}}{3^{h_r}}
\frac{3^{h_r}K_r-1}{2^{d_r}(2^{h_r}K_r-1)}\\
&=\frac{2^{h_r}K_r-(2/3)^{h_r}}{2^{h_r}K_r-1}.
\end{aligned}
\]

Hence

\[
\boxed{
M_r\frac{X_{r+1}}{X_r}
=
1+\frac{1-(2/3)^{h_r}}{X_r}.
}
\]

This is the exact block correction identity.

---

## 4. Product over blocks

Multiplying through `R` blocks gives

\[
\boxed{
\left(\prod_{r=0}^{R-1}M_r\right)
\frac{X_R}{X_0}
=
\prod_{r=0}^{R-1}
\left(
1+\frac{1-(2/3)^{h_r}}{X_r}
\right).
}
\]

The right-hand side is the full affine `+1` correction accumulated at block resolution.

Taking logarithms,

\[
\boxed{
\log\frac{X_{r+1}}{X_r}
=-\log M_r
+\log\left(1+\frac{1-(2/3)^{h_r}}{X_r}\right).
}
\]

Thus each block has:

- a multiplicative drift `-log M_r`;
- a positive correction credit depending only on its start `X_r` and credit depth `h_r`.

---

## 5. Critical block slope

Let

\[
\alpha:=\log_2\frac32.
\]

Then

\[
\boxed{
\log_2 M_r=d_r-\alpha h_r.
}
\]

Hence blocks split exactly into

\[
\boxed{
\begin{array}{ll}
d_r<\alpha h_r:&M_r<1\quad\text{(strict coefficient expansion)},\\
d_r>\alpha h_r:&M_r>1\quad\text{(coefficient contraction)}.
\end{array}
}
\]

Equality is impossible because powers of 2 and 3 do not coincide.

The tail-minimum lemma shows that every block leaving a tail minimum in a hypothetical nonperiodic divergent orbit lies strictly in the first class.

---

## 6. Relation to the event-level harmonic state

If block `r` contains `h_r` odd events and contributes `h_r+d_r` total accelerated steps, then after `R` blocks

\[
q_R=\sum_{r<R}h_r,
\qquad
A_R=\sum_{r<R}(h_r+d_r).
\]

Therefore

\[
\frac{2^{A_R}}{3^{q_R}}
=\prod_{r<R}M_r.
\]

The event-level critical discrepancy

\[
A_R-q_R\log_2 3
\]

is exactly

\[
\boxed{
\sum_{r<R}(d_r-\alpha h_r).
}
\]

Thus the harmonic mixed-place hard core can be expressed entirely as a lattice path of positive integer block pairs `(h_r,d_r)` coupled to the odd-core recurrence for `K_r`.

---

## 7. Current reduced hard core

A hypothetical nonperiodic positive-integer first-descent counterexample would induce an infinite sequence

\[
(h_r,d_r,K_r)_{r\ge0}
\]

satisfying simultaneously:

1. the exact integer recurrence
   \[
   3^{h_r}K_r+2^{d_r}-1=2^{d_r+h_{r+1}}K_{r+1};
   \]
2. positivity and oddness `h_r,d_r,K_r>=1`, `K_r` odd;
3. block-floor survival `X_r=2^{h_r}K_r-1>=n` for all `r`;
4. harmonic/mixed-place restrictions inherited from the full event orbit;
5. at every tail minimum, strict subcriticality
   \[
   d_r<\alpha h_r.
   \]

The next theorem task is to show that these conditions cannot support an infinite sequence of rising tail minima.