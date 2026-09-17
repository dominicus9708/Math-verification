# MATH-183 — exact resolution-bit contraction criterion

Date: 2026-09-17

Status: `EXACT STRUCTURAL LEMMA / WELL-FOUNDEDNESS REDUCTION / r=10 CLOSURE OPEN`

## 1. Purpose

MATH-182 reduced the non-enumerative low-paid problem to exact affine cylinders whose non-descending members form one initial parameter prefix.

The next question is not how many ordinary starts are in that prefix. It is whether one can prove, from a small number of structural comparisons, that the unresolved **resolution height** strictly decreases.

This note gives such a criterion.

No paid-count layer is newly closed here.

## 2. Exact cylinder and master defect

Let

\[
N(s)=a+2^H s,
\qquad 0\le s<M,
\]

be one exact same-parity / same-affine source cylinder, and let

\[
R=\lceil\log_2 M\rceil.
\]

Assume

\[
\rho>1.
\]

The MATH-080 self-comparison defect is

\[
\boxed{
\mathfrak D(s)=S-N(s)(\rho-1).
}
\]

By MATH-072,

\[
S=1+\Sigma-\rho,
\]

so the same defect has the equivalent form

\[
\boxed{
\mathfrak D(s)
=\Sigma-(N(s)+1)(\rho-1).
}
\]

Thus `S` and `Sigma` are not separate terminal-risk coordinates.

## 3. Strict ordering along the source parameter

For fixed `(S,rho,a,H)`,

\[
\mathfrak D(s+1)-\mathfrak D(s)
=-2^H(\rho-1)<0.
\]

Hence the non-descending members

\[
\mathfrak D(s)\ge0
\]

form exactly one initial prefix

\[
0\le s<M_{bad}.
\]

This is the MATH-182 threshold structure.

## 4. One-bit contraction test

Assume `R>=1`. By the definition of `R`,

\[
2^{R-1}<M\le2^R.
\]

Therefore the midpoint parameter

\[
s_{1}=2^{R-1}
\]

is an actual member of the source range.

If

\[
\boxed{
\mathfrak D(2^{R-1})<0,
}
\]

then strict monotonicity gives

\[
M_{bad}\le2^{R-1}.
\]

Consequently

\[
\boxed{
R_{bad}:=\lceil\log_2 M_{bad}\rceil\le R-1,
}
\]

with the convention `R_bad=0` if `M_bad<=1`.

The midpoint condition may be written without evaluating the defect function:

\[
\boxed{
S<\bigl(a+2^{H+R-1}\bigr)(\rho-1).
}
\]

Using MATH-072, it is equivalently

\[
\boxed{
\Sigma<\bigl(a+2^{H+R-1}+1\bigr)(\rho-1).
}
\]

Thus a single exact rational comparison certifies the loss of at least one unresolved address bit.

## 5. Multi-bit contraction

More generally, let

\[
1\le t\le R
\]

and define

\[
s_t=2^{R-t}.
\]

Since `s_t<=2^(R-1)<M`, this is always a valid parameter index.

If

\[
\boxed{
\mathfrak D(s_t)<0,
}
\]

then

\[
M_{bad}\le2^{R-t}
\]

and therefore

\[
\boxed{
R_{bad}\le R-t.
}
\]

Equivalent exact tests are

\[
\boxed{
S<\bigl(a+2^{H+R-t}\bigr)(\rho-1)
}
\]

or

\[
\boxed{
\Sigma<\bigl(a+2^{H+R-t}+1\bigr)(\rho-1).
}
\]

Define the **resolution contraction credit**

\[
\boxed{
\kappa
:=
\max\left(
\{0\}
\cup
\left\{
1\le t\le R:
\Sigma<\bigl(a+2^{H+R-t}+1\bigr)(\rho-1)
\right\}
\right).
}
\]

Then universally

\[
\boxed{
R_{bad}\le R-\kappa.
}
\]

No ordinary-source enumeration occurs in this test.

## 6. Relation to MATH-074

MATH-074 already proves that a legal symbolic edge with shortcut length `ell<=R` is Bellman-safe under

\[
H_R=-\frac{19}{503}R.
\]

It also gives

\[
R'\le\max(0,R-\ell).
\]

Therefore there are two different, compatible ways in which resolution decreases:

1. **symbolic congruence consumption:** a legal macro uses dyadic resolution before singleton handoff;
2. **orbit-gap threshold contraction:** at a `rho>1` crossing, an entire descending suffix is deleted and only a smaller bad prefix remains.

The first is controlled by MATH-074; the second by the present `kappa` criterion.

## 7. Candidate well-founded measure

For `R>=1`, a uniform lower bound

\[
\boxed{\kappa\ge1}
\]

at every legal residual terminal handoff would imply strict decrease of the integer coordinate `R`.

Since the pre-first-cell source bound gives

\[
R\le73,
\]

such a theorem would permit at most 73 nontrivial resolution-handoff contractions along one same-integer lineage before `R=0`.

This does **not** by itself finish the proof, because the terminal singleton case `R=0` remains a separate obligation.

The DSD decomposition is therefore now:

\[
\boxed{
R\ge1:
\text{ prove }\kappa\ge1
\qquad\text{and}\qquad
R=0:
\text{ prove direct singleton descent / incompatibility.}
}
\]

This is strictly sharper than the earlier request to prove an opaque lexicographic decrease on `(R,M_bad,remaining depth)`.

## 8. Exact `r=10` theorem target

For the `r=10` critical compatibility classes, the desired non-enumerative theorem can now be stated as two claims.

### A. Multi-source contraction

For every legal exact-compatible `r=10` residual state with `R>=1`, at the relevant first `rho>1` handoff,

\[
\boxed{
\Sigma<\bigl(a+2^{H+R-1}+1\bigr)(\rho-1).
}
\]

Equivalently,

\[
\boxed{\kappa\ge1.}
\]

### B. Singleton terminal closure

For every exact-compatible residual state with `R=0`,

\[
\boxed{
\mathfrak D(0)
=\Sigma-(a+1)(\rho-1)<0
}
\]

or the state is excluded by an exact compatibility/dominance condition already present in the audited address channel.

If both A and B are established for a future-complete transition system, the `r=10` layer closes without enumerating its ordinary source anchors.

## 9. Why this is stronger than source sharding

The MATH-115/MATH-176 path asks whether every one of 278,725 AP source records eventually closes.

The present target asks instead whether all legal states satisfy one midpoint inequality plus one singleton terminal inequality.

The source files then become regression witnesses for the theorem, not theorem premises.

## 10. DSD audit boundary

Established:

- exact defect identity in both `(S,rho)` and `(Sigma,rho)` coordinates;
- exact monotone ordering of a fixed affine cylinder for `rho>1`;
- one midpoint comparison implies one-bit resolution contraction;
- the general `t`-bit criterion and contraction credit `kappa`;
- a reduction of the well-foundedness target to `kappa>=1` for `R>=1` plus a separate `R=0` terminal theorem.

Not established:

- uniform `kappa>=1` for all legal `r=10` states;
- the singleton terminal theorem;
- `r=10` closure;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

Companion exact-rational regression:

`collatz/src/2026_09_17_math183_resolution_bit_contraction_certificate.py`
