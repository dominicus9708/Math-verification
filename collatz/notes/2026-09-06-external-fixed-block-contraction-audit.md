# External audit — fixed block / single-halving contraction claims

Date: 2026-09-06

Status: **ROOT WINDOW CLAIM FALSE AS A UNIVERSAL STATEMENT.**

This note audits recent Collatz manuscripts that attempt to prove deterministic global contraction from a fixed bound on consecutive accelerated odd steps with

\[
\nu_2(3n+1)=1.
\]

The exact scope is the fixed-window valuation lemma.  Any additional potential-function theorem in a particular manuscript must be audited separately from its full statement.

## 1. Accelerated odd map

For odd `n`, write

\[
U(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
\]

A `single-halving` accelerated step is one with

\[
\nu_2(3n+1)=1,
\]

so

\[
S(n)=\frac{3n+1}{2}.
\]

## 2. Exact countdown identity

If `n≡3 mod 4`, then `\nu_2(3n+1)=1`.  Moreover

\[
S(n)+1
=\frac{3n+1}{2}+1
=\frac{3(n+1)}2.
\]

Since `3` is odd,

\[
\boxed{
\nu_2(S(n)+1)=\nu_2(n+1)-1.
}
\]

Thus every single-halving step decrements the valuation `\nu_2(n+1)` by exactly one until it reaches `1`.

## 3. Unbounded family of single-halving runs

Take

\[
n_0=2^r-1.
\]

Then

\[
\nu_2(n_0+1)=r.
\]

Applying the countdown identity repeatedly gives exactly

\[
\boxed{r-1}
\]

consecutive accelerated odd steps satisfying

\[
\nu_2(3n_j+1)=1.
\]

Only after those `r-1` steps is a valuation at least `2` forced.

Hence the lengths of pure single-halving runs are unbounded.

## 4. Explicit K=21 counterexample

Set

\[
r=22,
\qquad
n_0=2^{22}-1=4,194,303.
\]

Then there are exactly

\[
\boxed{21}
\]

consecutive accelerated odd steps with valuation exactly one.

Therefore any statement of the form

\[
\boxed{
\text{every block of 21 consecutive accelerated odd steps contains a step with }\nu_2(3n+1)\ge2
}
\]

is false.

More generally, no fixed universal `K` can have this property: choose `r>K`.

## 5. DSD implication

A finite graph modulo `2^m` can have a maximum path depth of order `m`, but that does not yield one `m`-independent physical window bound on the full integers.

The parameter controlling the run is itself

\[
\nu_2(n+1),
\]

which is unbounded over positive integers.

Thus the invalid upgrade is

\[
\boxed{
\text{finite-quotient depth bound depending on }m
\not\Rightarrow
\text{fixed universal block length }K.
}
\]

This is a direct DSD `finite/growing parameter` failure mode.

## 6. Relation to current internal work

The internal Beatty/Hamming macro analysis never assumes a universal bound on runs of valuation one.  Indeed the neutral symbolic boundary and `00`-free/Hensel diagnostics explicitly retain arbitrarily long structured parity segments.

The external failure is therefore a useful regression test: any future internal block contraction must carry its dependence on the current dyadic valuation/state rather than replacing it by a global fixed constant.

## 7. Reproducibility

Source:

`collatz/src/external_fixed_block_single_halving_counterexample.py`

The script verifies the exact `K=21` example and the family through representative `r`, while the algebra above proves the result for every `r>=2`.

## 8. Verdict

\[
\boxed{
\text{FIXED UNIVERSAL SINGLE-HALVING WINDOW: REJECTED.}
}
\]

This does not by itself adjudicate every theorem in any manuscript containing such a lemma.  Downstream claims that rely essentially on the fixed-window lemma must, however, be reopened.
