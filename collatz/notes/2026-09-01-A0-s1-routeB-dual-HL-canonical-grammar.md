# A0 s=1 Route-B dual H/L canonical grammar

## Purpose

The previous critical-cut factorization reduced a finite-critical ballot family to two one-sided languages.  This note closes their intrinsic recursive grammar **before** any Christoffel specialization.

Let

\[
\alpha=\log_3 2,\qquad f(n)=\lfloor\alpha n\rfloor,\qquad \phi(n)=\{\alpha n\}.
\]

Define

\[
\mathcal H_h=\left\{W:\ |W|=h,\ Q_W(h)=f(h)+1,\ Q_W(u)\ge f(u)+1\ \forall 1\le u\le h\right\},
\]

and

\[
\mathcal L_h=\left\{W:\ |W|=h,\ Q_W(h)=f(h),\ Q_W(u)\le f(u)\ \forall 1\le u\le h\right\}.
\]

The empty word is used only as the neutral member of \(\mathcal L_0\).

---

## 1. Canonical H cut

For \(W\in\mathcal H_h\), put

\[
d_H(u)=Q_W(u)-f(u)\ge1.
\]

Since \(d_H(h)=1\), the set

\[
Z_H(W)=\{u:d_H(u)=1\}
\]

is nonempty.  Define

\[
\boxed{c_H(W)=\operatorname*{arg\,max}_{u\in Z_H(W)}\phi(u)}.
\]

Irrationality of \(\alpha\) makes the maximizer unique.

Write

\[
W=UV,\qquad |U|=c,\qquad |V|=s,
\]

with \(c=c_H(W)\).

Because \(1\in Z_H(W)\) and \(\phi(1)=\alpha\), maximality gives \(\phi(c)\ge\alpha\).  Hence the threshold does not jump at \(c\):

\[
\boxed{f(c)=f(c-1)}.
\]

The first bit of every \(\mathcal H\)-word is 1.  Put

\[
X=\operatorname{rev}(U_{2:c}).
\]

A suffix/prefix floor-carry calculation gives

\[
\boxed{X\in\mathcal L_{c-1}},
\]

so

\[
\boxed{U=1\operatorname{rev}(X)}.
\]

If \(s>0\), then \(h\in Z_H(W)\) and \(c<h\).  Maximality of \(\phi(c)\) gives \(\phi(h)<\phi(c)\), equivalently

\[
\boxed{\kappa(c,s)=f(c+s)-f(c)-f(s)=1}.
\]

The same phase argument for every prefix of \(V\) yields

\[
\boxed{V\in\mathcal H_s}.
\]

Therefore

\[
\boxed{
\mathcal H_h\ni W
\longmapsto
\bigl(c,\ X\in\mathcal L_{c-1},\ V\in\mathcal H_{h-c}\bigr).
}
\]

---

## 2. Canonical L cut

For \(W\in\mathcal L_h\), put

\[
d_L(u)=f(u)-Q_W(u)\ge0.
\]

Define

\[
\boxed{c_L(W)=\operatorname*{arg\,min}_{d_L(u)=0}\phi(u)}.
\]

Again the minimizer is unique.

Write \(W=UV\), \(|U|=c\), \(|V|=s\).

The first bit is 0.  If \(c=1\), the primitive block is simply \(U=0\).  If \(c>1\), minimality against the zero-deficit prefix at \(u=1\) implies \(\phi(c)<\alpha\), hence

\[
\boxed{f(c)=f(c-1)+1}.
\]

With

\[
X=\operatorname{rev}(U_{2:c}),
\]

the mirrored carry argument gives

\[
\boxed{X\in\mathcal H_{c-1}},
\qquad
\boxed{U=0\operatorname{rev}(X)}.
\]

If \(s>0\), minimality of \(\phi(c)\) gives

\[
\boxed{\kappa(c,s)=0},
\qquad
\boxed{V\in\mathcal L_s}.
\]

---

## 3. Converse / exact generation

The cut admissibility conditions are not merely necessary.

### H generation

If

\[
f(c)=f(c-1),\qquad X\in\mathcal L_{c-1},
\]

and either \(s=0\), or

\[
\kappa(c,s)=1,\qquad V\in\mathcal H_s,
\]

then

\[
W=1\operatorname{rev}(X)V
\]

lies in \(\mathcal H_{c+s}\) and

\[
\boxed{c_H(W)=c}.
\]

### L generation

If \(c=1\) with primitive block `0`, or if

\[
f(c)=f(c-1)+1,\qquad X\in\mathcal H_{c-1},
\]

and either \(s=0\), or

\[
\kappa(c,s)=0,\qquad V\in\mathcal L_s,
\]

then the corresponding concatenation lies in \(\mathcal L_{c+s}\) and has

\[
\boxed{c_L(W)=c}.
\]

Thus the grammar is exact in both directions.

---

## 4. Well-foundedness

Every nonempty parent of length \(h\) produces only children of lengths

\[
c-1<h,
\qquad
h-c<h.
\]

Hence

\[
\boxed{R(W)=|W|}
\]

is a strict well-founded rank for the grammar tree.

This is stronger than a target-only Christoffel decomposition: the grammar is defined for **every** member of the two ballot languages.

---

## 5. DSD audit

✅ languages defined before target specialization;

✅ canonical cut is intrinsic and unique;

✅ missing threshold-bit admissibility condition identified and included;

✅ forward decomposition proved;

✅ converse generation proved;

✅ both recursive children strictly reduce length;

✅ exhaustive finite regression implemented in `A0_s1_routeB_dual_HL_canonical_grammar_certificate.py`;

❌ no claim that every Route-B survivor is Christoffel;

❌ no claim yet that the target's H/L grammar equals its Stern-Brocot run grammar;

❌ correction/carry closure over the complete recursive H/L grammar remains to be combined;

❌ Collatz remains open.

## Next gate

Compare the canonical H/L cuts of the **already certified target word** with the independently constructed Stern-Brocot/continued-fraction hierarchy.  Equality may be used only after it is proved for that target; it must not be assumed for arbitrary ballot candidates.
