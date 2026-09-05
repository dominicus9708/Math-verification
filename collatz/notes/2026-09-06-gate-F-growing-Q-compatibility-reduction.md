# Gate F: growing-Q compatibility reduction

Date: 2026-09-06

Status: **PARTIALLY CLOSED ALGEBRA + OPEN MAP/UNIFORM GATES.**

This note refines the earlier fixed-`Q` fibre-compatibility discussion for the Beatty one-child + selector-repair route.

The main conclusion is that Gate F is not a single obligation.  It separates into three logically distinct layers:

\[
\boxed{
F_{\rm heal}
\quad+\quad
F_{\rm map}
\quad+\quad
F_{\rm unif}.
}
\]

The first is pointwise closed for every finite `Q`; the latter two remain open at different strengths.

---

## 1. Gate `F_heal`: exact finite-Q healing

The root-backtrace / plateau-swap compatibility mechanism tracks a residue defect modulo `3^Q`.

At each common odd event the defect transforms by a factor

\[
\Delta_{j+1}
=
3u_j\Delta_j
\pmod{3^Q},
\]

where `u_j` is a `3`-adic unit (the powers of `2` entering the formula are invertible modulo `3^Q`).

Therefore, unless the defect is already zero modulo `3^Q`,

\[
v_3(\Delta_{j+1})
=
v_3(\Delta_j)+1.
\]

Starting from the worst case `v_3(Delta_0)=0`, after `Q` common odd events,

\[
v_3(\Delta_Q)\ge Q,
\]

hence

\[
\boxed{
\Delta_Q\equiv0\pmod{3^Q}.
}
\]

The argument contains no step requiring `Q` to be one fixed numerical constant.  It is a finite-parameter algebra theorem:

\[
\boxed{
\forall Q\in\mathbb N_{>0},
\quad
\text{a residue defect modulo }3^Q
\text{ heals after at most }Q\text{ common odd events.}
}
\]

Thus if a proof later chooses a finite `Q=Q(L)` separately at each scale, this local healing theorem may be instantiated at that value of `Q(L)`.

Status: **SAFE LEMMA / `F_heal` CLOSED POINTWISE.**

This does **not** imply that the total fraction of contaminated sites remains small as `Q(L)` grows.

---

## 2. The active low-height window

The fixed-`Q` compatibility proof localizes possible plateau-swap contamination near low-height active events.

Write

\[
H_Q
:=
\left\lfloor
Q\log_2\frac32
\right\rfloor.
\]

Equivalently, without logarithmic rounding ambiguity,

\[
\boxed{
H_Q
=
\max\{H\in\mathbb Z_{\ge0}:2^{H+Q}\le3^Q\}.
}
\]

Let

\[
N_q(H)
:=
\#\{0\le i<q:h_i\le H\}
\]

be the number of relevant low-height positions among the first `q` coefficient/ballot positions.

A low-height event can contaminate only a healing window of order `Q`; the fixed-`Q` counting argument yields the schematic bound

\[
\boxed{
\#\operatorname{Bad}(q,Q)
\le
(Q+2)N_q(H_Q+1).
}
\]

The harmless `+2` absorbs the finite boundary/endpoint padding already present in the local compatibility bookkeeping.

Status: **SAFE REDUCTION**, using the existing fixed-Q localization architecture.

---

## 3. Why the old fixed-H hard-core estimate is not enough

The existing low-height hard-core estimate has the form

\[
\boxed{
N_q(H_0)
=O_{N,H_0}(q^{1/9})
}
\]

for each **fixed** height cutoff `H_0`.

For fixed `Q`, `H_Q` is fixed, so this immediately gives

\[
\frac{\#\operatorname{Bad}(q,Q)}q
=O_{N,Q}(q^{-8/9})
\to0.
\]

That is enough for the previously stated fixed-`Q` compatibility theorem.

However, if

\[
Q=Q(q)\to\infty,
\]

then

\[
H_{Q(q)}\to\infty.
\]

The constant hidden in `O_{N,H_0}` is allowed to depend arbitrarily on `H_0`.  Therefore the substitution

\[
H_0=H_{Q(q)}
\]

is not licensed by the fixed-height theorem.

This is precisely the missing uniformity.

Status: **DSD BARRIER.**

---

## 4. Exact growing-Q sufficient target

By the localization bound, growing-Q compatibility follows from

\[
\boxed{
(Q(q)+2)
N_q(H_{Q(q)}+1)
=o(q).
}
\]

Equivalently,

\[
\boxed{
\frac{Q(q)+2}{q}
N_q(H_{Q(q)}+1)
\longrightarrow0.
}
\]

This is the **moving low-height strip condition**.

It is strictly more precise than asking vaguely for a `uniform fixed-Q theorem`: it states exactly how much growing-height information is needed.

Status: **SAFE CONDITIONAL REDUCTION / `F_unif` TARGET.**

---

## 5. Conditional polynomial-height corollary

Suppose one strengthens the hard-core estimate to an explicit height-uniform form

\[
\boxed{
N_q(H)
\le
C_N(H+1)^Aq^\gamma
}
\]

for all relevant `H,q`, with

\[
A\ge0,
\qquad
\gamma<1.
\]

Since

\[
H_Q=O(Q),
\]

we obtain

\[
\#\operatorname{Bad}(q,Q)
=O_N\!\left(
Q^{A+1}q^\gamma
\right).
\]

Thus

\[
\boxed{
Q(q)^{A+1}
=o(q^{1-\gamma})
}
\]

is sufficient for growing-Q compatibility.

Equivalently, if

\[
Q(q)=q^\beta,
\]

then it is enough that

\[
\boxed{
\beta<\frac{1-\gamma}{A+1}.
}
\]

For the existing fixed-height exponent `gamma=1/9`, an eventual polynomial-in-height strengthening would give the transparent target

\[
\boxed{
\beta<\frac{8}{9(A+1)}.
}
\]

Examples:

\[
\begin{array}{c|c}
A&\beta\text{ may be any value below}\\\hline
0&8/9\\
1&4/9\\
2&8/27\\
3&2/9\\
4&8/45
\end{array}
\]

Status: **SAFE CONDITIONAL COROLLARY.**

No such polynomial dependence on `H` is claimed by the present fixed-height theorem.

---

## 6. Gate `F_map`: selector-to-canonical-fibre identification

The local healing theorem alone does not identify the selector multiplicity used in the min/max repair lemma with the exact mass carried by the Beatty coefficient-survivor sets `R_L` and `D_L`.

The existing selector construction supplies useful partial structure: fixing low ternary digits translates the high-selector distribution, so exact child selector counts on low ternary cylinders are translates of one common high-selector function `h`.

This supports orientation-independence of the min/max repair estimate and prevents an arbitrary left/right-child choice from changing the extrema.

But the new cumulative bridge requires a stronger statement:

\[
\boxed{
\text{the selector count }h_L
\text{ is the exact counting weight of the same canonical parent fibre}
\text{ on which }R_L,D_L\text{ live.}
}
\]

In particular one must specify:

1. the parent modulus/fibre at scale `L`;
2. the map from coefficient-survival words/residues into that parent fibre;
3. the two child lifts represented by `C(r)` and `C(r+M)`;
4. the one-child subset `D_L` after this identification;
5. normalization, so the candidate mass before and after a rise is measured in the same units.

Status: **OPEN `F_map`.**

The translation lemma is **supporting algebra**, not a complete identification theorem.

---

## 7. Revised Gate-F decomposition

The dependency is now

\[
\boxed{
\begin{array}{c}
F_{\rm heal}:\text{ finite-Q defect healing}\\
\textbf{CLOSED pointwise for every finite }Q\\[3pt]
+\\[-2pt]
F_{\rm map}:\text{ selector }\leftrightarrow\text{ canonical Beatty fibre}\\
\textbf{OPEN}\\[3pt]
+\\[-2pt]
F_{\rm unif}:\text{ growing-Q contaminated fraction }\to0\\
\textbf{OPEN, reduced to moving low-height strip}
\end{array}
}
\]

This is preferable to labeling all fixed-Q/growing-Q issues as one undifferentiated compatibility gate.

---

## 8. DSD audit

### SAFE

1. `3`-adic valuation of the residue defect gains one unit per common odd event.
2. Hence every finite modulus `3^Q` heals after at most `Q` common odd events.
3. Fixed-Q contamination is localized to `O(Q)` neighborhoods of low-height events.
4. Growing-Q compatibility is sufficient under
   \[
   (Q+2)N_q(H_Q+1)=o(q).
   \]
5. A height-uniform polynomial bound implies the stated power-law admissible growth for `Q(q)`.

### PARTIAL SUPPORT ONLY

- Low-ternary-cylinder selector distributions are translates of a common high-selector distribution.
- This supports the min/max repair algebra but does not by itself identify the Beatty candidate fibre.

### OPEN

- `F_map`: exact fibre identification.
- `F_unif`: moving low-height strip theorem.

### PROHIBITED UPGRADES

1. Do not infer growing-Q compatibility from `O_{N,H_0}(q^{1/9})` with fixed `H_0`.
2. Do not treat the hidden `H_0` dependence as polynomial unless proved.
3. Do not identify selector counts with Beatty-survivor counts merely because both are residue counts.
4. Do not infer Gate S from Gate F; compatibility and selector flatness are separate obligations.

---

## 9. Highest-value next target

There are now two concrete routes for `F_unif`:

### Route F1 — expose the hidden height dependence

Revisit the proof of

\[
N_q(H_0)=O_{N,H_0}(q^{1/9})
\]

and track every occurrence of `H_0` explicitly.  Any subexponential or polynomial bound strong enough for the chosen `Q(q)` may suffice.

### Route F2 — prove the moving-strip statement directly

Avoid a uniform theorem for every `H` and target only

\[
(Q(q)+2)N_q(H_{Q(q)}+1)=o(q)
\]

for a deliberately slow growth law `Q(q)`.

Because the proof route only needs `Q(q)\to\infty`, one should initially choose `Q(q)` as slowly as possible rather than demand a strong power law.

This is the next Gate-F calculation target.
