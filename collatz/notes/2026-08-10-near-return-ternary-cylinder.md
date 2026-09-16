# Near-return ternary cylinders at the isolated next resonance

Date: 2026-08-10

Status: **DERIVED EXACT CONSEQUENCE OF THE RATIONAL PREFIX BUDGETS**

This note converts the existing prefix-dependent correction budgets into a direct ternary coupling between the ordinary start `x` and the first-crossing endpoint `y`.  It does not eliminate the next resonance by itself, but it reduces the high-ternary endpoint matching state space.

## 1. Setup

The exact Worley isolation leaves only

\[
(q,\sigma)=
(137,528,045,312,\;217,976,794,617)
\]

in the current unverified first-crossing interval.

Write

\[
y=x+d,
\qquad d\ge0,
\]

for a paradoxical first crossing.

With normalized correction `S=R/3^q` and

\[
\delta=2^\sigma/3^q-1,
\]

the exact affine identity gives

\[
\boxed{
d=\frac{S-\delta x}{1+\delta}.}
\]

Let `U_S` and `Lambda_-` be the exact rational Denjoy--Koksma/crossing bounds from `rational-dk-next-resonance-certificate.md`.  Since

\[
S\le U_S,
\qquad
\delta\ge\Lambda_->0,
\]

we have for every prefix block with minimum start `X_min(p)`

\[
\boxed{
0\le d
< A(p):=U_S-\Lambda_-X_{\min}(p).
}
\]

The earlier prefix budget table recorded

\[
N_{\rm old}(p)=\lfloor12A(p)\rfloor.
\]

Because `d` is integral,

\[
\boxed{
d\le\left\lfloor\frac{N_{\rm old}(p)}{12}\right\rfloor.}
\]

## 2. Certified near-return table

Using the exact integer `N_old` values already certified for the nine surviving high-four `m=46` ternary prefixes gives:

| prefix | certified `d_max` | smallest `t` with `d_max<3^t` |
|:--|--:|--:|
| `0000` | 1,209,739,910 | 20 |
| `0001` | 1,166,037,900 | 20 |
| `0010` | 1,078,633,881 | 19 |
| `0011` | 1,034,931,872 | 19 |
| `0100` | 816,421,824 | 19 |
| `0101` | 772,719,815 | 19 |
| `0110` | 685,315,796 | 19 |
| `0111` | 641,613,786 | 19 |
| `1000` | 29,785,654 | 16 |

Thus every surviving `m=46` candidate is not merely bounded globally; it is a near-return:

\[
\boxed{0\le y-x<3^{20}.}
\]

For the strongest high prefix `1000`,

\[
\boxed{0\le y-x<3^{16}=43,046,721.}
\]

## 3. Ternary high-quotient cylinder

If

\[
0\le y-x<3^t,
\]

then ordinary integer division gives

\[
\boxed{
\left\lfloor\frac{y}{3^t}\right\rfloor
\in
\left\{
\left\lfloor\frac{x}{3^t}\right\rfloor,
\left\lfloor\frac{x}{3^t}\right\rfloor+1
\right\}.
}
\]

Therefore the high ternary digits of the endpoint are tied directly to those of the start, with at most one carry across the `3^t` boundary.

This is stronger than the previous endpoint ceiling `y<3^48`: it is a translated endpoint cylinder centered at the actual ordinary start.

## 4. Compression of the 40 free ternary digits

In one fixed high-four `m=46` prefix, write the remaining free part as

\[
S=S_{\rm hi}3^t+S_{\rm lo},
\]

where `S_lo` uses only the lower `t` free ternary digits.  The start is

\[
x=4(3^{46}+S_{\rm fixed}+S)+3.
\]

Because

\[
0\le S_{\rm lo}\le\frac{3^t-1}{2},
\]

the low contribution satisfies

\[
0\le4S_{\rm lo}+3\le2\cdot3^t+1.
\]

Hence, after division by `3^t`, all lower `t` ternary bits affect the high quotient only through a carry in

\[
\{0,1,2\}.
\]

The additional near-return increment `d<3^t` contributes at most one more carry.  Thus for each assignment of the upper `40-t` free ternary bits, the endpoint high quotient has at most four possible values.

Consequently the number of high-quotient states is at most

\[
\boxed{4\cdot2^{40-t}.}
\]

Selected bounds are therefore:

- `t=20`: at most `4*2^20 = 4,194,304` endpoint high-quotient states;
- `t=19`: at most `4*2^21 = 8,388,608` states;
- `t=16` (`1000`): at most
  \[
  \boxed{4\cdot2^{24}=67,108,864}
  \]
  states.

For `1000`, this replaces the raw `2^40` lower-digit assignments by at most `2^26` high-ternary endpoint states when matching against the terminal `3`-adic core.

This is a state compression, not a candidate elimination: many starts may map to the same high quotient.

## 5. Two-ended interpretation

The existing terminal-core theorem says that the last 48 odd positions determine `y` exactly because `0<=y<3^48`.

The present result sharpens the bridge to

\[
\boxed{
\text{recursive ternary start block}
\to
\text{near-return cylinder of width }3^t
\to
\text{48-odd terminal residue core}.
}
\]

For `1000`, the terminal core must land in a width-`3^16` translate of the start rather than merely somewhere below the global `3^48` ceiling.

The natural next computational/theorem target is therefore a terminal interval-count analogue: count or exclude last-odd-position configurations whose exact `3^48` endpoint residue lands in one of these high-quotient cylinders while also respecting the global sparse-defect budget.

## 6. Scope

Proved here:

- exact conversion of the rational prefix defect budget into an integer near-return bound;
- exact ternary quotient coupling;
- deterministic high-quotient state-count bounds.

Not proved:

- that any of the endpoint high-quotient states is empty;
- a local terminal defect-density bound;
- elimination of the `1000` or other ternary blocks.

The main benefit is that the start and endpoint ternary descriptions are no longer independent large sets: their high digits are forced into a narrow translated cylinder.
