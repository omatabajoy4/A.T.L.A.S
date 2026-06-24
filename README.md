# A.T.L.A.S.

Artificial Thinking, Learning and Action System

## Overview

A.T.L.A.S. is a personal artificial intelligence ecosystem designed to think, learn, remember and act.

The system combines conversational intelligence, long-term memory, web knowledge retrieval, automation capabilities and multi-device communication into a modular and scalable architecture.

A.T.L.A.S. is not a chatbot. It is a personal AI ecosystem.

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

## Main Modules

```text
A.T.L.A.S. Core
│
├── Brain
├── Memory
├── Voice
├── Agents
├── Automation
├── Web Knowledge
├── Integrations
└── API Layer
```

---

## Official Technology Stack

* Python 3.12+
* FastAPI
* Gemini Pro
* ChromaDB
* SQLite
* PostgreSQL in future versions
* Whisper
* Piper TTS
* CrewAI
* Playwright
* Windows APIs
* PowerShell
* PyAutoGUI only as fallback
* Docker
* GitHub

---

## Deployment Strategy

### V1

Docker Local on Windows PC.

### V2

Docker on Linux VPS.

### V3

Hybrid Infrastructure: Local + Cloud.

---

## Interface Independence

A.T.L.A.S. Core must never depend on a specific interface.

The same core must be able to serve:

* Desktop client
* Mobile client
* Alexa integration
* Smart TV integration
* Future interfaces

---

## Documentation

Project documentation is available in the `docs/` directory:

* `PROJECT_CHARTER.md`
* `ARCHITECTURE.md`
* `AI_CONTEXT.md`
* `ROADMAP.md`
* `TECH_STACK.md`
* `CORE_DESIGN.md`
* `decisions/`

---

## Development Assistants

Gemini Pro and Antigravity may be used as development assistants.

They are not production components of A.T.L.A.S.

A.T.L.A.S. must remain functional independently of any development assistant tool.

---

## Current Status

Project foundation and architecture definition.

The next development stage is the implementation of A.T.L.A.S. Core using Docker, FastAPI and the approved modular architecture.
