# MATH-241 — resource-safe exact coefficient-sign gate for the post-J r=10 survivor

Date: 2026-09-19

Status: EXACT EXECUTION REFACTOR / SAME MATH-239 GATE / NO NEW CLOSURE CLAIM UNTIL RUN PASSES

## Purpose

MATH-240 is mathematically exact but its monolithic union state reached 43,645,916 active states at round 15 and the GitHub runner terminated with exit code 143.

The failure was a resource failure, not a mathematical survivor or depth-184 frontier.

MATH-241 changes only execution geometry and, after the audited MATH-239 range ends, falls back to exact AP propagation rather than making any coefficient-sign inference.

## Exact split identity

A source endpoint family is

[
Y=B+3^Q s,qquad 0le s<M.
]

For any (1le m_1<M),

[
[0,M)
=
[0,m_1);dotcup;[m_1,M),
]

so the family is exactly the disjoint union

[
{B+3^Qs:0le s<m_1}
]

and

[
{B+3^Qm_1+3^Qt:0le t<M-m_1}.
]

Therefore parameter bisection is an exact set identity.

No parity branch, Bellman condition, coefficient-sign condition, or terminal rule changes.

## Gate

Each resource leaf runs the unchanged MATH-240 logic:

- endpoint (le2^{71}): close;
- (Hle183) and (3^Q<2^H): close by MATH-239;
- (3^Q>2^H): propagate exactly;
- still expanding at (H=184): emit unresolved frontier.

If the exact state exceeds a fixed memory cap, MATH-241 first splits the list of source families. If one source family alone is too large, only its parameter interval is bisected exactly. Beyond depth 183 the procedure is therefore no stronger than the already-audited MATH-108 style exact AP evolution.

Thus resource splitting cannot remove a true depth-184 survivor.

## Architectural role

This is not a return to the old r=10 128-shard proof architecture.

The theorem-facing recurrence remains one coefficient-sign transducer. The split is analogous to evaluating an exact union in separate memory pages.

A PASS is meaningful only if every recursively generated resource leaf becomes empty by exact floor closure and/or MATH-239 sign closure, with no 1000-round survivor.

## Claim boundary

Established by construction:
- exactness of source-interval bisection;
- unchanged MATH-239 closure predicate;
- exact set preservation under resource splitting;\n- no coefficient-sign inference is made beyond depth 183.

Not yet established until the full run succeeds:
- exhaustion of every exact resource leaf before the 1000-round cap;
- frozen r=10 layer closure;
- full r=10 closure.


## MATH-243 upgrade

The executable gate now uses the stronger synchronized first-failure rule.

The MATH-235 input begins coefficient-expanding and is inside the coefficient-surviving language. Because the recurrence preserves the same source origin, the first later state with

[
3^Q<2^H
]

is the first global coefficient failure of that source.

MATH-196 closes every such failure for (H<A_0=114208327604). Thus the executable no longer stops sign pruning at depth 183. It propagates only while (3^Q>2^H); the first contraction is closed by MATH-196. The practical 1000-round cap is many orders of magnitude below (A_0).

MATH-239 remains an independent cross-check but is not the limiting sign theorem for the current gate.


## MATH-246 SCOPE CORRECTION

MATH-246 SCOPE CORRECTION: this executable is DIAGNOSTIC ONLY in its current form. Any pruning based on local coefficient contraction / local-source self-descent is not a valid first-cell closure unless the state is first rebased to the MATH-188 synchronized original source.
