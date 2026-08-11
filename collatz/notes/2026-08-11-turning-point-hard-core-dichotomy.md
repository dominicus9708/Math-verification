# Turning-point hard-core dichotomy

Date: 2026-08-11

Status: **exact consequence of the macroblock sign theorem**. This note reduces the nonperiodic block dynamics to two terminal qualitative modes.

## 1. Block discrepancy sign

For a maximal block define

\[
\alpha:=\log_2\frac32,
\qquad
\delta_r:=d_r-\alpha h_r.
\]

The macroblock sign theorem gives, on every nonperiodic orbit,

\[
\boxed{
\delta_r<0\iff X_{r+1}>X_r,
\qquad
\delta_r>0\iff X_{r+1}<X_r.
}
\]

Equality is impossible.

Thus the sign word of `(delta_r)` exactly records the monotone direction of the odd block-start orbit.

---

## 2. Monotone runs

A maximal consecutive run of negative discrepancies

\[
\delta_r<0
\]

is a strictly increasing run of block states.

A maximal consecutive run of positive discrepancies

\[
\delta_r>0
\]

is a strictly decreasing run of positive odd integers.

Therefore every decreasing run is finite. Indeed, each block decreases the odd integer state by at least `2`.

Consequently an infinite nonperiodic block orbit must contain infinitely many subcritical (`delta<0`) blocks.

---

## 3. Exact turning-point skeleton

Compress every maximal monotone run to its endpoints. The resulting skeleton alternates between local maxima and local minima.

Because each maximal block contains only increasing credit states followed by its next block endpoint, the global no-first-descent condition is equivalent to requiring every local minimum of the block skeleton to remain at least the original starting integer `n`.

Thus

\[
\boxed{
\tau(n)=\infty
\iff
\text{every local minimum in the infinite block skeleton is }\ge n.
}
\]

---

## 4. Two nonperiodic terminal modes

There are only two possibilities for an infinite nonperiodic block orbit.

### Mode I: eventual monotone expansion

There is `R_0` such that

\[
\boxed{
\delta_r<0
\qquad(r\ge R_0).
}
\]

Equivalently,

\[
\boxed{
M_r<1,
\qquad
X_{r+1}>X_r
\qquad(r\ge R_0).
}
\]

The block-start sequence is eventually strictly increasing. Every sufficiently late block start is then a tail minimum.

### Mode II: infinite excursions

The sign of `delta_r` changes infinitely often. The orbit has infinitely many increasing and decreasing runs.

For a divergent orbit, the local minima tend to infinity. A first-descent counterexample requires all of them to stay above the fixed original start `n`.

Each local minimum leaves through a subcritical block. Each strict local maximum leaves through a supercritical block.

---

## 5. Relation to the harmonic hard core

The event-level harmonic theorem and mixed-place conditions remain valid in both modes.

Mode I asks whether an ordinary positive integer can generate an eventually all-subcritical infinite macroblock code satisfying the harmonic/mixed-place restrictions.

Mode II asks whether infinitely many supercritical return runs can coexist with the harmonic resource bound while their successive local minima never cross the original floor.

These are now the two nonperiodic terminal theorem targets. No separate block-level paradoxical sector is needed.

---

## 6. Complete terminal decomposition

A complete first-descent proof may now be organized into three terminal exclusions:

\[
\boxed{
\begin{array}{ll}
\text{Periodic branch:}&\text{exclude nontrivial exact block/orbit returns},\\[1mm]
\text{Aperiodic Mode I:}&\text{exclude eventual monotone block expansion},\\[1mm]
\text{Aperiodic Mode II:}&\text{exclude infinite above-floor excursions}.
\end{array}
}
\]

All three are formulated on exact closed state systems and require no increasing finite verification cutoff.