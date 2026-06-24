# A.T.L.A.S. Core Design

## Purpose

This document defines how the internal modules of A.T.L.A.S. Core communicate and operate together.

A.T.L.A.S. Core is the central system responsible for reasoning, memory, action execution, web knowledge retrieval and communication with external interfaces.

---

## Core Principle

A.T.L.A.S. Core must never depend on a specific interface.

Desktop, mobile, Alexa, Smart TV and future clients must communicate with A.T.L.A.S. Core through the API layer.

This ensures that the system can grow without rewriting the core logic for every new device or platform.

---

## High-Level Architecture

```text
User
│
▼
Interface
│
├── Desktop Client
├── Mobile Client
├── Alexa Integration
├── Smart TV Integration
└── Future Interfaces
│
▼
API Layer
│
▼
A.T.L.A.S. Core
│
├── Brain
├── Memory
├── Voice
├── Agents
├── Automation
├── Web Knowledge
└── Integrations
│
▼
Response
```

---

## Main Request Flow

```text
User Request
│
▼
API Layer
│
▼
Context Manager
│
├── Memory Retrieval
├── Web Knowledge Retrieval
└── User Preferences
│
▼
Brain
│
▼
Action Planner
│
├── Answer directly
├── Use an agent
├── Search the web
├── Execute automation
└── Use an integration
│
▼
Response Generator
│
▼
API Layer
│
▼
User Interface
```

---

## Voice Flow

```text
User Voice
│
▼
Speech To Text
│
▼
API Layer
│
▼
Brain
│
▼
Memory Retrieval
│
▼
Action Planning
│
▼
Response Generation
│
▼
Text To Speech
│
▼
User
```

---

## Core Modules

### Brain

The Brain is responsible for reasoning, planning and natural language understanding.

Primary provider:

- Gemini Pro

Responsibilities:

- Understand user intent.
- Generate responses.
- Plan tasks.
- Decide when to use memory.
- Decide when to use web search.
- Decide when to execute actions.
- Coordinate agents.

Requirements:

- The Brain must use a provider abstraction layer.
- The AI provider must be replaceable without rewriting the system.
- A.T.L.A.S. must not be hardcoded directly to Gemini APIs in the core logic.

---

### Memory

The Memory module is responsible for long-term memory and contextual retrieval.

Technologies:

- SQLite for structured storage.
- ChromaDB for semantic memory.

Responsibilities:

- Store conversations.
- Store user preferences.
- Store important facts.
- Retrieve relevant memories.
- Provide context to the Brain.
- Support learning through memory, not model retraining.

Memory strategy:

A.T.L.A.S. will not train a model from zero in V1.

Instead, it will learn through:

- Stored conversations.
- Retrieved context.
- User preferences.
- Semantic memory.
- Knowledge augmentation.

---

### Voice

The Voice module is responsible for voice input and voice output.

Technologies:

- Whisper for speech-to-text.
- Piper TTS for text-to-speech.

Responsibilities:

- Convert user voice into text.
- Convert A.T.L.A.S. responses into speech.
- Prepare future support for wake word detection.

Future capability:

- Wake word activation.
- Real-time voice conversations.
- Voice profile customization.

---

### Agents

The Agents module is responsible for specialized autonomous tasks.

Approved framework:

- CrewAI

Initial agents:

- Research Agent
- Automation Agent
- Spotify Agent
- Memory Agent
- Web Knowledge Agent

Responsibilities:

- Execute specialized workflows.
- Break complex tasks into smaller steps.
- Coordinate with the Brain.
- Return structured results to A.T.L.A.S. Core.

Requirement:

Agents must remain modular and replaceable.

---

### Automation

The Automation module is responsible for interacting with the computer and external workflows.

Priority technologies:

- Playwright
- Windows APIs
- PowerShell

Fallback technology:

- PyAutoGUI only when no better option exists.

Responsibilities:

- Open applications.
- Execute system commands.
- Automate web workflows.
- Control supported desktop actions.
- Interact with the operating system safely.

Automation strategy:

A.T.L.A.S. must prioritize robust automation through APIs, commands and official integrations before using visual automation.

---

### Web Knowledge

The Web Knowledge module is responsible for retrieving updated information from the internet.

Responsibilities:

- Search the web.
- Retrieve updated information.
- Compare sources.
- Summarize content.
- Extract useful facts.
- Provide updated context to the Brain.

Requirements:

- Web search must be modular.
- Retrieved information must be passed to the Brain as context.
- Web results should not overwrite long-term memory automatically without validation.

---

### Integrations

The Integrations module is responsible for connecting A.T.L.A.S. with external services and devices.

Initial integrations:

- Spotify
- Mobile
- Alexa
- Smart TV

Responsibilities:

- Provide service-specific functionality.
- Keep external service logic separated from the Core.
- Avoid coupling A.T.L.A.S. Core to any single platform.

Spotify example:

```text
User asks for music
│
▼
Brain detects Spotify intent
│
▼
Spotify Agent or Integration
│
▼
Spotify API
│
▼
Response to user
```

---

## API Layer

The API Layer exposes A.T.L.A.S. Core to external clients.

Technology:

- FastAPI

Responsibilities:

- Receive user requests.
- Route requests to the correct module.
- Return responses.
- Support desktop clients.
- Support mobile clients.
- Support future Alexa and Smart TV clients.
- Support future WebSocket communication.

Important:

The API Layer is the only official entry point for external interfaces.

---

## Interface Independence

A.T.L.A.S. Core must not know whether the request came from:

- PC
- Mobile
- Alexa
- Smart TV
- Browser
- Future device

The Core only receives structured requests and returns structured responses.

Example:

```json
{
  "source": "mobile",
  "type": "voice_command",
  "content": "Open Spotify and play relaxing music"
}
```

The Core processes the request without depending on the interface.

---

## Deployment Compatibility

All modules must be compatible with Docker from the beginning.

Deployment stages:

### V1

Docker local on Windows PC.

### V2

Docker on Linux VPS.

### V3

Hybrid infrastructure using local and cloud components.

---

## Development Assistant Policy

Gemini Pro and Antigravity may assist during development.

They can help with:

- Code generation.
- Refactoring.
- Debugging.
- Documentation.
- Architecture review.

They must not become required production components.

A.T.L.A.S. must remain functional independently of any development assistant tool.

---

## Security Principles

A.T.L.A.S. will eventually interact with personal devices and applications.

Therefore, the system must include:

- Environment variables for secrets.
- No hardcoded API keys.
- Permission control.
- Logs for important actions.
- Safe execution of commands.
- Separation between user input and system-level actions.

---

## V1 Core Success Criteria

A.T.L.A.S. Core V1 is successful when it can:

- Receive a request through FastAPI.
- Send the request to the Brain.
- Use Gemini Pro through an abstraction layer.
- Store and retrieve memory.
- Search the web when needed.
- Execute basic automation.
- Return a structured response.
- Run inside Docker locally on Windows.
