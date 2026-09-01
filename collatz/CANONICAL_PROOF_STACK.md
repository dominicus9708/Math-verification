# Canonical live proof stack

This is the shortest current live implication stack. Historical exploratory routes and implementation regressions are omitted.

A line here means only that the implication has an exact or explicitly SAFE certificate in its stated domain. Final global lines remain OPEN.

## S0 — Physical A0 domain

Work in the certified A0 `s=1` formation with the fixed long pre-bridge parameters and physical X/Z shell assumptions used by the Stage-4 branch.

Status: **DOMAIN / imported**.

## S1 — Near-threshold finite closure

Certified finite arithmetic closes radius `0..7` in the first-75 threshold window, giving the SAFE necessary condition

`d_75 >= 8`.

Status: **CERTIFIED ARITHMETIC -> SAFE**.

## S2 — Monotone defect and physical pruning

Target dominance makes threshold correction maximal; normalized defect is nonnegative and irreversible under continuation. Together with the directed real envelope this gives the certified physical pruning bound.

Status: **EXACT + CERTIFIED arithmetic -> SAFE pruning**.

## S3 — Exact 14-root source forest

Every remaining Route-B family lies in exactly one retained first-defect source root

`F14 = {2,5,8,10,13,16,18,21,24,27,29,32,35,37}`

after the stated upstream SAFE pruning.

Status: **EXACT search-family representation after SAFE inputs**.

## S4 — Exact structural compression

Available exact representations include:

- affine source cylinders and bit refinement;
- fixed-count ballot / target dominance;
- dual H/L grammar;
- correction front localization;
- projective carry/displacement cylinders;
- finite source interval payloads;
- one-dimensional ternary projective interval payloads.

Status: **EXACT structural lemmas**.

## S5 — Defect and physical Bellman score

With

\[
N=3^q\eta,
\qquad
P=m_{W,lo}N+\delta_{lo}3^qX_{lo},
\]

one `P_min` label per exact active source/control + payload state is sufficient for the directed physical rejection predicate because every common transition maps `P` by an increasing affine map.

Status: **EXACT / CLOSED for this physical gate**.

## S6 — Lazy terminal-ternary observation and critical-cut shielding

A final residue predicate `N_J mod 3^L` requires only

\[
m(q)=\max(0,L-(J-q))
\]

current ternary digits. At the existing critical cut the right H factor has `397,573,380` one-events, so terminal precisions `L=24,28,47` are completely right-local.

Status: **EXACT / CLOSED**.

## S7 — Right-H projective high-precision sharpening

For the current right H block

\[
h_R=630{,}138{,}897,
\qquad q_R=397{,}573{,}380,
\]

right-indexed slack capacity obeys

\[
D_t\le h_R-q_R=232{,}565{,}517.
\]

Since

\[
\lambda_{18}=2\cdot3^{17}=258{,}280{,}326,
\]

every prescribed projective cylinder is empty or singleton for `m>=18`.

Status: **EXACT / CLOSED for prescribed cylinders; distinct carry-path multiplicity remains OPEN**.

## S8 — Right-H affine checkpoint observation

For terminal precision 28,

\[
z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}},
\]

where

\[
2^s\equiv12{,}596{,}342{,}295{,}887,
\]

\[
C(H_s^*)\equiv2{,}677{,}095{,}985{,}033
\pmod{3^{28}}.
\]

Thus `z_H` is exactly equivalent to one residue `Z mod 3^28`.

Status: **EXACT / CLOSED**.

## S9 — Synchronized checkpoint CRT singleton

Using only the independent pre-defect corridor chain,

\[
Z_{min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241,
\]

\[
Z_{max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196.
\]

Its span is smaller than

\[
2^{27}3^{28}=3{,}070{,}471{,}107{,}232{,}407{,}748{,}608.
\]

Therefore a coherent pair

`Z mod 2^27 × z_H mod 3^28`

determines at most one ordinary checkpoint `Z` in the SAFE corridor.

Status: **EXACT / CLOSED for checkpoint exposure**.

## S10 — Checkpoint-conditioned source-fiber bound

For one retained source root

\[
X=r+2^h m
\]

and one exposed ordinary checkpoint `Z`, the independent debit corridor gives

\[
\frac{Z+75\,2^{33}-3r}{3\,2^h}<m<
\frac{Z+112\,2^{33}-3r}{3\,2^h}.
\]

Therefore the compatible source fiber has cardinality at most

\[
K_h=\left\lceil\frac{37\,2^{33}}{3\,2^h}\right\rceil.
\]

For the deepest current roots, per exposed checkpoint:

- `f>=24`: at most 3,668 source parameters;
- `f>=27`: at most 510;
- `f>=29`: at most 115;
- `f>=32`: at most 16;
- `f>=35`: at most 3;
- `f=37`: at most 1.

Canonical object:

- `theorems/SYNCHRONIZED_CHECKPOINT_SOURCE_FIBER_BOUND.md`.

Status: **EXACT / CLOSED for source-fiber cardinality after checkpoint exposure**.

## S11 — Current hybrid synchronized join

Backward first:

compressed right-H projective/carry export -> synchronized checkpoint observation -> zero or one ordinary `Z`.

Then source conditioning:

ordinary `Z` -> exact 14-root debit-compatible source fibers.

Only shallow fibers that remain large continue under compressed `source/control × interval payload × P_min`; deep fibers may be handled directly once genuinely small.

This avoids mandatory full source singleton expansion before checkpoint data are available.

Status: **ACTIVE**.

## S12 — Full Route-B local closure

For every joined survivor, discharge exact pre-bridge correction-language membership, ordinary checkpoint/debit coherence, tail first-passage, and any required renewal/C4F condition.

A small source fiber or one exposed `(X,Z)` pair is not itself membership.

Status: **OPEN**.

## S13 — Global completion

Route-A, `s>=2`, remaining formation branches, and branch completeness must be separately closed before any Collatz conclusion.

Status: **OPEN**.

---

# Forbidden shortcuts

- adic mismatch -> membership rejection;
- interval inclusion -> correction-language membership;
- endpoint/checkpoint exposure -> same orbit or full membership;
- small checkpoint-conditioned source fiber -> membership;
- one exposed `(X,Z)` pair -> same orbit without the long pre-bridge language check;
- local carry greedy -> global optimum before a cylinder sequence is fixed;
- singleton prescribed cylinder -> singleton carry path;
- marginal dyadic/ternary/source survival-ratio multiplication;
- later refined bound used retroactively;
- finite execution -> universal theorem;
- A0 `s=1` Route-B closure -> Collatz without remaining modules.
