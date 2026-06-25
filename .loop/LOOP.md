# .loop/LOOP.md - Framework Loop Engineering v1.0 - ProspectionCockpit

## Philosophie & Objectif

Ce fichier définit le **processus obligatoire** que l’agent IA (DeepSeek V4 Pro dans Cline) doit suivre pour **toute** intervention sur ProspectionCockpit.

Inspiré directement de **Loop Engineering** (Cobus Greyling, 2026) : au lieu de prompter l’IA tour à tour de manière manuelle, nous concevons un **système de boucle** qui :
- Lit l’état persistant (STATE.md)
- Analyse le contexte et les règles
- Planifie rigoureusement
- Applique avec qualité maximale
- Teste de manière exhaustive
- Améliore et persiste les apprentissages

**Résultat attendu** : Développement ultra-structuré, zéro approximation, amélioration continue du code **et** du funnel commercial, conformité RGPD native, et capitalisation des connaissances dans `skills/`.

## Niveaux de Boucle (L1 → L4)

| Niveau | Nom                    | Usage                                      | Exemple                          |
|--------|------------------------|--------------------------------------------|----------------------------------|
| L1     | Observation + Rapport  | Diagnostic, état des lieux, recommandations | Cette boucle de bootstrap       |
| L2     | Implémentation        | Feature, bugfix, intégration              | Ajouter scoring IA des leads    |
| L3     | Refactor & Optimisation| Dette tech, perf, structure                | Refactor domain models          |
| L4     | Revue Système         | Audit global, évolution architecture      | Mise à jour stack + skills     |

**Règle** : Toujours déclarer explicitement le niveau au début de la réponse.

## Processus en 5 Phases (Strictement Obligatoire)

Pour **chaque** boucle, suis EXACTEMENT cet ordre. Aucune phase ne peut être sautée, même pour une tâche "simple".

### 1. ANALYSE

**Actions obligatoires :**
- Lire **intégralement** (et internaliser) :
  - `.loop/STATE.md` (mémoire actuelle + décisions passées)
  - `skills/rules.md` (règles non négociables)
  - `skills/project-context.md` (utilisateurs, contraintes, objectifs)
  - `skills/architecture.md` (vue d’ensemble technique)
  - Fichiers de code pertinents (grep, tree si nécessaire)
- Identifier :
  - Objectif clair et mesurable de la tâche
  - Inputs / Outputs attendus
  - Contraintes (RGPD, coût LLM, performance, stack, légales)
  - Risques & edge cases (sécurité, conformité, hallucinations LLM, données manquantes)
  - Impact sur les autres modules / funnel commercial
- Outils : Utilise `bash`, `grep`, `find`, outils Cline pour explorer l’état réel.

**Sortie attendue** : Synthèse claire des découvertes, hypothèses, inconnues.

### 2. PLANIFICATION

**Actions obligatoires :**
- Produire un **plan détaillé** étape-par-étape avec critères de succès quantifiables.
- Choisir patterns architecturaux (Repository, Strategy pour scoring, State Machine pour séquences).
- Définir modèles de données (Pydantic schemas), endpoints, composants UI.
- Stratégie de test (unitaires, intégration, E2E, property-based, eval LLM).
- Estimer complexité, tokens LLM estimés, risques résiduels.
- Si la tâche est large (> L2), la décomposer en sous-boucles explicites.
- Toujours lier à l’amélioration du funnel : "Comment cette feature améliore-t-elle le taux de conversion ou la qualité des leads ?"

**Sortie attendue** : Plan numéroté, décisions techniques justifiées, check-list de validation.

### 3. APPLICATION

**Actions obligatoires :**
- Implémenter en suivant **100% des règles** de `skills/rules.md`.
- Code propre : Noms explicites, fonctions courtes, responsabilité unique, gestion d’erreurs robuste (never swallow exceptions), logging structuré avec correlation ID.
- Types stricts (Pydantic + mypy --strict).
- Documentation : Docstrings (format Google), commentaires seulement si nécessaire (le code doit se lire seul).
- Pour les features LLM : Templates de prompts versionnés dans `loop-prompts/`, variables claires, fallback, guardrails.
- Pour la prospection : Toujours vérifier le consentement avant toute action d’envoi.
- Utiliser les outils d’édition (edit_file, write_file) pour modifier le code.

**Sortie attendue** : Code fonctionnel, commit-ready, diffs clairs.

### 4. TEST

**Actions obligatoires :**
- Exécuter les tests existants + ajouter/mettre à jour les tests pour la nouvelle logique.
- Couvrir : Happy path, sad paths, edge cases, sécurité basique (injection, rate limit bypass).
- Pour LLM : Vérifier qualité des outputs (pas d’hallucination sur RGPD), latence, coût (via LiteLLM tracking).
- Lancer linters & type checkers (ruff check --fix, mypy, eslint).
- Test manuel si UI ou workflow complexe.
- **Si un test échoue** : Ne pas clore la boucle. Retourner en APPLICATION ou ouvrir nouvelle boucle L2 corrective.

**Sortie attendue** : Rapport de tests (passed/failed), couverture si applicable, captures d’écran ou logs si pertinent.

### 5. AMÉLIORATION

**Actions obligatoires :**
- Réflexion honnête et structurée :
  - Ce qui a bien fonctionné ?
  - Ce qui peut être amélioré (code smell, prompt faible, manque de test, lenteur du processus) ?
  - Impact réel sur les objectifs métier (conversion, temps artisan gagné) ?
- Proposer **au minimum 1 action concrète d’amélioration** (refactor, nouveau skill, mise à jour rules.md, nouveau cas de test, amélioration prompt).
- **Mettre à jour immédiatement `.loop/STATE.md`** avec le format structuré défini dedans.
- Si découverte réutilisable : Ajouter ou mettre à jour un fichier dans `skills/` ou `loop-prompts/`.

**Sortie attendue** : Synthèse des apprentissages + mise à jour STATE.md effective.

## Règles Strictes d’Exécution (Non Négociables)

1. **Zéro approximation** : Si tu ne sais pas ou si incertain sur un point critique (surtout RGPD, sécurité, logique métier), dis-le explicitement et propose une sous-boucle L1 d’investigation.
2. **Pas de skip de phase** : Même pour un "petit fix" de 5 lignes, faire les 5 phases en version allégée mais complète.
3. **Persistance obligatoire** : STATE.md est mis à jour à la fin de **chaque** boucle. C’est la source de vérité unique pour la mémoire long terme du projet.
4. **Qualité > Vitesse** : Un code parfait en 2 boucles L2 > 4 hacks rapides qui créent de la dette.
5. **Traçabilité maximale** : Commencer **chaque** réponse par :
   ```
   **L{ N } LOOP: [Nom clair de la tâche]**
   ```
   Puis structurer avec les 5 sections en **gras**.
6. **Outils réels** : Utiliser les outils Cline (terminal, édition fichiers) pour exécuter APPLICATION et TEST. Ne jamais simuler des résultats de tests.
7. **Conformité Prospection** : Avant toute logique d’envoi ou de séquence, le code doit passer par une vérification de consentement valide. Pas d’exception.

## Intégration Cline + DeepSeek V4 Pro (Configuration Immédiate)

Pour que le système fonctionne parfaitement avec ton éditeur :

### Étape 1 : Configuration unique dans Cline

Ajoute dans les **Custom Instructions** de Cline (ou crée `.cline/instructions.md` et référence-le) le texte suivant :

```
Tu opères sous le framework Loop Engineering v1.0 pour ProspectionCockpit.

MANDATORY AVANT TOUTE RÉPONSE OU ACTION :
1. Lis et internalise complètement :
   - .loop/LOOP.md (le processus exact)
   - .loop/STATE.md (mémoire persistante - tu dois la mettre à jour à la fin)
   - skills/rules.md (règles non négociables - zéro violation)
   - skills/project-context.md
   - skills/architecture.md

2. Structure TOUJOURS ta réponse comme suit :
   **L{ N } LOOP: [Nom de la tâche]**
   **ANALYSE:**
   ...
   **PLANIFICATION:**
   ...
   **APPLICATION:**
   ...
   **TEST:**
   ...
   **AMÉLIORATION:**
   (puis mise à jour effective de STATE.md)

3. Qualité maximale exigée. Zéro approximation. Si tu es incertain sur RGPD ou sécurité : arrête et signale.
```

### Étape 2 : Pour chaque nouvelle tâche / prompt

Commence ton prompt à Cline par :

```
Exécute en mode Loop Engineering strict (L2). Tâche : [Description précise et mesurable de ce que tu veux accomplir].

Lis d'abord intégralement les fichiers mémoire avant de commencer l'ANALYSE.
```

L’agent DeepSeek V4 Pro sera alors "harnessé" et produira des résultats de qualité professionnelle constante.

## Version & Évolution

- **Version actuelle** : 1.0 (Bootstrap L1 - 2026-06-25)
- Les mises à jour de ce fichier se font uniquement en boucle **L4**.
- Historique des changements tracké dans `.loop/STATE.md` (section Log des Boucles).

Ce framework est vivant et s’améliore avec chaque boucle.
