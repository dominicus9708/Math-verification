# Terminal dominance gate redundancy audit

Status: **REJECTED AS A PRUNING ENGINE / exact consistency condition only**

## Closed chain

The terminal-28 target-dominance suffix has exact acceptance condition

\[
z_H\bmod3\in\{0,1\}.
\]

Under

\[
z_H\equiv2^S Z-C(H_s^*)\pmod{3^{28}},
\]

this is equivalent to

\[
Z\bmod3\in\{1,2\}.
\]

But every genuine positive-one-count checkpoint identity

\[
2^hZ=3^qX+C(W),\qquad q\ge1,
\]

already satisfies this condition because

\[
C(W)\equiv2^{a_q}\not\equiv0\pmod3.
\]

Therefore

\[
\boxed{3\nmid Z}
\]

is automatic for every genuine candidate checkpoint.

## Consequence

The terminal-28 target-dominance ternary filter removes **zero genuine candidates**.

It remains useful as:

- a consistency check;
- an implementation regression;
- a proof that the earlier apparent 28-trit formation filter saturates.

It is not useful as a standalone pruning engine.

## Why the previous CRT singleton seam is still valid

The theorem

`SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON`

remains mathematically correct when a **full** value of

\[
z_H\bmod3^{28}
\]

is supplied by some independent stronger state.

What fails is the strategy of expecting target-dominance existence itself to supply a narrow full-precision `z_H` set.  It supplies only the automatic first-trit condition above.

## Weak synchronized channel

Combining dominance-only acceptance with a fixed dyadic checkpoint residue

\[
Z\bmod2^{27}
\]

gives two residue classes modulo

\[
3\cdot2^{27}.
\]

The ordinary debit interval for fixed `X` has width

\[
37\cdot2^{33}
=789(3\cdot2^{27})+2^{27}.
\]

Hence each accepted weak CRT class appears at least 789 times in that open debit interval, so the two classes contribute at least 1,578 checkpoint integers before other constraints.

Thus this weak channel cannot expose a checkpoint singleton.

Certificate:

- `../src/A0_s1_routeB_dominance_only_checkpoint_nonisolation_certificate.py`.

## DSD classification

### EXACT / CLOSED

- terminal dominance saturation;
- genuine-checkpoint nonzero mod-3 condition;
- redundancy implication;
- weak-CRT non-isolation width calculation.

### REJECTED STRATEGY

Continue refining or enumerating the terminal right-H target-dominance carry family in the hope that it alone will prune current genuine candidates.

### NEXT VALID ROUTES

1. `source/control -> exact full correction-language realization`;
2. `source/control × interval payload × P_min -> physical whole-family closure`;
3. use full `z_H mod 3^28` only if a stronger independent predicate actually determines it.

No Route-B or Collatz closure is claimed.
