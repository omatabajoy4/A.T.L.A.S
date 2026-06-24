# A.T.L.A.S. Roadmap

## Purpose

This document defines the official development roadmap for A.T.L.A.S.

A.T.L.A.S. will be developed progressively, starting with a local Docker-based core and evolving into a distributed, multi-interface AI ecosystem.

---

## Phase 1: Core Foundation

Goal:

Build the minimum foundation of A.T.L.A.S. Core.

Tasks:

* Create the official project structure.
* Configure Docker local development.
* Set up FastAPI.
* Create the first health-check endpoint.
* Define the internal module interfaces.
* Prepare environment variable handling.
* Add basic logging.
* Prepare the Gemini provider abstraction.

Success Criteria:

* A.T.L.A.S. runs locally inside Docker.
* FastAPI exposes a working endpoint.
* The project structure follows the approved architecture.
* No secrets are hardcoded.

---

## Phase 2: Brain

Goal:

Connect A.T.L.A.S. Core with Gemini Pro through a provider abstraction layer.

Tasks:

* Create the Brain module.
* Create an AI provider interface.
* Implement Gemini as the first provider.
* Add prompt management.
* Add basic request-response processing.
* Return structured responses.

Success Criteria:

* A.T.L.A.S. can receive a text request.
* A.T.L.A.S. can send it to Gemini through the Brain module.
* A.T.L.A.S. can return a structured response.
* Gemini is not hardcoded directly into all core logic.

---

## Phase 3: Memory

Goal:

Give A.T.L.A.S. persistent memory.

Tasks:

* Add SQLite for structured storage.
* Add ChromaDB for semantic memory.
* Store conversations.
* Store user preferences.
* Retrieve relevant memories.
* Pass memory context to the Brain.

Success Criteria:

* A.T.L.A.S. can save conversations.
* A.T.L.A.S. can retrieve relevant memories.
* A.T.L.A.S. can improve responses using memory context.
* Memory remains separated from the Brain module.

---

## Phase 4: Web Knowledge

Goal:

Allow A.T.L.A.S. to retrieve updated information from the web.

Tasks:

* Create the Web Knowledge module.
* Add web search capability.
* Add page retrieval.
* Add content summarization.
* Add source attribution.
* Pass retrieved information to the Brain as context.

Success Criteria:

* A.T.L.A.S. can search for updated information.
* A.T.L.A.S. can summarize retrieved content.
* A.T.L.A.S. can use web context in responses.
* Web results do not overwrite long-term memory automatically.

---

## Phase 5: Voice

Goal:

Allow A.T.L.A.S. to listen and speak.

Tasks:

* Add Whisper for speech-to-text.
* Add Piper TTS for text-to-speech.
* Create the Voice module.
* Connect voice input to the API layer.
* Connect generated responses to voice output.

Success Criteria:

* A.T.L.A.S. can receive voice input.
* A.T.L.A.S. can transcribe user speech.
* A.T.L.A.S. can respond using synthesized speech.
* Voice remains separated from the Brain module.

---

## Phase 6: Automation

Goal:

Allow A.T.L.A.S. to act on the computer and automate workflows.

Priority technologies:

* Official APIs.
* PowerShell.
* Windows APIs.
* Playwright.

Fallback:

* PyAutoGUI only when no better option exists.

Tasks:

* Create the Automation module.
* Add safe command execution.
* Add PowerShell task execution.
* Add basic Windows interaction.
* Add Playwright for browser automation.
* Define permission and safety checks.
* Keep PyAutoGUI as fallback only.

Success Criteria:

* A.T.L.A.S. can execute safe system actions.
* A.T.L.A.S. can automate web workflows with Playwright.
* A.T.L.A.S. does not depend primarily on visual automation.
* Automation remains separated from the Brain module.

---

## Phase 7: Agents

Goal:

Add specialized agents for complex tasks.

Tasks:

* Add CrewAI.
* Create the Research Agent.
* Create the Automation Agent.
* Create the Spotify Agent.
* Create the Memory Agent.
* Create the Web Knowledge Agent.
* Define communication between agents and A.T.L.A.S. Core.

Success Criteria:

* A.T.L.A.S. can delegate specialized tasks to agents.
* Agents return structured results.
* Agents remain modular and replaceable.

---

## Phase 8: Spotify Integration

Goal:

Allow A.T.L.A.S. to interact with Spotify.

Tasks:

* Create the Spotify integration module.
* Configure Spotify API credentials.
* Add authentication flow.
* Add basic playback control.
* Add playlist search.
* Connect Spotify actions to the Brain and Agents.

Success Criteria:

* A.T.L.A.S. can understand music-related requests.
* A.T.L.A.S. can interact with Spotify through its API.
* Spotify logic remains separated from the Core.

---

## Phase 9: Mobile Integration

Goal:

Allow mobile clients to communicate with A.T.L.A.S. Core.

Tasks:

* Define mobile API contract.
* Add authentication for external clients.
* Prepare WebSocket communication.
* Create basic mobile interaction flow.

Success Criteria:

* A mobile client can send requests to A.T.L.A.S. Core.
* A.T.L.A.S. Core does not depend on the mobile interface.
* Communication happens through the API layer.

---

## Phase 10: Alexa Integration

Goal:

Prepare A.T.L.A.S. for Alexa as a voice interface.

Tasks:

* Study Alexa Skill requirements.
* Create Alexa integration module.
* Define request-response mapping.
* Connect Alexa requests to A.T.L.A.S. Core through the API layer.

Success Criteria:

* Alexa acts only as an interface.
* A.T.L.A.S. Core remains the intelligence layer.
* Alexa does not replace the Brain.

---

## Phase 11: Smart TV Integration

Goal:

Prepare A.T.L.A.S. for Smart TV interaction.

Tasks:

* Define Smart TV client requirements.
* Create TV integration module.
* Define supported commands.
* Connect TV requests through the API layer.

Success Criteria:

* Smart TV integration remains separated from the Core.
* A.T.L.A.S. can support TV as another interface.

---

## Phase 12: VPS Deployment

Goal:

Move A.T.L.A.S. from local Docker to Linux VPS.

Tasks:

* Prepare production Docker configuration.
* Configure Linux VPS deployment.
* Add secure environment variables.
* Add HTTPS.
* Add authentication.
* Add persistent storage.
* Add basic monitoring.

Success Criteria:

* A.T.L.A.S. can run on a Linux VPS.
* A.T.L.A.S. can be accessed remotely.
* Secrets remain protected.
* Docker compatibility is preserved.

---

## Phase 13: Hybrid Infrastructure

Goal:

Evolve A.T.L.A.S. into a hybrid local and cloud ecosystem.

Tasks:

* Decide which modules run locally.
* Decide which modules run in the cloud.
* Add secure communication between local and cloud services.
* Improve reliability.
* Add monitoring and logs.
* Prepare future scaling.

Success Criteria:

* A.T.L.A.S. can operate across local and cloud components.
* Interfaces can connect from multiple devices.
* The Core remains modular and scalable.
