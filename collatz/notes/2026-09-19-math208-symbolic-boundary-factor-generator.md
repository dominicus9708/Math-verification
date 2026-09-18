# MATH-208 — closed-form boundary-factor generator from Beatty positions and paid gap vectors

Date: 2026-09-19

Status: `EXACT SYMBOLIC GENERATOR / NO DEPTH-WORD ENUMERATION / VARIABLE-r MAINLINE`

## 1. Purpose

MATH-207 removes the separate phase/depth loops.

The remaining source of combinatorial expansion is the explicit parity word itself.

This note replaces that word by two compact objects:

1. a closed Beatty-position formula for the zero-cost mechanical prefix;
2. an admissible even-gap vector for the paid first-return cluster.

The result is one exact formula for the complete affine factor

[
A+2^Htlongmapsto B+3^Qt
]

with (r) left as a parameter.

## 2. Zero-cost prefix without depth enumeration

Let the boundary-entry phase be

[
omegain(1/2,1].
]

For (jge1), define

[
p_j(omega)
=
j+m(j)+mathbf1_{{omegale	au_j}},
]

and put

[
p_0=0.
]

These are exactly the odd-step positions of the mechanical zero-cost spine.

Suppose the paid exit occurs after exactly (q) mechanical odd steps.

The condition that the exit slack is (u=1) gives the prefix length directly:

[
oxed{
L
=
q+m(q)+mathbf1_{{omegale	au_q}}-1.
}
]

Thus (L) is not an independent loop variable.

The zero-cost prefix correction is

[
oxed{
C_0(q,omega)
=
sum_{j=0}^{q-1}
3^{q-1-j}2^{p_j(omega)}.
}
]

This is exactly the correction obtained by iterating the parity bits.

## 3. Paid-cluster phase schedule

Let (arpi) be the paid-cluster entry phase.

For target paid count (r), define

[
E_j(arpi)
=
m(j)+mathbf1_{{arpile	au_j}},
]

and

[
arepsilon_j
=
E_{j+1}(arpi)-E_j(arpi),
qquad
j=0,ldots,r-1,
]

with (E_0=0).

Then

[
arepsilon_jin{0,1}
]

and the total number of even shortcut steps in the first-return paid cluster is

[
oxed{
1+E_r(arpi).
}
]

## 4. Exact admissible gap vector

Let

[
a_jge0
]

be the number of even shortcut steps after the (j)-th paid odd step.

The paid cluster begins at slack (u=1).

After the first (j+1) paid odds and their following gaps,

[
u_{j+1}
=
1+sum_{i=0}^{j}arepsilon_i
-
sum_{i=0}^{j}a_i.
]

First return occurs exactly after the (r)-th paid odd iff

[
oxed{
sum_{i=0}^{r-1}a_i
=
1+E_r(arpi)
}
]

and, for every (j<r-1),

[
oxed{
sum_{i=0}^{j}a_i
le
sum_{i=0}^{j}arepsilon_i.
}
]

These ballot-type inequalities replace explicit parity-word traversal.

## 5. Paid odd positions and correction

For an admissible gap vector

[
mathbf a=(a_0,ldots,a_{r-1}),
]

the (j)-th paid odd occurs at local position

[
oxed{
ell_j
=
j+sum_{i=0}^{j-1}a_i.
}
]

Therefore the paid-cluster correction is

[
oxed{
C_r(mathbf a)
=
sum_{j=0}^{r-1}
3^{r-1-j}2^{ell_j}.
}
]

The local cluster length is immediately

[
oxed{
h_r
=
r+sum_{j=0}^{r-1}a_j
=
r+1+E_r(arpi).
}
]

No depth-by-depth parity simulation is needed.

## 6. Complete boundary correction

Concatenation of affine parity words obeys

[
C(PW)
=
3^{|W|_1}C(P)
+
2^{|P|}C(W).
]

Hence the complete zero-prefix + paid-cluster correction is

[
oxed{
C_{m full}
=
3^r C_0(q,omega)
+
2^L C_r(mathbf a).
}
]

The complete factor has

[
oxed{
H=L+h_r,
qquad
Q=q+r.
}
]

Its canonical source residue is

[
oxed{
A
=
left(
-C_{m full}3^{-Q}
ight)mod2^H,
qquad
0le A<2^H,
}
]

and its target intercept is

[
oxed{
B
=
rac{3^Q A+C_{m full}}{2^H}.
}
]

Thus

[
oxed{
A+2^Ht
longmapsto
B+3^Qt
}
]

is obtained directly from

[
(q,omega,r,mathbf a)
]

without enumerating a depth interval and without reconstructing every parity bit.

## 7. r is an emitted parameter, not an outer loop

The formula above may be evaluated for a fixed (r), but the proof architecture should not run it as 21 unrelated calculations.

MATH-187 advances one common slack/paid counter.

When that counter first returns to zero, set

[
r=j
]

and apply the same formulas.

Therefore the proper implementation is

[
oxed{
	ext{one recurrence}
	o
	ext{first-return tag }r
	o
z_{min}(r)
	o
	ext{same carry/address gate}.
}
]

MATH-202's threshold is then a function evaluated at the emitted (r), not a reason to create a separate layer executor.

## 8. r=10 finite combinatorics as a regression only

For (r=10), the phase interval has 11 exact (arepsilon)-patterns.

The admissible gap-vector counts per pattern are finite; a regression audit gives a range

[
476le #mathcal A_{10}(arpi)le1966.
]

Across the 11 phase patterns there are 10,962 gap-vector occurrences before exact-state merging.

These numbers are not the intended theorem state.

They only show that the closed-form generator reproduces a manageable finite language for the current (r=10) regression.

The mainline should merge by the proof-relevant carry/residue/Hensel coordinates rather than preserve individual gap vectors.

## 9. Consequence for the remaining r=10 closure

MATH-206 established that the frozen first-cell (r=10) full-factor catalogue has no zero-carry compatible next factor.

MATH-208 identifies what must be proved to upgrade this to a theorem:

> show, directly from the symbolic generator and proof-state quotient, that no legal (r=10) first-return factor emitted by the common recurrence can satisfy the next dangerous carry/address gate.

The target is therefore a statement about the quotient of

[
(q,omega,r,mathbf a,d,mathcal H,J),
]

not a new enumeration of 278,725 AP leaves.

## 10. Claim boundary

Established:

- closed formula for mechanical odd positions;
- direct paid-exit prefix length;
- closed correction sum for the zero-cost prefix;
- exact ballot characterization of every paid first-return gap vector;
- closed correction sum for the paid cluster;
- exact complete boundary-factor formula;
- (L), local depth and parity bits need not be independent enumeration axes.

Not established:

- a bounded-size quotient of all gap vectors sufficient for arbitrary-depth closure;
- emptiness of the full (r=10) Hensel/address/terminal danger quotient;
- closure of (r=10);
- first universal Farey-cell emptiness;
- the Collatz conjecture.
