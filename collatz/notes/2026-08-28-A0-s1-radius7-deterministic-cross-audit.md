# A0 s=1: first-75 radius-seven deterministic cross-audit

Date: 2026-08-28

Status: **SAFE finite necessary-condition closure with two independent implementations.** This does not certify `C4F` and is not a proof of Collatz.

## 1. Previous frontier

The radius-six audit established that every A0 s=1 survivor satisfying the previously certified bound

\[
X\le 3295414002074039191016
\]

must differ from the exact threshold word in at least seven of the first 75 parity positions:

\[
d_{75}\ge7.
\]

## 2. New 72-bit determinization route

Because the physical A0 shell lies below `2^72`, the first 72 parity bits expose the ordinary integer start exactly:

\[
X=A_{72}(w_{<72}).
\]

The final three parity bits of the proposed first-75 word are therefore not free choices. They are obtained by directly iterating the unique exposed integer `X`.

The exact number of pure-ballot first-72 words at Hamming distance 7 from the threshold prefix is

\[
139752360.
\]

After imposing the physical shell, the certified A0 upper bound, the deterministic bits 73--75, and exact first-75 distance 7, the bounded candidate count is

\[
\boxed{4662684}.
\]

Every one of these candidates loses the pure-ballot condition by prefix 454. No candidate survives the scan.

## 3. Regression against radii 0--6

Before accepting the new route, the 72-bit determinization implementation was required to reproduce the older direct-75-bit audit exactly.

It returned:

| `d_75` | physical | bounded | latest pure-ballot failure |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 88 |
| 2 | 62 | 18 | 110 |
| 3 | 916 | 386 | 161 |
| 4 | 15,560 | 6,174 | 222 |
| 5 | 147,027 | 58,212 | 378 |
| 6 | 1,687,133 | 668,333 | 405 |

These values agree exactly with the independent earlier radius-six direct certificate.

The new row is

| `d_75` | physical | bounded | latest pure-ballot failure |
|---:|---:|---:|---:|
| 7 | 11,784,860 | 4,662,684 | 454 |

with zero survivors.

## 4. Independent direct-75-bit audit

A second implementation does not use the 72-bit determinization shortcut.

It directly enumerates every pure-ballot first-75 word through radius 7, computes the complete parity address modulo `2^75`, imposes the physical shell and the A0 upper bound, and checks the actual Collatz orbit.

At exact distance 7 it gives

\[
\boxed{
188574243
\to
11784860
\to
4662684
\to
0
}
\]

for

\[
\text{ballot}\to\text{physical}\to\text{bounded}\to\text{survivors}.
\]

Its latest pure-ballot failure is again exactly 454.

Thus the 72-bit determinization route and the direct 75-bit address route agree on the entire radius-seven physical/bounded sector.

## 5. New necessary condition

All first-75 pure-ballot candidates satisfying the existing A0 physical bound at Hamming distance at most 7 have now been excluded.

Therefore every remaining A0 s=1 survivor must satisfy

\[
\boxed{d_{75}\ge8.}
\]

This is a necessary condition only.

## 6. DSD audit classification

### EXACT / SAFE

- threshold word constructed by exact integer comparison `3^q>2^n`;
- pure-ballot filtering;
- finite parity-address bijection;
- 72-bit ordinary-start determinization in the A0 shell;
- direct 75-bit address cross-check;
- physical shell and previously certified `X_max` filter;
- deterministic actual Collatz continuation;
- complete radius-seven finite enumeration;
- conclusion `d_75>=8` for every survivor under the stated A0 assumptions.

### NOT USED

- interval filling assumptions;
- correction-language density assumptions;
- `C4F` identification;
- asymptotic extrapolation from the finite scan.

### STILL OPEN

- the exact meaning/predicate of `C4F` if it contains renewal/gap/global constraints beyond finite parity formation;
- the full `t0` correction-language membership problem;
- a non-brute-force mechanism that excludes all Hamming radii, rather than a fixed initial radius.

## 7. Strategic consequence

The next brute-force radius is much larger: the exact pure-ballot first-75 distance-eight layer contains more than one billion words. Continuing by radius alone is therefore no longer the preferred route.

The useful output of the radius-seven closure is instead structural:

1. the physical branch is already forced a definite distance away from the Christoffel threshold in the first 75 symbols;
2. the 72-bit address exposes the ordinary starting integer exactly;
3. the next economical step should convert `d_75>=8` into a lower bound on the Christoffel correction defect / tri-place coordinate, then test whether that forced defect is compatible with the A0 real-shadow and renewal-gap budgets.

That direction can potentially replace an exponentially growing Hamming-radius enumeration by an arithmetic defect bound.
