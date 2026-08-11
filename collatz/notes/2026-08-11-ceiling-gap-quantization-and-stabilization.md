# Ceiling-gap quantization and stabilization

Date: 2026-08-11

Status: **exact auxiliary theorem and strategy correction**. This note shows that a nonperiodic infinite survivor would not be characterized by survival ceilings drifting continuously down toward the initial integer. Instead, current contracting ceilings must escape upward and the cumulative past ceiling eventually stabilizes.

## 1. Contracting affine prefix

Fix a positive integer `n>=2` and one accelerated Collatz prefix of length `k` along its actual orbit. Write

\[
\boxed{
T^k(n)=a_k(n+c_k)
}
\]

with

\[
a_k=\frac{3^{q_k}}{2^k}>0.
\]

Assume the endpoint coefficient is contracting:

\[
\boxed{a_k<1.}
\]

The corresponding survival ceiling is

\[
\boxed{
C_k:=\frac{a_kc_k}{1-a_k}.
}
\]

The endpoint has not descended below the original start exactly when

\[
\boxed{n\le C_k.}
\]

---

## 2. Exact ceiling-gap identity

From

\[
T^k(n)=a_k(n+c_k)
\]

and

\[
a_kc_k=(1-a_k)C_k,
\]

we obtain

\[
\begin{aligned}
T^k(n)-n
&=a_kn+a_kc_k-n\\
&=-(1-a_k)n+(1-a_k)C_k.
\end{aligned}
\]

Therefore

\[
\boxed{
T^k(n)-n
=(1-a_k)(C_k-n),
}
\]

or equivalently

\[
\boxed{
C_k-n
=\frac{T^k(n)-n}{1-a_k}.
}
\]

This identity links the real survival ceiling to an integer orbit displacement.

---

## 3. Unit-gap quantization

Because `T^k(n)-n` is an integer and

\[
0<1-a_k<1,
\]

there are only two possibilities for a surviving contracting endpoint.

### Exact return

If

\[
T^k(n)=n,
\]

then

\[
\boxed{C_k=n.}
\]

The deterministic orbit has returned to its starting state, so the orbit is periodic from `n`.

### Strict survival above the start

If

\[
T^k(n)>n,
\]

then

\[
T^k(n)-n\ge1,
\]

hence

\[
\boxed{
C_k-n>1.
}
\]

Therefore

\[
\boxed{
n\le C_k<n+1
\Longrightarrow
C_k=n
\Longrightarrow
T^k(n)=n.
}
\]

A nonperiodic survivor ceiling cannot approach the start through the interval `(n,n+1)`.

---

## 4. General integer-band bound

Let `b>=0` be an integer. If a contracting survivor endpoint satisfies

\[
\boxed{
n+b\le C_k<n+b+1,}
\]

then

\[
0\le T^k(n)-n
=(1-a_k)(C_k-n)
<C_k-n
<b+1.
\]

Thus

\[
\boxed{
T^k(n)-n\in\{0,1,\ldots,b\}.
}
\]

For a nonperiodic survivor, the zero case is excluded, so

\[
\boxed{
T^k(n)\in\{n+1,\ldots,n+b\}.
}
\]

Hence a fixed ceiling band contains only finitely many possible orbit states.

---

## 5. Finite visits to bounded ceiling regions

### Theorem

Suppose the orbit of `n` is nonperiodic and never descends below `n`. For every finite real `B>n`, there are only finitely many contracting endpoint times `k` for which

\[
\boxed{C_k\le B.}
\]

### Proof

If `C_k<=B`, then

\[
0<T^k(n)-n
=(1-a_k)(C_k-n)
<C_k-n
\le B-n.
\]

Therefore `T^k(n)` belongs to the finite set of integers in `[n,B)`. If infinitely many contracting endpoint times satisfied `C_k<=B`, two of them would have the same orbit value. Determinism would then make the forward orbit eventually periodic, contradicting the nonperiodicity assumption.

---

## 6. Current contracting ceilings escape

Let

\[
k_1<k_2<\cdots
\]

be the contracting endpoint times of a nonperiodic infinite survivor, if there are infinitely many.

The finite-visit theorem implies that for every finite `B`, eventually

\[
C_{k_j}>B.
\]

Hence

\[
\boxed{
C_{k_j}\to+\infty
}
\]

in the ordinary real sense.

This is a necessary condition for any nonperiodic infinite survivor with infinitely many contracting endpoints.

---

## 7. Cumulative survival ceiling stabilizes

Define the cumulative survival ceiling

\[
\Theta_k
:=
\min_{\substack{1\le j\le k\\a_j<1}}C_j,
\]

with `Theta_k=+infinity` before the first contracting endpoint.

For a nonperiodic infinite survivor there are two possibilities.

### Finitely many contracting endpoints

Then `Theta_k` is trivially constant after the last one (or remains `+infinity` if none occurs).

### Infinitely many contracting endpoints

Since `C_{k_j}->+infinity`, the global minimum of the sequence of finite current ceilings is attained among finitely many early contracting endpoints. Therefore

\[
\boxed{
\Theta_k=\Theta_*
}
\]

for all sufficiently large `k`.

Thus in every nonperiodic infinite survivor,

\[
\boxed{
\text{the cumulative survival ceiling is eventually constant.}
}
\]

---

## 8. Consequence for proof strategy

The earlier floor/ceiling picture remains exact, but its long-time role is now clearer.

A hypothetical finite positive counterexample would have

\[
\rho_k=n
\]

eventually, by formation-floor stabilization.

If it is nonperiodic, then this note shows that also

\[
\Theta_k=\Theta_*
\]

eventually.

Therefore a divergent counterexample would asymptotically evade both monotone boundaries by **simultaneous stabilization**:

\[
\boxed{
\rho_k=n,
\qquad
\Theta_k=\Theta_*,
\qquad
T^k(n)\text{ unbounded/nonperiodic}.
}
\]

Consequently, a proof cannot rely on the expectation that the cumulative ceiling must keep decreasing forever. The remaining global attribute must distinguish the actual evolving orbit/resource state inside a fixed floor/ceiling corridor.

This is precisely where odd-event valuation, headroom, multiplicative balance, and arithmetic alignment remain necessary.
