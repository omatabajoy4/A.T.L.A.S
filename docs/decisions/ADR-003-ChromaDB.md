# ADR-003: ChromaDB for Semantic Memory

## Status

Accepted

## Decision

A.T.L.A.S. will use ChromaDB as the initial semantic memory system.

## Reason

ChromaDB allows local vector-based memory, semantic retrieval and context augmentation with low cost.

## Consequences

- A.T.L.A.S. can retrieve relevant memories from past conversations.
- The system can support RAG-style memory.
- Memory must be modular to allow future replacement or scaling.
