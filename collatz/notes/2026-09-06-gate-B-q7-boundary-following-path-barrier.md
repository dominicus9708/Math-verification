# Gate B: fixed-Q7 pathwise low-strip barrier

Date: 2026-09-06

## One-line result

Even inside the low strip, fixed `Q=7` reverse potential cannot be upgraded to a pathwise statement that kills every formal coefficient-surviving trajectory.  There is a formal Beatty-boundary-following path with constant surplus `d=2`, and every possible Q7 endpoint produced by the already-proved Beatty local restrictions has reverse potential at most

\[
\boxed{\frac{729}{256}<3<9.}
\]

Since `d=2` implies forward coefficient scale at least `9`, the Q7 coefficient-potential mechanism cannot eliminate this path.

## Status

- **SAFE BARRIER:** fixed-Q7 reverse-potential alone cannot provide universal pathwise low-strip elimination.
- **SAFE STRUCTURAL LEMMA:** the formal path `e_n=delta_n` keeps `d_n` constant.
- **SAFE FINITE-STATE EXHAUSTION:** after seven rises, the Q7 endpoint `z` forgets its earlier value; all suffixes in an overlanguage defined only by no-PP/no-RRR can be enumerated exactly.
- **NOT A COUNTEREXAMPLE:** the infinite formal parity path corresponds at most to a 2-adic parity specification; no positive integer realization is claimed.
- **OPEN:** use candidate-mass/tail-budget contraction, stronger canonical arithmetic, or growing/adaptive information to exclude actual positive-integer survivors.

No Collatz proof or counterexample is claimed.

---

## 1. Constant-surplus boundary-following path

Recall

\[
b(n)=\lceil n\log_3 2\rceil,
\qquad
\delta_n=b(n+1)-b(n)\in\{0,1\},
\]

and

\[
d_{n+1}=d_n+e_n-\delta_n.
\]

Choose the formal parity extension

\[
\boxed{e_n=\delta_n.}
\]

Then identically

\[
\boxed{d_{n+1}=d_n.}
\]

In particular, starting from

\[
d_n=2,
\]

the path stays forever in the fixed low strip

\[
\boxed{d=2.}
\]

This already shows that Beatty geometry alone does not force every formal coefficient-surviving path to return to `d=0`.

---

## 2. Q7 endpoint recurrence

At fixed ternary resolution

\[
Q=7,
\qquad
M=3^7,
\]

the endpoint state obeys

\[
z_{n+1}=2^{-1}z_n
\quad(e_n=0),
\]

and

\[
z_{n+1}=2^{-1}(3z_n+1)
\quad(e_n=1)
\]

modulo `3^7`.

Along the boundary-following path `e=delta`, every rise multiplies the inherited `z` coefficient by `3`.

After seven rises the coefficient of any earlier incoming `z` contains

\[
3^7
\]

and therefore vanishes modulo `3^7`.

Thus after the seventh most recent rise, the current Q7 state depends only on the finite suffix beginning at that rise.

---

## 3. Finite overlanguage of possible suffixes

The Beatty increment word has the already-proved restrictions

- no `PP`;
- no `RRR`.

Encode

\[
P=0,
\qquad
R=1.
\]

Take the suffix beginning at the seventh-most-recent `R`.

It contains exactly seven `R` symbols and begins with `R`.

Because `PP` is forbidden, there is at most one `P` between consecutive rises and at most one trailing `P`.  Hence the suffix length lies in

\[
7\le L\le14.
\]

The certificate deliberately uses only `no PP` and `no RRR`; it does **not** use the stronger no-AA rule.  Therefore the enumerated language is a strict over-approximation of the true Beatty factor language.

Exact enumeration gives

\[
\boxed{42}
\]

admissible suffix words in this overlanguage.

Any bound proved on all 42 therefore applies a fortiori to the true Beatty path.

---

## 4. Exact Q7 reverse-potential exhaustion

The existing compressed reverse DP is rebuilt with

\[
Q=7,
\qquad
K_{\max}=36.
\]

For each endpoint residue `z mod 3^7`, it finds the maximal coefficient potential

\[
\Lambda(z)=\frac{3^r}{2^K}
\]

available from a reverse code resolved within Q7.

For all 42 boundary-overlanguage endpoints, the maximum is

\[
\boxed{
\Lambda_{\max}^{\rm boundary,Q7}
=\frac{729}{256}
\approx2.84765625.
}
\]

It occurs for the suffix

```text
1011011011
```

at endpoint residue

\[
z=2177,
\]

with reverse coefficient pair

\[
(r,K)=(6,8).
\]

Therefore

\[
\boxed{
\Lambda_{\max}^{\rm boundary,Q7}<3.
}
\]

---

## 5. Comparison with the constant d=2 forward scale

For a coefficient-surviving state with surplus `d=2`,

\[
\Theta_n
=\frac{3^{q_n}}{2^n}
=\frac{3^{b(n)}}{2^n}3^2.
\]

Since

\[
1\le\frac{3^{b(n)}}{2^n}<3,
\]

we have

\[
\boxed{
9\le\Theta_n<27.
}
\]

But every Q7 reverse potential available along the boundary-following formal path satisfies

\[
\Lambda<3<9\le\Theta_n.
\]

Hence no Q7 reverse code in this mechanism can even pass the necessary coefficient-scale comparison

\[
\Lambda>\Theta_n.
\]

The exact affine-correction/minimality test is stronger still, so it cannot rescue this fixed-Q7 coefficient failure.

Thus

\[
\boxed{
\text{fixed Q7 reverse potential does not pathwise eliminate the low strip.}
}
\]

---

## 6. Why Kmax=36 is not hiding a stronger Q7 code

The resolved reverse length is at most `Q=7`.

Any code with total binary exponent `K>36` has

\[
\Lambda
\le
\frac{3^7}{2^{37}}
\ll1,
\]

so it certainly cannot exceed the `d=2` forward scale `Theta>=9`.

Thus truncating the coefficient search at `Kmax=36` cannot omit a Q7 code relevant to this barrier.

---

## 7. Interpretation

This result changes the role of Gate B.

The following stronger target is now closed as a proof route:

> choose fixed Q7 and prove that every formal low-surplus path is killed in bounded time.

That statement is false for the available reverse-potential mechanism.

What remains viable is weaker and more global:

1. **mass version:** enough low-strip candidate mass is killed repeatedly, even though an exceptional formal path survives the local automaton;
2. **same-integer/canonical version:** prove that the formal boundary-following 2-adic path cannot be the canonical tail of a positive integer minimal counterexample;
3. **adaptive-information version:** introduce stronger residue information only where required, without assuming positive generic density of strong reverse residues.

The first route integrates naturally with the new tail-budget atom-floor theorem.

---

## 8. Relation to Gate A

The boundary-following path has

\[
H=r
\]

on every completed Beatty block, hence

\[
\left(\frac32\right)^{H-r}=1.
\]

So it is exactly a **neutral** Lyapunov path, not an expanding one.

This explains why the unrestricted Beatty expectation can contract while a single path remains forever in a bounded strip.

Therefore the final argument cannot rely on expectation alone unless it is coupled to

- finite atom-floor extinction of an actual finite selector layer, or
- a same-integer arithmetic obstruction to the neutral path.

This is consistent with the current Gate A/C architecture.

---

## 9. DSD audit

### SAFE

1. `e=delta` implies constant surplus.
2. Seven rises erase the incoming Q7 `z` state modulo `3^7`.
3. `no PP` and `no RRR` imply a finite 42-word overlanguage for the seven-rise suffix.
4. Exact Q7 DP gives maximum potential `729/256` on that entire overlanguage.
5. Since `d=2` gives `Theta>=9`, Q7 cannot coefficient-wise reverse-kill the formal path.

### BARRIER

Fixed-Q7 pathwise low-strip elimination is unavailable.

### NOT CLAIMED

1. The formal parity path is not claimed to arise from a positive integer.
2. It is not a Collatz counterexample.
3. It does not invalidate Q7 finite mass-contraction certificates.
4. It does not rule out stronger canonical or adaptive arithmetic filters.

### OPEN

Use the finite-layer mass/atom-floor route or a same-integer canonical obstruction to eliminate the exceptional neutral formal language.

---

## Reproducibility

`collatz/src/gateB_q7_boundary_following_path_barrier.py`

Expected final line:

```text
PASS_FIXED_Q7_PATHWISE_BARRIER
```
