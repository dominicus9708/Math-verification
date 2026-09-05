# Pure-ballot correction-language recursion

Status: **EXACT / CLOSED as a language recursion**

## 1. Domain

Let

\[
Q(0)=0,
\]

and for `n>=1` let `Q(n)` be the least integer `q` such that

\[
3^q>2^n.
\]

Equivalently, for positive `n`,

\[
Q(n)=\lceil n\log_3 2\rceil.
\]

Fix an already legal pure-ballot state at absolute depth `h` with surplus

\[
S=q_0-Q(h)\ge0,
\qquad
q_0=Q(h)+S.
\]

For a binary suffix word `W` of length `n` containing exactly `p` ones, write its one-positions as

\[
0\le a_1<\cdots<a_p<n.
\]

Its ordinary accelerated-Collatz correction is

\[
C(W)=\sum_{r=1}^{p}3^{p-r}2^{a_r}.
\]

Define the pure-ballot correction language

\[
\mathcal C^{\mathrm{bal}}_{n,p}(h,S)
\]

to be the set of all such corrections for which every suffix prefix of length `t`, `1<=t<=n`, obeys

\[
q_0+\#_1(W_{<t})\ge Q(h+t).
\]

This theorem concerns this exact finite language only. It does not by itself impose endpoint, checkpoint, debit, H/L-history, C4F, or physical predicates.

## 2. Zero-one terminal case

If `p=0`, the suffix is forced to be `0^n`. Since `Q` is nondecreasing, all prefix ballot inequalities are equivalent to the last one. Hence

\[
\boxed{
\mathcal C^{\mathrm{bal}}_{n,0}(h,S)
=
\begin{cases}
\{0\},&S\ge Q(h+n)-Q(h),\\
\varnothing,&\text{otherwise}.
\end{cases}
}
\]

This includes `n=0`, where the empty suffix contributes correction `0`.

## 3. Exact first-one recursion

Assume `1<=p<=n` and let `a` be the first one-position. Necessarily

\[
0\le a\le n-p.
\]

The forced prefix is `0^a1`. By the closed valuation-jump ballot theorem, this block is legal exactly when

\[
S\ge Q(h+a)-Q(h)
\]

and

\[
S+1\ge Q(h+a+1)-Q(h).
\]

For a legal `a`, define

\[
h'=h+a+1,
\]

\[
S'=S+1-\bigl(Q(h')-Q(h)\bigr).
\]

Writing the remaining one-positions as

\[
a+1+b_1<\cdots<a+1+b_{p-1},
\]

the correction splits exactly as

\[
C(W)
=
3^{p-1}2^a
+
2^{a+1}
\sum_{j=1}^{p-1}3^{p-1-j}2^{b_j}.
\]

Therefore

\[
\boxed{
\mathcal C^{\mathrm{bal}}_{n,p}(h,S)
=
\bigcup_{a\in A_{n,p}(h,S)}
\left(
3^{p-1}2^a
+
2^{a+1}
\mathcal C^{\mathrm{bal}}_{n-a-1,p-1}(h',S')
\right),
}
\]

where `A_{n,p}(h,S)` is precisely the set of integers `a` satisfying

\[
0\le a\le n-p
\]

and the two ballot inequalities above.

The recursion is exact in both directions: every legal word enters exactly one branch, and every recursively generated branch concatenates to a legal word with exactly `p` ones.

## 4. The union is disjoint

For `p>0`, if `a=a_1` is the first one-position, then

\[
C(W)
=
2^a\left(3^{p-1}+2K\right)
\]

for an integer `K`. The factor in parentheses is odd. Hence

\[
\boxed{v_2(C(W))=a_1.}
\]

Consequently two different first-one branches cannot contain the same correction value. The displayed union is a disjoint union.

At fixed `(n,p)`, the previously certified correction decoder further implies that each correction identifies the entire parity word uniquely.

## 5. Unrestricted language and extrema

If the ballot restriction is removed, define

\[
\mathcal C_{n,p}
=
\left\{
\sum_{r=1}^{p}3^{p-r}2^{a_r}:
0\le a_1<\cdots<a_p<n
\right\}.
\]

The same first-one decomposition gives

\[
\mathcal C_{n,p}
=
\bigsqcup_{a=0}^{n-p}
\left(
3^{p-1}2^a+2^{a+1}\mathcal C_{n-a-1,p-1}
\right).
\]

For `p>0`, monotonicity of the weighted atoms gives

\[
\boxed{C_{\min}=3^p-2^p,}
\]

attained at positions `0,1,...,p-1`, and

\[
\boxed{C_{\max}=2^{n-p}(3^p-2^p),}
\]

attained at positions `n-p,...,n-1`.

Because fixed-`(n,p)` correction decoding is injective,

\[
|\mathcal C_{n,p}|=\binom np.
\]

## 6. Exact equivalence to residual valuation decoding

Suppose an exact residual/correction requirement `R` with remaining one-count `p>0` is given. Membership in the language forces

\[
a=v_2(R).
\]

After selecting this unique possible first branch, the remaining required correction is

\[
\boxed{
R'
=
\frac{R-3^{p-1}2^a}{2^{a+1}}.
}
\]

This is exactly the residual valuation-jump decoder restart. The ballot language recursion merely adds the already certified `(h,S,a)` legality gates before the same restart.

Thus, for an exact endpoint pair, recursive language membership and repeated residual valuation decoding are two presentations of the same exact information.

For an affine source family, splitting by the possible values of `v_2(R)` induces the same first-one residue partition that underlies the affine valuation-cylinder `0^a1` transition.

## 7. S10 consequence and non-independence warning

The exact language is reusable and can support an emptiness test of the form

\[
\mathcal R\cap\mathcal C^{\mathrm{bal}}_{n,p}(h,S)=\varnothing,
\]

provided an independently justified required-correction set `\mathcal R` is available at the same observation stage.

However, **materializing or recursively expanding the language branch by branch is not a new S10 contraction engine**. Without a stronger compressed representation or an additional active predicate, it reproduces the already certified valuation/residual refinement tree.

Therefore it is forbidden to count

- correction-language membership,
- residual valuation decoding, and
- valuation-cylinder branching

as independent pruning factors.

The open research target is a compressed exact representation (for example, a certified interval-gap, residue, automaton, or other quotient) that can decide useful whole-family disjointness without reconstructing the same valuation tree.

## 8. Scope

Closed here:

- exact unrestricted first-one correction recursion;
- exact pure-ballot restricted recursion;
- all-zero terminal condition;
- disjointness by `v_2`;
- exact algebraic equivalence to the residual first-one restart.

Not closed here:

- a horizon-independent compact representation of the language;
- whole-current-Route-B source-cylinder rejection from this language alone;
- checkpoint/debit compatibility;
- same-orbit provenance;
- Route-B, A0, or global Collatz closure.

## Certificate

- `../src/A0_s1_pure_ballot_correction_language_recursion_certificate.py`
