# A0 s=1 checkpoint terminal-residue join audit

Date: 2026-08-29

Status: **EXACT interface theorem + SAFE finite-corridor bounds.**

Certificate:

`collatz/src/A0_s1_checkpoint_terminal_residue_join_certificate.py`

This note does **not** close the long correction-language membership gate. Its purpose is to remove an ambiguity in the previous boundary-window description and to define a legal synchronized interface for the next Route-B computation.

## 1. Affine checkpoint identity

For a length-`n` parity word with `q` odd events at zero-based positions

\[
a_1<\cdots<a_q,
\]

the exact affine identity is

\[
2^n Z=3^qX+C,
\]

with

\[
C=\sum_{r=1}^{q}3^{q-r}2^{a_r}.
\]

For the A0 `s=1` pre bridge,

\[
n=t_0=104398605910,
\qquad
q=j_0=65868186701.
\]

## 2. Terminal cancellation theorem

Fix `k<=q` and reduce the affine identity modulo `3^k`.

Because

\[
3^qX\equiv0\pmod{3^k},
\]

and `2^n` is invertible modulo `3^k`, one obtains

\[
\boxed{
Z\equiv 2^{-n}C\pmod{3^k}.
}
\]

Moreover every correction term with `q-r>=k` is itself divisible by `3^k`. Hence only the final `k` odd-ordinal correction terms survive:

\[
\boxed{
Z\equiv
2^{-n}
\sum_{r=q-k+1}^{q}3^{q-r}2^{a_r}
\pmod{3^k}.
}
\]

Therefore the terminal correction gives the checkpoint `3`-adic address **without knowing X**.

For the certified boundary depth this specializes to

\[
\boxed{
C_{\mathrm{terminal},28}
\Longrightarrow
Z\bmod3^{28}.
}
\]

This is the correct interpretation of the 28-trit checkpoint channel.

## 3. Debit-channel correction

The physical debit satisfies

\[
\boxed{L_-=3X-Z.}
\]

Therefore

\[
L_-\equiv
3X-2^{-n}C_{\mathrm{terminal},k}
\pmod{3^k}.
\]

The factor `3` lowers the required X precision by one ternary digit:

\[
\boxed{
L_-\bmod3^k
\text{ depends on }
X\bmod3^{k-1}
\text{ and the final }k\text{ correction trits.}
}
\]

In particular,

\[
L_-\bmod3^{24}
\]

needs only

\[
X\bmod3^{23},
\]

not `X mod 3^24`.

However this dependence does **not** disappear. Thus the previous shorthand “24 trits expose `L_-`” must not be read as an independent terminal-language exposure.

### DSD correction

**REJECTED:** terminal 24 trits alone determine the ordinary debit.

**EXACT:** terminal 24 correction trits plus `X mod 3^23` determine `L_- mod 3^24`; because the present debit corridor is narrower than `3^24`, that residue then selects at most one ordinary debit value.

This distinction prevents a circular use of `L_-` to recover `X` while simultaneously using `X` to define the debit residue.

## 4. Checkpoint CRT singleton remains exact

The current checkpoint interval is

\[
7083549723369539339554
\le Z\le
9444732965739290427391,
\]

with width

\[
2361183242369751087837.
\]

The mixed-radix modulus is

\[
2^{27}3^{28}
=
3070471107232407748608,
\]

and therefore

\[
\boxed{
2^{27}3^{28}>Z_{\max}-Z_{\min}.
}
\]

Consequently any coherent pair

\[
\left(Z\bmod2^{27},\ Z\bmod3^{28}\right)
\]

selects at most one ordinary checkpoint `Z` in the current interval.

No independence assumption is involved: both residues must belong to the same checkpoint.

## 5. Join with the 14 first-defect roots

The current long-membership forest has the surviving first-defect set

\[
F_{14}=\{2,5,8,10,13,16,18,21,24,27,29,32,35,37\}.
\]

For shell `f`,

\[
X\equiv X_{th}+2^f\pmod{2^{f+1}},
\]

where

\[
X_{th}=4697939311072332635131.
\]

If the checkpoint dyadic address

\[
z_2=Z\bmod2^{27}
\]

is exposed, then from `L_-=3X-Z`

\[
\boxed{
L_-\equiv
3(X_{th}+2^f)-z_2
\pmod{2^{m_f}},
}
\]

with

\[
m_f=\min(f+1,27).
\]

Thus one checkpoint dyadic address converts every first-defect shell into a deterministic debit dyadic residue class.

## 6. Exact finite-corridor upper bounds

The debit corridor contains

\[
934928480993-669562762561+1
=
265365718433
\]

ordinary integers.

For a fixed residue modulo `2^m`, at most

\[
\left\lceil\frac{265365718433}{2^m}\right\rceil
\]

can occur.

The resulting shell-wise deterministic upper bounds are:

| first defect `f` | exposed debit bits `m_f` | max ordinary `L_-` candidates |
|---:|---:|---:|
| 2 | 3 | 33,170,714,805 |
| 5 | 6 | 4,146,339,351 |
| 8 | 9 | 518,292,419 |
| 10 | 11 | 129,573,105 |
| 13 | 14 | 16,196,639 |
| 16 | 17 | 2,024,580 |
| 18 | 19 | 506,145 |
| 21 | 22 | 63,269 |
| 24 | 25 | 7,909 |
| 27 | 27 | 1,978 |
| 29 | 27 | 1,978 |
| 32 | 27 | 1,978 |
| 35 | 27 | 1,978 |
| 37 | 27 | 1,978 |

These are **not probabilities** and they are **not multiplied by marginal language densities**. They are exact worst-case cardinality bounds for one congruence class inside a finite ordinary interval.

## 7. Correct synchronized interface

The safe next interface is therefore not

\[
(\text{independent }L_-\text{ trits})
\]

but

\[
\boxed{
\text{terminal correction}
\longrightarrow Z_3,
\qquad
\text{tail/checkpoint channel}
\longrightarrow Z_2,
}
\]

followed by

\[
\boxed{
(Z_2,Z_3)\longrightarrow Z
}
\]

and, for each first-defect root,

\[
\boxed{
(f,Z_2)\longrightarrow
L_-\bmod2^{m_f}.
}
\]

Only after a concrete ordinary `Z` and a compatible ordinary debit candidate are present may one form

\[
\boxed{
X=\frac{Z+L_-}{3}
}
\]

and test the full shell, physical interval, ballot/correction, and deterministic-continuation predicates.

This ordering avoids circular dependence.

## 8. Negative result from the current audit

No first-defect shell is closed merely by the algebra above.

The exact first-75 completion-defect oracle remains valid, but using it as a naive binary-prefix search engine grows to millions of states before useful depth. Therefore that implementation strategy is classified as:

**REJECTED AS SEARCH ENGINE, NOT REJECTED AS MATHEMATICS.**

The terminal ternary projection is also known to be highly saturated; terminal residue exposure alone must not be mistaken for long correction-language sparsity.

## 9. Current OPEN gate

The remaining decisive question is still

\[
\boxed{
C_{req}(X,Z)\in\mathcal C_{pre}\ ?
}
\]

but the boundary state is now cleaner:

1. generate or reject a coherent checkpoint residue pair from the long correction/tail language;
2. recover the unique ordinary checkpoint when the pair lies in the physical interval;
3. join that checkpoint to one of the 14 dyadic roots;
4. enumerate only the deterministic debit residue class allowed by that join;
5. reconstruct and audit the resulting ordinary `X` candidates;
6. keep C4F/renewal-gap/global formation compatibility as a separate OPEN predicate unless an exact invariant is supplied.

## 10. DSD classification

### EXACT

- affine checkpoint identity;
- terminal `k` odd-ordinal correction terms determine `Z mod 3^k` independently of X;
- `L_- mod 3^k` depends on `X mod 3^(k-1)` plus terminal correction data;
- `27` dyadic checkpoint bits + `28` checkpoint trits are injective on the current Z interval;
- shell `f` + `Z mod 2^27` determines `L_- mod 2^min(f+1,27)`.

### SAFE

- the displayed debit-candidate counts are worst-case finite-corridor upper bounds.

### REJECTED

- interpreting the 24-trit debit window as an X-independent terminal exposure;
- multiplying independent-looking boundary cardinalities without a proof of independence;
- using the exact completion-defect DP as an uncompressed binary-tree search engine.

### OPEN

- coherent long-language realization of the checkpoint residues;
- full correction-language membership/nonmembership;
- C4F / renewal-gap / global formation compatibility;
- global Collatz branch completeness.

No Collatz proof is claimed.
