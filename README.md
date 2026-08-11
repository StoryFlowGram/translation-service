# Translation Service

> Microservice providing word/sentence translations and AI-powered context explanations using Google Translate and Google Gemini.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Running the Service](#running-the-service)
- [Environment Variables](#environment-variables)
- [API](#api)
- [Project Structure](#project-structure)

---

## Overview

Translation Service powers language learning features across the platform:

- **Word & Sentence Translation**: Fast text translation between target languages via `googletrans`
- **AI Explanations**: Deep contextual vocabulary analysis and usage examples powered by `google-genai` (Gemini API)
- **Rate Limiting**: Built-in rate limiting (`InMemoryRateLimiter`) per user to prevent API quota exhaustion

---

## Architecture

```
Client ──▶ API Gateway ──▶ Translation Service ──┬──▶ Google Translate API
                                                 └──▶ Google Gemini API
```

---

## Technology Stack

| Package | Version | Role |
|--------|---------|------|
| `fastapi[all]` | ^0.121.0 | Web framework |
| `googletrans` | ^4.0.2 | Translation library |
| `google-genai` | ^2.8.0 | Google Gemini SDK for AI explanations |
| `slowapi` | ^0.1.9 | Rate limiting |
| Python | ≥ 3.12 | Runtime |

---

## Running the Service

### Locally (Poetry)

```bash
cd Backend/translation-service
cp .env.example .env
poetry install
uvicorn main:app --reload --port 8006
```

### Docker

```bash
docker build -t sfg-translation-service .
docker run -p 8006:8000 --env-file .env sfg-translation-service
```

---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GEMINI_API_KEY` | API Key for Google Gemini AI service | `AIzaSy...` |
| `INTERNAL_GATEWAY_TOKEN` | Secret token for validating inter-service requests | `replace_me` |

---

## API

### `GET /health`

```json
{
  "status": "ok",
  "service": "translation-service"
}
```

### `POST /translate/word`

Translates a single word.

```json
{
  "text": "hello",
  "src_lang": "en",
  "dest_lang": "uk"
}
```

### `POST /sentence`

Translates a sentence in context.

```json
{
  "text": "The quick brown fox jumps over the lazy dog.",
  "src_lang": "en",
  "dest_lang": "uk"
}
```

### `POST /ai/explain`

Generates an AI-based definition, translation, and usage examples for a word.

```json
{
  "word": "resilient"
}
```

---

## Project Structure

```
translation-service/
├── main.py                   # Entrypoint and router setup
├── app/
│   ├── domain/               # Exceptions & protocols
│   ├── application/          # Use cases for translation and AI analysis
│   ├── infrastructure/       # Google Translate & Gemini adapters, settings
│   └── presentation/         # Controllers, rate limiters, schemas
├── Dockerfile
└── pyproject.toml
```
