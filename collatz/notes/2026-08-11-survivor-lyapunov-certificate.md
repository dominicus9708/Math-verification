# Universal survivor-Lyapunov certificate

Date: 2026-08-11

Status: **exact conditional termination theorem**. This theorem identifies a complete non-enumerative proof certificate; constructing a potential satisfying its hypotheses remains open.

## 1. Exact survivor state system

Let \(K_k\) be an exact channel family partitioning the unresolved set

\[
U_k=\bigsqcup_{s\in K_k}\llbracket s\rrbracket.
\]

For each \(s\in K_k\), let \(\mathrm{Ch}(s)\subseteq K_{k+1}\) denote its exact surviving children under one closed refinement step.

Fix any \(z\in(0,1)\) and use the full-support geometric measure

\[
\mu_z(A)=\sum_{n\in A}(1-z)z^{n-2}.
\]

Write

\[
\mu_z(s):=\mu_z(\llbracket s\rrbracket).
\]

The unresolved mass is

\[
M_k(z)=\sum_{s\in K_k}\mu_z(s).
\]

---

## 2. Survivor potential

Let

\[
V:\bigcup_{k\ge0}K_k\to(0,\infty)
\]

be a positive state potential.

Assume a uniform positive lower bound

\[
\boxed{V(s)\ge v_*>0}
\]

for every exact survivor state.

Define the potential-weighted unresolved mass

\[
\boxed{
\mathcal E_k(z)
:=
\sum_{s\in K_k}\mu_z(s)V(s).
}
\]

Then

\[
M_k(z)\le \frac{\mathcal E_k(z)}{v_*}.
\]

---

## 3. Universal local contraction hypothesis

Suppose there exists a fixed constant

\[
0\le\lambda<1
\]

such that every exact survivor channel satisfies

\[
\boxed{
\sum_{s'\in\mathrm{Ch}(s)}
\mu_z(s')V(s')
\le
\lambda\,\mu_z(s)V(s).
}
\]

This inequality must be proved symbolically for the entire state domain. It is not a finite-sample estimate.

---

## 4. Contraction theorem

Summing the local inequalities over \(s\in K_k\) and using the exact child partition gives

\[
\begin{aligned}
\mathcal E_{k+1}(z)
&=
\sum_{s\in K_k}
\sum_{s'\in\mathrm{Ch}(s)}
\mu_z(s')V(s')\\
&\le
\lambda
\sum_{s\in K_k}\mu_z(s)V(s)\\
&=
\lambda\mathcal E_k(z).
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal E_k(z)
\le
\lambda^k\mathcal E_0(z)
\to0.
}
\]

Since \(V\ge v_*>0\),

\[
M_k(z)\le \mathcal E_k(z)/v_*\to0.
\]

The faithful generating-mass theorem then implies

\[
\boxed{\text{Collatz}.}
\]

Therefore:

\[
\boxed{
\text{exact survivor representation}
+
\text{full-support mass}
+
\text{positive potential}
+
\text{universal local contraction}
\Longrightarrow
\text{Collatz}.
}
\]

---

## 5. Role of the attribute frame

The attribute map should now be chosen to make the local contraction inequality provable.

A candidate attribute is useful only if it helps determine or bound one of:

1. the exact surviving child mass \(\mu_z(s')\);
2. the child potential \(V(s')\);
3. the ratio
   \[
   \frac{\sum_{s'\in\mathrm{Ch}(s)}\mu_z(s')V(s')}
        {\mu_z(s)V(s)}.
   \]

Thus previously introduced quantities such as coefficient balance, correction/headroom, valuation, carry/wrap, and arithmetic alignment should be retained only if they help produce a universal upper bound strictly below one.

---

## 6. Finite attribute transfer as a special case

If the exact state space is mapped to finitely many attribute classes \(a\in\{1,\dots,d\}\), and a nonnegative transfer majorant \(P\) satisfies

\[
\mathbf m_{k+1}\le P\mathbf m_k,
\]

then a positive vector \(v\) with

\[
v^\top P\le\lambda v^\top,
\qquad\lambda<1,
\]

defines a classwise-constant version of the survivor potential.

Hence the matrix certificate is a finite-dimensional special case of the general state-potential theorem.

---

## 7. Fixed-block version

If one-step contraction is too strong, the same proof works for any fixed block length \(B\ge1\):

\[
\boxed{
\sum_{s'\in\mathrm{Ch}^{(B)}(s)}
\mu_z(s')V(s')
\le
\lambda\mu_z(s)V(s),
\qquad\lambda<1.
}
\]

Then

\[
\mathcal E_{k+B}\le\lambda\mathcal E_k,
\]

which still forces \(M_k(z)\to0\).

The fixed block length must be universal; increasing \(B\) as computation proceeds would reintroduce the enumeration-depth dilemma.

---

## 8. Current next theorem task

The proof problem is therefore reduced to a constructive question:

> Find a fixed closed attribute frame and a positive potential \(V\) for which the exact Collatz survivor transition is uniformly contractive in full-support generating mass.

If uniform contraction is impossible for a coarse frame, the failure states identify precisely which additional attribute distinction is required. Attribute refinement should stop once the local inequality is universal; no numerical cutoff is part of the theorem.
