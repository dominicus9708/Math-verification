# Predicate activation schedule for source-family realization

Status: **EXACT / CLOSED for the stated activation and locality interfaces**

## Purpose

The active A0 `s=1` Route-B family state must not carry every later predicate from the beginning of the pre-bridge.  Exact correction locality shows that several coordinates are needed only at specific boundaries.

This theorem records the smallest currently justified activation schedule.  It does not define or discharge any still-undefined external predicate such as the working-label `C4F`.

## 1. Persistent source payload

At an active prefix depth `h`, retain the exact source/current-state cylinder

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

with its exact finite parameter interval.

Under pure-ballot control write

\[
S=q-Q(h),
\qquad
Q(h)=\lceil h\log_3 2\rceil.
\]

Then

\[
q=Q(h)+S,
\]

so the coefficient `3^q` is derived from `(h,S)` and is not an independent persistent state coordinate.

The source residue `r`, by contrast, must be retained whenever a later predicate can inspect the ordinary source integer `X`.

## 2. Block grammar is transient computation, not automatically a persistent axis

For any certified fixed parity block `B` with

\[
|B|=b,
\qquad
q(B)=p,
\qquad
C(B)=\gamma,
\]

the exact multibit source-channel transducer can consume the block directly.

A grammar such as H/L may therefore be used to *generate* certified triples `(b,p,gamma)` and admissibility conditions for the next transition.

Unless an additional future predicate is proved to depend on a grammar-history label after the block has been consumed, that label is not automatically a persistent state coordinate.

In particular, the H/L representation must not be counted as an independent probabilistic or pruning channel when it represents the same formation language already being enforced.

## 3. Terminal ternary checkpoint locality

Let the complete pre-checkpoint parity word split as

\[
W=AB,
\]

where the suffix `B` contains exactly the final `K` one-events of `W`. Thus

\[
q(B)=K.
\]

Correction composition gives

\[
C(W)=3^K C(A)+2^{|A|}C(B).
\]

If `X` is the pre-word source and `Z=T^{|W|}(X)` is the checkpoint, then

\[
2^{|W|}Z=3^{q(W)}X+C(W).
\]

Reduce modulo `3^K`. Since `q(W)>=K`, both the source term `3^{q(W)}X` and the prefix correction term `3^K C(A)` vanish. Therefore

\[
2^{|W|}Z
\equiv
2^{|A|}C(B)
\pmod{3^K}.
\]

Because `2` is invertible modulo `3^K`, and `|W|=|A|+|B|`,

\[
\boxed{
Z\equiv 2^{-|B|}C(B)\pmod{3^K}.
}
\]

Hence the prefix `A` exports **zero ternary checkpoint digits** once the suffix `B` containing the final `K` one-events is retained.

### Current specialization

For the synchronized Route-B checkpoint seam,

\[
K=28.
\]

Thus

\[
\boxed{
Z\bmod 3^{28}
}
\]

need not be carried during the early or middle pre-bridge. It activates only when the computation enters the suffix containing the final 28 one-events.

This agrees with the existing lazy-terminal-observation and critical-cut precision-absorption theorems.

## 4. Post-checkpoint dyadic activation

The first `L` parity symbols beginning at the ordinary checkpoint `Z` determine exactly one starting residue

\[
Z\pmod{2^L}
\]

through the ordinary parity-address bijection.

For the current synchronized seam,

\[
L=27.
\]

Therefore

\[
\boxed{
Z\bmod2^{27}
}
\]

is a post-checkpoint / tail observation. It need not be carried as a pre-bridge S10 coordinate.

Once the coherent pair

\[
(Z\bmod2^{27},\;Z\bmod3^{28})
\]

is available, the existing synchronized CRT singleton theorem may be invoked in its certified corridor.

## 5. Local same-orbit provenance activates only after a coherent splice

For a pre-checkpoint suffix `b` and post-checkpoint prefix `v`, the existing local-splice theorem combines their compatible ternary and dyadic observations by CRT. If the reconstructed pre-suffix source is a positive integer, the concatenation is an actual accelerated-Collatz orbit segment through the checkpoint.

Therefore a separate permanent `same-orbit provenance` label is not required before the observations that define the splice exist.

This does not permit checkpoint exposure to be treated as same-orbit compatibility automatically; the certified CRT/positivity hypotheses must still be checked.

## 6. Current state schedule

### Early / middle S10 pre-bridge

Persistent exact state:

\[
\boxed{
(r,y,[m_{lo},m_{hi}],h,S)
}
\]

plus only predicate labels that are already defined and currently active at that resolution.

Derived, not persistent:

\[
q=Q(h)+S,
\qquad
3^q.
\]

Transient:

- certified block/H-L grammar labels used only to generate the next block transition;
- correction values already discharged by residual recursion.

Inactive:

- `Z mod 3^28` before the final-28-one suffix;
- `Z mod 2^27` before the post-checkpoint 27-bit prefix;
- same-orbit splice status before coherent boundary observations exist;
- any undefined `C4F` coordinate.

### Final-28-one suffix

Activate

\[
Z\bmod3^{28}
\]

through terminal correction locality.

### Checkpoint / S11 tail entrance

Activate

\[
Z\bmod2^{27}
\]

from the first 27 post-checkpoint parity bits, then synchronize by the certified CRT seam and test the local-splice/debit hypotheses at their proper resolution.

## 7. DSD interpretation

This is a predicate-relative describability schedule:

- retain a coordinate while some unresolved future predicate can distinguish it;
- derive coordinates that are exact functions of retained state rather than duplicating them;
- activate observations only when their supporting local data exists;
- forget consumed local information only after an exact theorem proves that no later active predicate needs it.

The schedule is a state-minimization theorem, not a candidate-rejection theorem.

## Scope restrictions

This theorem does **not** prove:

- that H/L blocks alone realize the complete Route-B language;
- that any particular source family survives or fails;
- that the synchronized checkpoint pair will necessarily be exposed;
- any property of the working-label `C4F` beyond the fact that an undefined predicate cannot justify an invented state coordinate;
- S11 tail closure;
- A0 `s=1` Route-B closure;
- Collatz.

## Certificate

- `../src/A0_s1_checkpoint_late_activation_certificate.py`

Finite exhaustive checks in the certificate are regression guards. The ternary locality statement is the exact correction-composition argument above.
