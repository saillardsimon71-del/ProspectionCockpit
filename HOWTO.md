# HOWTO.md - Guide d'Utilisation Complet - ProspectionCockpit + Loop Engineering

> **Objectif de ce fichier** : Te permettre de commencer à utiliser le système **immédiatement** et correctement, sans confusion.

---

## 1. Comprendre où est ton projet

**Le dossier `ProspectionCockpit` que tu clones depuis GitHub EST ton projet.**

Tu ne dois **pas** mettre les dossiers `.loop/`, `.clinerules/`, `skills/` etc. dans un autre projet existant.

Tu travailles **directement dedans** :

```
ProspectionCockpit/          ← C'est la racine de ton projet
├── .clinerules/             ← Règles Cline (lu automatiquement)
├── .loop/                    ← Loop Engineering
├── skills/                  ← Règles + Contexte
├── src/                     ← Code source (que tu vas créer)
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── ...
```

---

## 2. Prérequis

- VS Code + extension **Cline**
- Docker Desktop
- Git

---

## 3. Configuration Cline (la bonne façon)

Cline lit automatiquement les règles depuis le dossier `.clinerules/`.

Tu n'as **presque rien à faire** :

1. Clone ce repo
2. Ouvre le dossier `ProspectionCockpit` dans VS Code
3. Redémarre VS Code (ou recharge la fenêtre)
4. Cline devrait détecter automatiquement `.clinerules/loop-engineering.md`

C'est tout. Les règles Loop Engineering sont maintenant actives à chaque prompt.

---

## 4. Comment lancer une tâche

Commence toujours tes prompts dans Cline par :

```text
Exécute en mode Loop Engineering strict (L2). Tâche : [Ce que tu veux faire]

Lis d'abord complètement .loop/LOOP.md, .loop/STATE.md, skills/rules.md...
```

---

## 5. Lancer le projet en local

```bash
docker compose up --build
```

Puis va sur `http://localhost:8000/docs`

---

## 6. Règles d'Or

- Le dossier que tu ouvres dans VS Code = `ProspectionCockpit`
- `.clinerules/` est déjà à la racine
- Tu n'as pas besoin de copier/coller les dossiers ailleurs

Si tu as un ancien projet local séparé, dis-le-moi et on verra comment migrer le système Loop dedans.
