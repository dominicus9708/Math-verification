# S10 eight-jump pruning and state-growth audit

Date: 2026-09-03

Status: **SAFE pruning advance / quotient pressure identified**

## Exact jump sequence

Starting from the 14 retained affine source roots, repeated valuation-cylinder + pure-ballot transitions give:

| odd-event jumps | cylinders | surviving source integers |
|---:|---:|---:|
| 0 | 14 | 125,072,439,875,999,947,649 |
| 1 | 32 | 94,018,492,189,951,139,878 |
| 2 | 74 | 78,277,356,063,975,556,852 |
| 3 | 174 | 59,912,679,889,581,873,141 |
| 4 | 374 | 50,489,422,254,631,626,671 |
| 5 | 986 | 44,710,237,164,104,400,785 |
| 6 | 2,192 | 36,555,835,392,716,456,688 |
| 7 | 5,752 | 32,306,978,271,327,268,319 |
| 8 | 14,224 | 26,859,837,368,845,079,186 |

Thus eight forced odd-event jumps reject

\[
98{,}212{,}602{,}507{,}154{,}868{,}463
\]

of the previous 14-root population under pure-ballot necessity alone.

The remaining fraction is approximately

\[
0.214754244784.
\]

## DSD analysis

### Positive result

The valuation jump is not merely a representation change. Coupled to the exact ballot predicate it provides substantial deterministic pruning while never enumerating individual integers.

### Emerging bottleneck

The number of live cylinders grows

\[
14\to32\to74\to174\to374\to986\to2192\to5752\to14224.
\]

Therefore naive continuation will eventually trade integer compression for state-count explosion.

This is the exact point at which a DSD future-equivalence quotient becomes necessary.

### Merge rule remains strict

Two live cylinders may not be merged merely because they have the same:

- current surplus;
- next valuation;
- interval size;
- physical score;
- residual congruence.

A legal merge needs a proof that every remaining predicate observes the two states identically, including future formation controls.

## Next active target

Before extending the jump depth much further, determine which coordinates of

\[
(y,A,[m_{lo},m_{hi}],h,S,\Gamma_{future})
\]

actually affect the next bounded block of valuation/ballot transitions.

The first candidate quotient should be **finite-horizon exact**:

1. choose a horizon of several odd-event jumps;
2. compute the exact future transition/rejection signature of each live cylinder;
3. group only equal signatures;
4. regress the grouped evolution against the unmerged 8-jump forest;
5. inspect which arithmetic coordinates determine the signature, then attempt a universal merge theorem.

Finite-horizon signature equality is an implementation compression only until a future-invariance theorem is proved.

## Certificate

- `../src/A0_s1_14root_8jump_ballot_pruning_certificate.py`
