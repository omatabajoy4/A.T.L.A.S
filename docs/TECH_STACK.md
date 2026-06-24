# A.T.L.A.S. Official Technology Stack

## Purpose

This document defines the officially approved technologies for A.T.L.A.S.

All development assistants such as Gemini, ChatGPT, Claude and Antigravity must respect these decisions unless a justified Architecture Decision Record is created.

---

## Programming Language

Primary Language:

* Python 3.12+

---

## Backend

Approved:

* FastAPI

Forbidden:

* Flask for new development.
* Django for the core backend.

Reason:

FastAPI provides scalability, typing support and an API-first architecture.

---

## AI Provider

Primary:

* Gemini Pro

Requirements:

* Provider abstraction layer required.
* The AI provider must be replaceable without rewriting the system.
* A.T.L.A.S. Core must not be directly coupled to Gemini APIs.

---

## Database

V1:

* SQLite

V2+:

* PostgreSQL

Requirements:

* Migration support.
* Future compatibility with scalable databases.
* Structured storage must remain separated from semantic memory.

---

## Long-Term Memory

Approved:

* ChromaDB

Purpose:

* Semantic memory.
* Conversation retrieval.
* Context augmentation.
* Long-term user preference retrieval.

Requirements:

* Memory must be modular.
* Memory must support future replacement or scaling.
* A.T.L.A.S. must learn through memory and retrieval, not model retraining in V1.

---

## Voice Recognition

Approved:

* Whisper

Requirements:

* Local execution preferred.
* Must be separated from the Brain module.
* Must be replaceable in the future.

---

## Text To Speech

Approved:

* Piper TTS

Requirements:

* Local execution preferred.
* Must be separated from the Brain module.
* Must be replaceable in the future.

---

## Agents

Approved:

* CrewAI

Requirements:

* Modular agent architecture.
* Agents must be specialized.
* Agents must return structured results to A.T.L.A.S. Core.
* Agents must not directly control the user interface.

Initial agents:

* Research Agent.
* Automation Agent.
* Spotify Agent.
* Memory Agent.
* Web Knowledge Agent.

---

## Automation

Priority 1:

* Playwright.
* Windows APIs.
* PowerShell.
* Official APIs from external services.

Priority 2:

* PyAutoGUI only as fallback.

Requirements:

* API-first automation strategy.
* PyAutoGUI must only be used when no better API-based option exists.
* Automation must be separated from the Brain module.
* System-level actions must include safety checks.

Reason:

Visual automation based on mouse movement and screen position is fragile. A.T.L.A.S. must prioritize robust automation through APIs, commands and official integrations.

---

## Web Knowledge

Approved:

* Search APIs.
* Web retrieval.
* Structured extraction.
* Source summarization.

Requirements:

* Source attribution.
* Modular implementation.
* Retrieved information must be passed to the Brain as context.
* Web results must not overwrite long-term memory automatically without validation.

---

## Integrations

Initial integrations:

* Spotify.
* Mobile.
* Alexa.
* Smart TV.

Requirements:

* Integrations must remain separated from A.T.L.A.S. Core.
* External service logic must not be hardcoded into the Brain.
* Every integration must communicate through clear interfaces.

---

## API Layer

Approved:

* FastAPI

Responsibilities:

* Receive user requests.
* Route requests to A.T.L.A.S. Core.
* Return structured responses.
* Support future WebSocket communication.
* Support multiple interfaces.

Requirement:

The API Layer is the official entry point for external clients.

---

## Deployment

V1:

* Docker Local on Windows PC.

V2:

* Docker on Linux VPS.

V3:

* Hybrid Infrastructure.

Requirements:

* Docker compatibility is mandatory from the beginning.
* All components must be container-ready.
* The system must be portable between local and cloud environments.

---

## Version Control

Approved:

* Git.
* GitHub.

Branch Strategy:

* main
* develop
* feature/*

---

## Documentation

Mandatory:

* PROJECT_CHARTER.md
* ARCHITECTURE.md
* AI_CONTEXT.md
* ROADMAP.md
* TECH_STACK.md
* CORE_DESIGN.md
* decisions/

---

## Development Assistants

Approved as development tools:

* Gemini Pro.
* Antigravity.
* ChatGPT.
* Claude.

Important:

Development assistants are not production components.

A.T.L.A.S. must remain functional independently of any development assistant tool.

---

## Development Principles

* Scalability First.
* Docker First.
* Interface Independence.
* Provider Independence.
* Modular Design.
* Long-Term Maintainability.
* API-First Automation.
* Local-First Development.
* Cost Efficiency.
