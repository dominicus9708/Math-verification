# Universal verified-floor parity spine and first Farey resonance

Date: 2026-09-06

Status: **SAFE LEMMA relative only to the external finite verification baseline `B0=2^71` + exact rational-log/Farey certificate**. This note does not use the disputed ternary recursive-sufficiency coverage and does not prove the Collatz conjecture.

## 1. Setup

Use the shortcut map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Let

\[
B_0=2^{71}.
\]

Take a hypothetical minimal positive counterexample `N>B0`.  Let `s_j` be the number of odd steps among the first `j` shortcut steps.

By minimality, every iterate on the orbit must remain at least `N`; otherwise a smaller positive iterate would converge and pull `N` into the convergent orbit.

At every odd state `x>=N>B0`,

\[
\frac{T(x)}x=\frac{3+1/x}{2}
<\frac{3+1/B_0}{2},
\]

whereas an even step contributes exactly `1/2`.  Hence for every `j>=1`,

\[
1\le\frac{T^j(N)}N
<\frac{(3+1/B_0)^{s_j}}{2^j}.
\]

Therefore

\[
\boxed{(3+1/B_0)^{s_j}>2^j}
\]

and, defining

\[
\beta(B_0)=\frac{\ln2}{\ln(3+1/B_0)},
\]

we obtain the universal prefix condition

\[
\boxed{\frac{s_j}{j}>\beta(B_0)\quad\text{for every }j\ge1.}
\]

This is a root-global minimal-counterexample condition.  No density interpretation is used.

## 2. Coarse rational recursively-sufficient spine

The exact integer inequality

\[
\boxed{(3B_0+1)^{306}<2^{485}B_0^{306}}
\]

implies

\[
\frac{306}{485}<\beta(B_0).
\]

Consequently any prefix with

\[
485s_j\le306j
\]

forces descent below its own start.  Thus every hypothetical minimal counterexample obeys

\[
\boxed{485s_j>306j\quad\text{for every prefix}.}
\]

This provides a parity-prefix recursively-sufficient spine independent of the ternary selector coverage.

## 3. First coefficient crossing produces an extremely narrow rational strip

Let

\[
\alpha=\log_3 2=\frac{\ln2}{\ln3}.
\]

At the first coefficient crossing, let `A` be the time and `q=s_A` the odd count.  The coefficient has just fallen below one, so

\[
3^q<2^A,
\qquad
\frac qA<\alpha.
\]

The minimality inequality from Section 1 simultaneously gives

\[
2^A<(3+1/B_0)^q,
\qquad
\frac qA>\beta(B_0).
\]

Hence every first coefficient crossing of a minimal counterexample must satisfy

\[
\boxed{\beta(B_0)<\frac qA<\alpha.}
\]

Equivalently, because `q=floor(alpha A)` at a crossing,

\[
\boxed{\{\alpha A\}<\bigl(\alpha-\beta(B_0)\bigr)A.}
\]

The strip width is approximately

\[
\alpha-\beta(B_0)\approx8.10747\times10^{-23},
\]

but the proof below uses only rational intervals.

## 4. Exact Farey isolation

Define

\[
r_L=\frac{6,586,818,670}{10,439,860,591},
\qquad
r_U=\frac{65,470,613,321}{103,768,467,013}.
\]

The accompanying rational-log certificate proves

\[
\boxed{r_L<\beta(B_0)<\alpha<r_U.}
\]

It also verifies the unimodular determinant

\[
65,470,613,321\cdot10,439,860,591
-
6,586,818,670\cdot103,768,467,013
=1.
\]

Thus `rL` and `rU` are Farey neighbors.  Every reduced rational strictly between them has denominator at least the sum of their denominators:

\[
10,439,860,591+103,768,467,013
=
\boxed{114,208,327,604}.
\]

Their mediant is

\[
\boxed{
\frac{72,057,431,991}{114,208,327,604}
}
\]

and the exact log intervals certify that this mediant lies inside the required strip.

Therefore every hypothetical minimal counterexample has first coefficient crossing time

\[
\boxed{A\ge114,208,327,604}
\]

and odd count

\[
\boxed{q\ge72,057,431,991}
\]

at the earliest possible crossing.

This conclusion uses `B0=2^71`, but does **not** use the Ansari ternary recursive-sufficiency bootstrap.

## 5. Exact cells through the previously isolated giant resonance

Because `(rL,rU)` is a unimodular basis, every reduced rational between them has a unique positive coprime representation

\[
\frac{a p_L+b p_U}{a q_L+b q_U}.
\]

Exhausting all such pairs with denominator at most

\[
217,976,794,617
\]

leaves exactly two rationals inside `(beta,alpha)`:

\[
\boxed{
(A,q)=
(114,208,327,604,
72,057,431,991)
}
\]

and

\[
\boxed{
(A,q)=
(217,976,794,617,
137,528,045,312).
}
\]

Thus, up to the old giant resonance, the universal `B0=2^71` branch contains exactly one additional cell below the formerly selector-conditional current cell.

The first cell is the same pair previously called the `first 72-bit resonance`.  Its old elimination used the stronger Ansari-extended floor `4*3^44+2`; after the coverage audit that elimination is **CONDITIONAL**, whereas its present isolation as the first universal cell is independent of that bootstrap.

## 6. Exact mixed-place dimensions of the two cells

For a fixed cell put

\[
D=2^A-3^q,
\qquad
\varepsilon=\frac D{3^q}.
\]

The dangerous-axis criterion is

\[
3^{q-i}\ge D
\iff
3^{-i}\ge\varepsilon.
\]

Rigorous comparisons of

\[
A\ln2-q\ln3
\]

with

\[
\ln(1+3^{-i})
\]

give

\[
\boxed{h=23}
\]

for the first universal cell and

\[
\boxed{h=25}
\]

for the giant cell.

For the buffered global co-order theorem, the minimal `B` satisfies

\[
D2^B>q3^{q-1}.
\]

Equivalently,

\[
\varepsilon>\frac q{3\,2^B}.
\]

The same exact log certificate gives

\[
\boxed{B=72}
\]

for the first cell and

\[
\boxed{B=76}
\]

for the giant cell.

Hence a paradoxical start in the first universal cell must satisfy

\[
\boxed{N<2^{72}.}
\]

Combined with the external verified baseline this confines that first cell to the one-bit start interval

\[
\boxed{2^{71}<N<2^{72}.}
\]

This is a logical localization, not a brute-force verification claim.

## 7. Reproducibility

Source:

`collatz/src/universal_verified_floor_parity_spine_farey_certificate.py`

The script uses only Python integer arithmetic and `fractions.Fraction`.

Logarithms are bounded by the convergent atanh expansion

\[
\ln x=2\sum_{k=0}^{n}\frac{z^{2k+1}}{2k+1}+R_n,
\qquad
z=\frac{x-1}{x+1},
\]

with explicit positive tail bound

\[
0<R_n
\le
\frac{2z^{2n+3}}{(2n+3)(1-z^2)}.
\]

No floating-point comparison enters any certificate assertion.

Expected output:

```text
PASS
B0 = 2361183241434822606848
first universal strip cell (A,q) = (114208327604, 72057431991)
cells through old giant resonance = [(114208327604, 72057431991), (217976794617, 137528045312)]
FIRST: h=23, B=72
SECOND: h=25, B=76
```

## 8. DSD audit status

### SAFE relative to external finite baseline

- minimal-counterexample prefix inequality `(3+1/B0)^s > 2^j`;
- rational spine `485s>306j`;
- first-crossing strip `beta<q/A<alpha`;
- Farey minimum `(A,q)=(114208327604,72057431991)`;
- exactly two strip cells through `A=217976794617`;
- cell dimensions `(h,B)=(23,72)` and `(25,76)`.

### External input

- ordinary Collatz verification below `B0=2^71`.

### CONDITIONAL only

- the older elimination of the first cell using `4*3^44+2`;
- the interpretation of `V33` as a continuous global floor;
- the former claim that the giant cell alone was the universal R1 residue.

### OPEN

The first universal cell must now be eliminated using root-global same-integer/minimality information inside

\[
2^{71}<N<2^{72},
\]

or by a stronger correction/renewal argument.  Repeated later-block Hensel/L7 maximality is not admissible for this purpose.
