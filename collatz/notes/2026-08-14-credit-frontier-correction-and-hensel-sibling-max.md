# Credit-frontier correction, denominator absorption, and Hensel sibling-max reduction

Date: 2026-08-14

Status: **logical correction + exact algebraic theorems + finite exact certificates**.  This note supersedes the earlier interpretation that a greedy maximum predecessor-credit chain is a well-founded candidate potential.  The local arithmetic identities in the earlier credit/handoff notes remain valid, but the global interpretation is corrected here.  Nothing in this note proves the Collatz conjecture.

## 1. Correction of the greedy-credit interpretation

A predecessor credit is a relation between one actual suffix and one alternate suffix.  If a right suffix `V` has a set of ordinary integer predecessor relations

\[
\mathcal C(V)\subset\mathbb Z_{\ge0},
\qquad 0\in\mathcal C(V),
\]

then prepending an actual left word `w` of length `L` and odd count `q` does **not** propagate only the largest member of `C(V)`.

For every alternate left word `u` with the same `L,q`, an incoming relation `delta` gives

\[
\boxed{
\delta'
=\frac{R_u-R_w+2^L\delta}{3^q}
}
\]

whenever the numerator is a positive multiple of `3^q`.

Thus the correct integer relation state is set-valued.  Retaining only the largest credit can delete smaller relations which survive a later block.

The previously recorded local type-17 statement

\[
148\longrightarrow\frac{440}{3}
\]

is still exact for that **one** incoming relation.  What is withdrawn is the stronger interpretation that every admissible relation state is forced through that handoff.

Exact finite diagnostics retaining all integer credits show that the integer relation set remains nonempty on the tested reachable length-19 contexts even when the greedy maximum relation fails.

## 2. Denominator absorption theorem

Suppose an incoming normalized alternate displacement is already nonintegral in reduced form

\[
\delta=\frac{a}{3^d},
\qquad d>0,
\qquad 3\nmid a.
\]

Prepend a left block `U` of length `L_U`, odd count `q_U`, and integer correction difference `D_U`.  The new displacement is

\[
\boxed{
\delta'
=\frac{3^dD_U+2^{L_U}a}{3^{q_U+d}}.
}
\]

Because `d>0`,

\[
3^dD_U\equiv0\pmod3,
\]

whereas

\[
2^{L_U}a\not\equiv0\pmod3.
\]

Hence

\[
\boxed{
v_3(3^dD_U+2^{L_U}a)=0.
}
\]

Therefore the reduced denominator exponent is exactly

\[
\boxed{d'=d+q_U.}
\]

### Consequence

Once a left-concatenated alternate displacement becomes nonintegral, no further left concatenation by integer correction blocks can make it integral again.

Thus, for the specific objective

> construct an ordinary smaller predecessor at the original start,

nonintegral branches are absorbing failure branches and may be dropped from the **integer-predecessor** recursion.  They remain relevant to the separate rational-grid / late-lift channel.

## 3. Credit is not a well-founded rank

For the length-19 neutral-factor quotient, retain all possible integer credits rather than only a greedy maximum.

The exact phase geometry of the mechanical slope

\[
\alpha=\log_3 2
\]

under a 19-step predecessor shift has increment

\[
\varepsilon=12-19\alpha.
\]

The length-19 factor intervals have only three widths:

\[
\varepsilon,
\qquad
S=8\alpha-5,
\qquad
L=7-11\alpha.
\]

Using the rational bounds

\[
\frac{41}{65}<\alpha<\frac{53}{84}
\]

gives

\[
\boxed{3\varepsilon<S<4\varepsilon,}
\qquad
\boxed{4\varepsilon<L<5\varepsilon.}
\]

Hence the possible consecutive dwell counts are exactly:

- type 0: `1`;
- short types: `3` or `4`;
- long types: `4` or `5`.

Allowing those dwell choices independently gives a strict over-approximation of the true Sturmian context process.

Starting from the previously certified incoming credit `30`, this over-approximation reaches a finite fixed credit set

\[
\boxed{
\mathcal C_*:
\quad |\mathcal C_*|=234,
\quad \min\mathcal C_*=7,
\quad \max\mathcal C_*=397.
}
\]

A full over-approximated phase cycle satisfies

\[
\boxed{F(\mathcal C_*)=\mathcal C_*.}
\]

Moreover the directed relation on these 234 credits induced by a full cycle has one strongly connected component containing all 234 states.

Thus integer credit is a **bounded recurrent internal channel**, not a well-founded proof potential.

This is a negative structural result: any proof program requiring predecessor credit to grow without bound must be abandoned at this quotient.

## 4. Low-bit divisibility of neutral credit

Let a mechanical neutral factor begin with `r` consecutive ones.  Any actual orientation with relative state

\[
(\Sigma,M)=(0,0)
\]

must share those first `r` ones; otherwise the relative height becomes negative immediately.

For fixed total odd count, their contributions to correction below bit `r` are therefore identical.  Hence for any two such neutral orientations

\[
\boxed{2^r\mid(R_u-R_w).}
\]

For a length-19 block, `2^19 delta` is also divisible by `2^r`, and every integer output credit obeys

\[
\boxed{2^r\mid\delta'.}
\]

This explains the observed phase-dependent credit lattices:

- types 0--7: no forced power of two;
- types 8--14: output credits are even;
- types 15--19: output credits are multiples of four.

## 5. Exact Hensel sibling-max theorem for the binary integerization sieve

Consider same-length, same-odd-count parity words `w,u` of length `L` and odd count `q`.  Put

\[
C=R_u-R_w>0,
\qquad
s=v_3(C)<q,
\qquad
d=q-s.
\]

Write the odd positions of `u` as

\[
p_1<\cdots<p_q
\]

with zero-based time positions.  The correction is

\[
R_u=\sum_{j=1}^q2^{p_j}3^{q-j}.
\]

Modulo `3^(s+1)`, every term with `j<d` vanishes because

\[
q-j\ge s+1.
\]

Therefore

\[
\boxed{
R_u\bmod3^{s+1}
}
\]

depends only on the last `s+1` odd positions

\[
\boxed{p_d,p_{d+1},\ldots,p_q.}
\]

The denominator-clearing / contraction test also depends on the first of these positions, namely the `d`-th odd time.

### Tail-max witness

Fix this tail.  Among all choices of the earlier `d-1` odd positions, the full correction is maximized by moving every earlier odd as far right as the order constraint permits:

\[
\boxed{
p_j=p_d-d+j\qquad(1\le j<d).}
\]

This move:

1. preserves `R_u mod 3^(s+1)`;
2. preserves the `d`-th odd time;
3. preserves the contracting integerization test;
4. weakly increases the full correction.

Hence every removing alternate witness with `s<q` can be replaced by a canonical **tail-max witness** with the same exact 3-adic valuation against `w` and no weaker correction advantage.

## 6. Sibling-max formulation

For fixed `L,q,s`, let `U_{q,s}` be the alternate words whose `d=q-s`-th odd prefix is contracting.  For each residue modulo `3^(s+1)` define

\[
\boxed{
M_{q,s}(r)
=
\max\{R_u:
 u\in U_{q,s},
 R_u\equiv r\pmod{3^{s+1}}\}.
}
\]

For a candidate correction `R_w`, put

\[
r_0=R_w\bmod3^s
\]

and let `a_w` be its next ternary digit modulo `3^(s+1)`.

Exact valuation `v_3(R_u-R_w)=s` means the lower `s` digits agree and the next digit differs.  Therefore the entire pairwise search at valuation `s` is equivalent to the single condition

\[
\boxed{
\max_{a\in\{0,1,2\}\setminus\{a_w\}}
M_{q,s}(r_0+a3^s)
>R_w.
}
\]

The immediate-integer case `3^q | (R_u-R_w)` is handled analogously by the maximum correction in the same residue modulo `3^q`.

Thus the exact binary alternate-predecessor sieve is a **3-adic Hensel sibling-max computation**, not intrinsically a quadratic word-pair computation.

## 7. Safe large-start simplification through depth 25

For the current `m=44` search, the certified lower start exceeds `3.9e21`.

When the denominator-clearing prefix is contracting,

\[
2^{t_d}>3^d,
\]

the correction before integerization obeys the crude bound

\[
R_{u,d}<2^{t_d}\frac{3^d}{2}<2^{2L-1}.
\]

Hence for the finite depths used below the large-start threshold in the exact integerization theorem is automatically far below the certified `N_min`.

The sibling-max test therefore reproduces the full exact pairwise sieve at depth 20 and extends it without changing the mathematical condition.

## 8. Exact finite extension

The exact sibling-max verifier gives:

\[
\boxed{
\begin{array}{c|r|r|r|c}
L&\text{surviving}&\text{removed}&\text{retained}&\text{removed fraction}\\\hline
20&27,328&11,458&15,870&0.419276932084309\\
21&46,611&18,464&28,147&0.396129668962262\\
22&93,222&41,046&52,176&0.440303790950634\\
23&168,807&70,829&97,978&0.419585680688597\\
24&286,581&113,713&172,868&0.396791831977696\\
25&573,162&251,141&322,021&0.438167568680408
\end{array}
}
\]

The depth-20 value exactly matches the earlier quadratic alternate-word certificate.

The oscillation also supplies a negative strategic result: no monotone approach to 100% removal is visible in this finite sequence, so the sieve should be treated as one hierarchical filter rather than extrapolated as a standalone convergence proof.

## 9. Decomposition of the depth-20 elimination

At depth 20 the exact removal counts by final odd count are

\[
\begin{array}{c|r|r}
q&\text{surviving}&\text{removed}\\\hline
13&8045&4871\\
14&9592&3909\\
15&6167&1916\\
16&2595&619\\
17&760&128\\
18&150&15
\end{array}
\]

The direct integer-start collision `3^q | C` accounts for a substantial part of this finite removal, while the remaining part is supplied by the Hensel sibling levels `s<q`.

Thus the tail-max theorem compresses all partial-integerization witnesses, while the full-residue `s>=q` channel remains a separate exact max-residue problem.

## 10. Correct proof-program target

The current hierarchy should therefore be read as follows.

1. Scalar predecessor credit is not a proof rank; it is a bounded recurrent relation coordinate at the length-19 quotient.
2. Nonintegral denominator branches are absorbing for the objective of recovering an integer predecessor at a still earlier original start.
3. A fixed actual candidate is an **adversarial coverage problem**: it must choose parity orientations avoiding every available integerizing alternate relation.
4. Equal-state neutral collisions alone admit symbolic local-max choices and therefore cannot close R2.
5. The stronger all-same-`q` integerization sieve is exactly representable by Hensel sibling maxima and canonical tail-max witnesses.
6. The remaining global obstruction must combine this hierarchical 3-adic coverage with same-integer dyadic address stabilization / late-lift rigidity and the real headroom channel.

The next natural state is therefore not a scalar credit but a max-plus/Hensel coverage state carrying

\[
\boxed{
(\text{return phase},\ \Sigma,M,\ \text{3-adic sibling maxima},\ \text{dyadic canonical prefix},\ \text{headroom/excess}).
}
\]

This preserves the user's intended set-level proof architecture while removing two now-falsified scalar shortcuts.
