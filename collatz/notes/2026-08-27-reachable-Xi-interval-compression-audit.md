# Reachable-Xi interval compression audit

Date: 2026-08-27

Status: **SAFE negative theorem / exact-compression rejection.** This identifies the information that the next Christoffel-DAG state representation must preserve. It does not prove the Collatz conjecture.

## 1. One-step reachable set already has holes

Take one ordered Hensel/control step with mechanical term `2^e` and allow every displacement

\[
d\ge0.
\]

Relative to the mechanical action `d=0`, the invariant defect is

\[
\boxed{
\Delta\Xi(d)=2^e(1-2^{-d}).
}
\]

Thus the exact reachable defect set is

\[
\boxed{
\left\{
0,
\frac12 2^e,
\frac34 2^e,
\frac78 2^e,
\ldots
\right\}.
}
\]

It is not an interval. For example

\[
\frac58 2^e
\]

lies strictly between two reachable values but is not reachable.

The raw invariant values

\[
\Xi(d)=-2^{e-d}
\]

have the same sparse dyadic structure.

## 2. Consequence for DAG compression

Replacing an exact reachable set by its convex hull or real interval fills arithmetic holes after the very first node.

Under Christoffel composition, Minkowski sums of such interval hulls can only fill more holes. Therefore interval propagation cannot be an exact reachable-set quotient.

The arithmetic holes are not numerical noise. They encode the discrete displacement control and may be exactly what separates the ordered reachable set from the physical target set.

## 3. Safe and unsafe uses of interval hulls

### REJECTED as an exact state

Do not assert

\[
\mathcal R_w=[\min\mathcal R_w,\max\mathcal R_w]
\]

or use interval membership as equivalent to reachability.

### SAFE as an outer relaxation

If `I_w` is proved to contain `R_w`, then

\[
I_w\cap\mathcal P_w=\varnothing
\]

is sufficient to conclude

\[
\mathcal R_w\cap\mathcal P_w=\varnothing.
\]

But a nonempty interval intersection proves nothing about exact reachability and must remain an unresolved branch.

Similarly, an interval lower bound may be useful for independent cost separation if its inequality direction is proved, but it cannot restore digital compatibility that has been projected away.

## 4. Natural digital descriptor

The one-step defect has binary form

\[
\frac{\Delta\Xi(d)}{2^e}
=0.\underbrace{11\ldots1}_{d\text{ ones}}_2.
\]

For the full correction defect, each displaced odd ordinal contributes

\[
3^{q-j}2^{a_j}(2^{d_j}-1),
\]
where the actual odd positions `a_j` are strictly increasing. Thus each nonzero term has a distinct lowest dyadic valuation `a_j`.

This suggests that a useful exact reachable-set representation should retain at least a bounded digital prefix / valuation trie, not only a real interval.

The existing formation-address theorem is the global version of the same phenomenon: late high-position defects vanish from low dyadic address projections and cannot repair an earlier low-bit mismatch.

## 5. DSD verdict

The descriptor test is:

\[
\boxed{
\text{real magnitude alone}
\text{ loses technical possibilities and impossibilities};
\quad
\text{digital valuation structure must be retained.}
}
\]

This is a state-loss rejection, not a failure of the reachable-Xi program.

## 6. Next gate

Test a mixed descriptor on the short exact terminal regressions:

\[
\boxed{
(\text{low dyadic prefix},\ \text{rigorous real interval},\ p)
}
\]

or an equivalent finite digital trie. The dyadic prefix preserves holes; the interval controls large-scale magnitude; `p` retains ordering memory.

Only after this mixed representation passes the terminal 45--65-odd exact certificates should it be promoted to the 138-node Christoffel DAG.
