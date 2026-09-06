# First universal cell: exact 1024-block correction cap and start-window reduction

Date: 2026-09-06

Status: **SAFE POSITIVE REDUCTION relative to `B0=2^71` and the exact first universal cell.**  This strengthens the first-cell start localization without assuming any ternary selector coverage or finite-to-infinite extrapolation.

---

## 1. Starting point

The first universal first-coefficient-crossing cell is

\[
(A_0,q_0)
=(114,208,327,604,
72,057,431,991),
\]

and the previously certified buffered co-order bound gives

\[
\boxed{2^{71}<N<2^{72}.}
\]

Put

\[
D=2^{A_0}-3^{q_0},
\qquad
\varepsilon=\frac{D}{3^{q_0}},
\qquad
S(w)=\frac{R(w)}{3^{q_0}}.
\]

A paradoxical first crossing requires

\[
\boxed{S(w)\ge\varepsilon N.}
\]

The companion correction-barrier note shows that a scalar correction bound cannot remove the entire interval. It can nevertheless be sharpened enough to remove most of its upper part.

---

## 2. Mechanical word gives the universal correction maximum

Let

\[
\lambda=\log_2 3.
\]

For the `r`-th odd bit of any first-crossing-admissible word, coefficient survival before that bit implies

\[
p_r\le\lfloor(r-1)\lambda\rfloor.
\]

Since each correction summand increases with `p_r`, the latest mechanical positions

\[
p_r^*=\lfloor(r-1)\lambda\rfloor
\]

maximize the correction termwise.

Hence every first-crossing word satisfies

\[
S(w)\le S_*
=\frac13\sum_{n=0}^{q_0-1}2^{-\{n\lambda\}}.
\]

Thus it suffices to obtain a strong deterministic upper bound on this one rotation sum.

---

## 3. Exact finite-block maximum

Because only the fractional part matters, put

\[
\theta=\lambda-1=\log_2(3/2).
\]

For a block length `m`, define

\[
H_m(x)
:=
\sum_{j=0}^{m-1}2^{-\{x+j\theta\}},
\qquad x\in[0,1).
\]

For each `j`, let

\[
a_j=\{j\theta\},
\qquad
u_j=2^{a_j},
\qquad
b_j=u_j^{-1}.
\]

Every `u_j` is an exact rational number because

\[
2^{\{j\theta\}}
=\frac{3^j}{2^{j+\lfloor j\theta\rfloor}}.
\]

Between the wrap thresholds

\[
x=1-a_j,
\]

`H_m(x)` is a positive rational constant times `2^{-x}`, hence strictly decreases. Therefore its global maximum occurs at `x=0` or immediately after one of finitely many wrap thresholds.

The certificate enumerates these rational candidates exactly for

\[
\boxed{m=1024}
\]

and proves

\[
\boxed{
\max_{x\in[0,1)}H_{1024}(x)
<\frac{361}{500}\,1024.
}
\]

No floating-point ordering of phases or thresholds is used.

---

## 4. Global correction upper bound

Exact division gives

\[
q_0=1024M+951.
\]

Split the rotation sum into `M` complete blocks of length 1024 and one remainder block of length 951.

Each complete block is below the exact 1024-block cap. Each remainder summand is at most `1`. Therefore

\[
\boxed{
S(w)
\le S_*
<
\frac13\left(
M\frac{361}{500}1024+951
\right)
=:S_{1024}^{\rm up}.
}
\]

This bound holds for **every** first-crossing-admissible word in the first universal cell.

---

## 5. New start cap

Let

\[
\delta=A_0\ln2-q_0\ln3,
\qquad
\varepsilon=e^\delta-1.
\]

The exact rational-log certificate proves

\[
\boxed{
\delta>
\ln\left(
1+
\frac{S_{1024}^{\rm up}}
{(1365/1024)B_0}
\right).
}
\]

Thus

\[
S_{1024}^{\rm up}
<
\varepsilon\frac{1365}{1024}B_0.
\]

If

\[
N\ge\frac{1365}{1024}B_0,
\]

then every admissible word obeys

\[
S(w)<\varepsilon N,
\]

so its first coefficient crossing is an actual descent and cannot belong to a minimal-counterexample orbit.

Therefore the first universal cell is sharpened to

\[
\boxed{
2^{71}<N<\frac{1365}{1024}2^{71}
=1365\cdot2^{61}.
}
\]

---

## 6. Exact reduction of the 72-bit address space

The old interval had width

\[
2^{72}-2^{71}=B_0.
\]

The new interval has width

\[
\left(\frac{1365}{1024}-1\right)B_0
=\frac{341}{1024}B_0.
\]

Hence the removed fraction is exactly

\[
\boxed{
1-\frac{341}{1024}
=\frac{683}{1024}
\approx66.70\%.
}
\]

At resolution `2^61`, the old top-half interval consisted of 1024 possible 11-bit address blocks numbered

\[
1024,1025,\ldots,2047.
\]

The new cap leaves only

\[
\boxed{1024,1025,\ldots,1364,}
\]

namely **341 top-11-bit blocks**.

The excluded boundary itself has the simple binary pattern

\[
1365=(10101010101)_2.
\]

This gives a concrete finite root-address alphabet for the next same-integer transfer.

---

## 7. DSD interpretation

### Before this step

The root address channel was only localized to one leading bit:

\[
N=(1.\text{anything})_2\,2^{71}.
\]

### After this step

A scalar correction bound and a 1024-term rotation descriptor interact to eliminate 683 of the 1024 top-level 11-bit address cells.

Thus the first-cell same-integer problem can now be organized as

\[
\boxed{
341\ \text{root address blocks}
\longrightarrow
\text{giant first-crossing extension language}.
}
\]

This is a genuine reduction of the source domain, not a density statement.

---

## 8. DSD audit

### CLOSED / SAFE

1. the latest mechanical word termwise maximizes correction over the first-crossing language;
2. the phase powers used by the block transfer are exact rationals;
3. the 1024-block maximum is reduced to finitely many exact wrap-threshold candidates;
4. the exact block maximum is below `(361/500)*1024`;
5. the resulting universal correction upper bound implies `N < (1365/1024)B0`;
6. 683/1024 of the old one-bit source interval is eliminated exactly.

### OPEN

1. eliminate or further split the remaining 341 top-11-bit source blocks;
2. couple each surviving root address block to the nested Hensel/root-max conditions through depth 195;
3. propagate that same integer into the terminal first-crossing correction language;
4. close the first universal cell.

### PROHIBITED UPGRADES

1. Do not infer emptiness of the remaining 341 blocks from their reduced proportion.
2. Do not treat the 1024-block rotation estimate as independence or equidistribution.
3. Do not forget that the terminal word and root address must be the same nested parity word.
4. Do not infer Collatz from elimination of this first cell alone; later universal strip cells and the coefficient-survival branch remain separate obligations.

---

## 9. Reproducibility

Certificate:

`collatz/src/first_universal_cell_1024block_start_cap_certificate.py`

Expected output:

```text
PASS
block length = 1024
exact block maximum is below (361/500)*1024
q remainder modulo 1024 = 951
new start cap: N < (1365/1024)*2^71 = 1365*2^61
old one-bit interval removed fraction = 683/1024
remaining top-11-bit blocks = 341
```

---

## 10. Next target

The next exact source-side object should preserve the 11-bit root address block rather than aggregate it away.

For each

\[
a\in\{1024,\ldots,1364\},
\]

define

\[
I_a=[a2^{61},(a+1)2^{61}).
\]

The required transfer question is whether a nested parity word whose ordinary start lies in `I_a` can simultaneously

1. satisfy the verified-floor prefix inequalities;
2. satisfy nested root-Hensel maximality through depth 195;
3. extend to the exact first crossing `(A0,q0)`;
4. retain enough terminal correction to keep the endpoint at least its own start.

The DSD target is therefore no longer a scalar tail estimate but an **address-indexed family of 341 exact extension problems**. These can next be grouped only when an audited right-congruence or Christoffel/Farey state proves that two address blocks have identical future obligations.