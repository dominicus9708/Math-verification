# DSD Beatty macrocycle Lyapunov rule and fixed-Q obstruction

Date: 2026-08-25

## Status

Safe structural lemma plus a negative scope result for the fixed-Q reverse route.

No Collatz proof is claimed.

## 1. Beatty boundary and surplus state

Let

\[
b(n)=\min\{q:3^q\ge2^n\}=\lceil n\log_3 2\rceil,
\]

and let

\[
\delta_n=b(n+1)-b(n)\in\{0,1\}.
\]

Write `P` for a plateau (`delta=0`) and `R` for a rise (`delta=1`).

For a coefficient-surviving parity prefix, define the endpoint surplus

\[
d_n=q_n-b(n)\ge0.
\]

If the next parity bit is `e in {0,1}`, then

\[
d_{n+1}=d_n+e-\delta_n.
\]

This is the first coordinate of the local DSD state.

The second coordinate at fixed ternary resolution Q is

\[
z_n=2^{-n}R_n\pmod{3^Q}.
\]

Its exact one-step update is

\[
z_{n+1}=2^{-1}z_n\quad(e=0),
\]

\[
z_{n+1}=2^{-1}(3z_n+1)\quad(e=1)
\]

modulo `3^Q`.

Thus, after endpoint decoupling (`q_n>=Q`), the state `(d,z)` has a closed local transfer rule.

## 2. Exact Beatty macrocycle restrictions

Three elementary power comparisons determine the local Beatty language.

### No PP

If two consecutive plateaus occurred, then `b(n+2)=b(n)`.  Minimality of `b(n)` gives

\[
3^{b(n)}<3\,2^n,
\]

while `b(n+2)=b(n)` would require

\[
3^{b(n)}\ge2^{n+2}=4\,2^n,
\]

contradicting `4>3`.

### No RRR

If three consecutive rises occurred, then `b(n+3)=b(n)+3`.  But

\[
3^{b(n)+2}\ge9\,2^n>8\,2^n=2^{n+3},
\]

so already `b(n)+2` is sufficient at depth `n+3`, contradicting minimality.  This is exactly `9>8`.

### No AA

Starting at a plateau, the next plateau is therefore reached after either

- `A=PR`, or
- `B=PRR`.

If two A macrocycles occurred consecutively, the Beatty increments would contain

`P R P R P`,

so over five increments there would be only two rises.  But

\[
3^{b(n)+2}<27\,2^n<32\,2^n=2^{n+5},
\]

using `32>27`, so depth `n+5` requires at least three additional rises.  Contradiction.

Hence every pair of consecutive plateau-to-plateau macrocycles is one of

\[
AB,\qquad BA,\qquad BB.
\]

Their `(length, number of rises)` are respectively

\[
(5,3),\qquad(5,3),\qquad(6,4).
\]

This gives an exact structural reason to group the dynamics beyond the earlier empirical three-step window.

## 3. Geometric surplus Lyapunov function

Choose

\[
a=\frac32
\]

and weight a surplus state by

\[
W(d)=a^d.
\]

For a block of length `L` with `D` Beatty rises, ignoring the non-negativity boundary can only add paths.  Averaging over all `2^L` dyadic parity extensions gives

\[
\frac{1}{2^L}\sum a^{d_{\rm out}-d_{\rm in}}
=
\frac{1}{a^D}\left(\frac{1+a}{2}\right)^L.
\]

For `AB` or `BA`,

\[
\sigma_5
=
\frac{1}{(3/2)^3}\left(\frac54\right)^5
=
\boxed{\frac{3125}{3456}}
\approx0.9042245370.
\]

For `BB`,

\[
\sigma_6
=
\frac{1}{(3/2)^4}\left(\frac54\right)^6
=
\boxed{\frac{15625}{20736}}
\approx0.7535204475.
\]

Therefore every pair of Beatty macrocycles satisfies the uniform weighted bound

\[
\boxed{
\mathbb E\,W(d_{\rm out})
\le
\frac{3125}{3456}W(d_{\rm in})
}
\]

for the coefficient-surviving dyadic lift process.  Paths that would make `d<0` are rejected and only make the left-hand side smaller.

The accompanying certificate enumerates all boundary-sensitive starting surpluses and verifies that the closed-form high-surplus value is indeed the worst case.

This is a genuine high-surplus drift theorem, not merely a finite-B regression.

## 4. Fixed-Q reverse obstruction

The same certificate rebuilds the compressed reverse-potential DP at

- `Q=7`,
- `Kmax=36`.

Its exact maximal reverse potential is

\[
\Lambda_{7,\max}
=
\boxed{\frac{2187}{128}}
\approx17.0859375.
\]

For the forward coefficient state,

\[
\Theta_n
=
\frac{3^{q_n}}{2^n}
=
\frac{3^{b(n)}}{2^n}3^{d_n},
\]

and

\[
1\le\frac{3^{b(n)}}{2^n}<3.
\]

Therefore if

\[
d_n\ge3,
\]

then

\[
\Theta_n\ge27>\Lambda_{7,\max}.
\]

So no strict coefficient reverse witness at fixed `Q=7,Kmax=36` can kill an endpoint with surplus `d>=3`.

This is an important negative result:

> fixed-Q reverse contraction cannot by itself supply a statewise uniform contraction on the unbounded surplus coordinate.

The finite Q7/H25 block contractions remain valid; what is ruled out is the naive asymptotic extrapolation that the same fixed-Q reverse mechanism kills every possible high-surplus state.

## 5. DSD interpretation

The current state decomposition is now

\[
\text{Beatty phase}
\times
\text{surplus }d
\times
\text{ternary endpoint }z.
\]

The two mechanisms have complementary roles:

1. **Beatty macro drift** controls the high-surplus tail in a weighted sense;
2. **reverse potential** removes a finite low-surplus strip depending on `z`.

This suggests a two-zone closure strategy rather than a pure fixed-Q cylinder contraction:

- low strip `0<=d<D`: finite `(d,z)` transfer with exact reverse killing;
- high strip `d>=D`: geometric Lyapunov control from the Beatty macrocycle theorem.

A successful proof still needs to connect this weighted tail control to the actual minimal-counterexample / selector language strongly enough to exclude exceptional zero-measure paths.

## 6. Remaining theorem

The earlier desired statement

\[
\eta_{Q,B,r}\ge\eta_0>0
\]

cannot simply be obtained from fixed-Q reverse killing on all surplus states.

A more accurate target is one of the following.

### Tail-tightness form

Prove that among the actual candidate language, the high-surplus weighted bound forces a uniform positive proportion into a finite strip `d<D`, where reverse killing has a finite-state gap.

### Adaptive-resolution form

Allow `Q` to increase with the surplus/scale so the reverse-potential strip grows while maintaining enough static selector mixing.

The first route is preferable if a generalized ballot/cycle-lemma estimate can provide a uniform endpoint-surplus tail bound.  Existing cycle-lemma literature for arbitrary real slopes is directly relevant to this subproblem, but no such external theorem is assumed here.

## 7. Reproducibility

Source:

`collatz/src/dsd_beatty_macro_lyapunov_certificate.py`

Expected terminal line:

`PASS`
