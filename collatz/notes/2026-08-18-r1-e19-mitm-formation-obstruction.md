# R1 E=19 MITM formation obstruction

Date: 2026-08-18

Status: **exact current-R1 finite formation certificate for total pre-G13 even count E=19**.
Together with the preceding E=13--18 exclusions, this upgrades the current isolated R1 core to

\[
\boxed{e_{1539}\ge20}.
\]

This is not a global proof of the Collatz conjecture.

## 1. E=19 event-position input

The necessary even-position vector entering this layer is

\[
[0,1,2,3,4,5,6,7,8,9,10,11,12,19,81,177,329,567,944].
\]

Hence rank 15 cannot occur before position 177.  In the 104 accelerated positions
73..176, a first-73 layer with \(k=e_{73}\) may therefore contain at most
\(15-k\) further even events.  Existing first-73 certificates already remove
\(k\le8\), while run-cover gives \(k\le15\).  Thus only \(k=9,\ldots,14\)
need explicit window-formation subtraction; \(k=15\) is excluded by the same
numerical/window endpoint intersection at the boundary used in the construction.

## 2. Direct sparse-address identity

If the 104-step window contains even-event positions

\[
p_0<\cdots<p_{z-1},
\]

then its starting address is obtained without rebuilding the whole parity word:

\[
\boxed{
U_{73}\equiv-
\sum_{i=0}^{z-1}2^{p_i}3^{-(p_i-i)}
\pmod{2^{104}}.
}
\]

This identity was checked against the former `canonical_U_residues` construction
on exhaustive small windows before applying it here.

## 3. Small first-73 layers

Exact direct enumeration gives

| \(e_{73}\) | raw address classes | numerical intersection | zero by |
|---:|---:|---:|---:|
| 14 | 105 | 0 | immediate |
| 13 | 5,461 | 2 | \(K=15\) |
| 12 | 187,565 | 219 | \(K=27\) |
| 11 | 4,785,691 | 18,688 | \(K=30\) |
| 10 | 96,748,211 | 1,137,712 | \(K=33\) |

For \(e_{73}=9\), the sublayer with at most five window-even events has the same
96,748,211 raw classes, 3,417,527 numerical endpoint states, and is empty by
\(K=33\).

## 4. The six-event k=9 layer

The remaining six-event layer alone contains

\[
\binom{104}{6}=1,517,381,580
\]

ordinary sparse words.  Including the zero-through-five-event sublayers, the
full \(k=9\) raw window count is

\[
\sum_{j=0}^{6}\binom{104}{j}=1,614,129,791.
\]

The six-event layer is split 3+3.  Left triples are indexed by their terminal
position so that the ordering constraint \(p_2<p_3\) is enforced before pairing.
Only sums whose dyadic address lies in the exact numerical \(U_{73}\) interval
are materialized.

The exact six-event counts are

\[
53,574,256
\to2,413,569\ (K=15)
\to378,769\ (K=18)
\to47,519\ (K=21)
\to5,225\ (K=24)
\to473\ (K=27)
\to54\ (K=30)
\to6\ (K=33)
\to0\ (K=36).
\]

Adding the already closed zero-through-five-event part gives the full
\(k=9\) checkpoint ladder

\[
56,991,783
\to2,567,037
\to402,737
\to50,445
\to5,548
\to506
\to56
\to6
\to0.
\]

Therefore \(k=9\) is empty, and all E=19 layers are empty.

## 5. Consequence

\[
\boxed{E=19\text{ is empty}}
\qquad\Longrightarrow\qquad
\boxed{e_{1539}\ge20}.
\]

For E=20..31 the exact relaxed run-cap maxima all satisfy
\(U_{1539}<2^{941}\).  At E=32 the coarse product bound is already below the
same threshold and decreases by a factor 1/2 for each additional even event.
Thus

\[
\boxed{x_{1539}<2^{941}}.
\]

Since

\[
941=49\cdot19+10,
\]

the natural G13 cut becomes

\[
\boxed{t_{49}<2^{10}=1024,\qquad t_b=0\ (b\ge50)}.
\]

The number of forced high zero G13 address bits is

\[
\boxed{20026-941=19085}.
\]

## Reproducibility

- `collatz/src/r1_e19_small_layers_formation_obstruction.cpp`
- `collatz/src/r1_e19_k9_six_event_mitm_obstruction.cpp`
- `collatz/src/r1_g13_entry_e20_941bit_upgrade_certificate.py`
