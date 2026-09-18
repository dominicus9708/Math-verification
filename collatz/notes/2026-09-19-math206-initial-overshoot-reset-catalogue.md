# MATH-206 — exact r=10 boundary-factor zero-carry audit

Date: 2026-09-19

Status: `EXACT FINITE BOUNDARY AUDIT / ZERO-CARRY CONTINUATION ABSENT IN FROZEN r=10 CATALOGUE / GLOBAL r=10 OPEN`

## 1. Scope correction

An earlier draft of MATH-206 composed zero-cost **suffix factors** directly with other zero-cost suffix factors.

That composition omitted the intervening paid cluster and therefore was not the correct MATH-205 boundary-to-boundary recurrence.

The suffix catalogue remains a valid finite address-language diagnostic, but its suffix-to-suffix carry chain must not be promoted to a proof-facing boundary chain.

This corrected note replaces that interpretation.

The correct factor is the entire exact transfer

[
oxed{
	ext{zero-cost prefix}
+
	ext{first-return }r=10	ext{ paid cluster},
}
]

from one ordinary-source boundary cylinder to the next.

## 2. Canonical full boundary factor

Use the unchanged MATH-065 exact (r=10) generator.

For one phase/address cell, let

- (L) be the initial zero-cost prefix length;
- (R_0) be its exact initial source residue;
- (q_0) be the odd count of that prefix;
- (h_{10}) be the exact local first-return cluster depth.

A terminal negative-candidate leaf has parameter

[
t=t_0+2^{h_{10}}s
]

and exact target

[
Y=B_0+3^{q_0+10}s.
]

Since the original source is

[
N=R_0+2^Lt,
]

substitution gives

[
N
=
left(R_0+2^Lt_0ight)
+
2^{L+h_{10}}s.
]

Therefore define

[
oxed{
H:=L+h_{10},
qquad
Q:=q_0+10,
}
]

[
oxed{
A:=R_0+2^Lt_0,
qquad
B:=B_0.
}
]

Each exact (r=10) leaf is therefore one canonical full boundary factor

[
oxed{
A+2^Hs
longmapsto
B+3^Qs.
}
]

This is the proper MATH-091/MATH-205 factor for boundary composition.

## 3. Regression against the frozen r=10 workload

Reconstructing the full factor catalogue with the unchanged MATH-065 arithmetic reproduces the frozen MATH-113 (r=10) invariants exactly:

[
oxed{994=91+396+507}
]

phase/address cells,

[
oxed{1,994,258}
]

branch nodes,

[
oxed{278,725}
]

negative-candidate AP leaf records,

[
oxed{27,557,263,803,397}
]

represented occurrence mass, and maximum leaf multiplicity

[
oxed{830,483,089,363}.
]

Thus the factor extraction changes no (r=10) source semantics.

## 4. Exact factor-type deduplication

Deduplicate the 278,725 leaf records by the proof-facing affine factor key

[
oxed{(H,Q,A,B).}
]

This leaves

[
oxed{258,242}
]

distinct exact full boundary factor types.

A duplicated type represents the same affine boundary transfer and does not need to be counted twice in the zero-carry compatibility relation.

## 5. MATH-205 zero-carry compatibility

Let (e) be the current full factor and (f) the next full factor.

MATH-205 gives

[
d'
=
rac{3^{Q_e}d+B_e-A_f}{2^{H_f}}.
]

For zero incoming carry,

[
d=0,
]

the exact compatibility condition is

[
oxed{
B_eequiv A_f
pmod{2^{H_f}}.
}
]

If this congruence holds, then

[
d'
=
rac{B_e-A_f}{2^{H_f}}.
]

A zero-to-zero exact reset would require the stronger equality

[
B_e=A_f.
]

## 6. Exact zero-reset audit

Across all 258,242 distinct frozen (r=10) full factor types,

[
oxed{
{A_f}cap{B_e}
=
arnothing.
}
]

Therefore

[
oxed{
#{(e,f):B_e=A_f}=0.
}
]

There is no zero-to-zero exact reset pair in the frozen (r=10) factor catalogue.

## 7. Full-modulus compatibility audit

The stronger and more relevant question is whether zero carry can transition to a **nonzero** carry.

For each possible next-factor modulus exponent (H_f), form the exact set

[
mathcal A_{H_f}
=
{A_fmod2^{H_f}}.
]

Then audit every current target (B_e) against

[
B_emod2^{H_f}.
]

The full catalogue gives

[
oxed{
#left{
(e,f):
B_eequiv A_fpmod{2^{H_f}}
ight}
=
0.
}
]

So the result is stronger than absence of an exact reset:

[
oxed{
	ext{zero incoming carry has no compatible next frozen }r=10
	ext{ full factor at all.}
}
]

No zero-to-nonzero carry case survives the complete source modulus.

## 8. Relation to the earlier suffix diagnostic

The earlier suffix-language calculation found 924 initial overshoot suffix types and several low-bit congruences.

Those calculations were algebraically valid for suffix address factors, but direct suffix-to-suffix composition is not the proof-facing boundary chain because it skips the (r=10) paid cluster.

The present full-factor audit supersedes that use.

The suffix catalogue may remain as a SIDE / SUPPORT diagnostic for local address language, but the theorem-facing finite result is now the full-factor statement:

[
oxed{
278,725	ext{ frozen leaves}
	o
258,242	ext{ exact full factor types}
	o
0	ext{ zero-carry compatible boundary edges}.
}
]

## 9. What this closes

Within the frozen initial MATH-113 (r=10) negative-candidate factor catalogue:

1. zero-to-zero reset is impossible;
2. zero-to-nonzero continuation is also impossible;
3. therefore any boundary state entering this catalogue with zero carry cannot concatenate another factor from the same frozen catalogue.

This is an exact finite exclusion, not a density statement.

## 10. What remains open

The factor catalogue above is the frozen initial first-cell (r=10) workload.

After an arbitrary composed boundary, the synchronized MATH-187 state may regenerate a factor with a different source origin / phase-address lineage.

Therefore the next theorem target is:

[
oxed{
	ext{prove that every regenerated legal }r=10	ext{ factor}
	ext{ lies in an equivalent zero-carry-incompatible class,}
}
]

or derive a stronger invariant that makes explicit catalogue regeneration unnecessary.

This is the actual arbitrary-depth step.

## 11. DSD audit lesson

The scope correction is itself important.

The hierarchy is

[
	ext{parity suffix factor}

eq
	ext{full paid boundary factor}.
]

A local address factor may be used to prove a local congruence lemma, but it cannot be composed as though the intervening paid dynamics were absent.

The corrected MATH-206 therefore restores the exact formation boundary before applying MATH-205.

## 12. Claim boundary

Established:

- exact extraction of a full boundary factor from each frozen (r=10) negative-candidate leaf;
- exact reproduction of all frozen MATH-113 (r=10) workload invariants;
- 278,725 leaf records;
- 258,242 distinct ((H,Q,A,B)) factor types;
- zero exact reset pairs;
- zero full-modulus zero-carry compatible ordered factor pairs.

Superseded as proof-facing interpretation:

- direct suffix-to-suffix carry chaining from the earlier MATH-206 draft.

Not established:

- completeness of the frozen factor catalogue for every later regenerated boundary;
- arbitrary-depth zero-carry exclusion;
- nonzero-carry closure;
- closure of (r=10);
- first universal Farey-cell emptiness;
- the Collatz conjecture.
