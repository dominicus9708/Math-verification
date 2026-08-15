# R1 finite mixed-filter projection barrier

Date: 2026-08-15

Status: **exact finite mixed-place diagnostic + proof-strategy limitation**. This note combines the current renewal-gap bound, ternary Cantor fibres, start-side Hensel filtering, endpoint contracting-backtrace cylinders, and record-admissible suffixes. The combined finite filters still leave the full low-ternary projection. Therefore the missing information is the same-word affine/canonical-address bridge between the start and the final suffix. This does not prove Collatz.

Use the unique current R1 coefficient pair

\[
(A,H)=(217,976,794,617,137,528,045,312)
\]

and the `m=44` recursively-sufficient core

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

The certified companion gap theorem gives

\[
0<g<30,265,456,191,
\qquad g=4k,
\]

so

\[
\boxed{1\le k\le7,566,364,047<3^{21}.}
\]

## 1. Gap localization at every ternary depth Q >= 22

For every `Q` with `22<=Q<=44`, put

\[
S_Q=\sum_{i=0}^{Q-1}a_i3^i\in C_Q.
\]

The final `Q` odd-event suffix determines the endpoint residue

\[
Y_Q\equiv N+g\pmod{3^Q}.
\]

After normalizing by four,

\[
Z_Q:=4^{-1}(Y_Q-3)\equiv S_Q+k\pmod{3^Q}.
\]

Because `k<3^21`, compatible `S_Q` lie in one cyclic interval of length `<3^21`.

### Uniform Cantor interval lemma

For every `Q>=22`, every cyclic interval of length `<3^21` contains at most

\[
\boxed{2^{21}}
\]

points of `C_Q`.

Indeed, split `C_Q` into copies of `C_21` according to digits `a_21,...,a_{Q-1}`. Consecutive copy anchors differ by at least `3^21`, while each copy itself lies in an interval of width `(3^21-1)/2`. An interval shorter than `3^21` can meet at most the tail of one copy and the head of the next relevant copy; after translation these are disjoint subsets of one `C_21`, so their total cardinality is at most `2^21`.

Hence every fixed final-`Q` suffix fibre satisfies

\[
\boxed{|\text{compatible }S_Q|\le2^{21}.}
\]

At `Q=44` this is a fibrewise contraction from `2^44` starts to at most `2^21`, i.e. a factor `2^-23`.

## 2. Record-only suffixes erase the global gain

The fibre contraction is not global under the record condition alone.

For every full ternary coordinate

\[
S\in C_{44},
\]

choose simply

\[
k=1,\qquad g=4.
\]

Then

\[
Y\equiv4(S+1)+3\pmod{3^{44}}.
\]

Since `S mod 3` is either `0` or `1`, `Y mod 3` is either `1` or `2`; hence `Y` is a 3-adic unit.

The companion suffix-unit-surjectivity theorem applies at arbitrary finite depth, so there exists a record-admissible 44-odd valuation suffix realizing this unit endpoint residue.

Therefore the nested gap constraints for all `Q=22,...,44`, together with the coefficient-record condition, still admit every `S in C_44` in a local over-approximation.

## 3. Exact start-side Hensel weighted-fibre audit

To test whether an early dyadic minimality filter breaks the gap fibre, use the audited Hensel sibling-max retained start residues.

For a fixed low-22 ternary coordinate `S`, aggregate over the upper 22 selectors `a_22,...,a_43`. Let `w_L(S)` be the number of upper-selector assignments whose start residue survives the depth-`L` Hensel filter.

The upper-selector subset-sum distribution modulo `2^(L-2)` and the retained-residue indicator were combined by an exact cyclic NTT modulo `998244353`.

Using the already-certified safe gap interval length `k<=7,566,364,047`, the exact weighted maxima are:

\[
\boxed{\begin{array}{c|r|r|c}
L&W_{\rm total}&W_{\rm max\ gap\ fibre}&W_{\max}/W_{\rm total}\\\hline
20&1,065,017,122,841&532,508,636,837&0.500000070812477\\
24&725,060,335,093&362,530,194,479&0.500000037145185\\
25&675,326,540,210&337,663,290,657&0.500000030432685
\end{array}}
\]

At all three depths the maximizing interval starts at

\[
\boxed{S=3^{21},}
\]

so it essentially selects the `a_21=1` half-copy of `C_22`.

At depth 25 the pointwise weights satisfy

\[
\boxed{159,293\le w_{25}(S)\le162,464}
\]

for **every** `S in C_22`. Thus the low-22 projection of the start-side Hensel survivors is still all of `C_22`.

The near-`1/2` weighted fibre ratios show that the fixed early dyadic Hensel filter is almost perfectly uncorrelated with the final gap-Cantor half at these depths.

## 4. Endpoint contracting-backtrace cylinders through Q=16

For an exact odd reverse depth `q`, write the exponents as

\[
k_i=1+e_i,\qquad e_i\ge0.
\]

Contraction requires

\[
\sum_i e_i\le\lfloor q\log_2(3/2)\rfloor.
\]

Enumerate every contracting reverse code of depths `1,...,Q`, convert each to its unique forbidden endpoint residue modulo `3^q`, and lift those cylinders to modulus `3^Q`.

The allowed unit fractions are:

\[
\boxed{\begin{array}{c|c|c}
Q&\text{allowed unit fraction}&\max_{S\in C_Q}\min k\\\hline
8&0.3052\ldots&9\\
10&0.3031\ldots&9\\
12&0.3003\ldots&15\\
14&0.2995\ldots&15\\
16&0.2991169989\ldots&18
\end{array}}
\]

The last column is computed after normalizing endpoint residues by

\[
Z=4^{-1}(Y-3).
\]

It says that for every ternary Cantor point `S in C_Q`, there is an endpoint residue avoiding **all** contracting backtrace cylinders of depth at most `Q` at a positive distance

\[
1\le k\le18
\]

when `Q=16`.

Thus every low-16 ternary start can avoid all endpoint contracting reverse ancestors through depth 16 using a renewal gap

\[
\boxed{g=4k\le72,}
\]

which is negligible compared with the certified current gap allowance.

## 5. Combined finite projection countermodel

Fix any low-22 ternary coordinate `S in C_22`.

1. Section 3 gives at least `159,293` choices of the upper 22 ternary selectors for which the resulting start passes the depth-25 Hensel filter.
2. The low 16 digits of the same `S` admit a `k<=18` for which the normalized endpoint avoids every contracting-backtrace cylinder through depth 16.
3. The resulting endpoint is a 3-adic unit.
4. The record-surjectivity theorem supplies a record-admissible 44-odd suffix realizing that endpoint residue.
5. The gap is only `g<=72`, far inside the current R1 gap bound.

Therefore the over-approximated finite constraint system

\[
\boxed{
\text{depth-25 start Hensel}
+\text{small renewal gap}
+\text{record-admissible final suffix}
+\text{endpoint backtrace through depth 16}
}
\]

still projects onto **all** of `C_22`.

This does **not** construct an actual Collatz orbit satisfying the combined conditions, because the independently chosen start cylinder and final suffix have not been required to be the two ends of the **same full affine parity word**.

That missing condition is exactly the point.

## 6. Strategic consequence

The next R1 proof object should not be another stronger left-only or right-only finite filter. The surviving over-approximation is already extremely permissive despite strong local deletion on both sides.

The missing channel is

\[
\boxed{
\text{same-word affine / canonical-address consistency}
}
\]

between the start and the final suffix.

Equivalently, after splitting the current resonance into a start prefix, a long middle block, and a final odd suffix, one must preserve a state that ties together

- the start's dyadic canonical residue;
- the middle affine correction/carry;
- the final suffix's 3-adic endpoint residue;
- and the small ordinary renewal gap.

This is a stronger diagnosis than any single-filter percentage: the current obstruction is a **bridge-consistency problem**, not a lack of local pruning.
