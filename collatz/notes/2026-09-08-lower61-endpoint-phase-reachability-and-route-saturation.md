# Lower-61 endpoint-phase reachability and saturation of the 61+11 coefficient sieve

Date: 2026-09-08

Status: **DERIVED LEMMA + EXACT FINITE CERTIFICATE / ROUTE SATURATION.**

Global status: **Collatz remains OPEN.**

## 1. Question

MATH-006 established the exact 61+11 affine continuation

\[
N=a2^{61}+x,
\qquad
T^{61}(N)=T^{61}(x)+a3^{q_{61}(x)},
\]

and MATH-007 showed that, in the strongest low-surplus ranges, the surviving 340-label mask distinguishes all ambient endpoint phases

\[
y=T^{61}(x)\pmod{2048}.
\]

The next question was whether the actual lower-61 universal-spine language reaches only a small subset of these 2048 phases.

Define

\[
\operatorname{Reach}_{61}(q)
=
\left\{
T^{61}(x)\bmod2048:
0\le x<2^{61},
\ q_{61}(x)=q,
\ 3^{q_k(x)}\ge2^k\ \forall 1\le k\le61
\right\}.
\]

The prefix condition is exactly the coefficient-survival language already used by MATH-006/007.

## 2. Exact parity-word lift

Let a valid length-`k` parity prefix have canonical representative

\[
0\le x_k<2^k,
\qquad
y_k=T^k(x_k),
\qquad q_k=\#\{\text{odd bits in the prefix}\}.
\]

The two lifts of the same `k`-bit residue to length `k+1` are

\[
x_k,
\qquad x_k+2^k.
\]

After `k` shortcut steps their endpoints are exactly

\[
y_k,
\qquad y_k+3^{q_k}.
\]

Because `3^{q_k}` is odd, these two endpoints have opposite parity. Therefore for a prescribed next parity bit `b_k`, exactly one lift is admissible.

Writing

\[
e_k=b_k\oplus(y_k\bmod2),
\]

we obtain

\[
x_{k+1}=x_k+e_k2^k,
\qquad
z_k=y_k+e_k3^{q_k},
\]

and

\[
y_{k+1}=
\begin{cases}
 z_k/2,&b_k=0,\\[4pt]
 (3z_k+1)/2,&b_k=1.
\end{cases}
\]

Thus every parity word has one and only one ordinary integer representative in `[0,2^61)`, and its exact endpoint can be reconstructed without replacing the ordinary-integer lineage by a quotient representative.

## 3. Exact reachability result

The certificate generates universal-spine parity words in deterministic lexicographic order and reconstructs their exact ordinary starts.

For `q61=39,...,58`, the scan is stopped only after all 2048 endpoint residues have separately obtained and directly reverified ordinary-integer witnesses.

For `q61=59,60,61`, the complete valid parity-word languages are small enough to enumerate exhaustively.

The result is

\[
\boxed{
\#\operatorname{Reach}_{61}(q)=2048
\quad\text{for }39\le q\le58.
}
\]

The high-odd-count tail is

\[
\boxed{
\#\operatorname{Reach}_{61}(59)=1166,
\qquad
\#\operatorname{Reach}_{61}(60)=58,
\qquad
\#\operatorname{Reach}_{61}(61)=1.
}
\]

For `q61=61`, the unique word is the all-odd word and its canonical start is

\[
x=2^{61}-1,
\]

with

\[
T^{61}(x)\equiv274\pmod{2048}.
\]

### Deterministic witness-completion counts

The first lexicographic scan position at which all 2048 phases have explicit witnesses is:

| q61 | words scanned until all 2048 phases are witnessed |
|---:|---:|
| 39 | 14,954 |
| 40 | 15,131 |
| 41 | 18,417 |
| 42 | 13,048 |
| 43 | 19,853 |
| 44 | 16,848 |
| 45 | 15,409 |
| 46 | 16,130 |
| 47 | 14,917 |
| 48 | 18,355 |
| 49 | 21,604 |
| 50 | 18,493 |
| 51 | 20,103 |
| 52 | 19,877 |
| 53 | 15,039 |
| 54 | 18,840 |
| 55 | 21,077 |
| 56 | 17,266 |
| 57 | 14,187 |
| 58 | 19,822 |

These counts are reproducibility regressions, not probability estimates.

### Exhaustive high-q tail

- `q61=59`: 1,708 valid universal-spine words, 1,166 distinct endpoint phases.
- `q61=60`: 59 valid words, 58 distinct endpoint phases.
- `q61=61`: 1 valid word, 1 endpoint phase.

Sorted reachable-phase SHA-256 regressions:

```text
q59 c2d6c693dd3273eae6cea81d34d068df47277b995d2fafb2121564369dd09d8f
q60 7da3ed95ffb1b47a2e85d44029d665acef589ef13767499c3bd31e292743b11c
q61 718127812c05853f0bec61582a4a3840b1c844fe11fe1a004b5b7eb8b8b59846
```

## 4. Direct verification layer

Every retained witness is rerun under the shortcut map

\[
T(n)=
\begin{cases}
 n/2,&n\equiv0\pmod2,\\[4pt]
 (3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

The regression checks:

1. the direct parity sequence equals the generated parity word;
2. every prefix obeys
   \[
   3^{q_k}\ge2^k;
   \]
3. the direct final odd count is the requested `q61`;
4. the direct endpoint equals the lifted endpoint;
5. its residue modulo 2048 equals the recorded phase.

Hence the full-phase statements for `q=39,...,58` are constructive existence statements, not statistical coverage claims.

## 5. Consequence for MATH-006/007

The only `q61` ranges in which the MATH-006 coefficient-only 11-bit sieve can exclude any of the 340 block labels are

\[
q_{61}=39,40,41,42,43,44,45.
\]

For every one of these ranges,

\[
\boxed{
\operatorname{Reach}_{61}(q)=\mathbb Z/2048\mathbb Z.
}
\]

Therefore the ambient phase space used in MATH-006/007 is not an artifact of over-resolution. Every phase actually occurs in the lower-61 universal-spine candidate language.

In particular,

\[
\text{reachable-phase restriction}
\not\Rightarrow
\text{additional block-label elimination}
\]

for the current 61+11 coefficient-only transducer.

The earlier pointwise bound

\[
q_{61}=39
\Longrightarrow
\#\{\text{surviving labels at a fixed phase}\}\le47
\]

remains correct, but there is no smaller reachable phase set that turns those pointwise masks into a fixed global set of excluded labels.

## 6. Route classification

This closes the proposed next branch as a **SATURATED ROUTE**, not as a contradiction in the underlying theorems.

Survives:

- exact 61+11 affine transducer;
- pointwise 47/141/235/... label caps;
- right-congruence barrier;
- ordinary-integer lineage.

Closed:

- the hope that lower-61 universal-spine phase reachability alone is sparse enough to sharpen the coefficient-only label sieve.

The restricted phase sets at `q61=59,60,61` do not help this sieve because MATH-006 already has the trivial mask there: every one of the 340 labels survives the coefficient condition through depth 72 for all `q61>=46`.

## 7. Next proof-facing target

The next state refinement must carry a **new same-integer observable**, not merely a coarser or reachable subset of `(q61,y mod2048)`.

The highest-value candidates are:

1. correction/address order information that distinguishes starts within the same endpoint phase;
2. endpoint/Hensel eligibility beyond the coefficient-only depth-72 sieve, with the existing non-independence rule preserved;
3. an address-local invariant inside the already certified `<2^35` adjacent-block halos.

Any such refinement must preserve the exact ordinary start and must not count endpoint quotienting and root-Hensel maximality as independent filters.

## 8. Evidence

Exact certificate:

`collatz/src/2026_09_08_lower61_endpoint_phase_reachability_certificate.py`

Certificate commit:

`764696d443c10cfbebd610893f0e517182a08512`

No new external theorem is imported. The parity-vector residue uniqueness used by the construction was already audited as safe external prior art; the actual witness reconstruction and shortcut-map checks in this note are internal exact arithmetic.

## 9. Prohibited upgrades

- do not interpret the lexicographic completion counts statistically;
- do not infer that all ordinary starts are covered by the witness subset;
- do not discard the valid pointwise MATH-006 caps merely because the reachability refinement saturates;
- do not use the restricted `q59..61` phases as pruning where all 340 labels already survive;
- do not infer first-cell closure or the Collatz conjecture from this route saturation.
