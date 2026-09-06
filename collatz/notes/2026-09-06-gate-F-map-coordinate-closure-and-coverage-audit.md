# Gate F map: exact coordinate closure and recursive-sufficiency coverage audit

Date: 2026-09-06

Status: **`F_map^coord` CLOSED / `F_map^cover` OPEN.**  The ternary-selector multiplicity, dyadic parent coordinate, Beatty survivor set, one-child boundary, and child normalization are already the same exact finite-group objects in the coefficient-mass transport theorem.  However, the previous claim that a hypothetical minimal counterexample must lie in the infinite ternary 0/1 Cantor core depended on Ansari (2025), Lemma 3.1.  An exact audit of the printed induction finds a failure already in the step `F_1 -> F_2`.  Therefore the selector transport remains exact for the selector family, but its universal minimal-counterexample coverage is not currently established.  This is not a proof of the Collatz conjecture.

---

## 1. Exact reduced coordinate

Every member of the ternary selector family used by the mass-transport theorem has the form

\[
N=4Y+3.
\]

At binary depth `L>=2`, fixing `N mod 2^L` is equivalent to fixing

\[
\boxed{Y\pmod{2^{L-2}}.}
\]

Indeed,

\[
4Y_1+3\equiv4Y_2+3\pmod{2^L}
\iff
Y_1\equiv Y_2\pmod{2^{L-2}}.
\]

Set

\[
M:=2^{L-2}.
\]

Then a parent class `r mod M` has exactly two lifts modulo `2M`:

\[
\boxed{r,\qquad r+M.}
\]

This is precisely the coordinate used in the existing coefficient-mass transport theorem (`2026-08-13-coefficient-mass-transport-fourier-bridge.md`).

Status: **SAFE LEMMA.**

---

## 2. Parity-prefix coordinate is the same dyadic class

Under the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

a length-`L` parity word determines one residue class modulo `2^L` by the standard parity-vector bijection.

Every integer `N=4Y+3` begins with shortcut parity bits `11`:

\[
N\equiv3\pmod4,
\qquad
T(N)=6Y+5\equiv1\pmod2.
\]

Consequently the fixed `11` head removes exactly two dyadic bits and the remaining class is exactly `Y mod 2^(L-2)`.  Thus the reduced parent group in the selector theorem is not an auxiliary look-alike: it is the same integer's parity-prefix class after the affine wrapper is removed.

Status: **SAFE COORDINATE IDENTIFICATION.**

---

## 3. Exact selector multiplicity and Beatty sets

The existing mass-transport theorem defines, on the child group `Z/(2M)Z`,

\[
c_0(r),\ c_1(r)
\]

as the **exact integer numbers of ternary selector assignments** landing in the two children `r` and `r+M`.

It then sets

\[
c(r)=c_0(r)+c_1(r),
\qquad
u(r)=c_0(r)-c_1(r).
\]

On the same parent group `Z/MZ`, it defines

\[
R_L
\]

as the coefficient-surviving classes, where every parity prefix obeys

\[
q_j\ge b_j,
\qquad
b_j=\lceil j\log_3 2\rceil.
\]

At a Beatty rise `b_(L+1)=b_L+1`, the one-child parents are exactly the boundary layer with odd count `q_L=b_L`.  If

\[
\beta_0(r),\beta_1(r)\in\{0,1\}
\]

are child-survival indicators, then

\[
m(r)=\beta_0(r)+\beta_1(r),
\qquad
v(r)=\beta_0(r)-\beta_1(r),
\]

and on a one-child parent

\[
m(r)=1,
\qquad
v(r)=\pm1.
\]

Therefore the selector count and Beatty one-child set are already attached to the same parent residue.

Status: **SAFE / no additional fibre-identification hypothesis is needed.**

---

## 4. Exact mass normalization

The same theorem defines

\[
\boxed{C_L=\sum_{r\in R_L}c(r)}
\]

and, at a Beatty rise,

\[
\boxed{D_L=
\sum_{\substack{r\in R_L\\m(r)=1}}c(r)},
\]

\[
\boxed{K_L=
\sum_{\substack{r\in R_L\\m(r)=1}}v(r)u(r)}.
\]

For a one-child parent the surviving selector count is exactly

\[
\frac{c(r)+v(r)u(r)}2.
\]

Hence

\[
\boxed{C_{L+1}=C_L-\frac{D_L}{2}+\frac{K_L}{2}.}
\]

All quantities are integer counts before the optional normalization by `2^d`.  In particular, `C_L<1 => C_L=0` is logically valid whenever `C_L` itself, rather than a normalized measure, is the object being bounded.

Status: **SAFE EXACT TRANSPORT.**

This does not by itself establish that a hypothetical minimal counterexample is among the selector assignments being counted.

---

## 5. Consequence: `F_map^coord` is closed

The previously open map gate should be split as

\[
\boxed{
F_{\rm map}
=
F_{\rm map}^{\rm coord}
+
F_{\rm map}^{\rm cover}.
}
\]

The coordinate part consists of:

1. same parent modulus;
2. same integer-to-residue map;
3. exact child lifts;
4. exact one-child Beatty boundary;
5. exact selector multiplicity;
6. exact normalization/transport.

Every item is already present in the existing mass-transport theorem.

Therefore

\[
\boxed{F_{\rm map}^{\rm coord}\ \textbf{CLOSED}.}
\]

---

## 6. Previous coverage input

The previous coverage reduction used Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471--480 (2025).

The paper defines

\[
F_n=
\bigcup_{a_0,\ldots,a_{n-1}\in\{0,1\}}
\left(
4\cdot3^n\mathbb N_0
+4\sum_{i=0}^{n-1}a_i3^i
+3
\right)
\]

and Lemma 3.1 claims that every `F_n` is recursively sufficient.  Lemma 3.2 then identifies their intersection with the ternary 0/1 Cantor core

\[
F=
\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 m\ge0,\ a_i\in\{0,1\}
\right\}.
\]

If every `F_n` were recursively sufficient, then their intersection would be recursively sufficient, and a hypothetical minimal counterexample would indeed have to lie in `F`.

The DSD audit must therefore inspect Lemma 3.1 itself rather than importing the conclusion as a black box.

---

## 7. Exact failure of the printed induction at `F_1 -> F_2`

Modulo `36`, the definitions give

\[
\boxed{F_1=\{3,7,15,19,27,31\}\pmod{36}},
\]

whereas

\[
\boxed{F_2=\{3,7,15,19\}\pmod{36}}.
\]

Therefore

\[
\boxed{
F_1\setminus F_2
=(36\mathbb N_0+27)
\cup
(36\mathbb N_0+31).
}
\]

The printed proof introduces an auxiliary `F'_n` and a recursive subset `A'_n`, then asserts

\[
F_{n+1}=F'_n\setminus A'_n.
\]

At `n=1`, the printed definitions give

\[
F'_1\pmod{36}
=\{3,7,11,15,19,23,27,31,35\},
\]

and

\[
A'_1\pmod{36}=\{35\}.
\]

Hence

\[
F'_1\setminus A'_1
\equiv
\{3,7,11,15,19,23,27,31\}
\pmod{36},
\]

which is **not** `F_2`.

Thus the equality closing the printed induction is false already at the first nontrivial induction step.

Status: **SAFE COUNTERCHECK OF THE PRINTED PROOF.**

This disproves the proof step, not necessarily the statement that every `F_n` is recursively sufficient.

---

## 8. One of the two missing classes is repairable exactly

For

\[
x=36k+31,
\]

put

\[
m=32k+27.
\]

Then

\[
m<x
\]

for every `k>=0`, and the shortcut Collatz map gives

\[
32k+27
\mapsto
48k+41
\mapsto
72k+62
\mapsto
36k+31.
\]

Therefore

\[
\boxed{36\mathbb N_0+31\text{ is recursive}.}
\]

The other removed progression is

\[
\boxed{36\mathbb N_0+27.}
\]

No universal smaller-merge theorem for this progression is established by the present audit.

Since `F_1` is recursively sufficient, the unresolved first coverage obligation can be isolated as

\[
\boxed{
36\mathbb N_0+27\text{ is recursive?}
}
\]

If that proposition were proved, `F_2` would be recursively sufficient.  Higher `F_n` would still require a corrected induction or separate proof.

Status: **31-class CLOSED / 27-class OPEN.**

---

## 9. Revised Gate-F status

After the harmonic moving-strip closure of growing-Q uniformity and the present coordinate audit,

\[
\boxed{
\begin{array}{ll}
F_{\rm heal}:&\textbf{CLOSED},\\
F_{\rm unif}:&\textbf{CLOSED for admissible logarithmic }Q(q),\\
F_{\rm map}^{\rm coord}:&\textbf{CLOSED},\\
F_{\rm map}^{\rm cover}:&\textbf{OPEN}.
\end{array}
}
\]

Thus Gate F is **not fully closed**.  Its surviving obstruction is no longer a dyadic/ternary coordinate mismatch.  It is a global covering theorem for minimal counterexamples.

---

## 10. Effect on existing finite certificates

The following objects remain exact without any coverage theorem:

- selector multiplicities `c_0(r),c_1(r)`;
- finite selector distributions;
- `C_L,D_L,K_L,U_L` transport identities;
- exact `m=44` survivor counts;
- Fourier identities and finite spectral calculations.

What changes is their interpretation.

They prove statements about the specified ternary selector family.  Until `F_map^cover` is repaired, they may not be promoted to statements covering every hypothetical minimal Collatz counterexample.

In particular:

\[
\boxed{
\text{exact selector contraction}
\not\Rightarrow
\text{minimal-counterexample elimination}
}
\]

without a valid coverage theorem.

---

## 11. DSD audit labels

### SAFE

1. `N=4Y+3` reduces depth `L` to `Y mod 2^(L-2)`.
2. The two child lifts are exactly `r` and `r+M`.
3. Existing `R_L`, one-child boundary, selector multiplicities, and `C_L,D_L,K_L` inhabit the same finite group.
4. The mass-transport identity is an exact integer-count identity.
5. The printed Ansari induction equality fails at `n=1` by explicit residue computation.
6. `36N_0+31` is recursive by the displayed affine merge.

### OPEN

1. `36N_0+27` recursive sufficiency obligation.
2. A corrected proof that all original `F_n` are recursively sufficient.
3. Any alternative theorem placing every hypothetical minimal counterexample in the infinite ternary 0/1 selector core.

### CONDITIONAL

Any use of the infinite ternary Cantor core as universal minimal-counterexample coverage is conditional on a repaired recursive-sufficiency theorem.

### PROHIBITED UPGRADES

1. Do not cite Ansari Lemma 3.1 as a verified coverage theorem without addressing the failed induction identity.
2. Do not discard the exact selector transport identities merely because coverage is open; coordinate algebra and global coverage are separate layers.
3. Do not infer that the ternary Cantor core is not recursively sufficient; only the published proof has been invalidated here.
4. Do not infer Collatz from any finite `m=44` selector exhaustion while coverage remains open.

---

## 12. Regression certificate

`collatz/src/ansari_recursive_sufficiency_induction_audit.py`

checks the exact residue mismatch and the affine recursion of the `31 mod 36` class.  The unresolved `27 mod 36` class is deliberately not guessed or numerically promoted.

---

## 13. Next proof target

The highest-value next target has changed.

Before investing further effort in selector flatness, the proof program should attempt one of:

### Route COV-1 — repair the original ternary spine

Prove the missing recursion of `36N_0+27`, then derive and audit the correct general removed layer `F_n\F_(n+1)` rather than the printed auxiliary equality.

### Route COV-2 — construct a different recursively sufficient family compatible with the same ternary selector coordinate

The replacement must preserve enough exact `3`-adic/ternary product structure that the existing selector Fourier and mass-transport machinery still applies.

### Route COV-3 — bypass recursive sufficiency

Derive the ternary selector restriction directly from minimal-counterexample dynamics or another independently verified theorem.

Until one route closes, `F_map^cover` remains the sole Gate-F obstruction.
