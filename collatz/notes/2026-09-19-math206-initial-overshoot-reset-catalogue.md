# MATH-206 — initial first-cell overshoot suffix catalogue and zero-carry reset elimination

Date: 2026-09-19

Status: `EXACT FINITE CATALOGUE / INITIAL ZERO-CARRY RESET ELIMINATED / GLOBAL r=10 OPEN`

## 1. Purpose

MATH-205 reduces consecutive dangerous singleton handoffs to the ordinary carry recurrence

[
d'
=
rac{3^{q_e}d+B_e-A_f}{2^{z_f}},
]

with compatibility

[
3^{q_e}d+B_e-A_f
equiv0
pmod{2^{z_f}}.
]

For a zero-carry state (d=0), a zero-to-zero reset requires the exact equality

[
B_e=A_f.
]

Before attempting an arbitrary-depth theorem, this note audits the exact finite catalogue of overshoot suffix factors that already occur inside the frozen initial first-cell zero-cost prefixes of MATH-058R.

The scope is deliberately finite and explicit. It does not claim that every later regenerated zero-cost factor is contained in this catalogue.

## 2. Frozen source of legal initial zero-cost prefixes

Use the corrected MATH-058R generator

[
	exttt{2026_09_11_paid_macro_transition_certificate.py}.
]

For each

[
1le Lle72
]

and every exact record returned by `paid_exit_sources(L)`, reconstruct its exact mechanical zero-cost parity word

[
w=(b_0,ldots,b_{L-1}).
]

Across all (L), the frozen generator contains exactly

[
oxed{937}
]

reachable phase/address prefix records.

## 3. Canonical factor attached to a suffix word

Let (v) be a suffix of one such legal zero-cost word, of length

[
z:=|v|ge13.
]

Let (q(v)) be its odd count and let (C(v)) be the usual affine correction:

[
T_v^z(x)
=
rac{3^{q(v)}x+C(v)}{2^z}.
]

Define the unique canonical source residue

[
oxed{
A_v
equiv
-C(v)3^{-q(v)}
pmod{2^z},
qquad
0le A_v<2^z,
}
]

and

[
oxed{
B_v
=
rac{3^{q(v)}A_v+C(v)}{2^z}.
}
]

Then every integer in that exact parity cylinder has the canonical affine form

[
oxed{
A_v+2^z t
longmapsto
B_v+3^{q(v)}t.
}
]

This is exactly the MATH-091/MATH-205 factor notation.

## 4. Exact catalogue size

Enumerating every suffix length (zge13) of every one of the 937 frozen legal initial prefixes gives

[
oxed{32,508}
]

suffix-factor occurrences.

After exact deduplication by

[
(z,q,A,B),
]

there remain only

[
oxed{924}
]

distinct canonical overshoot factor types.

No Hensel or terminal-defect pruning is used here. Therefore this 924-factor set is an address-side over-approximation of the actually dangerous subset, which is safe for exclusion results.

## 5. Zero-to-zero reset audit

For zero carry, MATH-205 says that transition from factor (e) to factor (f) is compatible only if

[
B_eequiv A_fpmod{2^{z_f}}.
]

The next carry is

[
d'=rac{B_e-A_f}{2^{z_f}}.
]

A repeated zero carry requires the stronger equality

[
B_e=A_f.
]

Across all ordered pairs of the 924 exact factor types, the audit finds

[
oxed{
#{(e,f):B_e=A_f}=0.
}
]

Thus the frozen initial first-cell overshoot catalogue contains **no exact zero-to-zero reset edge at all**.

In particular, within this catalogue there is no zero-carry reset cycle.

## 6. 13-bit necessary resonance audit

The current (r=10) danger threshold from MATH-202 is

[
z_fge13.
]

The weak necessary low-bit test is therefore

[
B_eequiv A_fpmod{8192}.
]

Among all ordered factor pairs, exactly

[
oxed{388}
]

pairs satisfy this 13-bit necessary resonance.

All 388 have

[
B_e
e A_f.
]

Thus every low-13-bit candidate is already a zero-to-nonzero possibility rather than an exact reset.

## 7. Full factor-depth compatibility

The actual factor (f) requires divisibility by its full source modulus (2^{z_f}), not merely (2^{13}).

After imposing

[
B_e-A_fequiv0pmod{2^{z_f}},
]

only

[
oxed{8}
]

ordered zero-carry transitions remain.

They come from four current factors, all with the same target intercept

[
B_e=4,681,055,033,
]

and two possible next factor types.

### Target factor F14

[
(z_f,q_f,A_f,B_f)
=
(14,9,15,161,18,218).
]

Then

[
4,681,055,033-15,161
=
285,708cdot2^{14},
]

so

[
oxed{d'=285,708},
]

and

[

u_2(B_e-A_f)=16.
]

### Target factor F17

[
(z_f,q_f,A_f,B_f)
=
(17,11,80,697,109,070).
]

Then

[
4,681,055,033-80,697
=
35,713cdot2^{17},
]

so

[
oxed{d'=35,713},
]

and

[

u_2(B_e-A_f)=17.
]

The four current factors are

[
(32,21,1,922,017,147,4,681,055,033),
]

[
(33,21,3,844,034,294,4,681,055,033),
]

[
(34,22,2,562,689,529,4,681,055,033),
]

[
(35,22,5,125,379,058,4,681,055,033).
]

Each connects to both F14 and F17, giving (4	imes2=8) transitions.

## 8. One more carry step

MATH-205 must then be applied again with the nonzero carry.

For F14,

[
3^9(285,708)+18,218
=
5,623,608,782.
]

Its low 13 bits are

[
5,623,608,782mod8192
=
5,582.
]

No factor in the 924-factor catalogue has

[
A_gequiv5,582pmod{8192}.
]

For F17,

[
3^{11}(35,713)+109,070
=
6,326,559,881,
]

and

[
6,326,559,881mod8192
=
1,161.
]

Again, no factor in the catalogue has

[
A_gequiv1,161pmod{8192}.
]

Therefore none of the eight first compatible transitions can make even the minimum 13-bit resonance needed for another (r=10)-danger handoff inside this frozen catalogue.

Hence

[
oxed{
	ext{within the MATH-058R initial overshoot catalogue,}
quad
	ext{zero carry}
	o
	ext{at most one nonzero-carry handoff}
	o
	ext{13-bit exit}.
}
]

## 9. DSD interpretation

The original initial-prefix address space compresses as

[
937	ext{ reachable prefixes}
	o
32,508	ext{ suffix occurrences}
	o
924	ext{ exact factor types}
	o
388	ext{ low-13 resonant pairs}
	o
8	ext{ full-depth compatible pairs}
	o
0	ext{ second danger continuations}.
]

Each arrow is an exact representation/refinement step.

The dramatic reduction is not itself a universal proof because the finite catalogue is tied to the frozen initial first-cell zero-cost prefixes.

## 10. Consequence for the next theorem target

The initial zero-carry reset question is now closed inside the frozen first-cell catalogue:

- zero-to-zero exact reset: absent;
- zero-to-nonzero full compatibility: only eight cases;
- all eight fail the next 13-bit necessary resonance within the same catalogue.

Therefore the next structural obligation is not to revisit the 278,725 AP leaves.

It is to generalize the suffix-factor construction **under the synchronized MATH-187 recurrence after a regenerated boundary**, and prove that the same reset/resonance exclusion persists for every later legal factor.

That is the correct route toward an arbitrary-depth (r=10) carry theorem.

## 11. Claim boundary

Established:

- exact canonical factor construction for every (zge13) suffix of every frozen MATH-058R legal initial zero-cost prefix;
- 937 frozen prefix records;
- 32,508 suffix occurrences;
- 924 distinct exact factors;
- zero exact zero-to-zero reset edges;
- 388 weak 13-bit pair resonances;
- eight full factor-depth zero-to-nonzero compatible transitions;
- only two resulting carry values, 285,708 and 35,713;
- zero second (r=10) 13-bit continuation inside this finite catalogue.

Not established:

- completeness of this catalogue for later regenerated zero-cost factors;
- arbitrary-depth elimination of zero-carry or nonzero-carry paths;
- closure of (r=10);
- first universal Farey-cell emptiness;
- the Collatz conjecture.
