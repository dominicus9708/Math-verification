# Ordering-only Bellman closed form and acyclic lower-bound layer

Date: 2026-08-27
Status: **SAFE local lemma / exact finite certificate**
Scope: ordering-only relaxation used as a lower-bound layer for the `s=1` two-boundary Hensel problem.

## 1. Purpose

The current open gate is to lower-bound the exact two-boundary Hensel defect cost in the `s=1` no-cross-checkpoint-transport sector and compare that bound against an independently derived near-root defect budget.

This note deliberately does **not** use a near-root budget, an `A0/J0` macro contraction, a Cantor-core selector, or a local-to-global pullback theorem in deriving the Bellman quantity below.  This makes the dependency direction one-way and prevents a circular proof.

## 2. Ordering-only relaxation

Let

\[
w=(g_1,\ldots,g_n),\qquad g_i\in\{1,2\}.
\]

For an initial right-boundary displacement `p>=0`, remove every Hensel congruence condition and retain only the ordering recurrence

\[
p_i=\max(0,p_{i-1}-g_i+1),\qquad p_0=p.
\]

If

\[
N_2(i)=\#\{t\le i:g_t=2\},
\]

then induction gives the exact state formula

\[
\boxed{p_i=\max(0,p-N_2(i)).}
\]

Thus gap-1 preserves the ordering displacement and gap-2 decreases it by exactly one until zero.

Define the prefix weight

\[
\lambda_i=\frac{3^i}{2^{g_1+\cdots+g_i}}.
\]

The ordering-only normalized defect cost is

\[
B_w(p)=\sum_{i:p_i>0}2\lambda_i(1-2^{-p_i}).
\]

Because the exact Hensel problem has all of these ordering restrictions plus additional congruence restrictions, deleting the congruences enlarges the feasible set.  Therefore

\[
\boxed{\mathcal T_w^{\mathrm{Hensel}}\ge B_w(p).}
\]

This inequality is a relaxation inequality only; it makes no assertion that the ordering optimum is Hensel-realizable.

## 3. Exact closed form

Let `i_p` be the position of the `p`-th gap-2 when it exists.  Define the last active index

\[
m_w(p)=
\begin{cases}
0,&p=0,\\
i_p-1,&1\le p\le N_2(w),\\
n,&p>N_2(w).
\end{cases}
\]

Set

\[
A_m=\sum_{i=1}^{m}\lambda_i.
\]

For every active index `i<=m_w(p)`, one has `p_i=p-N_2(i)>0`.  Since every gap is either one or two,

\[
g_1+\cdots+g_i=i+N_2(i).
\]

Hence the key cancellation is

\[
\boxed{
\lambda_i2^{N_2(i)}
=
\frac{3^i}{2^{i+N_2(i)}}2^{N_2(i)}
=
\left(\frac32\right)^i.
}
\]

Therefore

\[
\begin{aligned}
B_w(p)
&=2\sum_{i=1}^{m}\lambda_i
-2^{1-p}\sum_{i=1}^{m}\lambda_i2^{N_2(i)}\\
&=2A_m
-2^{1-p}\sum_{i=1}^{m}\left(\frac32\right)^i.
\end{aligned}
\]

Using

\[
\sum_{i=1}^{m}\left(\frac32\right)^i
=3\left[\left(\frac32\right)^m-1\right],
\]

we obtain

\[
\boxed{
B_w(p)
=
2A_{m_w(p)}
-
6\,2^{-p}
\left[
\left(\frac32\right)^{m_w(p)}-1
\right].
}
\]

For `p=0`, `m=0` and the same formula yields zero.

## 4. Monotonicity

For fixed `w`, every state

\[
p_i(p)=\max(0,p-N_2(i))
\]

is nondecreasing in `p`, and each local cost

\[
2\lambda_i(1-2^{-p_i})
\]

is nondecreasing for `p_i>=0`.  Hence

\[
\boxed{p\le p'\implies B_w(p)\le B_w(p').}
\]

When `p>N_2(w)`, all positions remain active and

\[
B_w(p)=2A_n-6\,2^{-p}\left[\left(\frac32\right)^n-1\right],
\]

so `B_w(p)` increases to `2A_n` from below.

## 5. Exact block composition

For a concatenation `w=uv`, let

\[
\lambda(u)=\frac{3^{|u|}}{2^{\sum u}},
\qquad
F_u(p)=\max(0,p-N_2(u)).
\]

Then

\[
\boxed{F_{uv}=F_v\circ F_u}
\]

and the normalization of the second block gives

\[
\boxed{
B_{uv}(p)
=
B_u(p)+\lambda(u)B_v(F_u(p)).
}
\]

Thus a block can be represented without loss inside the ordering relaxation by

\[
\boxed{(F_w,B_w,\lambda_w).}
\]

The closed form above further shows that evaluating `B_w(p)` requires only the weighted prefix sum through the last active index and the positions of gap-2 letters.

## 6. Certificate

Exact rational regression is in

`collatz/src/ordering_only_bellman_closed_form_certificate.py`.

The certificate checks:

1. direct recurrence cost equals the closed form for every binary gap word up to length 12 and every `0<=p<=16`;
2. monotonicity in `p` over the same state set;
3. exact block composition for all binary words up to total length 8 and every `0<=p<=10`;
4. the cancellation `lambda_i 2^{N_2(i)}=(3/2)^i` exactly.

All arithmetic is `fractions.Fraction`.

## 7. Circularity audit

The permitted dependency graph is

\[
\boxed{
\text{gap word / ordering recurrence}
\longrightarrow
B_w(p)
\longrightarrow
\text{lower bound for exact Hensel cost}
\longrightarrow
\text{finite-depth Hensel refinements}
\longrightarrow
\text{comparison with independent near-root budget}.
}
\]

The following reverse arrows are forbidden and are not used here:

- near-root gap budget `->` ordering Bellman cost;
- `A0/J0` macro contraction `->` local Hensel lower bound;
- an observed local residue pattern `->` global predecessor theorem;
- a finite Hensel search `->` infinite closure without an explicit extension theorem.

Accordingly this lemma is **SAFE** but, by itself, does **not** close the Collatz proof gate.

## 8. Next non-circular step

Construct a hierarchy `B_w^(h)` in which the first `h` Hensel congruence decisions are enforced exactly and only the suffix is relaxed to the ordering problem.  The target is a monotone sequence

\[
\boxed{
\mathcal T_w^{\mathrm{Hensel}}
\ge B_w^{(h+1)}
\ge B_w^{(h)}
\ge B_w.
}
\]

Only after this lower-bound chain is independently certified should any value be compared against the near-root defect budgets.  Failure to exceed those budgets remains an **OPEN** result, not evidence of closure.
