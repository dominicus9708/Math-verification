# Global first-resonance handoff after the sharp parity-RS gate

Date: 2026-08-26

Status: exact finite reduction conditional only on the published convergence verification below \(2^{71}\), the mechanical first-crossing envelope, and the Worley--Dujella Diophantine theorem. No ternary selector family and no repeated local L7/L14 pullback is used. This is not a proof of Collatz.

## 1. Input from the sharp constant-wall theorem

The exact parity-RS/Farey certificate proves that a hypothetical minimal counterexample satisfies coefficient survival through

\[
H_0=114,208,327,603.
\]

The first depth where a single constant parity-RS wall can fail to force the exact coefficient wall is

\[
\boxed{A_0=114,208,327,604}.
\]

At a first coefficient crossing at this depth, the odd count is forced to be

\[
\boxed{q_0=72,057,431,991}.
\]

Thus the first possible coefficient-crossing pair after the sharp constant-wall gate is

\[
\boxed{(A_0,q_0)=(114,208,327,604,\ 72,057,431,991).}
\]

## 2. First-crossing mechanical ceiling

For a first coefficient crossing with accelerated length \(A\), odd count \(q\), and

\[
P=\frac{2^A}{3^q}>1,
\]

the mechanical/Christoffel envelope gives

\[
S_w\le S_{\rm chr}\le\frac{q}{6\ln2}+\frac13.
\]

A no-descent start \(N\) must satisfy

\[
N(P-1)\le S_w.
\]

For the boundary pair \((A_0,q_0)\), the companion exact rational-log certificate proves

\[
\boxed{
N<\frac43\,2^{71}<2^{72}.
}
\]

Therefore any minimal counterexample whose first coefficient crossing occurs at the first sharp-wall resonance is automatically a **72-bit start**.

This is a finite-address consequence independent of the old m44/m45 ternary selector family.

## 3. Global Worley scan after the first boundary

Now consider a later first coefficient crossing with

\[
q_0<q\le q_1,
\qquad
q_1=137,528,045,312.
\]

Using only the global floor

\[
N\ge2^{71},
\]
not the stronger old m44-specific floor, the mechanical envelope gives the rigorous approximation constant

\[
k(q)<2.779
\]
throughout this interval.

The Worley--Dujella theorem therefore reduces every primitive approximation to adjacent-convergent combinations with

\[
rs<2k<5.558,
\]
so

\[
\boxed{rs\le5}.
\]

Exact rational continued-fraction enumeration yields

\[
\boxed{41}
\]
primitive candidates in the full Worley superset.

Applying the direct mechanical first-crossing error bound leaves exactly one:

\[
\boxed{
(A_1,q_1)
=(217,976,794,617,\ 137,528,045,312).
}
\]

The multiplicity is \(1\).

Thus in the entire interval after the first boundary and through this next resonance, there is no continuum of possible coefficient-crossing depths: there is one exact later pair.

## 4. Two-cell reduction

Combining the sharp constant-wall theorem with the global mechanical/Worley scan gives the proof-valid global reduction

\[
\boxed{
\text{first coefficient crossing up to }A_1
\Rightarrow
(A,q)\in\{(A_0,q_0),(A_1,q_1)\}.
}
\]

Explicitly,

\[
\boxed{
(A,q)
\in
\left\{
(114,208,327,604,72,057,431,991),
(217,976,794,617,137,528,045,312)
\right\}.
}
\]

The first pair is the sharp constant-wall boundary itself. The second is the previously identified deep resonance, now recovered without using a ternary selector floor.

## 5. Why the first cell is now the main obstruction

The first cell cannot be eliminated merely from the mechanical real ceiling using the published \(2^{71}\) base, because the rigorous ceiling is above that verified floor. However it is below \(2^{72}\).

Hence the first unresolved global cell has been reduced to

\[
\boxed{
2^{71}<N<\frac43\,2^{71}<2^{72},
}

together with a fixed first coefficient-crossing pair \((A_0,q_0)\).

This changes the nature of the problem. Before the handoff, the unresolved start was an unbounded integer. At the first resonance it is a finite 72-bit formation address followed by a deterministic tail.

The relevant remaining condition is therefore

\[
\rho_{A_0}(w)\le\Theta_{A_0}(w)
\]
for a first-crossing ballot word of the exact pair \((A_0,q_0)\), with

\[
2^{71}<\rho_{A_0}(w)<\frac43\,2^{71}.
\]

## 6. Relation to survivor-Hensel maximality

Every proper prefix before \(A_0\) is coefficient-surviving. The repaired global parity-RS gate and the linear survivor-Hensel credit theorem therefore make whole-prefix survivor maximality valid on every proper prefix of a minimal-counterexample candidate.

The final crossing step itself is coefficient-subcritical, so the survivor-Hensel theorem cannot simply be applied to the completed \(A_0\)-word. The next proof task is instead to use the \(A_0-1\) maximal survivor state plus the final forced crossing bit to constrain the 72-bit formation floor.

This is a precise binary-domain target and avoids the defective repeated local pullback.

## 7. Current live verification context

Barina's project page on 2026-08-23 reports a live continuous verified frontier slightly beyond the published \(2^{71}\) milestone, at least \(2075\cdot2^{60}\). This improves the lower edge of the finite first-resonance band slightly, but is not used in the durable theorem above. The peer-reviewed \(2^{71}\) frontier remains the formal external input in the certificate.

## 8. Immediate next target

The next exact target is the **boundary-cell formation theorem**:

> For every first-crossing ballot word with
> \[
> (A,q)=(114,208,327,604,72,057,431,991),
> \]
> satisfying survivor-Hensel maximality on all proper prefixes, prove either
> \[
> \rho_A>\frac43\,2^{71}
> \]
> or produce a smaller-root merge/descent certificate.

If this cell is closed, coefficient survival jumps directly to the second isolated resonance at \(A_1=217,976,794,617\).

Certificate:

`collatz/src/global_first_resonance_post_constant_gate_certificate.py`.
