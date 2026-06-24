# ADR-001: Docker as Official Deployment Foundation

## Status

Approved

## Decision

A.T.L.A.S. will use Docker as the official deployment foundation from the beginning.

## Reason

Docker allows A.T.L.A.S. to run locally on Windows during V1 and later migrate to a Linux VPS during V2 without redesigning the system.

## Consequences

- All core components must be Docker compatible.
- Local development must be reproducible.
- Future VPS deployment must be considered from the start.
