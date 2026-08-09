# Endpoint-merge dominance — 2026-08-09

## Verified lemma

Consider two coefficient-surviving states at the same prefix depth \(k\):

\[
S_1=(r_1,q_1,y),\qquad S_2=(r_2,q_2,y),
\]

with the same endpoint \(y=T^k(r_i)\).  If

\[
r_1\le r_2,\qquad q_1\ge q_2,
\]

then \(S_1\) dominates \(S_2\) for every future continuation when computing the minimal-survivor function.

Indeed, from the common endpoint \(y\) the future orbit and the number \(s_u\) of future odd steps over any additional \(u\) steps are identical.  Hence

\[
q_1+s_u\ge q_2+s_u.
\]

If state 2 satisfies the coefficient barrier at any future depth \(k+u\), state 1 also satisfies it, while its starting residue is no larger.  Therefore state 2 can never improve \(\mu(K)\) for any \(K\ge k\).

**Status:** verified algebraic lemma.

## Computational experiment

`collatz/src/endpoint_merge_quotient.cpp` enumerates the full coefficient-survivor set at each depth, groups states by common endpoint, and applies the exact dominance lemma.

Exact results include:

| k | survivors | endpoint classes | collision groups | Pareto kept | max group |
|---:|---:|---:|---:|---:|---:|
| 20 | 27,328 | 25,644 | 1,676 | 25,644 | 3 |
| 24 | 286,581 | 269,145 | 17,328 | 269,145 | 4 |
| 28 | 3,524,586 | 3,312,992 | 210,107 | 3,312,992 | 4 |

At \(k=28\), same-endpoint quotienting removes 211,594 states, about 6.00% of the survivor set.

More strikingly, through every tested depth \(k\le28\), each endpoint collision group has exactly one Pareto survivor: the smallest starting residue in the group also has a sufficiently large odd-count to dominate all larger starts in that group.

The stronger statement

> among equal-depth preimages of a common endpoint, the minimum positive start has maximum odd-count

has not been proved here.  It is currently **computational evidence / theorem candidate**, not a verified theorem.

A literature search found related rigorous backward-tree work, notably Applegate and Lagarias, *The Distribution of 3x+1 Trees* (Experimental Mathematics, 1995), but did not immediately surface this exact ordering statement.

## Cross-branch merge examples

The mod-32 branch profiles contain exact endpoint coincidences such as

\[
T^{56}(703)=13211=T^{54}(1583),
\]

\[
T^{73}(10087)=28403=T^{72}(15131),
\]

\[
T^{135}(432923)=86751245=T^{137}(577231).
\]

Because these merges occur at different depths, the same-depth dominance lemma does not apply directly.  They nevertheless show that branch profiles repeatedly enter common future orbits and motivate a clock-aware merge state carrying \((k,q,r,y)\).

## Next structural target

Test whether the one-Pareto-state-per-endpoint observation persists beyond \(k=28\), and seek a backward-tree proof.  If true, the full survivor dynamic program can quotient by endpoint rather than by parity prefix, yielding a deterministic future-state representation with exact dominance.
