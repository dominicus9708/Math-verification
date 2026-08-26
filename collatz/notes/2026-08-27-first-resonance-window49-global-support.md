# First resonance: window-49 local exclusion gives a global support lower bound

Date: 2026-08-27

Status: **proof-level combinatorial consequence of the exact local support-6 certificate.** This note does not prove the Collatz conjecture.

## 1. Local input

The exact C++ certificate

`collatz/src/first_resonance_base_shell_support6_local_certificate.cpp`

proves that a first-resonance counterexample cannot have a 49-odd-state
base-shell window with at most six positive displacement states.

Thus every length-49 odd-state window obeys

\[
\boxed{\#\{j:d_j>0\}\ge7.}
\]

The extension from a base-shell starting window to every window is elementary:
if a length-49 window had fewer than seven positives, choose a window with
minimum positive count among its forward translates.  If its first state were
positive, shifting one step right cannot increase that minimum until a zero
start is reached; that would contradict the certified zero-start exclusion.
(Equivalently one may formulate the argument by the first zero of a
minimum-count translate.)

## 2. Double counting

There are

\[
Q-48
\]

ordinary length-49 windows in the first-resonance odd-ordinal interval, where

\[
Q=72,057,431,991.
\]

Each positive-displacement ordinal lies in at most 49 such windows.  Therefore

\[
49r_*\ge7(Q-48).
\]

Hence

\[
\boxed{
r_*\ge
\left\lceil\frac{7(Q-48)}{49}\right\rceil
=10,293,918,849.
}
\]

So at least about one seventh of all odd ordinals must leave the base dyadic
shell.

## 3. Coarse defect consequence

Each positive displacement contributes strictly more than \(1/12\) to the
normalized Christoffel correction defect.  Therefore

\[
\boxed{
\frac{E}{3^Q}>
\frac{10,293,918,849}{12}
>857,826,570.
}
\]

This is still below the certified first-resonance budget

\[
E/3^Q<4,314,000,000,
\]

so it is not yet an exclusion of the first resonance.

## 4. DSD interpretation

This is the desired finite-to-structural transition:

\[
\boxed{
\text{finite local quotient}
\to
\text{forbidden local descriptor}
\to
\text{all-window law}
\to
\text{global support density}.
}
\]

The global theorem no longer enumerates the \(Q\) odd ordinals individually.
