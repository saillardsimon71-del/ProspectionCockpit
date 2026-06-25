# loop-prompts/loop-execute.md - Template Prompt pour Exécution d'une Boucle Lx

## Usage

Copie ce template et remplis les sections entre [crochets] quand tu veux exécuter une nouvelle boucle via Cline/DeepSeek.

Ce prompt force le respect du framework et maximise la qualité.

---

```
Exécute en mode Loop Engineering strict pour ProspectionCockpit.

**Niveau de boucle** : L[1|2|3|4]
**Nom de la tâche** : [ex: Implémenter le scoring IA des leads avec règles métier + embeddings]

**Contexte supplémentaire** : [optionnel - détails spécifiques, liens vers tickets, exemples de leads, etc.]

**Instructions spéciales** : [ex: Priorise la conformité RGPD. Utilise LiteLLM. Ajoute des tests property-based.]

---

Avant de commencer, lis et internalise complètement :
- .loop/LOOP.md
- .loop/STATE.md (version actuelle)
- skills/rules.md
- skills/project-context.md
- skills/architecture.md

Puis structure ta réponse EXACTEMENT comme suit :

**L2 LOOP: Implémenter le scoring IA des leads avec règles métier + embeddings**

**ANALYSE:**
[Synthèse de la lecture des fichiers mémoire, découvertes, risques identifiés, edge cases (ex: lead sans localisation, artisan sans historique, etc.)]

**PLANIFICATION:**
1. ...
2. ...
[Plan détaillé avec décisions techniques justifiées et critères de succès]

**APPLICATION:**
[Description des changements de code, modèles Pydantic, nouvelles fonctions, diffs ou chemins de fichiers modifiés. Utilise les outils d’édition réels.]

**TEST:**
[Rapport des tests exécutés (commandes, résultats), couverture, cas passés/échoués, vérification manuelle si pertinent.]

**AMÉLIORATION:**
[Apprentissages, ce qui peut être amélioré, actions concrètes, mise à jour de STATE.md effectuée avec résumé des changements clés.]

---

À la fin de la boucle, tu DOIS mettre à jour le fichier .loop/STATE.md avec les nouvelles informations (phase, décisions, learnings, nouveaux backlog items, etc.) en utilisant le format structuré existant.
```

**Conseil** : Sauvegarde ce template dans tes snippets Cline ou utilise-le systématiquement pour garder une qualité constante.
