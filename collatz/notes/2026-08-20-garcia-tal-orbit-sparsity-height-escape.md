# Garcia--Tal orbit sparsity implies reciprocal summability and height escape

Date: 2026-08-20

Status: **published external input + exact deduction for the accelerated Collatz map.** This closes the bounded-height branch of the current coefficient-survivor program for infinite nonperiodic orbits. It does not exclude nontrivial finite cycles, does not prove the remaining sublinear-height branch, and is not a proof of the Collatz conjecture.

External input:

Manuel V. P. Garcia and Fabio A. Tal, *A note on the generalized 3n + 1 problem*, Acta Arithmetica 90.3 (1999), 245--250.

For the classical accelerated Collatz map

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

the Garcia--Tal Hasse function specializes exactly to this map.

## 1. Quantitative orbit sparsity from Garcia--Tal

Garcia--Tal prove the following stronger fact before taking the Banach-density limit.

There exist

\[
\delta_1,\delta_2\in(0,1)
\]

and a function

\[
g(K)=O(K^{\delta_2})
\]

such that a complete set \(P\) of their equal-time orbit-equivalence representatives satisfies, uniformly in the interval start \(a\),

\[
\#\bigl(P\cap[a,a+K-1]\bigr)
\le
2(\lfloor\log_2K\rfloor+1)
\left(K^{1-\delta_1}+g(K)\right).
\]

Their Corollary 1 observes that every infinite nonperiodic orbit \(O(x_0)\) can be included in such a representative set \(P\). Hence the same interval estimate applies to the orbit itself.

Put

\[
\boxed{
\beta=\max(1-\delta_1,\delta_2)<1.
}
\]

After absorbing the big-O constant, there is \(C>0\) such that for all sufficiently large \(K\), uniformly in \(a\),

\[
\boxed{
\#\bigl(O(x_0)\cap[a,a+K-1]\bigr)
\le
C(1+\log K)K^\beta.
}
\]

This quantitative estimate, not merely the statement of Banach density zero, is the external fact used below.

## 2. Reciprocal summability of every infinite nonperiodic orbit

An infinite nonperiodic orbit has no repeated value: a repetition in a deterministic map would make the subsequent orbit periodic.

Partition the positive integers into dyadic shells

\[
I_r=[2^r,2^{r+1}-1].
\]

Using the uniform interval estimate with \(K=2^r\),

\[
\#(O\cap I_r)
\le
C'(r+1)2^{\beta r}.
\]

Therefore

\[
\begin{aligned}
\sum_{x\in O\cap I_r}\frac1x
&\le
\frac{\#(O\cap I_r)}{2^r}\\
&\le
C'(r+1)2^{-(1-\beta)r}.
\end{aligned}
\]

Because \(1-\beta>0\),

\[
\sum_{r\ge0}(r+1)2^{-(1-\beta)r}<\infty.
\]

Hence

\[
\boxed{
\sum_{j=0}^\infty\frac1{x_j}<\infty
}
\]

for every infinite nonperiodic accelerated Collatz orbit.

This reciprocal-summability statement is a direct deduction from Garcia--Tal equation (6), not a separately quoted theorem from their paper.

## 3. Exact multiplicative identity

Let

\[
m_k=\#\{0\le j<k:x_j\text{ is odd}\}.
\]

At an odd step,

\[
\frac{3x+1}{2}
=x\frac32\left(1+\frac1{3x}\right),
\]

while at an even step the multiplicative factor is \(1/2\).

Thus, exactly,

\[
\boxed{
 x_k
 =
 x_0\frac{3^{m_k}}{2^k}
 \prod_{\substack{0\le j<k\\x_j\text{ odd}}}
 \left(1+\frac1{3x_j}\right).
}
\]

Define

\[
\Pi_k
:=
\prod_{\substack{0\le j<k\\x_j\text{ odd}}}
\left(1+\frac1{3x_j}\right).
\]

Because

\[
0<\log(1+u)\le u
\qquad(u>0)
\]

and the reciprocal orbit sum is finite,

\[
\sum_{j:\,x_j\text{ odd}}
\log\left(1+\frac1{3x_j}\right)<\infty.
\]

Therefore

\[
\boxed{
1\le\Pi_k\uparrow\Pi_\infty<\infty.
}
\]

## 4. Identification with the normalized height variable

Let

\[
b_k=\lceil k\log_3 2\rceil,
\qquad
h_k=m_k-b_k.
\]

Then the exact product identity becomes

\[
 x_k
 =
 x_0\,3^{h_k}
 \frac{3^{b_k}}{2^k}\Pi_k.
\]

Because powers of two and three are distinct,

\[
3^{b_k-1}<2^k<3^{b_k}
\]

for every positive \(k\). Consequently

\[
1<\frac{3^{b_k}}{2^k}<3.
\]

Thus every infinite nonperiodic orbit satisfies the uniform comparison

\[
\boxed{
 x_0\,3^{h_k}
 < x_k
 < 3x_0\Pi_\infty\,3^{h_k}
}
\]

for \(k\ge1\).

In asymptotic notation,

\[
\boxed{x_k\asymp3^{h_k}.}
\]

This is much sharper for the present proof program than the earlier crude zero-lift linear corridor.

## 5. Exact identification of v with the correction product

The current sparse-tail normalization is

\[
 v_k
 :=
 \frac{2^k x_k}{3^{m_k}}.
\]

Substitution into the product identity gives the exact formula

\[
\boxed{
 v_k=x_0\Pi_k.
}
\]

Hence Garcia--Tal reciprocal summability implies

\[
\boxed{
 v_k\uparrow v_\infty=x_0\Pi_\infty<\infty.
}
\]

The previously derived one-step additive cocycle

\[
 v_{k+1}-v_k
 =
 \begin{cases}
 0,&x_k\text{ even},\\[1mm]
 2^k/3^{m_k+1},&x_k\text{ odd}
 \end{cases}
\]

is therefore exactly the additive expansion of this convergent correction product.

## 6. Bounded height is impossible

Assume now that the orbit is coefficient-surviving, so

\[
h_k\ge0
\]

throughout the relevant tail.

If \(h_k\le H\) for infinitely many \(k\), then the comparison above gives

\[
 x_k
 <
3x_0\Pi_\infty 3^H
\]

for infinitely many distinct orbit values.

But there are only finitely many positive integers below this fixed bound. This is impossible for a nonperiodic orbit.

Therefore

\[
\boxed{
h_k\to+\infty.}
\]

This is stronger than merely saying that height is unbounded.

Thus the entire bounded-height coefficient-survivor branch is closed for infinite nonperiodic orbits by a published orbit-sparsity theorem plus the exact product identity.

## 7. Record-climb segmentation

Since

\[
h_k\to+\infty,
\]

choose successive first-passage times

\[
\tau_r<\tau_{r+1}<\cdots
\]

with

\[
h_{\tau_{j+1}}=h_{\tau_j}+1.
\]

Each segment from \(\tau_j\) to \(\tau_{j+1}\) is an admissible macro with strict net height gain one.

By the companion surplus-gain macro theorem, **every such record-climb macro** satisfies

\[
P_W-E_W>0
\]

(the inequality is strict because \(3^Q\ne2^L\)).

Thus the negative normalized low-q pieces found in a fixed five-block partition are not persistent asymptotic objects: once the trajectory is grouped by successive height climbs, each complete climb has positive exact normalized syndrome-minus-rebate transport.

This is a substantial reduction of the sparse-tail problem.

## 8. What remains

This result does not prove that an infinite nonperiodic coefficient-surviving orbit is impossible.

The remaining difficult asymptotic regime is now:

\[
\boxed{
h_k\to\infty}
\]

with possible slow/sublinear height growth, together with eventual-zero Hensel lift constraints.

Positive linear height drift is naturally entropy-deficient and belongs to the bulk/Haar side. The sharp boundary regime is therefore a slowly diverging height process near the mechanical coefficient barrier.

The next deterministic target is no longer bounded-height exclusion. It is:

> **Record-climb Hensel transversality:** show that an infinite sequence of strict-height-gain macros cannot simultaneously have an eventual-zero dyadic Hensel lift while satisfying all ternary endpoint syndromes.

Companion internal notes:

- `collatz/notes/2026-08-20-height-excursion-macro-reduction.md`
- `collatz/notes/2026-08-20-height-neutral-phase-coboundary.md`

External source used:

Garcia--Tal (1999), especially Proposition 1, equation (6), Theorem 1 and Corollary 1.
