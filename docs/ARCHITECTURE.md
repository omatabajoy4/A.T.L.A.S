# A.T.L.A.S. Architecture

## Core Principle

A.T.L.A.S. Core must never depend on a specific interface.

## High Level Architecture

```text
Clients
│
├── Desktop App
├── Mobile App
├── Alexa
├── Smart TV
│
▼
API Layer (FastAPI)
│
▼
ATLAS Core
│
├── Brain
├── Memory
├── Agents
├── Automation
├── Voice
├── Web Knowledge
│
▼
Infrastructure
│
├── SQLite
├── ChromaDB
├── Docker
└── Future PostgreSQL
```

## Deployment Strategy

V1:
Docker local on Windows

V2:
Docker on Linux VPS

V3:
Hybrid Local + Cloud
