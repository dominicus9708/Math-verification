# Minimal-survivor record basins — 2026-08-09

## Definition

For the accelerated Collatz map define

\[
\mu(K)=\min\{n\ge1:\tau_c(n)>K\},
\]

where \(\tau_c(n)\) is the first coefficient-contraction depth.

This note separates two objects that must not be conflated:

1. record holders of large coefficient stopping time as the numerical start bound increases;
2. every plateau of the inverse/minimal-survivor function \(\mu(K)\).

The second list can contain intermediate values that are omitted by a coarse record-holder list.

## Exact corrected plateau chain

The four mod-32 branch profiles plus direct interval certificates give the following exact chain through \(K=546\):

| K interval | mu(K) | tau_c(mu) |
|---|---:|---:|
| 5--6 | 7 | 7 |
| 7--58 | 27 | 59 |
| 59--80 | 703 | 81 |
| 81--104 | 10087 | 105 |
| 105--134 | 35655 | 135 |
| 135--163 | 270271 | 164 |
| 164 | 362343 | 165 |
| 165--172 | 381727 | 173 |
| 173--175 | 626331 | 176 |
| 176--182 | 1027431 | 183 |
| 183--223 | 1126015 | 224 |
| 224--245 | 8088063 | 246 |
| 246--286 | 13421671 | 287 |
| 287--291 | 20638335 | 292 |
| 292--297 | 26716671 | 298 |
| 298--307 | 56924955 | 308 |
| 308--375 | 63728127 | 376 |
| 376--394 | 217740015 | 395 |
| 395--397 | 1200991791 | 398 |
| 398--432 | 1827397567 | 433 |
| 433--446 | 2788008987 | 447 |
| 447--546 | 12235060455 | 547 |

The new exact value found in this run is

\[
\boxed{\mu(447)=12235060455},
\qquad
\tau_c(12235060455)=547.
\]

A continuous exact interval scan has currently eliminated all starts below

\[
\boxed{96235060456}
\]

for \(\tau_c(n)>547\), so

\[
\boxed{\mu(547)\ge96235060456}.
\]

## Exact mod-32 decomposition

Every survivor beyond depth five has

\[
n\bmod32\in\{7,15,27,31\}.
\]

Hence for \(K\ge5\), defining

\[
\mu_a(K)=\min\{n\equiv a\pmod{32}:\tau_c(n)>K\},
\]

we have the exact finite-channel decomposition

\[
\boxed{\mu(K)=\min_{a\in\{7,15,27,31\}}\mu_a(K)}.
\]

For \(n=a+32t\), five accelerated steps give

\[
\begin{aligned}
T^5(7+32t)&=20+81t, & q_5&=4,\\
T^5(15+32t)&=40+81t, & q_5&=4,\\
T^5(27+32t)&=71+81t, & q_5&=4,\\
T^5(31+32t)&=242+243t, & q_5&=5.
\end{aligned}
\]

Thus the first three branches have the same multiplier \(3^4=81\) and barrier slack zero at depth five, while the \(31\pmod{32}\) branch has one unit of odd-count surplus and multiplier \(3^5=243\).

Selected exact branch minima are:

| K | mu_7 | mu_15 | mu_27 | mu_31 | global winner |
|---:|---:|---:|---:|---:|---:|
| 100 | 10087 | 60975 | 57115 | 37503 | 10087 |
| 150 | 288615 | 577231 | 543515 | 270271 | 270271 |
| 200 | 6079559 | 4053039 | 6631675 | 1126015 | 1126015 |
| 250 | 13421671 | 22649071 | 20132507 | 19638399 | 13421671 |
| 275 | 13421671 | 22649071 | 20132507 | 20638335 | 13421671 |
| 300 | 145324775 | 96883183 | 56924955 | 63728127 | 56924955 |
| 330 | 145324775 | 96883183 | 217987163 | 63728127 | 63728127 |

The global record process is therefore better viewed as the lower envelope of four nondecreasing branch functions than as a Markov transition among residue classes.

## Consecutive-record geometry

For consecutive plateau values, the first parity divergence depth is exactly

\[
v_2(n_{i+1}-n_i),
\]

because length-k parity prefixes are in bijection with residues modulo \(2^k\).

For the current record chain these first divergences occur only about 2--7 steps from the root.  Over the common survival horizon, the parity-word Hamming distance has empirical mean about 0.458 of the horizon and median about 0.463.

Therefore a new global record is usually not a small terminal modification of the previous record path.  It is a winner switch between 2-adically separated basins whose long parity words are substantially different.

At depth five the entire survivor language already consists of exactly four residues

\[
\{7,15,27,31\}\pmod{32},
\]

and all four occur as winners somewhere in the current record chain.  Thus low-bit clustering itself is partly forced by the coefficient barrier; the nontrivial object is the competition between the four branch-minimum curves.

## Computational consequence

Use `collatz/src/minimal_survivor_mod32_profile.cpp` to compute a complete branch profile in one best-first traversal.  Use `collatz/src/minimal_survivor_interval_scan_mod32.cpp` for fast exact interval certificates after a plateau endpoint is known.

The next computational target is \(\mu(547)\), while the next structural target is a lower bound on each branch function \(\mu_a(K)\) or on their common lower envelope.
