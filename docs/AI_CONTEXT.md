# A.T.L.A.S. AI CONTEXT

Before proposing any solution, every AI assistant must read and follow this document.

This document defines the official context, architecture rules, technology constraints and development boundaries for A.T.L.A.S.

---

## Project Name

A.T.L.A.S.

Artificial Thinking, Learning and Action System

---

## Main Objective

Build a free, scalable, modular and multiplatform personal AI ecosystem capable of thinking, learning, remembering, acting and interacting with devices, applications and external services.

A.T.L.A.S. is not a chatbot.

A.T.L.A.S. is a personal AI ecosystem.

---

## Core Vision

A.T.L.A.S. must be able to:

* Think using Gemini Pro.
* Learn through memory and contextual retrieval.
* Act through automation and integrations.
* Communicate through voice and multiple interfaces.
* Search the web for updated knowledge.
* Scale from a local Windows PC to a Linux VPS and later to hybrid infrastructure.

---

## Approved Technologies

### Programming Language

* Python 3.12+

### Backend

* FastAPI

### AI Provider

* Gemini Pro

### Databases

* SQLite for V1.
* PostgreSQL for future versions.

### Semantic Memory

* ChromaDB

### Voice

* Whisper for speech-to-text.
* Piper TTS for text-to-speech.

### Agents

* CrewAI

### Automation

Priority 1:

* Playwright.
* Windows APIs.
* PowerShell.
* Official APIs from external services.

Priority 2:

* PyAutoGUI only as fallback.

### Deployment

* Docker

### Version Control

* Git
* GitHub

---

## Architecture Rules

All AI assistants must respect these rules:

* Use modular architecture.
* Follow Docker-first development.
* Prioritize scalability.
* Keep provider independence.
* Keep interface independence.
* Keep A.T.L.A.S. Core separated from clients.
* Keep automation separated from the Brain.
* Keep memory separated from the Brain.
* Keep integrations separated from the Core.
* Use API-first automation before visual automation.

---

## Interface Independence Rule

A.T.L.A.S. Core must never depend on a specific interface.

The same Core must be able to serve:

* Desktop client.
* Mobile client.
* Alexa integration.
* Smart TV integration.
* Future interfaces.

External interfaces must communicate with A.T.L.A.S. Core through the API layer.

---

## AI Provider Rule

Gemini Pro is the primary AI provider.

However, A.T.L.A.S. must be provider-agnostic.

The Brain module must use an abstraction layer so the AI provider can be replaced in the future without rewriting the entire system.

Forbidden:

* Hardcoding Gemini directly into all core logic.
* Making A.T.L.A.S. impossible to migrate to another provider.
* Mixing provider-specific logic with business logic.

---

## Memory Rule

A.T.L.A.S. must learn through memory and retrieval, not model retraining in V1.

Memory must support:

* Stored conversations.
* User preferences.
* Important facts.
* Semantic retrieval.
* Context augmentation.

Approved memory technologies:

* SQLite for structured storage.
* ChromaDB for semantic memory.

---

## Automation Rule

A.T.L.A.S. must prioritize robust automation.

Priority order:

1. Official APIs.
2. PowerShell or system commands.
3. Windows APIs.
4. Playwright for browser automation.
5. PyAutoGUI only when no better option exists.

PyAutoGUI must not be used as the main automation strategy.

Reason:

Visual automation based on mouse position and screen layout is fragile and does not scale well.

---

## Web Knowledge Rule

A.T.L.A.S. must be able to search the web for updated information.

Web Knowledge must support:

* Web search.
* Source retrieval.
* Summarization.
* Structured extraction.
* Source attribution.

Web results must be passed to the Brain as context.

Web results must not overwrite long-term memory automatically without validation.

---

## Development Assistant Rule

Gemini Pro, Antigravity, ChatGPT and Claude may be used as development assistants.

They can help with:

* Code generation.
* Refactoring.
* Debugging.
* Documentation.
* Architecture review.

They must not become required production components.

A.T.L.A.S. must remain functional independently of any development assistant tool.

---

## Forbidden Actions

AI assistants must not:

* Replace FastAPI without strong justification.
* Use obsolete or unmaintained libraries.
* Couple A.T.L.A.S. Core to a specific UI.
* Break Docker compatibility.
* Introduce paid dependencies without approval.
* Replace the approved architecture without creating an ADR.
* Use PyAutoGUI as the main automation system.
* Hardcode secrets or API keys.
* Put production secrets inside the repository.
* Mix experimental code with core architecture without approval.

---

## Official Deployment Strategy

### V1

Docker local on Windows PC.

### V2

Docker on Linux VPS.

### V3

Hybrid infrastructure using local and cloud components.

All components must be Docker-compatible from the beginning.

---

## Documentation Reading Order

Before implementing features, AI assistants must read:

1. PROJECT_CHARTER.md
2. ARCHITECTURE.md
3. AI_CONTEXT.md
4. TECH_STACK.md
5. CORE_DESIGN.md
6. ROADMAP.md
7. docs/decisions/

---

## Current Development Stage

A.T.L.A.S. is currently in the foundation and architecture stage.

The next stage is the implementation of A.T.L.A.S. Core using:

* Docker.
* FastAPI.
* Gemini provider abstraction.
* Basic request-response flow.
* Modular project structure.
