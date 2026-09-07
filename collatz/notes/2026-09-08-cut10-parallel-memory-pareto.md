# MATH-030 — cut-10 parallel-memory Pareto point

Date: 2026-09-08

Status:

`CONFIRMED / EXACT SCHEDULING OPTIMIZATION / COMPUTATIONAL ONLY`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Question

MATH-029 showed that a cut-frontier + DFS traversal can reproduce the MATH-028 `r<=10^9` bounded-lift tree with far less live memory.  The next question is how low the cut can be moved without creating a single huge DFS subtree that becomes a 16-worker load-balancing bottleneck.

## Exact cut comparison

For the exact `RMAX=10^9` coefficient-surviving bounded-lift tree, cuts 0 through 7 expose fewer than 16 tasks and therefore cannot independently occupy 16 workers.

The first cuts with at least 16 tasks are:

| cut | frontier tasks | largest tail subtree branch attempts |
|---:|---:|---:|
|8|19|27,928,598|
|9|38|17,725,864|
|10|64|10,943,447|

The exact total branch attempts after cut 10 are

\[
\boxed{187,063,811}.
\]

The ideal equal 16-worker tail share is therefore

\[
\frac{187,063,811}{16}
=11,691,488.1875.
\]

Thus

\[
W_{\max}(8)>W_{\rm ideal},
\qquad
W_{\max}(9)>W_{\rm ideal},
\]

but

\[
\boxed{W_{\max}(10)=10,943,447<W_{\rm ideal}}.
\]

Hence cut 10 is the first audited cut at which no single exact tail subtree is itself larger than the ideal total-tail/16 workload, while cuts below 8 do not even expose 16 tasks.

This does not claim perfect real scheduler balance; it removes the specific single-subtree lower-bound obstruction.

## Memory-state count

The exact cut-10 frontier has

\[
\boxed{64}
\]

states and the maximum audited local DFS stack is

\[
\boxed{20}.
\]

For 16 workers,

\[
64+16\cdot20
=\boxed{384}
\]

algorithmic live-prefix states.

For comparison:

- MATH-029 cut-24 live-prefix count: `286,693`;
- MATH-028 breadth-first peak: `11,894,128`.

Therefore

\[
\frac{286,693}{384}\approx\boxed{746.60}
\]

and

\[
\frac{11,894,128}{384}\approx\boxed{30,974.29}.
\]

These are state-storage ratios, not mathematical pruning ratios and not guaranteed wall-clock speedups.

## Exact tree preservation

The cut-10 certificate still produces

\[
\boxed{1,796,718}
\]

depth-61 leaves and the total bounded-lift branch-attempt count remains

\[
180+187,063,811
=\boxed{187,063,991},
\]

identical to MATH-028/029.

No candidate state is merged or removed by the scheduling choice.

## DSD interpretation

The DSD criterion used here is not simply “minimize memory.”  It balances:

1. exact-state preservation;
2. sufficient task decomposition for the intended worker count;
3. removal of a dominant single-subtree work bottleneck;
4. minimal simultaneous state storage.

Under that criterion, cut 10 is the first audited 16-worker Pareto point for this finite `RMAX=10^9` tree.

## Scope boundary

Cut 10 is not asserted to be optimal for another `RMAX`, worker count, scheduler, or different candidate predicate.  Those require a fresh scheduling audit.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_cut10_parallel_memory_pareto_certificate.cpp`

Certificate commit:

`6c984b2f2bedc1011ca2bc7741ff643f53e51e94`
