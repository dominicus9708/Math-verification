# Block exclusion-credit globalization criterion

Date: 2026-08-18

Status: **exact reduction theorem / bridge target**.

This note combines the formation entropy budget, the static transversality
budget identity, the existing overlapping-window defect-density theorem, and
the CRT repair-localization mechanism.

It is not a proof of the Collatz conjecture.  It identifies a weaker block-level
condition sufficient for finite extinction, avoiding the need for contraction at
every individual depth.

---

## 1. Block information and repair budgets

Let \(C_K\) be finite candidate mass after formation depth K, let
\(A_K=|T_K|\) be the number of formation-allowed residues modulo \(3^K\), and
let

\[
B_K=\log_2\Xi_K
\]

be the cumulative transversality/repair budget from the static identity

\[
\log_2C_K=\log_2C_0-I_K+B_K,
\qquad
I_K=-\log_2(A_K/3^K).
\]

For a block K..K+B define

\[
I_{K:B}:=I_{K+B}-I_K,
\]

\[
R_{K:B}:=B_{K+B}-B_K,
\]

and the **net exclusion credit**

\[
\boxed{
\Gamma_{K:B}:=I_{K:B}-R_{K:B}.
}
\]

Then exactly

\[
\boxed{
\log_2 C_{K+B}-\log_2 C_K=-\Gamma_{K:B}.
}
\]

No probability or equidistribution assumption is used.

---

## 2. Block extinction theorem

Take any sequence of disjoint blocks

\[
[K_j,K_j+B_j).
\]

Telescoping gives

\[
\log_2 C_{K_n+B_n}
\le
\log_2 C_{K_0}
-
\sum_{j=0}^n\Gamma_{K_j:B_j},
\]

with any omitted intermediate blocks absorbed into their exact net credits.

Therefore, if

\[
\boxed{
\sum_j\Gamma_{K_j:B_j}=+\infty,
}
\]

then the finite nonnegative integer mass must become zero at some finite depth.

A convenient sufficient form is:

* there are at least \(cH+o(H)\) disjoint useful blocks through depth H, with
  \(c>0\);
* every useful block has \(\Gamma\ge\gamma_*>0\);
* the total negative credit of the remaining blocks is \(o(H)\), or is already
  included in the repair term used to define the useful-block lower bound.

Then the cumulative net exclusion is linear and finite extinction follows.

---

## 3. Why this is weaker than per-step contraction

It is unnecessary to prove

\[
C_{K+1}\le(1-\varepsilon)C_K
\]

for every K.  Some individual levels may even have

\[
C_{K+1}/C_K>A_{K+1}/(3A_K),
\]

that is, positive repair bias.

Only the cumulative balance matters:

\[
\sum I_{K:B}
>
\sum R_{K:B}
+
\log_2C_0.
\]

This matches the observed finite E=13--21 ladders, in which a few depths can
retain more states than a naive uniform estimate while the total block still
ends at zero.

---

## 4. Connection to the overlapping-window defect theorem

The existing exact overlapping-window certificate at the current upper-CF
resonance uses length-48 windows and Sturmian factor complexity to prove a
positive lower density of defects.  Its exact threshold is

\[
r_* = 21,960,410,645
\]

inside

\[
H=137,528,045,312,
\]

giving

\[
\boxed{
r_*/H>0.1596795082.
}
\]

The proof is combinatorial: it uses the \(m+1\) Sturmian factors and a global
incidence inequality, not enumeration of all starts.

Therefore, if a local theorem assigns a uniform positive net exclusion credit to
a suitable disjoint subfamily of these defect windows, or if it bounds their
aggregate repair below their aggregate formation exclusion, then the block
extinction theorem supplies the desired divergent cumulative exclusion.

The missing step is not defect density; positive defect density is already
available in the current resonance.  The missing step is a **defect-to-net-credit
bridge**.

---

## 5. CRT repair localization lemma already available in the transition channel

For an equal-weight length-\(N=3h\) transition block, correction differences
satisfy

\[
v_2(R(u)-R(v))=p,
\]

where p is the earliest differing binary position.

A balanced Hensel repair has the form

\[
D=-T_h(\delta)+k\,3^{F+h}.
\]

Before ternary wrap, if the exact correction span S and target range obey

\[
\boxed{
S+T_{\max}<3^{F+h},
}
\]

only \(k=0\) can occur.  But \(v_2(T_h)\ge N\), whereas every nonzero
equal-weight correction difference has valuation at most \(N-2\).  Thus the
whole repair channel is empty in this no-wrap region.

After wrap, while \(|k|<2^N\), the same two-ended argument gives

\[
\boxed{
v_2(k)=p.}
\]

Thus every nonzero repair must pay two simultaneous structural conditions:

1. its ternary lift must have entered the correction interval;
2. the 2-adic layer of that lift index must equal the earliest binary difference
   axis.

For the G13-neutral survival-conditioned gate, the existing exact certificate
pushes the no-repair range through \(h=5232\) and finds the first nonzero lift at
\(h=5233\) of \(F=5245\).

Whenever a same-state transition repair is realized there, the exact parent
credit is quantized as

\[
\boxed{
\Delta_{\rm gate}=k\,2^{F-h}.
}
\]

This is the current strongest concrete mechanism for bounding the repair side
of \(\Gamma\).

---

## 6. Characteristic unrestricted CRT-wrap scale

The unrestricted equal-weight correction span satisfies

\[
S_h\le(2^h-1)(9^h-4^h)<18^h.
\]

The ternary lift spacing is \(3^{F+h}\).  Hence the correction-width component
of the wrap condition changes exponential scale near

\[
18^h\sim3^{F+h}
\]

or

\[
\boxed{
\frac hF\sim\frac{\log3}{\log6}
\approx0.6131471928.
}
\]

This is a characteristic scale, not by itself a complete no-wrap theorem because
the Hensel target term must also fit inside the modulus margin.  In the existing
G81, G82, G13 and G14 unrestricted certificates, the first nonunique widths are
indeed close to this ratio.  The survival-conditioned G13 restriction is much
stronger and delays nonzero repair almost to h=F.

---

## 7. The new proof target

The globalization problem can now be attacked by either of two equivalent
sufficient statements.

### Static-bias form

Prove

\[
\limsup_{H\to\infty}\frac{B_q}{H}<
\delta=1-H_2(1-\log_3 2).
\]

### Defect-credit form

Construct a positive-density family of disjoint structural defect blocks and
prove that their cumulative net credit obeys

\[
\boxed{
\sum_j\Gamma_j=+\infty.
}
\]

The second form is now especially attractive because the project already has:

1. a combinatorial positive defect-density theorem;
2. exact CRT no-wrap exclusion;
3. the valuation identity \(v_2(k)=p\) after wrap;
4. exact quantization of realized parent credit in the G13 transition channel.

The next missing proposition is therefore narrow:

> **Defect-to-credit proposition (target).**  A positive-density subfamily of
> structural defects has repair budget strictly smaller than its formation /
> transition exclusion information, uniformly under recursive gate extension.

Proving that proposition would turn the existing finite and resonance-specific
certificates into a genuine cumulative-extinction mechanism.
