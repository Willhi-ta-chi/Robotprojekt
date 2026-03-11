"""Simple random-action controller for Gymnasium environments."""

from __future__ import annotations


def sample_action(env):
    """Return one random action from the environment action space."""
    return env.action_space.sample()
