# constants.py — Mathematical constants for cryptographic system
# This file contains only public mathematical constants (no secret keys)
# The actual combination method is stored locally in Qwen only
# ─────────────────────────────────────────────────────────────────────
# Riemann Zeta Non-Trivial Zeros (public mathematical values)
# Values of ρ satisfying ζ(½ + iρ) = 0
# ─────────────────────────────────────────────────────────────────────
RIEMANN_ZEROS = [
    14.134725141734695,
    21.022039638771556,
    25.010857580145689,
    30.424876125859512,
    32.935061587739192,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
]
 
# ─────────────────────────────────────────────────────────────────────
# Speed of Light (physical constant)
# ─────────────────────────────────────────────────────────────────────
c = 299_792_458  # m/s
 
# ─────────────────────────────────────────────────────────────────────
# Ternary State Values
# S = +1 → Hydrogen (proton)  = Public Key
# S = -1 → Oxygen (electron)  = Private Key
# S =  0 → Zero Point (water) = Moment of encryption, time collapses
# ─────────────────────────────────────────────────────────────────────
S_HYDROGEN =  1   # Hydrogen +1
S_OXYGEN   = -1   # Oxygen   -1
S_ZERO     =  0   # Zero point (collapses upon observation)
 
# ─────────────────────────────────────────────────────────────────────
# Core Formula
# ψ = Σ A_n · e^(i · ρ_n · (x/c - t)) · S
# Zero-point condition: when x/c = t, time collapses
# ─────────────────────────────────────────────────────────────────────
import cmath
 
def wave_function(x: float, t: float, S: int) -> complex:
    """
    Modified wave function.
 
    Parameters
    ----------
    x : float
        Position (meters)
    t : float
        Time (seconds)
    S : int
        State (+1 Hydrogen / -1 Oxygen / 0 Zero Point)
 
    Returns
    -------
    complex
        Wave function value ψ at (x, t, S)
    """
    if S == S_ZERO:
        return complex(0, 0)  # Zero point — unobservable, time collapses
 
    psi = sum(
        cmath.exp(1j * rho * (x / c - t))
        for rho in RIEMANN_ZEROS
    )
    return psi * S
 
 
def is_zero_point(x: float, t: float) -> bool:
    """
    Check if (x, t) satisfies the zero-point condition.
 
    The zero-point occurs when x/c = t,
    i.e. when position equals the distance light travels in time t.
    At this point, time collapses and the wave function is unobservable.
 
    Parameters
    ----------
    x : float
        Position (meters) — must be on the scale of c × t
    t : float
        Time (seconds)
 
    Returns
    -------
    bool
        True if the zero-point condition is satisfied
    """
    return abs(x / c - t) < 1e-15
 
