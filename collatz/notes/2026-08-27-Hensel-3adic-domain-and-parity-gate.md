# Hensel 3-adic domain and exact parity gate

Date: 2026-08-27

Status: **SAFE correction / exact finite-depth specialization.**  
This note supersedes the earlier temporary concern that `d<=e_i` might be required to interpret `u_i(d)=2^{e_i-d}`.

It does not prove the Collatz conjecture.

## 1. Source-level domain correction

The original two-boundary operator defines `K` as the current **3-adic Hensel carry** and states that continuation requires the successor carry to remain a 3-adic unit.

The transition is

\[
u_i(d)=2^{e_i-d},
\qquad
K+u_i(d)\equiv0\pmod3,
\qquad
K'=\frac{K+u_i(d)}3.
\]

The relevant coefficient ring is therefore not the ordinary integers with only nonnegative exponents. It is the 3-adic ring

\[
\mathbb Z_3.
\]

Because

\[
2\in\mathbb Z_3^\times,
\]

all integral powers, including negative powers, are defined 3-adic units:

\[
\boxed{2^m\in\mathbb Z_3^\times\qquad(m\in\mathbb Z).}
\]

Hence `d>e_i` does not make `u_i(d)` undefined.

The earlier proposed extra condition

\[
d\le e_i
\]

is **not needed** and must not be inserted.

## 2. Mod-3 parity law for every integral exponent

Since

\[
2\equiv-1\pmod3
\]

and `2` is invertible modulo 3, for every integer exponent `m`, positive, zero, or negative,

\[
\boxed{2^m\equiv(-1)^m\pmod3.}
\]

Thus

\[
K+2^{e-d}\equiv0\pmod3
\]

is exactly a parity selector.

If

\[
K\equiv0\pmod3,
\]

there is no admissible action because `2^{e-d}` is a unit modulo 3.

For a unit carry:

### `K == 1 mod 3`

\[
2^{e-d}\equiv-1\pmod3,
\]

so

\[
e-d\equiv1\pmod2,
\]

or equivalently

\[
\boxed{d\equiv e+1\pmod2.}
\]

### `K == 2 mod 3`

\[
2^{e-d}\equiv1\pmod3,
\]

so

\[
e-d\equiv0\pmod2,
\]

and therefore

\[
\boxed{d\equiv e\pmod2.}
\]

## 3. Exact one-step minimizing action

Let the ordering lower bound at one prepend step be

\[
L:=\max(0,p-g+1).
\]

For `K in Z_3^x`, let `pi(K,e)` be the parity selected above.

The admissible displacements are exactly the integers

\[
d\ge L,
\qquad
d\equiv\pi(K,e)\pmod2.
\]

Because the local cost

\[
\kappa(d)=2w(1-2^{-d}),\qquad w>0,
\]

is strictly increasing in `d`, and a larger `d` only weakly tightens every later ordering constraint, the exact one-step-prefix Bellman minimizer is the smallest admissible displacement:

\[
\boxed{
d_*=L+\chi,\qquad\chi\in\{0,1\},}
\]

where

\[
\chi=0
\iff
L\equiv\pi(K,e)\pmod2.
\]

Thus the first Hensel refinement has only two possibilities:

- parity match: `d_*=L`;
- parity mismatch: `d_*=L+1`.

No search over an unbounded displacement set is required at depth one.

## 4. Exact formula for the first refined Bellman layer

Let `B_{2:n}^{inh}(q)` denote the ordering-only suffix minimum beginning at state `q`, using the already inherited global weights `w_2,...,w_n`.

Then for a unit starting carry,

\[
\boxed{
B_w^{[1]}(K,p)
=
\kappa_1(d_*)+B_{2:n}^{\rm inh}(d_*).
}
\]

If `K == 0 mod 3`, the exact first-step feasible set is empty and

\[
B_w^{[1]}(K,p)=+\infty.
\]

When parity matches,

\[
B_w^{[1]}(K,p)=B_w(p).
\]

When parity mismatches,

\[
\begin{aligned}
B_w^{[1]}(K,p)-B_w(p)
&=
\kappa_1(L+1)-\kappa_1(L)\\
&\quad+
B_{2:n}^{\rm inh}(L+1)-B_{2:n}^{\rm inh}(L)\\
&\ge
\boxed{w_1 2^{-L}}.
\end{aligned}
\]

The suffix term is nonnegative and is generally a genuine persistence tax, not an error term.

## 5. Persistence form of the one-step mismatch tax

After a parity mismatch, the ordering state enters the suffix at `L+1` instead of `L`.

Let

\[
c_i:=\#\{t\in\{2,\ldots,i\}:g_t=2\}.
\]

The perturbed relaxed state exceeds the original greedy state by exactly one while

\[
c_i\le L,
\]

and the difference disappears after the `(L+1)`-st suffix gap-2.

Therefore, if `m` is the last index for which `c_m<=L` (or `m=n` if there are not enough gap-2 symbols), the exact one-step mismatch penalty is

\[
\boxed{
B_w^{[1]}(K,p)-B_w(p)
=
\sum_{i=1}^{m} w_i2^{-L_i}.
}
\]

This is strictly stronger than the local floor `w_1 2^{-L}` whenever the extra displacement persists into the suffix.

## 6. Exact finite-depth greedy address for the original operator

The abstract greedy-address theorem can now be specialized without an added `d<=e_i` hypothesis.

For the ordering-greedy controls `L_i`, define modulo `3^h`

\[
\boxed{
\Theta_h
\equiv
-\sum_{i=1}^{h}3^{i-1}2^{e_i-L_i}
\pmod{3^h}.
}
\]

If an exponent `e_i-L_i` is negative, the power is interpreted using the inverse of `2` in

\[
(\mathbb Z/3^h\mathbb Z)^\times.
\]

This is exact because `gcd(2,3^h)=1`.

The greedy controls are Hensel-admissible through depth `h` iff

\[
\boxed{K\equiv\Theta_h\pmod{3^h}.}
\]

Hence

\[
\boxed{
B_w^{[h]}(K,p)=B_w(p)
\iff
K\equiv\Theta_h\pmod{3^h}
}
\]

for the original 3-adic operator, subject to the same finite-prefix relaxation convention at the left endpoint.

The addresses remain nested:

\[
\boxed{
\Theta_{h+1}\equiv\Theta_h\pmod{3^h}.
}
\]

## 7. Unit continuation audit

The original operator additionally says that continuation requires the successor `K'` to remain a 3-adic unit.

For a genuinely exact prefix of length `h`, this condition is automatic at every **internal** carry `K_i`, `i<h`: the next congruence is

\[
K_i+2^{e_{i+1}-d_{i+1}}\equiv0\pmod3,
\]

and the power of 2 is a unit, so `K_i` must itself be a unit.

The terminal carry `K_h` need not be a unit in the relaxed quantity `B^[h]` because that carry is deliberately forgotten after depth `h`. This only enlarges the feasible set and therefore preserves the lower-bound direction.

At depth `h+1`, a nonunit terminal carry is automatically rejected because no next exact action exists.

Thus the finite-depth hierarchy remains sound.

## 8. Correction to the previous domain audit

The earlier note `2026-08-27-Hensel-prefix-relaxation-hierarchy.md` temporarily classified the parity specialization as CONDITIONAL because it treated `K'` as though it had to be an ordinary integer expression involving an ordinary negative power of two.

The original two-boundary note resolves that ambiguity by explicitly defining `K` as a **3-adic Hensel carry**.

Corrected status:

- abstract finite-depth hierarchy: **SAFE**;
- specialization `u_i(d)=2^{e_i-d}` in `Z_3`: **SAFE**;
- exact mod-3 parity gate: **SAFE**;
- exact one-step minimizer `d_*=L or L+1`: **SAFE**;
- fixed `K mod 3^m` as an unbounded-horizon quotient: still **REJECTED**.

No rejected global quotient has been revived.

## 9. DSD structural chain

The corrected state flow is

\[
\boxed{
(K,p)
\to
K\bmod3
\to
\text{one allowed displacement parity}
\to
B^{[1]}
\to
K\bmod3^h
\to
\Theta_h
\to
B^{[h]}.
}
\]

The resolution level in the 3-adic coordinate grows with the exact horizon. It is not held fixed.

This is exactly the finite-resolution behavior required by the earlier state-compression audit.

## 10. Circularity audit

Allowed direction:

\[
\text{original 3-adic operator}
\to
\text{parity gate}
\to
B^{[1]}
\to
\Theta_h/B^{[h]}
\to
\text{independent boundary intersection}
\to
\text{near-root budget comparison}.
\]

Forbidden directions remain:

- near-root budget -> parity or residue constraints;
- finite `Theta_h` compatibility -> existence of an infinite integer predecessor;
- fixed residue depth -> exact infinite Hensel dynamics;
- this 3-adic address -> repair of the separate ternary-selector entry theorem.

## 11. Next gate

The domain ambiguity is no longer the principal obstruction.

The next proof-level object is the actual low-surplus boundary set:

\[
\boxed{
\mathcal K_{s=1,h}
\cap
[\Theta_h]_{3^h}.
}
\]

If this intersection empties at some finite depth, every admissible `s=1` boundary state has a positive mismatch tax. If it survives, the unique nested 3-adic low-cost address must be followed deeper.

The quantitative task is still to accumulate a Hensel lower defect strong enough to compare, only afterward, with the independent reset budget

\[
D<0.981G.
\]

Status of that closure: **OPEN**.
