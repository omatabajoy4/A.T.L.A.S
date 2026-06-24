# ADR-002: Gemini Pro as Primary AI Provider

## Status

Accepted

## Decision

A.T.L.A.S. will use Gemini Pro as the primary AI provider.

## Reason

Gemini Pro will be used as the main reasoning engine for the first versions of A.T.L.A.S.

## Consequences

- A.T.L.A.S. must include an AI provider abstraction layer.
- The system must not be permanently coupled to Gemini.
- Future providers such as OpenAI, Claude or local models must be replaceable without redesigning the architecture.
