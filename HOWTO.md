# HOWTO.md - Guide d'Utilisation Complet - ProspectionCockpit + Loop Engineering

> **Objectif de ce fichier** : Te permettre de commencer à utiliser le système **immédiatement** et correctement, sans confusion.

---

## 1. Prérequis

- VS Code + extension **Cline** (ou équivalent type Continue.dev configuré avec DeepSeek V4 Pro)
- Docker Desktop installé et lancé
- Git clone du repo
- Clé API DeepSeek (gratuite ou payante selon usage)

---

## 2. Configuration Unique de Cline (5 minutes)

C'est l'étape la plus importante.

### Option A (Recommandée) - Custom Instructions

1. Ouvre VS Code
2. Va dans les paramètres de **Cline** (icône Cline dans la barre latérale ou Command Palette > Cline: Open Settings)
3. Colle **tout le contenu** du fichier :
   ```
   loop-prompts/cline-integration.md
   ```
   dans le champ **Custom Instructions** / **System Prompt**.

### Option B - Fichier .cline/instructions.md

Crée un fichier `.cline/instructions.md` à la racine du projet et colle le même texte dedans. Cline le lit souvent automatiquement.

**Une fois fait**, DeepSeek V4 Pro saura **automatiquement** qu'il doit suivre le Loop Engineering à chaque fois.

---

## 3. Comment Lancer une Tâche (Workflow Quotidien)

**NE JAMAIS** commencer à coder directement.

### Étape par étape :

1. Ouvre Cline dans VS Code sur le dossier `ProspectionCockpit`
2. Dans la fenêtre de chat Cline, écris **exactement** ceci au début de ton prompt :

```text
Exécute en mode Loop Engineering strict (L2). Tâche : [Description claire et précise de ce que tu veux faire]

Lis d'abord complètement .loop/LOOP.md, .loop/STATE.md, skills/rules.md et skills/project-context.md.
```

3. Appuie sur Entrée.

Cline / DeepSeek va alors :
- Lire les fichiers mémoire
- Suivre les **5 phases** (ANALYSE → PLANIFICATION → APPLICATION → TEST → AMÉLIORATION)
- Te proposer les modifications de code
- **Mettre à jour automatiquement** `.loop/STATE.md` à la fin

---

## 4. Exemple Concret de Premier Prompt

```text
Exécute en mode Loop Engineering strict (L2). Tâche : Ajouter Alembic + configuration SQLModel engine dans le lifespan de FastAPI et créer la première migration.

Lis d'abord complètement .loop/LOOP.md, .loop/STATE.md, skills/rules.md et skills/project-context.md.
```

Cline va alors produire une boucle complète L2 structurée.

---

## 5. Lancer le Projet en Local (Test Immédiat)

```bash
# 1. Clone ou pull le repo
cd ProspectionCockpit

# 2. Crée ton fichier .env
cp .env.example .env

# 3. (Optionnel) Ajoute ta clé DeepSeek dans .env
# DEEPSEEK_API_KEY=sk-...

# 4. Lance tout
docker compose up --build

# 5. Teste
curl http://localhost:8000/health
# ou ouvre http://localhost:8000/docs
```

Tu devrais voir :
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "message": "ProspectionCockpit API is running (Loop Engineering mode)"
}
```

---

## 6. Règles d'Or à Respecter

- **Toujours** commencer par "Exécute en mode Loop Engineering strict (L2)..."
- **Jamais** demander à Cline de "juste faire le code" sans la boucle.
- À la fin de chaque tâche, vérifie que `.loop/STATE.md` a bien été mis à jour.
- Si Cline saute une phase → arrête-le et rappelle-lui la règle.
- Pour les petites questions : utilise L1 ("Exécute en mode Loop Engineering strict (L1). Tâche : Analyse de...")

---

## 7. Prochaines Actions Recommandées

1. Configure Cline (section 2)
2. Teste `docker compose up`
3. Fais ta **première vraie boucle L2** avec l'exemple du section 4
4. Lis `.loop/LOOP.md` en entier (une seule fois)

---

**Tu es maintenant opérationnel.**
Le système est conçu pour que même DeepSeek V4 Pro produise un travail de niveau Senior Principal Engineer à chaque itération.

Si tu as la moindre question sur l'utilisation, pose-la en mode L1 et je t'aiderai.
