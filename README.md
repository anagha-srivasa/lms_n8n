# IntelliLearn: Agentic AI Learning Management System Workflow

## Project Overview

IntelliLearn is an adaptive Learning Management System (LMS) that leverages an automated n8n workflow to orchestrate local Large Language Models (LLMs) via LM Studio, facilitating personalized educational experiences.

This repository details the backend architecture of IntelliLearn. It demonstrates a low-code, highly observable agentic workflow utilizing n8n to integrate a Streamlit frontend with a locally hosted Qwen 3.5 model.

## n8n Workflow Architecture

The core artificial intelligence processing is managed by a custom n8n workflow. This system routes student queries, Retrieval-Augmented Generation (RAG) context derived from textbooks, and student metadata (such as historical learning rates) directly to the local LLM.

**Data Pipeline:**

1. **Streamlit Frontend:** Captures user input, subject matter, student learning metrics, and textbook RAG context.
2. **n8n Webhook (`POST`):** Receives the structured JSON payload.
3. **HTTP Request Node:** Formats the system and user prompts utilizing dynamic expressions and transmits the request to the local LM Studio server.
4. **Webhook Response:** Extracts the generated `llm_response` from the model (configured with a token limit of 2048 to accommodate comprehensive reasoning traces) and returns the parsed JSON to the frontend application.

## n8n Project Configuration

The complete n8n workflow utilized in this project can be viewed and imported via the following link:
**[Insert n8n Cloud / Workflow URL Here]**

*(Note for local implementation: Copy the raw workflow JSON from `workflow.json` within this repository and import it directly into your n8n workspace).*

## Key Features

* **Dynamic Query Resolution:** Customizes mathematical and scientific explanations based on the individual student's historical learning rate metric (scale: 1-100).
* **Local LLM Integration:** Ensures complete data privacy and offline inference capabilities using the Qwen 3.5 9B model via LM Studio.
* **Context-Aware Processing (RAG):** Injects instructor-uploaded textbook content directly into the prompt context to ensure factual accuracy and alignment with course material.
* **Visual Orchestration:** Enables streamlined debugging, payload inspection, and prompt modification directly through the n8n user interface, eliminating the need to alter backend Python code.

## Prerequisites

* **n8n:** Local npm installation, Docker container, or Desktop application.
* **LM Studio:** Configured to serve a local model on port `1234`, exposed to the local network (`0.0.0.0`).
* **Python 3.9+:** Required for executing the Streamlit dashboard.

## Implementation Guide

1. **Initialize LM Studio:** Load the designated Qwen model and start the local server. Ensure Cross-Origin Resource Sharing (CORS) is enabled if required by your network configuration.
2. **Import Workflow:** Open the n8n application, import the provided workflow, update the HTTP Request IP address to match your active IPv4 address, and set the workflow status to **Active**.
3. **Execute Frontend:**
```bash
pip install streamlit requests
streamlit run n8n_frontend.py

```



Would you like me to draft a specific section detailing the JSON payload structures to include in this documentation?
