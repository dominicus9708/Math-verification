# External audit — spectral gap does not imply deterministic Collatz closure

Date: 2026-09-06

Status: **SAFE EXTERNAL NEGATIVE CONTROL / PERMANENT DSD REGRESSION TEST.**

A 2026 Syracuse-transfer-operator project proved a genuine uniform spectral gap on finite `2`-adic quotient operators and initially attempted to infer elimination of nontrivial Collatz cycles.  The authors later withdrew that implication after an exact control experiment.

## 1. What survives externally

The external project retains a theorem-level operator statement: a uniformly gapped transfer/Markov operator on the finite `2`-adic quotients, with elementary finite-group/coset arguments and a Lean formalisation of part of the combinatorial core.

This is a legitimate result about the **averaged operator**.

## 2. What failed

The withdrawn implication was schematically

\[
\boxed{
\text{uniform spectral gap of averaged Syracuse operator}
\Longrightarrow
\text{no nontrivial deterministic cycles}.
}
\]

The authors tested the same certificate on the `3x-1` control map.  That map has known nontrivial cycles, but the transfer operator satisfies the same kind of spectral-gap certificate, even strongly.

Therefore the implication is false.

## 3. DSD diagnosis

The transfer operator averages over lifts/branches.  This averaging can destroy precisely the pathwise information needed to identify a special deterministic periodic orbit.

Thus

\[
\boxed{
\text{mixing of an annealed projection}
\not\Rightarrow
\text{absence of exceptional quenched paths}.
}
\]

Equivalent DSD wording:

- state-space projection is many-to-one;
- spectral decay controls distributions/observables after averaging;
- a deterministic orbit is an atom/path-level object;
- a bridge preserving that path information is required before one can infer orbit elimination.

## 4. Direct connection to current repository barriers

This external refutation independently confirms several internal safeguards.

### Gate A / Walsh-Fourier work

Aggregate Fourier flatness or Walsh cancellation is useful only after establishing that the actual occupied distribution is the object being averaged.  It cannot be silently upgraded to arbitrary-subset or pathwise contraction.

### Selector energy barrier

A small/controlled average over the full group does not imply the same bound on a sparse support after the support barrier.

### Fixed-Q path barrier

The formal `d=2` Beatty boundary path survives fixed-Q reverse-potential elimination even though averaged macro blocks contract.  This is the same structural separation between distributional contraction and exceptional path survival.

### Gate C / same-integer requirement

A symbolic or `2`-adic path is not automatically realized by a positive ordinary integer. Conversely, an averaged operator that forgets exact integer ancestry cannot prove that no exceptional integer path exists.

## 5. Comparison with newer entropic-Laplacian frameworks

A more careful recent entropic/spectral formulation explicitly separates:

- unconditional annealed spectral/Dirichlet statements;
- deterministic Collatz hitting-time conclusions only under an additional uniform refresh/minorization hypothesis.

This is the correct DSD separation.

The missing theorem is exactly a `quenched bridge`:

\[
\boxed{
\text{actual deterministic parity history}
\Longrightarrow
\text{enough refresh/mixing to inherit the annealed gap}.
}
\]

Without that bridge, a spectral theorem is not a Collatz theorem.

## 6. Verdict

\[
\boxed{
\text{SPECTRAL GAP THEOREM: MAY SURVIVE;}\\
\text{GAP }\Rightarrow\text{ DETERMINISTIC CYCLE ELIMINATION: FALSE.}
}
\]

This external self-correction should remain a permanent regression test in the repository.  Any future spectral/Fourier closure must explicitly identify the information-preserving bridge from averaged state to actual integer path.
