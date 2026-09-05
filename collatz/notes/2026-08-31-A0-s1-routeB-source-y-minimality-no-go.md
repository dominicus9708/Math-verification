# A0 s=1 Route-B — generic source-Y minimality no-go

Date: 2026-08-31  
Branch: `collatz-stage4-window-threshold`

## 1. Question

The reduced finite-resolution DAG bound left one exponential-looking coordinate:

\[
Y=y\bmod2^d.
\]

Can one construct a smaller **generic exact** quotient of `Y` that still preserves every future `d`-step parameter-to-parity behavior?

The answer is no.

---

## 2. Distinguishing input

A source channel has the form

\[
z=y+g n,
\qquad g=3^q\text{ odd}.
\]

Consider the single future parameter input

\[
n=0.
\]

Then

\[
z=y,
\]

so the next `d` output parity bits are exactly the ordinary length-`d` parity word of `y` under

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

The coefficient `g` disappears completely on this input.

---

## 3. Parity-cylinder injectivity

The standard parity-cylinder theorem gives a bijection

\[
\boxed{
\mathbb Z/2^d\mathbb Z
\longleftrightarrow
\{0,1\}^d.
}
\]

Equivalently, every length-`d` parity word has exactly one canonical source residue modulo `2^d`.

Therefore

\[
y\not\equiv y'\pmod{2^d}
\]

implies that the length-`d` parity words of `y` and `y'` are different.

---

## 4. Minimality theorem

Let a `d`-step source transducer state be required to preserve the complete mapping

\[
\{	ext{future parameter residues mod }2^d\}
\longrightarrow
\{	ext{future parity words of length }d\}.
\]

Suppose two states with

\[
Y\ne Y'\pmod{2^d}
\]

were identified.

Feed both states the same zero parameter input.  Their outputs are the parity words of `y` and `y'`, which are distinct by parity-cylinder injectivity.

This contradicts exact behavioral equivalence.

Hence

\[
\boxed{
Y=y\bmod2^d
\text{ has }2^d\text{ behaviorally distinguishable classes.}
}
\]

In particular,

\[
\boxed{
\text{no smaller generic exact }Y\text{-quotient can preserve all }d\text{-step future inputs.}
}
\]

This is a lower bound on the generic transducer semantics, not merely a failure to discover a better encoding.

---

## 5. Consequence for the current DAG bound

The previous finite-resolution bound

\[
N_{\rm DAG}
\le
2^{D/2}
\,2^{1+K/2}3^{L/2}(D+1)^{5/2}
\]

cannot be pushed to polynomial size by simply replacing `Y mod 2^d` with a universally smaller exact state while preserving every future parameter input.

Therefore a further improvement must weaken the required generic semantics in a mathematically justified way.

The available legitimate routes are:

1. **A-closure:** stop a family before all future parity distinctions matter;
2. **B-equivalence under the Route-B predicate:** identify states that differ as raw parity transducers but are equivalent for the specific membership/closure question;
3. **restricted admissible inputs:** prove that large sets of future parameter residues are already impossible and need not be distinguished;
4. **hierarchical/lazy observation:** request only the boundary/interior information actually needed by the next certificate rather than the complete future parity word;
5. **recursive structural coordinates:** use a proven hierarchy, such as a run decomposition, only after its applicability to the relevant survivor family is independently certified.

---

## 6. DSD audit

### Exact / closed

- zero future parameter input eliminates the affine coefficient `g` from the distinguishing argument;
- distinct `Y mod 2^d` states produce distinct length-`d` parity words;
- the generic full-output source transducer therefore needs at least `2^d` source-Y classes;
- a universal exact coordinate-only compression of `Y` is impossible under these semantics.

### Finite regression only

`collatz/src/A0_s1_routeB_source_y_minimality_certificate.py` directly checks the parity-cylinder injectivity through `d=14` as an implementation guard.  The theorem itself uses the exact parity-cylinder bijection already established upstream.

### Not implied

- Route-B-specific state equivalence may be much coarser than full parity-transducer equivalence;
- the no-go theorem does not rule out lazy boundary localization or hierarchical certificates;
- it does not prove a lower bound for every conceivable Collatz proof strategy.

---

## 7. Updated route selection

The generic source-channel quotient has reached its natural minimality boundary.

Accordingly, the next productive target is not

\[
\text{“compress }Y\text{ further for every possible future.”}
\]

It is

\[
\boxed{
\text{“prove that the Route-B closure predicate needs strictly less future information than the full parity transducer.”}
}
\]

The existing exact lazy-boundary frontier and target-specific Christoffel/run hierarchy are relevant here, but the latter must remain target-specific until universal applicability is proved.
