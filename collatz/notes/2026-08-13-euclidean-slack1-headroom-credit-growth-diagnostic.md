# Euclidean slack-one headroom-credit growth diagnostic

Date: 2026-08-13

Status: **exact finite Euclidean-scale diagnostic**.  The calculation measures integer predecessor credits inside the low-slack survival fibre `(Sigma,M)=(-1,-1)` of the first return-word macroblocks.  It supplies evidence and a quantitative target for a future growth theorem; it is not an asymptotic theorem and does not prove Collatz.

## 1. Credit inside one survival-state fibre

Fix a deterministic mechanical macroblock `U` of length `L` with `Q` mechanical odd symbols.  Consider actual orientations `w` with

\[
\boxed{(\Sigma,M)=(-1,-1).}
\]

Every such word contains

\[
\boxed{q=Q-1}
\]

odd symbols, requires only one unit of incoming Beatty slack, and exits with that slack decreased by one.

For one actual orientation `w`, an orientation `u` in the same fibre gives an immediate integer predecessor credit whenever

\[
R_u>R_w,
\qquad
R_u\equiv R_w\pmod{3^q}.
\]

The credit is

\[
\boxed{
\Delta(u,w)=\frac{R_u-R_w}{3^q}.
}
\]

The local rewrite theorem gives

\[
T_u^L(x-\Delta)=T_w^L(x).
\]

Thus if `w` occurs on a hypothetical minimal-counterexample orbit at block input `x`, positivity of the alternate state implies the headroom condition

\[
\boxed{x-N\ge\Delta.}
\]

## 2. First five nontrivial Euclidean macroblocks

Use the return-word representatives

\[
\begin{aligned}
U_2&=101,\\
U_3&=01101,\\
U_4&=01101101,\\
U_5&=10101101101,\\
U_6&=1010110110101101101.
\end{aligned}
\]

They have

\[
(L,Q)=(3,2),(5,3),(8,5),(11,7),(19,12).
\]

The exact verifier enumerates only the one-slack fibre at each level and groups its corrections modulo `3^q`.

## 3. Exact credit profile

The results are

\[
\boxed{
\begin{array}{c|r|r|r|r|r|r}
U&L&q&|\mathcal F|&\#\text{ residue classes}&\#\text{ orientations with }\Delta>0&\Delta_{\max}\\\hline
101&3&1&3&2&1&1\\
01101&5&2&9&5&4&2\\
01101101&8&4&53&30&23&3\\
10101101101&11&6&299&179&120&5\\
1010110110101101101&19&11&35174&21856&13318&11
\end{array}
}
\]

Thus the largest available predecessor credit in this fixed low-slack fibre grows through

\[
\boxed{1,2,3,5,11.}
\]

This is an exact finite sequence, not an asserted recurrence.

The fraction of the fibre carrying at least one positive immediate integer credit is respectively

\[
\boxed{
\frac13,
\frac49,
\frac{23}{53},
\frac{120}{299},
\frac{13318}{35174}.
}
\]

At the largest checked level this is

\[
\boxed{0.3786319440\ldots}
\]

or about `37.86%`.

## 4. Explicit largest level-6 credit

For

\[
U_6=1010110110101101101
\]

the mechanical odd count is `Q=12`, so the one-slack fibre has

\[
q=11.
\]

One exact correction class modulo `3^11` contains

\[
R_{\rm low}=457643,
\qquad
R_{\rm high}=2406260.
\]

Their difference is

\[
\boxed{
2406260-457643
=1948617
=11\cdot3^{11}.
}
\]

Therefore the corresponding low-correction orientation has local predecessor credit

\[
\boxed{\Delta=11.}
\]

The two witness orientations are

\[
\boxed{
1111011100001111000
}
\]

and

\[
\boxed{
0010110110101111010.
}
\]

Both lie in the exact same survival-state fibre `(Sigma,M)=(-1,-1)` relative to `U_6`.

## 5. Lower levels and witness growth

The maximum-credit witness pairs at the preceding levels are:

\[
\begin{array}{c|c|c|c}
L&q&\Delta_{\max}&(R_{\rm low},R_{\rm high})\\\hline
3&1&1&(1,4)\\
5&2&2&(10,28)\\
8&4&3&(179,422)\\
11&6&5&(1297,4942)\\
19&11&11&(457643,2406260)
\end{array}
\]

Each difference is exactly `Delta_max * 3^q`.

## 6. What this establishes

The earlier Euclidean multiplicity theorem showed that higher return-word scales create multiple internal orientations with identical survival state.  The correction-collision theorem then showed that some such fibres contain integer alternate predecessors.

The present calculation adds a third fact:

\[
\boxed{
\text{the size of the available integer predecessor credit can increase with Euclidean scale even when the required incoming slack stays fixed at one.}
}
\]

This is the first direct evidence that the local rewrite mechanism may eventually impose headroom requirements stronger than the trivial nonreturn gap `x>=N+1`.

## 7. Limitation

The calculation does **not** show that every orientation in the one-slack fibre has a positive credit, nor that the maximum credit grows without bound.  The positive-credit coverage remains around forty percent in the checked levels, and no monotone asymptotic law has been proved.

Therefore one must not infer a uniform R2 exclusion from the sequence `1,2,3,5,11`.

## 8. R2 connection

For a nonperiodic no-first-descent candidate, the odd-event state may be written

\[
x_i=2^{-D_i}(N+c_i),
\]

with

\[
D_i=A_i-i\log_2 3\le0.
\]

The harmonic-correction result gives

\[
c_i=O_N(i^{1/9}),
\]

while critical-strip sparsity says fixed-width returns to `D_i` near zero are sparse.

At any Euclidean macroblock beginning at such a return, an orientation with predecessor credit `Delta` requires

\[
\boxed{
2^{-D_i}(N+c_i)-N\ge\Delta.
}
\]

Thus the desired asymptotic theorem can be stated quantitatively:

> prove that the Euclidean correction-collision credit forced on every sufficiently long critical-return orientation eventually exceeds the headroom available at that return.

A theorem of this type would attack the remaining aperiodic R2 branch without enumerating integers or flat parity strings.

## 9. Next computational target

Flat enumeration beyond the 19-bit macroblock is not the preferred next step.  The correction-residue state

\[
(\Sigma,M,q,R\bmod3^J,\text{multiplicity})
\]

should be propagated recursively along the continued-fraction return-word construction.  In addition to multiplicity, each residue class should retain the minimum and maximum exact correction compatible with the class.

This would compute the credit distribution at the next Euclidean levels by state aggregation rather than `2^L` enumeration, preserving the original proof strategy of eliminating whole sets through propositions and finite state recursions.
