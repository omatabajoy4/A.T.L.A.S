# A.T.L.A.S. Official Technology Stack

## Purpose

This document defines the officially approved technologies for A.T.L.A.S.

All development assistants such as Gemini, ChatGPT, Claude and Antigravity must respect these decisions unless a justified Architecture Decision Record is created.

---

## Programming Language

Primary Language:

- Python 3.12+

---

## Backend

Approved:

- FastAPI

Forbidden:

- Flask for new development
- Django for the core backend

Reason:

FastAPI provides scalability, typing support and an API-first architecture.

---

## AI Provider

Primary:

- Gemini Pro

Requirements:

- Provider abstraction layer required.
- The AI provider must be replaceable without rewriting the system.

---

## Database

V1:

- SQLite

V2+:

- PostgreSQL

Requirements:

- Migration support.
- Future compatibility with scalable databases.

---

## Long-Term Memory

Approved:

- ChromaDB

Purpose:

- Semantic memory
- Conversation retrieval
- Context augmentation

---

## Voice Recognition

Approved:

- Whisper

Requirements:

- Local execution preferred.

---

## Text To Speech

Approved:

- Piper TTS

Requirements:

- Local execution preferred.

---

## Agents

Approved:

- CrewAI

Requirements:

- Modular agent architecture.

---

## Automation

Priority 1:

- Playwright
- Windows APIs
- PowerShell
- Official APIs from external services

Priority 2:

- PyAutoGUI

Requirements:

- API-first automation strategy.
- PyAutoGUI must only be used when no better API-based option exists.

---

## Web Knowledge

Approved:

- Search APIs
- Web retrieval
- Structured extraction
- Source summarization

Requirements:

- Source attribution.
- Modular implementation.

---

## Deployment

V1:

- Docker Local on Windows PC

V2:

- Docker on Linux VPS

V3:

- Hybrid Infrastructure

Requirements:

- Docker compatibility is mandatory from the beginning.

---

## Version Control

Approved:

- Git
- GitHub

Branch Strategy:

- main
- develop
- feature/*

---

## Documentation

Mandatory:

- PROJECT_CHARTER.md
- ARCHITECTURE.md
- AI_CONTEXT.md
- ROADMAP.md
- TECH_STACK.md

---

## Development Principles

- Scalability First
- Docker First
- Interface Independence
- Provider Independence
- Modular Design
- Long-Term Maintainability# A.T.L.A.S. Official Technology Stack

## Purpose

This document defines the officially approved technologies for A.T.L.A.S.

All development assistants such as Gemini, ChatGPT, Claude and Antigravity must respect these decisions unless a justified Architecture Decision Record is created.

---

## Programming Language

Primary Language:

- Python 3.12+

---

## Backend

Approved:

- FastAPI

Forbidden:

- Flask for new development
- Django for the core backend

Reason:

FastAPI provides scalability, typing support and an API-first architecture.

---

## AI Provider

Primary:

- Gemini Pro

Requirements:

- Provider abstraction layer required.
- The AI provider must be replaceable without rewriting the system.

---

## Database

V1:

- SQLite

V2+:

- PostgreSQL

Requirements:

- Migration support.
- Future compatibility with scalable databases.

---

## Long-Term Memory

Approved:

- ChromaDB

Purpose:

- Semantic memory
- Conversation retrieval
- Context augmentation

---

## Voice Recognition

Approved:

- Whisper

Requirements:

- Local execution preferred.

---

## Text To Speech

Approved:

- Piper TTS

Requirements:

- Local execution preferred.

---

## Agents

Approved:

- CrewAI

Requirements:

- Modular agent architecture.

---

## Automation

Priority 1:

- Playwright
- Windows APIs
- PowerShell
- Official APIs from external services

Priority 2:

- PyAutoGUI

Requirements:

- API-first automation strategy.
- PyAutoGUI must only be used when no better API-based option exists.

---

## Web Knowledge

Approved:

- Search APIs
- Web retrieval
- Structured extraction
- Source summarization

Requirements:

- Source attribution.
- Modular implementation.

---

## Deployment

V1:

- Docker Local on Windows PC

V2:

- Docker on Linux VPS

V3:

- Hybrid Infrastructure

Requirements:

- Docker compatibility is mandatory from the beginning.

---

## Version Control

Approved:

- Git
- GitHub

Branch Strategy:

- main
- develop
- feature/*

---

## Documentation

Mandatory:

- PROJECT_CHARTER.md
- ARCHITECTURE.md
- AI_CONTEXT.md
- ROADMAP.md
- TECH_STACK.md

---

## Development Principles

- Scalability First
- Docker First
- Interface Independence
- Provider Independence
- Modular Design
- Long-Term Maintainability
