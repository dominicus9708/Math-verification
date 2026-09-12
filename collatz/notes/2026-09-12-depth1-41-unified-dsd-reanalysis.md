# Unified DSD reanalysis and re-audit of Collatz depths 1--41

Date: 2026-09-12

Status: `EXACT FINITE RE-AUDIT / DEPTH 1--41 COVERED / COMMON-STATE REDUCTION / GLOBAL COLLATZ OPEN`

This note re-audits the existing depth results under the current DSD analysis rules. It deliberately excludes paid-count layers `2<=r<=13`, because those layers have not yet been closed and the user requested that unperformed layers not be folded into this audit.

The purpose is not to rerun every raw parity word. The canonical exact ledgers and prior exact dynamics audit are treated as input evidence, and their lineage, accounting, state sufficiency, and compatibility with the newer `(S,rho,Omega,R,address)` description are checked again.

## 1. Audit scope

Included:

- depth `1..41` prefix coefficient-survival language;
- exact depth-state dynamics through depth 32 from the integrated DSD audit;
- endpoint/block representation and same-depth endpoint quotient through depth 32;
- q-partitioned one-sided Hensel ledgers at depths 32--34;
- complete one-sided Hensel ledgers at depths 35--41;
- exact nested survivor lineage from depth 32 through 41;
- the MATH-051 fixed-d / bounded-carry representation;
- MATH-072 common-coordinate identities.

Excluded from any closure claim:

- paid-count layers `2<=r<=13`;
- first universal Farey cell emptiness;
- later Farey cells;
- the full Collatz conjecture.

## 2. Exact coefficient-prefix language through depth 41

At every prefix depth `j`, coefficient survival is

\[
3^{q_j}\ge2^j.
\]

Define

\[
q_{\min}(j)=\min\{q:3^q\ge2^j\}.
\]

The coefficient language consists of parity words whose every prefix satisfies

\[
q_j\ge q_{\min}(j).
\]

The new certificate recomputes this language by exact integer dynamic programming. No floating point threshold is used.

| depth k | q_min(k) | coefficient language L_k |
|---:|---:|---:|
|1|1|1|
|2|2|1|
|3|2|2|
|4|3|3|
|5|4|4|
|6|4|8|
|7|5|13|
|8|6|19|
|9|6|38|
|10|7|64|
|11|7|128|
|12|8|226|
|13|9|367|
|14|9|734|
|15|10|1,295|
|16|11|2,114|
|17|11|4,228|
|18|12|7,495|
|19|12|14,990|
|20|13|27,328|
|21|14|46,611|
|22|14|93,222|
|23|15|168,807|
|24|16|286,581|
|25|16|573,162|
|26|17|1,037,374|
|27|18|1,762,293|
|28|18|3,524,586|
|29|19|6,385,637|
|30|19|12,771,274|
|31|20|23,642,078|
|32|21|41,347,483|
|33|21|82,694,966|
|34|22|151,917,636|
|35|23|263,841,377|
|36|23|527,682,754|
|37|24|967,378,591|
|38|24|1,934,757,182|
|39|25|3,611,535,862|
|40|26|6,402,835,000|
|41|26|12,805,670,000|

The anchor values `L_20=27,328`, `L_24=286,581`, `L_28=3,524,586`, `L_32=41,347,483`, and all `L_32..L_41` values reproduce the canonical repository results.

When `q_min` does not rise, every admissible prefix has both coefficient-admissible children and the language doubles. Examples are

\[
L_{33}=2L_{32},\qquad
L_{36}=2L_{35},\qquad
L_{38}=2L_{37},\qquad
L_{41}=2L_{40}.
\]

When `q_min` rises, the lower-q child layer is deleted exactly. This is a Beatty/mechanical boundary event, not a statistical pruning rule.

## 3. Re-audit of the original DSD depth state

The integrated depth-32 DSD audit used

\[
\Xi_k=(r_k,y_k,R_k,u_k,v_k,Q_k,e_k),
\]

with

\[
u_k=3^{Q_k},\qquad v_k=2^k,
\]

and exact closure identity

\[
\boxed{v_k y_k=u_k r_k+R_k}.
\]

That audit checked 100,701,368 exact branch transitions through depth 32 with zero closure failures and zero transition-identity failures.

Under the current notation put

\[
q=Q_k,
\qquad
S=\frac{R_k}{3^q},
\qquad
\rho=\frac{2^k}{3^q}.
\]

Dividing the closure identity by `3^q` gives

\[
\boxed{\rho y=r+S},
\]

hence

\[
\boxed{y=\frac{r+S}{\rho}}.
\]

This exposes redundancy in the older state description. At fixed depth, the following quantities are derived:

\[
u=3^q,\quad v=2^k,\quad R=3^qS,\quad \rho=2^k/3^q,\quad y=(r+S)/\rho,
\]

and the old coefficient excess `e` is determined by `(k,q)`.

Thus an exact reduced depth state may be represented as

\[
\boxed{(k,q,r,S)}
\]

or, when coupling to the phase description,

\[
\boxed{(r,S,\rho,\Omega)}.
\]

The address `r` is irreducible: replacing it by a real interval or by `S` alone would lose exact future compatibility.

## 4. Exact transition agreement with MATH-072

For the normalized correction and inverse coefficient ratio,

\[
S=\frac{C}{3^q},\qquad \rho=\frac{2^k}{3^q},
\]

one parity extension obeys

\[
\begin{array}{c|cc}
& S'&\rho'\\
\hline
\text{even}&S&2\rho\\
\text{odd}&S+\rho/3&(2/3)\rho.
\end{array}
\]

MATH-051's fixed-d signature satisfies

\[
\boxed{\Sigma=S+\rho-1}.
\]

Therefore

\[
\begin{array}{c|c}
\text{even}&\Sigma'=\Sigma+\rho\\
\text{odd}&\Sigma'=\Sigma.
\end{array}
\]

The old depth-state dynamics and the new depth/Hensel/paid common-coordinate dynamics are therefore algebraically compatible; they are not independent empirical descriptions.

## 5. Endpoint quotient and Hensel relation

From

\[
y=(r+S)/\rho,
\]

a same-depth endpoint equality is

\[
\frac{r_1+S_1}{\rho_1}
=
\frac{r_2+S_2}{\rho_2}.
\]

At fixed `(k,q)`, `rho` is fixed, so endpoint coincidence requires

\[
\Delta r=-\Delta S.
\]

Because `r` is integral, integral `Delta S` is the natural exact translation condition. This is the same integer-translation quantity tested by the fixed-d Hensel signature, where

\[
\Delta S=\Delta\Sigma.
\]

DSD boundary: integrality of `Delta S` describes a translation/Hensel compatibility class. It must not by itself be upgraded to equality of the actual canonical source addresses; the exact dyadic address relation remains necessary.

## 6. Nested Hensel ledger lineage, depths 32--41

The q-layer canonical ledgers were rechecked under the current same-candidate-lineage rule.

For every depth `k=33,...,41` and every admissible q layer, the pre-Hensel population is exactly

\[
\boxed{
P_{k,q}=S_{k-1,q}+S_{k-1,q-1},
}
\]

where `S_{k-1,q}` is the prior-depth nested survivor count and layers below the new coefficient threshold are removed.

The identity passes at every q-layer of every depth 33--41. Hence the later ledgers are one exact nested survivor chain, not independent flat samples.

Totals:

| depth | coefficient language | nested prefilter | nested survivors | newly pruned | cumulative removed |
|---:|---:|---:|---:|---:|---:|
|32|41,347,483|33,894,412|33,880,411|14,001|7,467,072|
|33|82,694,966|67,760,822|67,727,277|33,545|14,967,689|
|34|151,917,636|124,547,105|124,486,440|60,665|27,431,196|
|35|263,841,377|216,540,217|216,467,460|72,757|47,373,917|
|36|527,682,754|432,934,920|432,738,821|196,099|94,943,933|
|37|967,378,591|794,068,949|793,742,593|326,356|173,635,998|
|38|1,934,757,182|1,587,485,186|1,586,644,081|841,105|348,113,101|
|39|3,611,535,862|2,964,038,401|2,962,750,556|1,287,845|648,785,306|
|40|6,402,835,000|5,259,076,592|5,257,502,632|1,573,960|1,145,332,368|
|41|12,805,670,000|10,515,005,264|10,511,130,714|3,874,550|2,294,539,286|

For every row,

\[
\boxed{P_k-S_k=\text{newly pruned}_k}
\]

and

\[
\boxed{L_k-S_k=\text{cumulative Hensel removed}_k}.
\]

No unexplained count category remains in these ledgers.

## 7. DSD interpretation of the Hensel data

Two finite patterns are visible in depths 32--41.

First, cumulative Hensel removal remains near 18% of the coefficient language:

- depth 32: about 18.059%;
- depth 41: about 17.918%.

Second, each *new* depth removes only a small fraction of its nested prefilter, roughly 0.03--0.05% in this range.

At depth 41, 3,835,337 of 3,874,550 newly pruned states occur in `q<=29`, i.e. within three q-levels of the lower coefficient boundary `q_min=26`. This is about 98.99% of the new pruning.

These are finite structural observations, not asymptotic theorems. They suggest that one-sided Hensel dominance acts mainly as a near-boundary compression channel rather than as a rapidly strengthening global descent mechanism.

## 8. Finite-state compression audit

MATH-051 replaces raw fixed-d parity words by

\[
\text{gap signature}
\to
\text{bounded carry}
\to
\text{viable competitor subset}.
\]

The primitive future-viability state is of the form

\[
(rem,n_A,n_B,h),
\]

and histories with identical future competitor/carry subsets are merged.

This is a valid quotient for the specific question "can a positive exact Hensel translation witness still exist?".

It is **not** a sufficient quotient for arbitrary future Collatz compatibility. Exact macro compatibility still depends on a 2-adic source/endpoint address. Therefore the current address state must remain split as

\[
\boxed{
\mathcal A=(\mathcal A_{compat},\mathcal A_{dom}).
}
\]

Here `A_compat` is the exact dyadic compatibility coordinate, while `A_dom` is the Hensel/carry dominance coordinate.

## 9. Depth-by-depth audit verdict

### Depths 1--31

PASS for exact coefficient-prefix formation and exact single-channel/block transition architecture. These depths are contained in the prior exhaustive depth-32 dynamics audit, which reported zero closure and transition-identity failures.

No claim is made that every depth 1--31 has a separately published modern fixed-d Hensel ledger. Their role in this re-audit is the exact prefix/state-dynamics chain leading into the canonical depth-32 checkpoint.

### Depth 32

PASS as the bridge depth:

- full coefficient language `41,347,483`;
- integrated DSD dynamics audit available;
- q-partitioned one-sided Hensel ledger available;
- nested survivors `33,880,411`.

### Depths 33--34

PASS under q-partitioned one-sided Hensel ledgers and exact nested-lineage regression. Depth 34 explicitly records four candidate-class representation collisions; they are accounted for in the distinct-class column and do not create hidden state loss.

### Depths 35--40

PASS under complete one-sided Hensel ledgers. Different exact implementations (residue buckets, shards, tail hashes) change representation cost but preserve the same candidate semantics and nested survivor accounting.

### Depth 41

PASS as a complete finite-state one-sided Hensel checkpoint:

\[
L_{41}=12,805,670,000,
\]

\[
P_{41}=10,515,005,264,
\]

\[
S_{41}=10,511,130,714.
\]

The finite-state method is validated backward against canonical depth-40 central layers. It remains a finite depth result, not a uniform bound for arbitrary depth.

## 10. Common-state result of the reanalysis

The strongest current exact common description is

\[
\boxed{
(k,q,r,S)
}
\]

with optional derived/common coordinates

\[
\rho=2^k/3^q,
\qquad
\Sigma=S+\rho-1,
\qquad
\rho=2^{-u}\Omega.
\]

For paid/Bellman work the useful expanded state remains

\[
\boxed{
(S,\rho,\Omega,R,\mathcal A_{compat},\mathcal A_{dom})
}
\]

where `R` denotes address-resolution height, not the older correction numerator.

This notation distinction is mandatory: the old depth-state symbol `R_k` was the correction numerator, while the newer resolution potential uses `R(M)=ceil(log2 M)`. They must not be conflated.

## 11. What this re-audit establishes

Established:

1. exact coefficient-prefix counts for every depth 1--41;
2. compatibility of the old DSD depth state with the new `(S,rho,Sigma)` coordinates;
3. exact nested Hensel lineage from depth 32 to 41;
4. complete Hensel accounting for every canonical ledger depth 32--41;
5. separation of dyadic future compatibility from Hensel dominance state;
6. no evidence of an internal contradiction among the canonical depth 1--41 results under the current DSD claim rules.

Not established:

- a uniform finite-state bound for arbitrary depth;
- that the approximately 18% Hensel-removal fraction converges;
- that low-q pruning concentration persists indefinitely;
- that Hensel dominance alone closes a Collatz path;
- first-cell emptiness;
- the Collatz conjecture.

## 12. Reproducibility

New unified certificate:

`collatz/src/2026_09_12_depth1_41_unified_dsd_reaudit_certificate.py`

Canonical source inputs include:

- `collatz/notes/2026-08-11-dsd-dynamics-integrated-audit.md`;
- `collatz/results/2026-09-08-depth32-q-partitioned-one-sided-hensel.tsv`;
- `collatz/results/2026-09-08-depth33-q-partitioned-one-sided-hensel.tsv`;
- `collatz/results/2026-09-08-depth34-q-partitioned-one-sided-hensel.tsv`;
- `collatz/results/2026-09-09-depth35-complete-one-sided-hensel.tsv`;
- `collatz/results/2026-09-10-depth36-complete-one-sided-hensel.tsv`;
- `collatz/results/2026-09-10-depth37-complete-one-sided-hensel.tsv`;
- `collatz/results/2026-09-10-depth38-complete-one-sided-hensel.tsv`;
- `collatz/results/2026-09-10-depth39-complete-one-sided-hensel.tsv`;
- `collatz/results/2026-09-10-depth40-complete-one-sided-hensel.tsv`;
- `collatz/results/2026-09-10-depth41-complete-one-sided-hensel.tsv`;
- MATH-051 and MATH-072.
