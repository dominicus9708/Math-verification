# First resonance: exact support-7 local exclusion

Date: 2026-08-27

Status: **exact finite certificate.** This result is local to the repaired first-global-resonance branch and does not prove the Collatz conjecture.

## 1. Window

Use 49 consecutive odd states with initial dyadic-shell displacement

\[
d_0=0.
\]

The mechanical gap factor has length 48.  The rational first-resonance word has exactly 49 distinct such gap factors, and the exact certificate enumerates all of them.

## 2. Exact support-7 enumeration

After the previously certified support-\(\le6\) layer is removed, enumerate every displacement path satisfying

\[
\#\{j:d_j>0\}=7
\]

and the ordering rule

\[
d_{j+1}\le d_j+g_j-1,
\qquad g_j\in\{1,2\}.
\]

The exact path count is

\[
\boxed{261,551,336}.
\]

Support-7 paths expose at least 72 time bits.  The certificate therefore uses either the exact \(2^{72}\) or \(2^{73}\) canonical address, according to the final exposed odd position, and lifts that address into the broad base shell

\[
2^{71}<x<\frac83\,2^{71}.
\]

Processing the 49 mechanical phases separately gives a total of

\[
\boxed{102,984,111}
\]

phase-deduplicated canonical starts.  Duplicate starts occurring in different phases are harmless because each phase is independently certified.

Every such start reaches a value below \(2^{71}\) under exact accelerated Collatz iteration.  The largest stopping depth encountered is

\[
\boxed{455}.
\]

Hence no first-resonance minimal-counterexample orbit can realize a base-shell 49-odd-state window with exactly seven positive displacement states.

Together with the support-\(\le6\) certificate,

\[
\boxed{
d_i=0
\Longrightarrow
\#\{j\in[i,i+48]:d_j>0\}\ge8.
}
\]

## 3. All-window upgrade

Let \(b_j=\mathbf1_{\{d_j>0\}}\).  Suppose some length-49 window had fewer than eight ones.  It cannot contain 49 ones, so a zero occurs inside it.  If the current starting bit is one, shifting one step right changes the window count by

\[
S_{i+1}=S_i-1+b_{i+49}\le S_i.
\]

Repeat until the first zero inside the original window becomes the starting bit.  The resulting zero-start window still has fewer than eight ones, contradicting the exact local certificate.

Therefore

\[
\boxed{
\text{every length-49 odd-state window contains at least eight }d_j>0.
}

## 4. Role in the DSD chain

The certificate has now passed through the intended hierarchy:

\[
\boxed{
\text{finite local quotient}
\to
\text{zero-start forbidden descriptor}
\to
\text{all-window rule}
\to
\text{global shell-density theorem}.
}
\]

Companion source:

`collatz/src/first_resonance_base_shell_support7_local_certificate.cpp`.
