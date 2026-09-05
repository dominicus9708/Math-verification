#!/usr/bin/env python3
"""Numerical/exact-formula audit of the unconditional safe-horizon entropy budget.

Let alpha=log_3(2), delta_form=1-H_2(alpha), and
rho=log_2(3)/(1-alpha), the asymptotic root-maximality-safe binary horizon
per ternary selector digit.

The recursively sufficient selector family has 1 binary choice bit per ternary
depth m.  If one uses only the currently unconditional coefficient/formation
exclusion rate delta_form, the total asymptotic exclusion accumulated by the
safe horizon H~rho*m is delta_form*rho*m bits.

This script records the constants.  It is a budget diagnosis, not a proof of
independence or extinction.
"""

import math


def H2(p: float) -> float:
    return -p*math.log2(p)-(1-p)*math.log2(1-p)


def main() -> None:
    alpha=math.log(2)/math.log(3)
    delta=1-H2(alpha)
    rho=math.log2(3)/(1-alpha)
    safe_exclusion=delta*rho
    residual=1-safe_exclusion
    horizon_for_one_bit=1/delta
    extension_factor=horizon_for_one_bit/rho

    assert 0.0500 < delta < 0.0501
    assert 4.29 < rho < 4.30
    assert 0.214 < safe_exclusion < 0.216
    assert 0.784 < residual < 0.786
    assert 19.98 < horizon_for_one_bit < 19.99
    assert 4.65 < extension_factor < 4.66

    print("alpha=",repr(alpha))
    print("delta_form=",repr(delta))
    print("rho_safe=",repr(rho))
    print("safe_horizon_exclusion_bits_per_m=",repr(safe_exclusion))
    print("residual_selector_bits_per_m=",repr(residual))
    print("formation_only_horizon_needed_per_m=",repr(horizon_for_one_bit))
    print("needed/safe horizon factor=",repr(extension_factor))
    print("general-m safe-horizon exclusion budget: PASS")


if __name__=="__main__":
    main()
