# S10 pure-ballot correction-language audit

Date: 2026-09-03

Status: **EXACT language recursion CLOSED / independent S10 pruning engine REJECTED / compressed exact quotient OPEN**

Canonical theorem:

- `../theorems/PURE_BALLOT_CORRECTION_LANGUAGE_RECURSION.md`.

Certificate:

- `../src/A0_s1_pure_ballot_correction_language_recursion_certificate.py`.

## Audited question

Can the exact set of pure-ballot correction values for a fixed remaining length and one-count provide a new whole-family S10 contraction mechanism, stronger than the already certified residual valuation decoder and affine valuation-cylinder refinement?

## D — Domain

The audited object is

\[
\mathcal C^{\mathrm{bal}}_{n,p}(h,S),
\]

the corrections of length-`n`, exactly-`p`-one suffixes that remain pure-ballot when appended to an already legal state at absolute depth `h` with surplus `S`.

This audit is pre-checkpoint. It does not activate debit, post-checkpoint dyadic residues, or same-orbit splice predicates.

## R — Resolution

The theorem keeps exact integer corrections, not floating-point envelopes or densities.

For each word with first one-position `a`,

\[
C=3^{p-1}2^a+2^{a+1}C_{tail}.
\]

Hence the first branch is observable exactly from

\[
a=v_2(C).
\]

No residue truncation is used in the theorem.

The executable certificate performs finite direct-word regressions only. Those regressions are implementation evidence, not the proof of the algebraic recursion.

## S — State sufficiency

For the pure-ballot language alone, `(n,p,h,S)` is sufficient:

- `n` = remaining raw-bit length;
- `p` = remaining one-count;
- `h` = current absolute depth;
- `S` = current pure-ballot surplus.

For the active fixed Route-B target, `n` and `p` are derivable from the persistent source state `(h,S)` and target constants, so this theorem does not justify adding them as independent persistent S10 coordinates.

The language state is not sufficient for source-sensitive predicates because it omits `(r,y,[m_lo,m_hi])` and all late observations.

## E — Equivalence

The first-one recursion is exact and bidirectional.

For `p>0`, different first-one branches are disjoint because

\[
v_2(C)=a_1.
\]

At fixed `(n,p)`, the existing correction-language injective decoder then identifies the complete parity word from the exact correction.

However, equality of a correction-language control state does not imply equality of source families. No source-payload merge is licensed.

## T — Transition

For an exact required correction/residual `R`, the only possible first branch is

\[
a=v_2(R),
\]

followed by

\[
R'=
\frac{R-3^{p-1}2^a}{2^{a+1}}.
\]

This is exactly the already certified residual valuation restart.

When the residual belongs to an affine source family, partitioning by possible `v_2(R)` values is the same first-one partition implemented by affine valuation-cylinder `0^a1` refinement.

Therefore a naive recursive materialization of the language reproduces the existing valuation tree rather than contracting it.

## C — Closure

Closed:

1. unrestricted first-one correction-language recursion;
2. pure-ballot restricted recursion;
3. all-zero terminal legality condition;
4. disjointness of first-one branches;
5. algebraic equivalence of one language-recursion step and one residual valuation restart.

Not closed:

1. an exact compact representation whose cost is sublinear in the full valuation tree for the current enormous target;
2. a whole-current-source-cylinder emptiness test that uses such a compact representation;
3. Route-B family closure.

## N — Non-independence

This is the decisive audit result.

The following are not independent pruning factors:

- exact correction-language first-one membership;
- residual valuation decoding;
- affine valuation-cylinder first-one refinement;
- pure-ballot legality attached to the same forced block `0^a1`.

Counting them separately would double-count the same parity/correction information.

Thus the previously proposed idea

\[
\mathcal R\cap\mathcal C^{\mathrm{bal}}_{n,p}(h,S)=\varnothing
\]

is useful only if `\mathcal R` is supplied by an independently justified active constraint and the intersection can be certified without simply enumerating the same valuation branches.

## O — Outstanding

The productive continuation is now narrower:

1. search for an exact compressed representation of `\mathcal C^{bal}` or of its intersection with an independently available source-required set;
2. prefer summaries that can reject an entire affine parameter interval without expanding all `v_2` branches;
3. test candidate summaries for right-congruence / continuation invariance before any state merge;
4. keep checkpoint/debit observations late according to the activation schedule;
5. do not revive H/L as persistent state unless a later predicate is proved to inspect its history;
6. retain exact source payload `(r,y,[m_lo,m_hi])` until source-sensitive obligations are discharged.

Candidate summary forms that may be investigated, but are not yet certified, include exact interval-gap trees, residue automata, semilinear descriptions, and grammar/DAG representations whose nodes are proved to preserve future membership.

## Finite certificate scope

The certificate checks:

- recursive language against direct word enumeration for `n<=10`, `0<=h<=20`, `0<=S<=4`;
- the all-zero base over a wider finite grid;
- unrestricted injectivity/cardinality/extrema through `n<=12`;
- exact first-one residual restart on all tested fixed-count words through `n<=12`.

These checks are finite regressions only.

## Verdict

\[
\boxed{
\text{correction-language recursion = exact reusable theorem, but not a new independent pruning axis.}
}
\]

The principal S10 problem remains source-sensitive whole-family contraction. The next useful theorem must compress or bound the language/source intersection without reconstructing the already known valuation tree.
