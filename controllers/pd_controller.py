"""Minimal PD controller utility for educational use."""

from __future__ import annotations

import numpy as np


def pd_control(
    target: np.ndarray,
    current: np.ndarray,
    current_velocity: np.ndarray,
    kp: float = 2.0,
    kd: float = 0.1,
) -> np.ndarray:
    """Compute a clipped PD control action.

    This helper is intentionally simple so students can inspect and modify it.
    """
    error = target - current
    derivative = -current_velocity
    action = kp * error + kd * derivative
    return np.clip(action, -1.0, 1.0)
