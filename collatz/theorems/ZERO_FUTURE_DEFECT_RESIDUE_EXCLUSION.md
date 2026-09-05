# Zero-future-defect residue exclusion on an exact source cylinder

Status: **EXACT theorem / finite execution horizon-dependent**

## 1. Setting

Let an active source cylinder be

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\qquad
m\in[m_{lo},m_{hi}]\cap\mathbb Z,
\]

with exact current target-displacement defect numerator `N` and pure-ballot control.
Let

\[
t_q<t_{q+1}<\cdots
\]

be the target one-positions for future odd ranks.

For a legal next one-event at actual position `u`,

\[
N'=3N+2^{t_q}-2^u.
\]

Hence the one-step future atom is zero exactly when

\[
u=t_q.
\]

## 2. Unique zero-defect next child

The valuation jump `0^a1` from depth `h` places the next one at

\[
u=h+a.
\]

Therefore the unique zero-defect valuation is

\[
\boxed{a_*=t_q-h.}
\]

When `a_*>=0`, the source-preserving valuation theorem selects one exact dyadic parameter residue

\[
m\equiv\rho_{a_*}\pmod{2^{a_*+1}}.
\]

Consequently the zero-defect next child is either

1. one exact nonempty source subcylinder, or
2. empty.

There is no second zero-defect branch.

## 3. Unique zero-defect horizon-r path

Iterating the previous construction gives a unique formal target-exact path through the next `r` one-events:

\[
t_q,t_{q+1},\ldots,t_{q+r-1}.
\]

At each step, intersect the current parameter interval with the unique required dyadic residue and quotient by the corresponding power of two.

Therefore the horizon-r zero path is either one exact nonempty source cylinder or empty.

For the finite-horizon min-plus quantity

\[
F_r=\sum_{k=0}^{r-1}3^{r-1-k}
\left(2^{t_{q+k}}-2^{u_k}\right),
\]

all atoms are nonnegative, so for a nonempty legal horizon-r descendant set,

\[
\boxed{F_r^{min}=0}
\]

if and only if the unique target-exact source path is nonempty.

If the target-exact path is empty, then either

- no legal horizon-r descendant exists, in which case the parent is already ballot-closed before that horizon; or
- every legal horizon-r descendant has strictly positive new future defect.

Thus zero-path exclusion is a source-sensitive positivity-or-closure certificate without expansion of positive-defect branches.

## 4. Universal positive floor after zero-path exclusion

Suppose a legal horizon-r descendant exists but the zero path is absent.
Then at least one future one-event `k` has

\[
u_k\le t_{q+k}-1.
\]

For that event,

\[
2^{t_{q+k}}-2^{u_k}
\ge
2^{t_{q+k}-1}.
\]

Therefore every legal horizon-r descendant satisfies

\[
\boxed{
F_r\ge L_r(q)
:=
\min_{0\le k<r}
3^{r-1-k}2^{t_{q+k}-1}.
}
\]

This floor is deliberately weak but universal once the all-zero-defect path is excluded.
It does not assume which rank is displaced.

## 5. Safe parent-level physical composition

Let the directed physical score at descendant normalization be

\[
P=M_{lo}N+\delta_{lo}3^qX_{lo}.
\]

For every descendant of a parent source interval,

\[
X_{desc,lo}\ge X_{parent,lo}.
\]

If the horizon-r zero path is absent, then every legal horizon-r descendant obeys

\[
N_{desc}\ge3^rN_{parent}+L_r(q).
\]

Hence the parent-level safe floor is

\[
\boxed{
P_{floor}
=
M_{lo}\bigl(3^rN_{parent}+L_r(q)\bigr)
+
\delta_{lo}3^{q+r}X_{parent,lo}.
}
\]

If

\[
P_{floor}>B\,3^{q+r},
\]

where `B` is the certified physical barrier constant, then the whole parent is closed by the following exhaustive alternative:

- a branch dies pure ballot before horizon `r`; or
- it survives to horizon `r`, necessarily has positive future defect, and is physically rejected by the common floor.

No descendant enumeration is needed for this implication.

## 6. Non-independence warning

The zero-path test does not create a new probabilistic pruning factor.
It is a direct exact test on the same source interval and future parity language.

Likewise `L_r(q)` is not added to current `N` at current normalization.
It is inserted only in

\[
3^rN+L_r(q)
\]

at descendant odd-count normalization.

## 7. Finite execution consequence for the current jump-8 frontier

The accompanying certificate evaluates the unique zero-defect path on all 14,224 certified jump-8 source cylinders.

The finite result is:

- horizons 1 through 11: all 14,224 parents retain a target-exact path;
- horizon 12: zero-path exclusion begins;
- horizon 40: exactly one parent still retains the target-exact path;
- horizon 41: no jump-8 parent retains it.

Thus by horizon 41 every jump-8 parent satisfies the exact disjunction

\[
\boxed{
\text{ballot-closed before horizon 41}
\quad\text{or}\quad
F_{41}^{min}>0.
}
\]

However the universal one-displacement floor `L_41(q)` is too weak to trigger the directed physical whole-parent gate for any of the 14,224 parents.
The next useful object must therefore force a stronger cumulative/weighted displacement amount, not merely the existence of one displacement.

## 8. DSD classification

### EXACT / CLOSED

- uniqueness of the zero-defect next valuation;
- uniqueness of the finite target-exact path;
- zero-floor equivalence for a nonempty legal descendant set;
- positivity-or-ballot-closure disjunction after zero-path exclusion;
- universal positive floor `L_r(q)`;
- safe parent-level physical composition.

### SAFE finite execution

- the horizon-41 exclusion result on the current 14,224 jump-8 parents.

### OPEN

- a source-sensitive lower bound on the **amount** or multiplicity of unavoidable future displacement strong enough to close whole parents;
- an analytic horizon-independent compression of that stronger lower bound.

## Dependencies

- `FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md`
- `AFFINE_VALUATION_CYLINDER_JUMP.md`
- `TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`
