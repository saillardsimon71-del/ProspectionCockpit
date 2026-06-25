# ProspectionCockpit

> **Outil d’automatisation intelligente du funnel complet de prospection → conversion pour artisans sans site web.**

Leads → Scoring IA → Séquences multicanales (Email/SMS/LinkedIn) → Qualification → Conversion + Boucle d’amélioration continue (logiciel + commerciale).

## Objectif

Permettre aux artisans (plombiers, électriciens, couvreurs, etc.) d’automatiser et d’optimiser en continu leur prospection commerciale de manière **conforme RGPD / ePrivacy**, avec un focus sur la qualité des leads, la personnalisation et le suivi du ROI.

## Philosophie & Framework

Ce projet est construit sur **Loop Engineering** (inspiré de Cobus Greyling) : un système où l’IA (DeepSeek V4 Pro via Cline) ne répond pas de manière libre, mais exécute des boucles structurées (ANALYSE → PLANIFICATION → APPLICATION → TEST → AMÉLIORATION) qui lisent/ écrivent un état persistant (STATE.md), respectent des règles non négociables et capitalisent les apprentissages.

Résultat : Développement de très haute qualité, traçable, auto-améliorant et résistant aux hallucinations.

## Structure du Projet (Loop Engineering)

```
ProspectionCockpit/
├── .loop/
│   ├── LOOP.md          # Définition stricte du processus + intégration Cline
│   ├── STATE.md         # Mémoire persistante (mise à jour à chaque boucle)
├── skills/
│   ├── rules.md         # Règles de qualité non négociables
│   ├── project-context.md # Contexte global, utilisateurs, contraintes, métriques
│   ├── architecture.md  # Architecture logicielle (clean/DDD/hexagonale)
├── loop-prompts/
│   ├── loop-execute.md   # Template de prompt pour exécuter une boucle
│   ├── cline-integration.md # Instructions prêtes à copier pour Cline/DeepSeek
├── src/               # (Futur) Code source backend/frontend
├── tests/             # (Futur) Tests
├── docs/              # Documentation utilisateur & technique
├── README.md
├── .gitignore
└── pyproject.toml     # (Futur) ou package.json
```

## Stack Technique Proposée (v1 - à valider L2)

**Backend (Python)**
- FastAPI + Pydantic v2 + SQLModel + Alembic
- Celery + Redis (queues, rate limiting, séquences stateful)
- PostgreSQL 16 + pgvector (embeddings leads + performance séquences)
- LiteLLM (routage multi-LLM : DeepSeek prioritaire pour coût/qualité)

**Frontend**
- Next.js 15 (App Router, TypeScript strict, RSC)
- Tailwind CSS 4 + shadcn/ui + TanStack Table/Query + Recharts

**IA & Automatisation**
- Personnalisation séquences via LLM + RAG léger
- Scoring leads multi-critères (IA + règles métier)
- Workflow engine pour séquences (retry, branching sur réponse/ouverture)

**Qualité & Ops**
- Ruff + mypy + pre-commit
- pytest (backend) + Vitest + Playwright (frontend)
- GitHub Actions CI + Docker Compose local
- Observabilité : Structlog + Sentry + (futur) Langfuse/Helicone pour LLM

**Conformité**
- Module Consent & Suppression List en coeur de domaine
- Audit logs complets + export RGPD
- Rate limiting + frequency capping + double opt-in

## Démarrage Rapide (pour le développeur)

1. Clone le repo
2. Lis **.loop/LOOP.md** en entier
3. Configure Cline (voir .loop/LOOP.md > section Intégration Cline)
4. Lis **.loop/STATE.md** et **skills/rules.md**
5. Commence toute nouvelle tâche par : "Exécute Loop Engineering L2. Tâche : [..]" 

## Prochaines Étapes Immédiates (issu de L1)

Voir le rapport L1 dans `.loop/STATE.md` (section Backlog Prioritaire).

**Statut** : Bootstrap Loop Engineering terminé (L1). Prêt pour développement itératif de haute qualité.

---

*Conçu avec rigueur par Senior Principal Engineer - Loop Engineering mode activé.*