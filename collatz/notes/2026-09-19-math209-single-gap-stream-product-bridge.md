# MATH-209 — single gap-stream product bridge for affine correction, Hensel legality, and emitted-r danger gates

Date: 2026-09-19

Status: `EXACT STATE-SPACE MERGE / NO DOUBLE ENUMERATION / r=10 KERNEL TARGET`

## 1. Purpose

MATH-208 represents a paid first-return cluster by even-gap counts

[
a_j=#{	ext{even steps after exactly }j+1	ext{ paid odds and before the next paid odd/return}}.
]

MATH-189 represents the Hensel signature by gap blocks counting even steps after a fixed number of odd steps.

These are the same chronological gap data.

Therefore affine correction, first-return legality, and forward Hensel viability must be updated from one common gap stream rather than by separate enumerators.

## 2. Common gap coordinates

For a paid cluster with gap vector

[
mathbf a=(a_0,ldots,a_{r-1}),
]

define

[
oxed{
p_j=sum_{i<j}a_i.
}
]

Then the (j)-th paid odd is at local shortcut position

[
oxed{
ell_j=j+p_j.
}
]

MATH-208 gives the affine correction

[
oxed{
C_r
=
sum_{j=0}^{r-1}
3^{r-1-j}2^{j+p_j}.
}
]

MATH-189's Hensel candidate block at the same gap level is

[
oxed{
A_j
=
2^{p_j}(2^{a_j}-1).
}
]

Thus both channels are deterministic functions of the same pair

[
oxed{(p_j,a_j).}
]

## 3. Online correction update

Let (C^{(j)}) be the affine correction after the first (j) paid odds.

At the next paid odd, whose position is

[
ell_j=j+p_j,
]

the standard affine recurrence is

[
oxed{
C^{(j+1)}
=
3C^{(j)}+2^{j+p_j}.
}
]

Hence the correction needs only

- current paid count (j);
- assigned-even count (p_j);
- current correction (C^{(j)}).

No parity history is required.

## 4. Online Hensel update

When gap (a_j) is finalized, MATH-189 supplies

[
A_j=2^{p_j}(2^{a_j}-1)
]

and updates each competitor frontier state

[
(s,W)
]

by

[
oxed{
(s,W)
longmapsto
left(
s+b,,
3W+2^j(B_j-A_j)
ight),
}
]

for each legal competitor gap length (b), with

[
B_j=2^s(2^b-1).
]

Therefore the same event that closes one gap block simultaneously

1. fixes the candidate Hensel block (A_j);
2. advances the Hensel witness frontier;
3. advances the assigned-even counter (p).

## 5. One chronological product state

Inside one positive-slack excursion, a sufficient chronological core is

[
oxed{
mathscr G
=
(j,u,p,a_{m cur},C,mathcal V),
}
]

where

- (j): paid odd count so far;
- (u): current slack;
- (p): completed even-gap rank count;
- (a_{m cur}): current unfinished even gap;
- (C): affine correction of the paid cluster;
- (mathcal V): MATH-189 forward Hensel witness frontier.

The exact address cylinder/carry and phase coordinates from MATH-187/205 are carried in parallel, not identified with (mathcal V).

## 6. Event updates

### Even shortcut

An even shortcut performs

[
oxed{
umapsto u-1,
qquad
a_{m cur}mapsto a_{m cur}+1.
}
]

No new Hensel level or paid correction term is finalized.

### Paid odd shortcut

Before advancing to the next odd level, finalize the preceding gap block using

[
a=a_{m cur},
qquad
A=2^p(2^a-1),
]

and update (mathcal V) by the MATH-189 forward recurrence.

Then update the affine correction at the new odd position using

[
Cmapsto3C+2^{j+p},
]

advance the paid count and reset the gap accumulator.

The exact ordering at the opening odd is handled by the same convention used in MATH-189/MATH-208; no historical parity word is reconstructed.

## 7. First return emits r

When the slack first reaches

[
u=0,
]

the excursion terminates and

[
oxed{r=j}
]

is emitted.

At that moment the common state supplies simultaneously:

- paid count (r);
- local depth through MATH-207/208;
- exact affine correction;
- exact Hensel frontier;
- exact same-integer address/carry from MATH-187/205;
- terminal defect (J) from MATH-197.

Thus the terminal danger predicate is evaluated once:

[
oxed{
mathsf{Danger}
=
mathsf{HenselLegal}
wedge
(Jge0)
wedge
left(

u_2(C_R)ge z_{min}(r)
ight).
}
]

For the current frontier,

[
r=10
Longrightarrow
z_{min}(10)=13.
]

But the executor itself is not (r=10)-specific.

## 8. Consequence for the r=10 closure program

The correct final r=10 task is now:

> prove that the common product recurrence has no reachable first-return terminal state with emitted tag (r=10) satisfying the single danger predicate above.

This replaces all of the following as mainline strategies:

- a new AP scan over the 278,725 frozen leaves;
- a new depth-by-depth r=10 scan;
- an r=10-specific parity-word enumerator;
- a separate Hensel enumerator followed by a separate address enumerator.

Those remain regression paths only.

## 9. Consequence for lower r

Once the terminal product quotient is closed, lower paid counts require no architectural rewrite.

The same terminal predicate is evaluated with

[
r=9,8,ldots
]

and only

[
z_{min}(r)
]

changes.

Thus MATH-209 preserves the intended program:

[
oxed{
	ext{one recurrence}
+
	ext{one product quotient}
+
	ext{emitted }r
+
	ext{derived depth}.
}
]

## 10. Claim boundary

Established:

- exact identity of the MATH-208 paid-gap data and the MATH-189 chronological gap blocks;
- affine correction and Hensel frontier can be advanced from one gap stream;
- no separate parity history or separate r/depth enumerator is mathematically required;
- exact common terminal danger predicate.

Not established:

- emptiness of the (r=10) reachable danger quotient;
- a uniformly bounded final quotient for arbitrary depth;
- closure of (r=10);
- first universal Farey-cell emptiness;
- the Collatz conjecture.
