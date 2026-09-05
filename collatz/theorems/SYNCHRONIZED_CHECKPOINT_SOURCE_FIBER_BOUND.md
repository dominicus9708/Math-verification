# Synchronized checkpoint source-fiber bound

Status: **EXACT / CLOSED for source-fiber cardinality after checkpoint exposure**

## Setting

Take one retained 14-root source cylinder

\[
X=r+2^h m,
\]

with exact root depth `h=f+1` for first-defect position

`f in {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`.

Suppose a synchronized dyadic/right-H observation pair has already exposed one ordinary checkpoint `Z` in the SAFE checkpoint corridor by `SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON.md`.

Use only the independent pre-defect debit corridor

\[
75\,2^{33}<L_-<112\,2^{33},
\qquad L_-=3X-Z.
\]

No later defect-derived `X` bound is needed for the theorem below.

## Exact parameter interval for fixed Z

Substitute `X=r+2^h m` into the debit inequalities:

\[
75\,2^{33}<3(r+2^h m)-Z<112\,2^{33}.
\]

Therefore

\[
\frac{Z+75\,2^{33}-3r}{3\,2^h}
<m<
\frac{Z+112\,2^{33}-3r}{3\,2^h}.
\]

This is an open interval in the integer parameter `m` of exact real width

\[
W_h=\frac{37\,2^{33}}{3\,2^h}.
\]

Hence the number of integer parameters in the fiber is at most

\[
\boxed{
K_h=\left\lceil\frac{37\,2^{33}}{3\,2^h}\right\rceil.
}
\]

Intersecting this interval with the root's original finite `[m_lo,m_hi]` can only decrease the count.

Equivalently, exact integer bounds for a supplied `Z,r,h` are

\[
m_{lo}^{(Z)}=
\left\lfloor
\frac{Z+75\,2^{33}-3r}{3\,2^h}
\right\rfloor+1,
\]

\[
m_{hi}^{(Z)}=
\left\lceil
\frac{Z+112\,2^{33}-3r}{3\,2^h}
\right\rceil-1.
\]

The actual joined source fiber is

\[
[m_{lo},m_{hi}]\cap[m_{lo}^{(Z)},m_{hi}^{(Z)}].
\]

## 14-root bounds

| first defect `f` | root depth `h=f+1` | maximum source parameters per exposed `Z` |
|---:|---:|---:|
| 2 | 3 | 13,242,815,830 |
| 5 | 6 | 1,655,351,979 |
| 8 | 9 | 206,918,998 |
| 10 | 11 | 51,729,750 |
| 13 | 14 | 6,466,219 |
| 16 | 17 | 808,278 |
| 18 | 19 | 202,070 |
| 21 | 22 | 25,259 |
| 24 | 25 | 3,158 |
| 27 | 28 | 395 |
| 29 | 30 | 99 |
| 32 | 33 | 13 |
| 35 | 36 | 2 |
| 37 | 38 | 1 |

Useful deep-root cumulative bounds for one exposed checkpoint are

\[
\sum_{f\ge24}K_{f+1}=3668,
\]

\[
\sum_{f\ge27}K_{f+1}=510,
\]

\[
\sum_{f\ge29}K_{f+1}=115,
\]

\[
\sum_{f\ge32}K_{f+1}=16,
\]

\[
\sum_{f\ge35}K_{f+1}=3,
\qquad
K_{38}=1.
\]

Thus the deepest root `f=37` has at most one ordinary source integer compatible with any one exposed checkpoint `Z`; the three deepest roots `f>=32` contribute at most sixteen source parameters in total per exposed `Z`.

## Computational consequence

The synchronized join does not need to expand a root all the way to ordinary-X singleton depth before using checkpoint information.

Once a coherent pair `(z2,z_H)` exposes `Z`, the exact root parameter interval can be intersected immediately with the source fiber above. For deep roots this changes the join from a huge source-family problem to a tiny exact finite fiber.

For shallow roots the bound is still large, so the forward Bellman/projective compression remains useful there.

This theorem therefore supports a **hybrid join**:

1. keep compressed `P_min`/source states while checkpoint data are absent;
2. expose one `Z` by synchronized CRT;
3. intersect each relevant root with its exact `m` fiber;
4. enumerate only when the resulting exact fiber is genuinely small;
5. otherwise continue compressed source refinement.

## DSD audit

### EXACT / CLOSED

- substitution of the affine source cylinder into `L_-=3X-Z`;
- exact open interval for `m`;
- universal integer-lattice cardinality bound `K_h`;
- the listed 14-root values and deep-root cumulative bounds.

### SAFE dependency

The theorem inherits the pre-defect debit corridor as an upstream SAFE input. It does not strengthen that corridor.

### REJECTED inferences

- `small source fiber => membership`;
- `one source integer + one checkpoint => same orbit` without the full pre-bridge language check;
- multiplying source-fiber cardinalities by marginal right-H/dyadic survival ratios;
- using the later refined defect-based `X` bound retroactively in this theorem.

## Certificate

- `../src/A0_s1_routeB_synchronized_checkpoint_source_fiber_certificate.py`

Finite sample endpoint checks in the certificate are implementation guards; the general cardinality statement follows from the interval-width proof above.
