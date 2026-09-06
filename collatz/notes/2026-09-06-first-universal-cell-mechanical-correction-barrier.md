# First universal cell: mechanical-correction barrier to correction-only closure

Date: 2026-09-06

Status: **SAFE NEGATIVE/PRUNING LEMMA relative to the external verified floor `B0=2^71`, the exact first universal Farey cell, and the repository's first-crossing correction formula.**

This note does **not** produce a Collatz counterexample and does **not** close the first universal cell.  It closes a proof strategy: sharpening a word-independent or correction-only upper envelope for `C(w)` cannot by itself eliminate this cell.  The remaining obstruction must couple the correction to the same word's dyadic start address.

---

## 1. Current first universal cell

The verified-floor/Farey reduction gives

\[
B_0=2^{71}
\]

and the earliest possible first coefficient crossing of a hypothetical minimal positive counterexample at

\[
\boxed{
(A_0,q_0)
=(114,208,327,604,
72,057,431,991).
}
\]

The buffered co-order theorem simultaneously confines its start to

\[
\boxed{2^{71}<N<2^{72}.}
\]

At the first crossing, put

\[
D=2^{A_0}-3^{q_0}>0,
\qquad
\varepsilon=\frac{D}{3^{q_0}}.
\]

For a parity word `w` with correction `R(w)`, define the normalized correction

\[
S(w)=\frac{R(w)}{3^{q_0}}.
\]

The first-crossing endpoint is at least the start exactly when

\[
R(w)\ge DN,
\]

or equivalently

\[
\boxed{S(w)\ge\varepsilon N.}
\]

Thus a correction-only elimination at the verified floor would need an upper bound forcing

\[
S(w)<\varepsilon B_0
\]

for every first-crossing-admissible word.

---

## 2. Latest-possible mechanical first-crossing word

Let

\[
\alpha=\log_3 2,
\qquad
\lambda=\alpha^{-1}=\log_2 3.
\]

For `r=1,...,q_0`, place the `r`-th odd bit at the zero-indexed position

\[
\boxed{
p_r=\lfloor(r-1)\lambda\rfloor.
}
\]

This is the latest-possible mechanical/Beatty word compatible with coefficient survival before the first crossing.

Its prefix odd count is the minimal count needed to retain

\[
3^{q_j}\ge2^j
\]

at every `j<A_0`, while the terminal pair `(A_0,q_0)` satisfies

\[
3^{q_0}<2^{A_0}.
\]

Hence this is an actual member of the first-crossing admissible language of the cell, not merely an ambient binary word.

---

## 3. Exact normalized correction identity

For this mechanical word,

\[
R_*
=\sum_{r=1}^{q_0}3^{q_0-r}2^{p_r}.
\]

Therefore

\[
\begin{aligned}
S_*
&=\frac{R_*}{3^{q_0}}\\
&=\sum_{r=1}^{q_0}\frac{2^{p_r}}{3^r}\\
&=\frac13\sum_{n=0}^{q_0-1}2^{-\{n\lambda\}}.
\end{aligned}
\]

This identity converts the correction problem into an exact rotation sum.

---

## 4. Uniform pair lower bound

Write

\[
\theta=\lambda-1=\log_2(3/2).
\]

For `x in [0,1)`, define

\[
h(x)=2^{-x}+2^{-\{x+\theta\}}.
\]

There are two cases.

If

\[
x<1-\theta,
\]

then no wrap occurs, and using

\[
2^{-\theta}=\frac23
\]

gives

\[
h(x)=\frac53\,2^{-x}>\frac54.
\]

If

\[
x\ge1-\theta,
\]

then one wrap occurs, and using

\[
2^{1-\theta}=\frac43
\]

gives

\[
h(x)=\frac73\,2^{-x}>\frac76.
\]

Consequently every adjacent rotation pair obeys the global strict bound

\[
\boxed{h(x)>\frac76.}
\]

Because

\[
q_0=72,057,431,991
\]

is odd, pairing the first `q_0-1` terms and leaving the final term unpaired gives

\[
\sum_{n=0}^{q_0-1}2^{-\{n\lambda\}}
>
\frac{7(q_0-1)}{12}+\frac12
=
\frac{7q_0-1}{12}.
\]

Thus

\[
\boxed{
S_*>
\frac{7q_0-1}{36}.
}
\]

This lower bound is fully symbolic and requires no equidistribution assumption.

---

## 5. Exact first-cell comparison

Let

\[
\delta=A_0\ln2-q_0\ln3.
\]

Then

\[
\varepsilon=e^\delta-1.
\]

The accompanying exact rational-log certificate proves

\[
\boxed{
\delta
<
\ln\left(
1+
\frac{100(7q_0-1)}{107\cdot36B_0}
\right).
}
\]

Therefore

\[
\varepsilon
<
\frac{100}{107B_0}
\frac{7q_0-1}{36}.
\]

Combining this with the mechanical lower bound yields

\[
\boxed{
S_*>\frac{107}{100}B_0\varepsilon.
}
\]

In particular,

\[
\boxed{
S_*>B_0\varepsilon.
}
\]

So the explicit admissible mechanical word has **more than 7% correction headroom** above what would be needed to keep the terminal first-crossing endpoint at least `B0`, considered only at the level of the scalar correction inequality.

---

## 6. What this proves — and what it does not

### SAFE conclusion

The first universal cell cannot be eliminated by any argument whose decisive step is only

1. first-crossing admissibility;
2. a scalar upper envelope for `S(w)` or `R(w)`;
3. comparison of that envelope with `B0*epsilon`.

There exists an exactly admissible word for which the correction budget itself is already large enough by a certified margin.

Hence the missing obstruction must use information discarded by a correction-only envelope.

### NOT a counterexample

The parity word fixes a canonical dyadic start residue

\[
n_{A_0}(w)
\equiv
-R(w)3^{-q_0}
\pmod{2^{A_0}}.
\]

The mechanical word's correction capacity says nothing by itself about whether this fixed residue is an ordinary integer in

\[
(2^{71},2^{72}).
\]

For the actual first-cell candidate, the **same word must simultaneously supply both**

- enough correction;
- the correct small dyadic address.

Therefore the barrier theorem is a pruning theorem, not an existence theorem.

---

## 7. DSD analysis

The current proof architecture separates naturally into three channels.

### Channel C — correction capacity

Observable:

\[
S(w)=R(w)/3^{q_0}.
\]

Result here:

\[
\boxed{\text{correction capacity alone does not close the cell}.}
\]

This channel is now insufficient as a standalone elimination mechanism.

### Channel A — dyadic address

Observable:

\[
n_L(w)\equiv-R(w)3^{-q_L}\pmod{2^L}.
\]

At depth `72`, because a candidate start is below `2^72`, its canonical residue is already the ordinary integer itself.

This is a high-value same-integer channel.

### Channel J — joint compatibility

Required statement:

\[
\boxed{
\text{large enough correction}
\quad\land\quad
2^{71}<n_{72}(w)<2^{72}
\quad\land\quad
\text{first crossing at }(A_0,q_0)
}
\]

must be impossible for one and the same nested word.

This is the surviving structural target.

---

## 8. DSD audit

### CLOSED / SAFE

1. the latest mechanical word is first-crossing admissible;
2. its normalized correction has the exact rotation-sum representation;
3. every two-term rotation pair is strictly greater than `7/6`;
4. `q0` odd gives `S_*>(7q0-1)/36`;
5. exact rational logarithm bounds certify
   `S_*>1.07*B0*epsilon`;
6. therefore correction-only closure of the first universal cell is impossible.

### OPEN

1. same-integer coupling between `S(w)` and the dyadic address `n_72(w)`;
2. a compressed transfer from the 72-bit canonical start to the giant first-crossing terminal correction;
3. elimination of the first universal cell;
4. COV-1 and the genuinely aperiodic inverse-limit branch.

### PROHIBITED UPGRADES

1. Do not interpret the mechanical word as a positive-integer counterexample.
2. Do not infer that a large correction envelope is attained by a word whose canonical start lies in `(2^71,2^72)`.
3. Do not replace the required joint dyadic/correction theorem by a density or average statement.
4. Do not extrapolate finite root-Hensel neutrality into independence; the same-integer dependence is exactly what must now be retained.

---

## 9. Reproducibility

Certificate:

`collatz/src/first_universal_cell_mechanical_correction_barrier_certificate.py`

Expected output:

```text
PASS
first universal cell (A,q) = (114208327604, 72057431991)
mechanical normalized correction lower bound = (7q-1)/36
correction-only floor barrier: S_* > B0*epsilon
certified slack: S_* > 1.07*B0*epsilon
same-integer dyadic address remains the required obstruction
```

No floating-point comparison is used in the certificate assertions.

---

## 10. Next exact target

Define a same-integer transfer from the 72-bit root address into the first-cell terminal language.

For a candidate

\[
N\in(2^{71},2^{72}),
\]

its first 72 parity bits are fixed by `N`.  Let

\[
\mathcal E(N)
\]

be the set of all coefficient-surviving extensions of that fixed prefix which first cross at `(A0,q0)`.

The exact next inequality to establish is

\[
\boxed{
\sup_{w\in\mathcal E(N)}S(w)<\varepsilon N
\qquad
\text{for every }2^{71}<N<2^{72}.
}
\]

Unlike the discarded correction-only route, this formulation preserves the same ordinary integer from the root through the terminal cell.  Any compressed Christoffel/Farey, dangerous-axis, Fourier, or Hensel transfer should now be audited against this joint target.