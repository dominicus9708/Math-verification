# A0 s=1: 72-bit deterministic formation bridge

Date: 2026-08-28

Status: **SAFE exact finite-parity/address reduction.** This note deliberately does not identify the separate working label `C4F` with finite parity formation.

## 1. Input shell

The previously certified A0 s=1 necessary bound is

\[
2^{71}<X\le X_{\max}<2^{72},
\qquad
X_{\max}=3295414002074039191016.
\]

Hence every physical A0 start is represented by its ordinary integer value in the complete residue window modulo `2^72`.

## 2. Universal parity address

For a parity word

\[
w=(b_0,\ldots,b_{n-1}),
\]

let the one positions be `a_r` in zero-based coordinates. Define

\[
A_K(w)
:=
-\sum_{r}2^{a_r}3^{-r}\pmod{2^K}.
\]

For `K=n`, this is the standard exact Collatz parity conjugacy address. Therefore

\[
\boxed{
A_n:\{0,1\}^n\longrightarrow \mathbb Z/2^n\mathbb Z
}
\]

is a bijection: every length-`n` parity word is realized by exactly one residue class modulo `2^n`.

The accompanying certificate exhaustively regresses this statement for all words through length 9 and checks direct orbit recovery.

## 3. 72-bit determinization theorem for A0

Let `w` be any proposed parity word of length at least 72. If it is realized by a physical A0 integer `X`, then necessarily

\[
\boxed{
X=A_{72}(w_{<72}).
}
\]

There cannot be two different A0 starts with the same first 72 parity bits because both starts lie strictly below `2^72` and the address is unique modulo `2^72`.

Consequently, once depth 72 is reached, the future parity sequence is not an abstract choice. It is the deterministic Collatz orbit of that one integer `X`.

Thus any candidate tail that disagrees with the actual orbit after depth 72 is nonphysical and may be pruned at its first disagreement.

## 4. Endpoint-odd formation is already encoded

The endpoint-odd formation residue used in the earlier Christoffel formation notes does not require a new independent state coordinate.

If `q` is the number of ones in `w`, then

\[
\boxed{
\rho(w)
=A_{n+1}(w1)
=A_{n+1}(w)-2^n3^{-(q+1)}
\pmod{2^{n+1}}.
}
\]

This is exactly the endpoint term appearing in the earlier tri-place formation formula.

Therefore **finite parity formation plus endpoint oddness** is reconstructible from the ordinary address state once sufficient 2-adic precision is retained.

## 5. Relation to the Christoffel tri-place defect

The earlier Christoffel defect note introduced

\[
\eta(s)=\frac{\mathcal E(s)}{3^H}
\]

and showed that the same coordinate controls

1. Archimedean shadow lowering,
2. the 2-adic formation-address shift,
3. the modular renewal-gap shift.

The present theorem resolves only item 2 for the finite A0 parity word: after 72 bits its ordinary integer start is exposed exactly.

Items 1 and 3 remain independent renewal/gap gates. They must not be erased merely because the finite parity address has become deterministic.

## 6. DSD audit of `C4F`

The current composable ballot/address state explicitly stated that it did **not** certify `C4F`. Inspection of the renewal-shadow, two-block, debit-only formation, tri-place defect, square-prefix formation, Hensel-budget, checkpoint, and local-gap records yields the following safe separation:

### SAFE

- pure-ballot composition;
- finite 2-adic parity address;
- endpoint-odd formation residue;
- after 72 bits, unique ordinary A0 start `X`;
- deterministic physical continuation from that `X`.

### NOT YET IDENTIFIED WITH `C4F`

- renewal-floor compatibility;
- modular gap compatibility;
- any global or multi-checkpoint predicate that the working label `C4F` may have been intended to denote.

Therefore the legal inference is

\[
\boxed{
\text{finite parity formation is resolved at depth 72}
}
\]

but not

\[
\boxed{
\text{C4F is resolved}.
}
\]

This prevents an illegal state merge while still removing one previously ambiguous memory component.

## 7. Target regression

For the exact threshold prefix,

\[
A_{72}(W_{\rm th,<72})
=4697939311072332635131.
\]

This lies inside `(2^71,2^72)` but exceeds the previously certified A0 upper bound `X_max`. Hence the exact threshold address is already excluded by the A0 bound.

If the upper bound is temporarily ignored and this address is iterated directly, the first disagreement with the infinite threshold word occurs at zero-based position 74, i.e. the 75th parity bit. This agrees with the earlier block-jump audit.

## 8. Consequence for the next block-jump stage

For any DAG or Christoffel block decomposition, the safe merge protocol is now:

1. before depth 72, compose `(n,q,dq,s_min,D,A_72)` exactly;
2. at depth 72, reject addresses outside the physical A0 interval or above `X_max`;
3. for a surviving address, set `X=A_72` as an ordinary integer;
4. from then on, compare every proposed abstract block with the deterministic orbit of `X` and prune at the first mismatch;
5. keep renewal/gap/`C4F` constraints as separate filters until their exact predicate is recovered.

The key gain is that no additional hidden **finite-parity formation history** is required after the 72-bit exposure point.

This is a structural reduction, not a proof of the Collatz conjecture.
