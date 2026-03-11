# Robot Safety (Simulation-First Course)

## Core Principle

Simulation first, hardware later. Students should prove behavior in simulation before any real robot testing.

## Classroom Safety Rules

- No unsupervised hardware operation
- Clear emergency stop procedure before any robot power-on
- Keep a marked safe zone around robot test space
- Assign operator and spotter roles for each test

## Software Safety Rules

- Log each experiment configuration
- Use conservative action limits in early tests
- Validate controller outputs before execution
- Keep rollback versions of stable code

## Transition to Humanoid Hardware

Before using humanoid hardware (e.g., Unitree G1):

- Confirm communication and control limits
- Test low-risk motions first (stand, small posture changes)
- Run checklist-based preflight and shutdown procedures
