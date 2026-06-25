# skills/rules.md - Règles de Qualité Non Négociables - ProspectionCockpit

> **Ces règles sont absolues.** Toute violation doit être signalée immédiatement dans l’ANALYSE et corrigée avant APPLICATION. Elles s’appliquent à **toutes** les boucles, tous les niveaux.

## Règle 1 : Processus Loop Engineering Obligatoire

- Toute tâche (même un fix de 3 lignes ou une question de clarification) **doit** suivre les 5 phases dans l’ordre.
- Pas d’exception, pas de "je vais juste faire ça vite".
- Si la tâche est trop petite pour 5 phases complètes, utiliser une version allégée mais **complète** (mini-ANALYSE → mini-PLAN → mini-APPLICATION → mini-TEST → mini-AMÉLIORATION).

## Règle 2 : Sécurité & Secrets Zéro Tolérance

- **Jamais** de credentials, clés API, tokens en dur dans le code ou les commits.
- Toujours utiliser des variables d’environnement (`.env`, `pydantic-settings`, `python-dotenv`).
- Secrets management : `git-crypt` ou Doppler / Infisical en prod.
- Toute nouvelle intégration externe (Brevo, Twilio, LLM) passe par un adapter avec rotation possible.

## Règle 3 : Conformité RGPD & ePrivacy (Core Business Risk)

- **Avant toute action d’envoi** (email, SMS, LinkedIn, WhatsApp) : vérification **obligatoire** d’un consentement valide et traçable (double opt-in ou consentement explicite enregistré).
- Système de suppression (suppression list) centralisé et synchronisé avant tout envoi.
- Frequency capping + cooldown entre séquences.
- Tous les envois loggés avec : timestamp, canal, lead_id, template_version, consent_id, status.
- Export des données personnelles (droit à l’oubli) implémenté dès MVP.
- **Aucune** cold outreach automatisée sans consentement dans les 6 premiers mois.

## Règle 4 : Qualité de Code & Type Safety

- Type hints **stricts** partout (Pydantic v2 models, pas de `Any` sauf cas extrêmement justifié et documenté).
- Linter : Ruff avec zéro warning toléré (`ruff check --fix` avant commit).
- Type checker : mypy `--strict` mode activé en CI.
- Format : Ruff format (Black-compatible).
- Complexité : Fonctions < 20 lignes idéalement, responsabilité unique.
- Pas de code commenté mort. Supprimer ou refactoriser.

## Règle 5 : Tests & Vérification

- **Nouveau code métier critique** (scoring, séquences, consent, envoi) : tests unitaires + intégration obligatoires avant merge.
- Couverture minimale cible : 85% sur les modules core (mesurée en CI).
- Tests E2E (Playwright) pour les parcours critiques du cockpit.
- Pour les features LLM : au moins 3-5 cas de test "eval" (promptfoo ou custom harness) + revue humaine des outputs.
- Property-based testing (Hypothesis) encouragé pour les parsers et validateurs.
- Si un test échoue en CI : le build est cassé. Pas de merge.

## Règle 6 : Documentation & Traçabilité

- Docstrings obligatoires sur toutes les fonctions/classes publiques (format Google ou NumPy).
- READMEs et docs/ mis à jour dans la même boucle que le code.
- Conventional Commits stricts (`feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`).
- Chaque décision architecturale importante documentée dans `skills/architecture.md` ou ADR dans `docs/adr/`.
- STATE.md mis à jour systématiquement à la fin de chaque boucle.

## Règle 7 : Amélioration Continue & Capitalisation

- Chaque boucle **doit** identifier au moins **une** amélioration concrète (code, processus, prompt, test, skill).
- Les patterns réussis sont extraits dans `skills/` ou `loop-prompts/` pour réutilisation.
- Les erreurs répétées (hallucination sur un sujet) donnent lieu à une règle supplémentaire dans `rules.md`.
- Mesurer l’impact métier : "Cette feature a-t-elle amélioré le taux de réponse ou la qualité des leads ?"

## Règle 8 : Performance & Coût LLM

- Toujours mesurer/estimer le coût en tokens et latence avant d’implémenter une feature LLM-heavy.
- Utiliser LiteLLM pour le routage intelligent (DeepSeek d’abord, puis fallback plus cher si qualité insuffisante).
- Caching agressif des embeddings et des réponses LLM quand possible (Redis + semantic cache).
- Batching des appels LLM quand le cas d’usage le permet.
- Guardrails et output parsing stricts (instructor ou Pydantic + retry).

## Règle 9 : Collaboration Humain-IA

- L’IA propose, l’humain valide les décisions critiques (surtout RGPD, pricing, UI majeure).
- En cas de désaccord ou d’incertitude forte, ouvrir une boucle L1 de clarification avec l’utilisateur.
- L’humain peut forcer une boucle L4 de revue à tout moment.

## Règle 10 : Zéro Dette Technique Acceptée

- Pas de TODOs laissés sans ticket lié et date.
- Pas de code "quick & dirty" validé "pour l’instant".
- Si la complexité augmente, refactor immédiat ou planifié dans la même boucle.

**Ces 10 règles constituent le socle de qualité de ProspectionCockpit. Elles sont vérifiées implicitement dans chaque ANALYSE.**
