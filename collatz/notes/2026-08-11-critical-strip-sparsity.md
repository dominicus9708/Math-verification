# Critical-strip sparsity and exclusion of bounded-discrepancy hard cores

Date: 2026-08-11

Status: **exact necessary-condition theorem for nonperiodic no-first-descent orbits**. It separates the divergent hard core from balanced Christoffel/Sturmian-type critical codes.

Let

\[
D_i:=A_i-i\log_2 3,
\qquad
\lambda_i=2^{D_i}.
\]

For a fixed odd positive start `n` whose odd-event orbit is nonperiodic and never descends below `n`, the harmonic-correction theorem gives

\[
\boxed{
\sum_{i=0}^{q-1}\lambda_i=O_n(q^{1/9}).
}
\]

Fix any real constant `C>=0`. If

\[
D_i\ge-C,
\]

then

\[
\lambda_i=2^{D_i}\ge2^{-C}.
\]

Therefore

\[
2^{-C}
\#\{0\le i<q:D_i\ge-C\}
\le
\sum_{i<q}\lambda_i,
\]

and hence

\[
\boxed{
\#\{0\le i<q:D_i\ge-C\}
=O_{n,C}(q^{1/9}).
}
\]

Consequently, for every fixed-width strip around or above the critical line,

\[
\boxed{
\frac1q
\#\{i<q:D_i\ge-C\}
\longrightarrow0.
}
\]

Thus a hypothetical nonperiodic first-descent counterexample spends density one of its odd-event checkpoints below every fixed lower translate of the critical line.

In particular, no such orbit can have bounded discrepancy

\[
D_i=O(1),
\]

nor can it spend a positive density of event times in any bounded discrepancy band.

This excludes, as possible divergent no-first-descent hard cores, mechanical/Sturmian/Christoffel-type exponent schedules whose cumulative exponent satisfies

\[
A_i=i\log_2 3+O(1).
\]

The conclusion is compatible with a relative critical-density condition only in a much less balanced form: `D_i/i` may approach zero while `D_i` itself tends to `-infinity` on a density-one set, with only sparse returns toward the critical strip.

This distinction is important when comparing with balanced-word extremal results for periodic/cyclic Collatz structures: balanced words can be extremal for a fixed-length cycle functional without being viable as the nonperiodic no-first-descent hard core considered here.
