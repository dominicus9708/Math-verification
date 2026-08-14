# Contracting-backtrace residue entropy barrier

Date: 2026-08-14

Status: **exact code-count upper bound + asymptotic entropy limitation**. It shows that fixed-depth contracting reverse codes alone cannot make the odd endpoint residue family dense enough to close the current R1 suffix problem. It is a proof-strategy limitation, not a Collatz proof.

Put

\[
\gamma:=\log_2(3/2),
\qquad
\beta:=\log_2 3=1+\gamma.
\]

Consider an odd-to-odd reverse code of exact odd depth `q`. Write its binary exponents as

\[
\boxed{k_i=1+e_i,\qquad e_i\in\mathbb Z_{\ge0}.}
\]

The total exponent is

\[
K=q+E,
\qquad
E:=\sum_{i=1}^{q}e_i.
\]

## 1. Exact contraction budget

Multiplicative contraction requires

\[
2^K<3^q.
\]

Thus

\[
q+E<q\log_2 3
=q(1+\gamma),
\]

so

\[
E<q\gamma.
\]

Because `q gamma` is irrational,

\[
\boxed{
E\le B_q:=\lfloor q\gamma\rfloor.
}
\]

## 2. Number of contracting exponent codes

The number of nonnegative `q`-tuples with total at most `B_q` is the stars-and-bars count

\[
\boxed{
C_q
=
\binom{q+B_q}{B_q}.
}
\]

Every fixed reverse exponent code determines at most one endpoint residue modulo

\[
3^q
\]

for which the corresponding `q`-step ancestor is integral. Different codes may collide on the same residue, so `C_q` is an upper bound, not a lower bound, for the number of forbidden residues.

The relevant odd-event endpoint residues are units modulo `3^q`, of which there are

\[
\boxed{
\varphi(3^q)=2\cdot3^{q-1}.
}
\]

Hence the fraction of unit endpoint residues that can possibly be covered by exact-depth contracting codes satisfies

\[
\boxed{
F_q
\le
\frac{\binom{q+B_q}{B_q}}
{2\cdot3^{q-1}}.
}
\]

No assumption about collisions is used.

## 3. Current gap-localization depth q=22

For

\[
q=22,
\]

\[
B_{22}=\lfloor22\log_2(3/2)\rfloor=12.
\]

Therefore

\[
C_{22}
=\binom{34}{12}
=\boxed{548,354,040}.
\]

The unit residue count is

\[
2\cdot3^{21}
=\boxed{20,920,706,406}.
\]

Thus even in the impossible best case where all contracting codes hit distinct residues,

\[
\boxed{
F_{22}
<0.0262111.
}
\]

So an exact-depth-22 contracting-backtrace filter can cover at most about `2.62%` of all possible unit endpoint residues modulo `3^22`.

This explains why adding an ordinary contracting-backtrace filter to the gap-22 suffix address cannot by itself turn the fibrewise Cantor halving theorem into a small global residue family.

## 4. Asymptotic entropy barrier

Since

\[
B_q=\gamma q+O(1),
\]

Stirling's formula gives

\[
\log_2 C_q
=
(1+\gamma)
H_2\left(\frac{\gamma}{1+\gamma}\right)q
+O(\log q),
\]

where `H_2` is the binary entropy.

Because

\[
1+\gamma=\beta=\log_2 3
\]

and

\[
\frac{\gamma}{\beta}
=1-\frac1\beta
=1-\log_3 2,
\]

symmetry of binary entropy yields

\[
H_2\left(\frac\gamma\beta\right)
=H_2(\log_3 2).
\]

Therefore

\[
\boxed{
\log_2 F_q
\le
-\kappa q+O(\log q),
}
\]

with

\[
\boxed{
\kappa
=
\log_2 3\,
\left(1-H_2(\log_3 2)\right)
\approx0.0793186.
}
\]

Consequently

\[
\boxed{F_q\to0\text{ exponentially}.}
\]

This is a strong negative structural result: increasing the **exact reverse depth** does not make the contracting endpoint-residue sieve denser. It makes its maximal possible residue coverage exponentially sparser.

## 5. Relation to the binary survivor entropy

The same entropy

\[
H_2(\log_3 2)
\]

already appeared as the topological entropy of the coefficient-surviving binary Beatty language.

Here it reappears in a dual form: the number of contracting reverse exponent allocations has entropy

\[
\log_2 3\,H_2(\log_3 2),
\]

while the ambient `3`-adic residue space has entropy `log_2 3` per odd step.

Thus the forward critical-language sparsity and reverse contracting-code sparsity are controlled by the same entropy constant, but neither one alone excludes a specific ordinary integer.

## 6. Strategic consequence

The current R1 closure cannot be obtained by simply increasing a single reverse depth `q` and hoping that contracting backtraces cover almost every suffix residue. The exact-depth coverage upper bound tends in the opposite direction.

The useful reverse information must instead be coupled to another channel, for example

- a fixed ternary Cantor fibre as in the gap-22 theorem;
- the phase/skew state;
- the strengthened dyadic renewal address;
- or repeated multiscale constraints on the **same** ordinary integer.

This is another reason the terminal proof must be cross-scale and mixed-place rather than a one-depth residue sieve.
