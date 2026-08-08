# Safe-tail matrix status

## Purpose

Test whether the Dangerous-Core Extremal Reduction (DCER) can be proved merely from edgewise co-order of the canonical start x and descent margin z=x-y along coordinates satisfying the safe-coordinate inequality.

## Negative result: unique-sink route is too strong

Edgewise co-order alone does not imply a common global minimizer on a general connected graph. Even if every edge has the same orientation under x and z, two distinct local minima can have their depths reversed between the two functions.

The actual first-coefficient-crossing lattice confirms that a unique-sink hypothesis is false in the full admissible graph.

Exact enumeration of admissible first-crossing words and one-coordinate adjacency gave the following numbers of strict local minima of x:

- J=16: 476 states, 94 local minima
- J=18: 961 states, 171 local minima
- J=20: 2652 states, 304 local minima
- J=21: 8045 states, 1474 local minima
- J=23: 17637 states, 2309 local minima
- J=24: 51033 states, 4805 local minima
- J=27: 312455 states, 24691 local minima
- J=29: 663535 states, 50985 local minima

Nevertheless, in all of these tested levels the global minimizer of x coincided with the global minimizer of z. Therefore the observed Hierarchical Extremal Principle, if true, is genuinely global and cannot be reduced to a unique local sink argument.

## Matrix-semigroup representation

For the accelerated map, use homogeneous upper-triangular generators

E = [[1,0],[0,2]],
O = [[3,1],[0,2]].

For a parity word w of length j containing q odd steps, the ordered product has the form

A(w) = [[3^q, R(w)],[0,2^j]].

Thus:
- the diagonal ratio 3^q/2^j is the coefficient channel;
- the upper-right entry R(w) is the complete +1 correction channel;
- at fixed (j,q), all variation among words is carried by R(w).

The canonical start is determined by

3^q x + R(w) == 0 (mod 2^j),

and the descent margin by

D x - 2^j z = R(w),
D=2^j-3^q.

Hence a transfer calculation must preserve both the Archimedean value of R and its modular image; ordinary 0/1 adjacency matrices discard exactly the information needed for FCS/CST.

## Appropriate next transfer object

The next useful object is a weighted/tropical transfer, not a plain adjacency matrix. Each admissible transition should carry at least:

(state slack, correction contribution, modular correction class, extremal x, extremal z/Pareto record).

Because the dangerous dimension h(q) is O(log j), explicit modular branching should be concentrated on the dangerous core. The safe tail should be eliminated by a global dynamic-programming certificate rather than local unique-sink monotonicity.

## Status

Proved/derived:
- matrix-semigroup product representation;
- exact relation D x - 2^j z = R;
- edgewise co-order is insufficient in graph theory;
- unique-sink strategy is contradicted by exact finite Collatz lattices.

Computational evidence only:
- global argmin x = argmin z at tested first-crossing levels.

Open:
- DCER / Hierarchical Extremal Principle;
- a min-plus or Pareto transfer theorem that contracts all safe-tail states without losing the global extremal candidate.
