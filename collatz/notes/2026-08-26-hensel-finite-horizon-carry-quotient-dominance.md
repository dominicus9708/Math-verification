# Finite-horizon Hensel carry quotient and Pareto dominance

Date: 2026-08-26

Status: **exact finite-horizon state-reduction lemma.** This is a state-compression tool for the two-boundary min-plus program. It does not prove the Collatz conjecture.

## 1. Hensel transition

At a fixed mechanical phase, a zero-target prepend with displacement d has

\[
K'={K+2^{e-d}\over3},
\]

when the numerator is divisible by 3.  The ordering state is the previous earliest displacement `p`; across mechanical gap `g` the new action must satisfy

\[
d\ge\max\{0,p-g+1\}.
\]

## 2. Finite-horizon carry quotient

Suppose exactly r further Hensel digits remain.  Let two current carries satisfy

\[
\boxed{K_1\equiv K_2\pmod{3^r}.}
\]

Apply the same admissible displacement sequence to both states.  After i steps,

\[
\boxed{
K_i^{(1)}-K_i^{(2)}={K_1-K_2\over3^i}.
}
\]

Hence for every `0<=i<r`,

\[
K_i^{(1)}\equiv K_i^{(2)}\pmod{3^{r-i}},
\]

and in particular the two states have the same residue modulo 3 at every decision point.

Therefore over an r-step future:

- the same displacement parity is required at each step;
- divisibility by 3 succeeds or fails simultaneously;
- the next-carry unit/nonunit test agrees whenever continuation is required.

Thus **K modulo `3^r` is a complete carry quotient for r future Hensel digits**.

## 3. Ordering dominance

Consider two states at the same mechanical boundary with

\[
K_1\equiv K_2\pmod{3^r},
\qquad
p_1\le p_2.
\]

Any first action feasible from `p_2` obeys

\[
d\ge\max\{0,p_2-g+1\}
\ge
\max\{0,p_1-g+1\},
\]

so it is also feasible from `p_1`.  After taking the same first action, both ordering memories become the same new value `d`; subsequent ordering constraints are identical.

Hence the smaller-p state has a superset of all r-step continuations available to the larger-p state.

## 4. Min-plus Pareto pruning

If the two states also carry accumulated real costs `C_1,C_2` with

\[
C_1\le C_2,
\]

then state 1 dominates state 2 for every common r-step continuation:

\[
\boxed{
K_1\equiv K_2\pmod{3^r},
\ p_1\le p_2,
\ C_1\le C_2
\Longrightarrow
\text{state 2 may be discarded.}
}
\]

For each carry residue modulo `3^r`, an exact implementation therefore needs only the Pareto frontier in

\[
(p,C).
\]

No one-state-per-residue assumption is made.

## 5. Relation to existing endpoint Pareto pruning

This is the terminal-Hensel analogue of the already audited endpoint Pareto principle used in the forward minimal-survivor dynamic program.  Both are legal because they compare states at the **same remaining domain/horizon** and preserve every future continuation of the dominated state.

The two dominance principles should not be conflated: one works in the forward binary formation tree, the other in the backward terminal Hensel tower.

## 6. Use in Christoffel block composition

For a block with exactly r unresolved digits on its left, block-interface carries may be reduced modulo `3^r`.  After quotienting, retain only nondominated `(p,C)` pairs in each residue class before performing the next weighted min-plus composition.

This is an exact compression, not a heuristic truncation.

The remaining challenge is that `3^r` itself is large for macroscopic blocks.  Further compression must therefore come from the Christoffel/continued-fraction block hierarchy or from a Bellman dual potential; the quotient lemma supplies the legality condition for any such implementation.

## 7. DSD audit role

The lemma preserves precisely the state information needed by the future domain:

\[
\boxed{
\text{full 3-adic carry}
\to
K\bmod3^r
\quad\text{only because the future horizon is fixed to }r.
}
\]

Using a smaller modulus without reducing the future horizon would be an invalid DSD domain projection.  This horizon-aware quotient records the exact point at which information may safely be discarded.
