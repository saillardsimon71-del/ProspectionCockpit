# skills/architecture.md - Architecture Logicielle Initiale - ProspectionCockpit

> Version 0.9 | Mise à jour : L1 Bootstrap | À enrichir en L3/L4 avec diagrammes Mermaid et décisions ADR.

## Principes Architecturaux Directeurs

1. **Clean Architecture / Hexagonale** : Séparation stricte entre Domain (règles métier pures), Application (use cases), Infrastructure (adapters : DB, LLM, Email/SMS providers).
2. **Domain-Driven Design (DDD)** : Bounded Contexts clairs (LeadManagement, ConsentCompliance, SequenceOrchestration, Analytics, UserTenant).
3. **Type Safety First** : Pydantic v2 comme source de vérité pour tous les contrats (API, LLM outputs, DB models).
4. **Event-Driven léger** : Les changements d’état importants (lead scored, sequence step executed, consent withdrawn) émettent des events pour découpler (future Kafka ou simple Redis pub/sub + DB outbox).
5. **Observability Native** : Correlation ID sur tous les flux, logging structuré, tracing LLM calls.
6. **Fail Fast + Graceful Degradation** : Si LLM down ou provider email en panne → fallback + alerte + mode dégradé (ex: séquence mise en pause).

## Vue d’Ensemble des Bounded Contexts (MVP)

```
┌─────────────────────────────────────────────────────────────────┐
│                        API Layer (FastAPI)                       │
├─────────────────────────────────────────────────────────────────┤
│  Lead API   │  Consent API  │  Sequence API  │  Analytics API   │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                     Application Services                        │
├─────────────────────────────────────────────────────────────────┤
│  LeadScoringService  │  SequenceOrchestrator  │  ConsentService │
│  EnrichmentService   │  NotificationService   │  AuditService   │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                        Domain Layer                             │
├─────────────────────────────────────────────────────────────────┤
│  Entities: Lead, Consent, Sequence, Campaign, Interaction       │
│  Value Objects: Score, Channel, ConsentStatus, TemplateVars     │
│  Aggregates: LeadAggregate (avec historique interactions)       │
│  Domain Services: ScoringEngine, ComplianceChecker              │
│  Domain Events: LeadScored, ConsentGranted, StepExecuted        │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                   Infrastructure Adapters                       │
├─────────────────────────────────────────────────────────────────┤
│  Postgres + pgvector (via SQLModel)  │  Redis (cache + queue)   │
│  LiteLLM Adapter (DeepSeek/Groq)     │  Brevo/Resend Adapter    │
│  Twilio Adapter (SMS)                │  CSV Import Adapter      │
│  Webhook Handlers                    │  File Storage (S3-like)  │
└─────────────────────────────────────────────────────────────────┘
```

## Stack Technique Détaillée (Proposée)

**Backend (Python)**
- FastAPI (routers, dependencies, lifespan)
- SQLModel (ORM + Pydantic en un) + Alembic migrations
- Celery + Redis (tasks pour exécution séquences asynchrones, retries avec backoff)
- LiteLLM + instructor (structured outputs LLM)
- structlog + contextvars pour correlation

**Frontend**
- Next.js 15 App Router
- Server Actions + tRPC ou simple fetch + React Query
- UI components library : shadcn/ui (accessible, thème artisan-friendly)

**Data**
- PostgreSQL 16 (tables leads, consents, sequences, interactions, audit_logs)
- pgvector extension (embeddings pour similarité leads / RAG contexte artisan)
- Redis (hot cache, Celery broker/backend, rate limit counters)

## Flux Critique Exemple : Scoring + Lancement Séquence

1. Artisan importe CSV ou ajoute lead manuellement → Lead entity créée
2. LeadScoringService (domain) : Règles métier + embedding + LLM classification → Score + raison
3. ConsentService vérifie existence consentement valide
4. SequenceOrchestrator crée Sequence aggregate + schedule les tasks Celery
5. Celery worker exécute Step 1 (email personnalisé via template + LLM vars)
6. Webhook réception (open/reply) → met à jour Interaction + déclenche Step 2 ou branche
7. Analytics mise à jour en batch ou event

## Points d’Extension Futurs (v1.5+)

- Multi-tenant (row level security + tenant_id sur toutes les tables)
- Workflow engine plus avancé (Temporal.io ou Prefect pour orchestration complexe)
- RAG complet sur historique de l’artisan (LlamaIndex + pgvector)
- Fine-tuning ou DSPy optimization des prompts de séquence
- Voice outbound (Twilio Voice + LLM)

## Recommandations pour le Code

- `src/` layout :
  ```
  src/
  ├── domain/          # Entités, VO, events, domain services (pur)
  ├── application/     # Use cases, services (orchestration)
  ├── infrastructure/ # Adapters DB, LLM, providers
  ├── api/             # FastAPI routers + schemas
  ├── shared/          # Utils, logging, exceptions
  ```
- Tests miroir : `tests/unit/domain/`, `tests/integration/`, `tests/e2e/`

**Ce fichier sera enrichi avec des diagrammes Mermaid et des ADR (Architecture Decision Records) dès la première boucle L3.**
