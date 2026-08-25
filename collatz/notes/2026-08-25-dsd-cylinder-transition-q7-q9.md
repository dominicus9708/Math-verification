# SUPERSEDED — DSD cylinder-transition audit Q=7 -> 8 -> 9

Date: 2026-08-25

## Status

This note is retained only as an audit marker.

The earlier Q=8 and Q=9 survivor totals and the large parent-to-child contraction ratios recorded here were not reproducible under an independent implementation of the same safe frontier logic.

The defect was in the refinement bookkeeping when a selector digit moved from the high-selector aggregate into the fixed low-ternary mask.  It produced an artificial loss of mass at Q refinement.

The Q=7 combined total `784,787,338,151` was correct, but the previously recorded Q=8 and Q=9 combined totals `373,717,485,431` and `254,500,051,362` are withdrawn.

The corrected exact certificate is:

`collatz/src/dsd_q7_q10_corrected_transition_certificate.cpp`

Corrected H24/B20 combined totals are:

- Q7: `784,787,338,151`
- Q8: `776,902,007,561`
- Q9: `758,110,858,098`
- Q10: `752,548,965,765`

All parent cylinders still contract strictly in the tested Q transitions, but only weakly:

- Q7 -> Q8 worst ratio: `0.989954390562391209`
- Q8 -> Q9 worst ratio: `0.994219546983941871`
- Q9 -> Q10 worst ratio: `0.997036735078904575`

Therefore the qualitative observation `rho_Q < 1` survives, while the earlier claim of strong Q-axis contraction is withdrawn.

See the new correction/audit note for the DSD interpretation and the stronger B-axis contraction result.
