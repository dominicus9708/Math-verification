# First resonance: symmetric 44-odd mechanical-credit bounds at both exposed boundaries

Date: 2026-08-26

Status: **exact two-boundary finite theorem** inside the repaired first-global-resonance branch.  This is not a proof of the Collatz conjecture.

## 1. Endpoint side

The previously certified endpoint/Hensel calculation gives

\[
\boxed{\mathfrak a_{\rm end}\le44.}
\]

Equivalently, no admissible endpoint can support 45 consecutive terminal odd ordinals with mechanical displacement zero.  A positive Hensel repair is forced within the first 45 odd ordinals when the word is reconstructed from the endpoint backward.

At depth 44 the unique all-mechanical-compatible endpoint in the near-return band is

\[
2729562462203742221059,
\]
whereas depth 45 has no endpoint candidate.

## 2. Start side

Now examine the all-mechanical parity prefix from the original start.

For a prefix of `k` parity steps with `q` odd steps and correction `R_k`, its canonical start residue is

\[
\rho_k\equiv-R_k3^{-q}\pmod{2^k}.
\]

The first-resonance start band is

\[
2^{71}<N<\frac43 2^{71}.
\]

For the exact mechanical word:

- at `k=69` there are exactly `q=44` odd ordinals and the residue class has one representative in the start band,

\[
\boxed{N_{69}=2927051879996215679995;}
\]

- at `k=70` there are `q=45` odd ordinals and the canonical residue class has no representative in the start band.

Therefore

\[
\boxed{
\text{no admissible start can follow the mechanical ray through its first 45 odd ordinals.}
}
\]

Define the start-side mechanical odd-ordinal credit by the maximum initial number of odd ordinals whose positions agree with the mechanical word.  Then

\[
\boxed{\mathfrak a_{\rm start}\le44.}
\]

## 3. Symmetric two-boundary statement

The first resonance therefore has the exact symmetric boundary condition

\[
\boxed{
\mathfrak a_{\rm end}\le44,
\qquad
\mathfrak a_{\rm start}\le44.
}
\]

So, measured in odd ordinals rather than parity-bit depth,

\[
\boxed{
\text{a nonmechanical repair/displacement is forced within 45 odd ordinals of each end.}
}
\]

The coincidence of the number 44 on the two sides is an exact arithmetic result of the current resonance; no symmetry principle is assumed.

## 4. Relation to stronger local support bounds

The project already has stronger finite support information:

- the first 72 parity bits force at least 11 early ordinal displacements;
- terminal Hensel low-support certificates force many terminal displacements in windows near 60--66 odd ordinals.

The present theorem serves a different purpose.  It supplies **boundary alignment credit** for an amortized Bellman argument:

- the endpoint cannot donate an arbitrarily long free zero-control Hensel block;
- the start cannot absorb an arbitrarily long final mechanical block either.

This directly removes the arbitrary-boundary counterexample that invalidates local positive-cost block estimates.

## 5. Mechanical-scaled Hensel state and audit caution

The natural two-boundary Hensel state may be mechanically scaled so that both ends are ordinary small integers.  If `K_m` is the Hensel carry and `B_m` the current mechanical position, define

\[
X_m=2^{A-B_m}K_m.
\]

For mechanical gap `g` and displacement `d`,

\[
X_{m+1}=\frac{2^gX_m+2^{-d}}3.
\]

With the natural endpoint convention,

\[
X_0=-y,
\qquad
X_Q=-N.
\]

This is a convenient two-boundary coordinate.  However, if one additionally rescales by the **actual** displacement and rewrites the state as an ordinary odd integer, the recurrence becomes the ordinary backward odd Collatz relation.  Such a rewrite is only a coordinate equivalence and must not be presented as new proof content.

The proof-level gain comes from the compressed block/Bellman analysis and the two fixed boundary-credit constraints, not from merely rewriting the original orbit.

## 6. Current finite-crossing Bellman target

The repaired first-resonance problem is now naturally posed as

\[
\boxed{
\begin{array}{c}
\text{start boundary credit }\le44\\
\downarrow\\
138\text{-node anchored Christoffel gap DAG}\\
+\\
\text{Hensel ternary-tree isometry / repair control}\\
+\\
\text{one-sided displacement ordering}\\
\downarrow\\
\text{endpoint boundary credit }\le44
\end{array}}
\]

with total normalized correction defect constrained by

\[
E/3^Q<4314000000.
\]

The next theorem sought is an amortized two-boundary Bellman lower bound exceeding that budget.

Companion certificates:

- `collatz/src/first_resonance_initial_alignment_credit44_certificate.py`;
- `collatz/src/first_resonance_start_mechanical_credit44_certificate.py`.
