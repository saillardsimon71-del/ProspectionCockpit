# skills/project-context.md - Contexte Global du Projet ProspectionCockpit

## Vision

ProspectionCockpit est l’outil qui permet aux artisans indépendants (sans site web ou présence digitale faible) de **professionnaliser et automatiser leur prospection commerciale** de A à Z, avec une boucle d’amélioration continue basée sur les résultats réels (taux de réponse, conversion, coût par lead).

L’artisan n’a plus à "chasser" manuellement tous les soirs. Le système trouve des leads qualifiés, les score, leur envoie des séquences personnalisées multicanales, qualifie les réponses et optimise en continu les messages et les critères.

## Utilisateurs Cibles (Personas)

**Persona principal : L’Artisan Indépendant**
- Métier : Plombier, électricien, couvreur, peintre, menuisier, serrurier, chauffagiste (BTP & services à domicile)
- Taille : 1 à 5 salariés, CA 80k–400k€/an
- Douleur actuelle : Passe 8-12h/semaine à chercher des chantiers (Pages Jaunes, Google, bouche à oreille, réseau). Taux de conversion faible (~5-8%). Beaucoup de déplacements inutiles.
- Objectif avec l’outil : Gagner 6-10h/semaine, augmenter le taux de closing de 30-50%, avoir une visibilité claire sur son pipeline.
- Contraintes : Budget limité (50-150€/mois max), peu de temps pour configurer des outils complexes, besoin de simplicité et de résultats rapides.
- Niveau tech : Moyen (utilise WhatsApp, Google Maps, pas de CRM avancé).

**Persona secondaire : Le Chef d’Équipe / Petite Entreprise BTP**
- 5-15 salariés, veut scaler la prospection sans recruter un commercial full-time.

## Marché & Contraintes Légales (France / UE)

- **RGPD + ePrivacy Directive** : Extrêmement strictes sur la prospection électronique. Cold email/SMS sans consentement = risque d’amende élevé.
- **Loi "anti-spam" française** et CNIL : Consentement explicite, information claire, désinscription facile, conservation limitée.
- **Scraping** : Légalement risqué (surtout LinkedIn, Pages Jaunes automatisé). Privilégier les sources avec droit d’utilisation clair ou import CSV + enrichissement éthique.
- **Première version (MVP 6 mois)** : Focus sur **leads fournis par l’artisan** (CSV, import Google Sheets, formulaire web simple) + enrichissement IA + séquences sur contacts déjà chauds ou avec consentement. Pas de cold scraping massif.

## Objectifs Métier & KPIs Succès

**KPIs Primaires (mesurés dans le Cockpit)**
- Taux de réponse global par canal et par template
- Taux de conversion lead → RDV / devis / chantier
- Temps gagné par l’artisan par semaine
- Coût par lead qualifié (si tracking budget)
- Nombre de leads dans le pipeline / taux de pipeline couvert

**KPIs Secondaires**
- Taux d’ouverture email / SMS
- Temps moyen de réponse de l’artisan aux leads chauds
- Score de qualité des leads (auto-évalué par artisan)
- Taux de désinscription / plainte
- Coût LLM par lead traité

**Objectif à 12 mois** : 200+ artisans actifs, churn < 5%/mois, NPS > 50, amélioration moyenne de +40% du CA généré par prospection.

## Périmètre Fonctionnel (MVP → v2)

**MVP (3-4 mois)**
- Import leads (CSV + mapping IA)
- Enrichissement basique (secteur, taille estimée, localisation)
- Scoring IA + règles métier (proximité, urgence potentielle, similarité avec chantiers passés)
- Constructeur de séquences visuel (3-5 étapes, templates personnalisables avec variables {{prenom}}, {{ville}})
- Exécution séquences (email via Brevo/Resend + SMS via Twilio)
- Suivi réponses (webhook + inbox unifiée dans le cockpit)
- Dashboard simple (kanban leads + analytics basiques)
- Gestion consentements & désinscriptions

**v1.5**
- Intégration WhatsApp Business API (si pertinent)
- Scoring avancé avec embeddings + RAG sur historique de l’artisan
- A/B testing automatique des templates
- Recommandations IA pour prochaines séquences

**v2+**
- Lead acquisition semi-automatisée (intégration Pages Jaunes API si disponible, Google Business, réseau de partenaires)
- Voice AI pour qualification téléphonique (outbound calls ou callback)
- Prédiction de closing probability + pricing dynamique
- Marketplace de templates "validés par la communauté artisans"

## Contraintes Techniques & Non-Fonctionnelles

- **Budget LLM** : L’artisan paie un abonnement fixe. Coût LLM doit rester < 15% de la marge.
- **Simplicité** : L’UI doit être utilisable en < 10 min de formation. Pas de jargon tech.
- **Fiabilité** : Les séquences doivent tourner même si l’artisan ferme l’onglet (background jobs robustes).
- **Sécurité des données** : Données clients/artisans très sensibles. Chiffrement, audit, localisation France/EU préférée.

## Hypothèses & Inconnues Majeures

- Les artisans accepteront-ils de payer pour un outil d’automatisation de prospection ? (validation via landing page ou interviews prévues)
- Quelle est la source de leads la plus efficace et légale pour ce segment ? (hypothèse : import + enrichissement > scraping pur)
- DeepSeek V4 Pro sera-t-il suffisant pour la génération de messages de qualité "humaine" en français BTP ? (tests prévus L2)

---

**Ce fichier est mis à jour en boucle L3/L4 ou quand le contexte métier évolue significativement.**
