"""
Script de création de la structure du projet FCC Fake News Detector
Exécutez ce script et tous les dossiers seront créés dans le MÊME dossier que le script
"""

import os

def create_project_structure():
    """
    Crée la structure complète du projet FCC Fake News Detector
    dans le dossier COURANT (même dossier que le script)
    """
    
    print("=" * 70)
    print("🏗️  CRÉATION DE LA STRUCTURE DU PROJET")
    print("=" * 70)
    print("\n📂 Projet: FCC Fake News Detector API")
    print("🎯 Mission: Détecter les fake news pour la FCC\n")
    
    # Obtenir le dossier courant (où se trouve le script)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"📍 Emplacement: {base_dir}")
    print(f"📁 Les dossiers seront créés ici !\n")
    
    # Structure des dossiers (dans le dossier courant)
    folders = [
        "models",                    # Modèles ML
        "api",                       # Code API Flask
        "tests",                     # Tests
        "frontend",                  # Interface web
        "notebooks",                 # Notebooks Jupyter
        "docs",                      # Documentation
    ]
    
    print("📁 Création des dossiers...")
    print("-" * 70)
    
    # Créer les dossiers
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✓ Créé: {folder}/")
        else:
            print(f"ℹ️  Existe déjà: {folder}/")
    
    print("\n" + "-" * 70)
    print("✅ Structure des dossiers créée avec succès !")
    
    # Créer les fichiers de base
    print("\n📄 Création des fichiers de base...")
    print("-" * 70)
    
    files_to_create = {
        "README.md": create_readme_content(),
        ".gitignore": create_gitignore_content(),
        "requirements.txt": create_requirements_content(),
        os.path.join("api", "app.py"): "# API Flask - À créer à l'étape suivante\n",
        os.path.join("api", "config.py"): create_config_content(),
        os.path.join("api", "requirements.txt"): create_requirements_content(),
        os.path.join("tests", "test_api.py"): "# Tests API - À créer plus tard\n",
        os.path.join("tests", "test_manual.sh"): create_test_script_content(),
        os.path.join("docs", "API_DOCUMENTATION.md"): create_api_doc_content(),
        os.path.join("docs", "USAGE_GUIDE.md"): create_usage_guide_content(),
        os.path.join("frontend", ".gitkeep"): "# Fichier pour garder le dossier dans Git\n",
        os.path.join("notebooks", ".gitkeep"): "# Placez votre notebook ici\n",
        os.path.join("models", "README.md"): create_models_readme(),
    }
    
    for file_path, content in files_to_create.items():
        full_path = os.path.join(base_dir, file_path)
        
        # Créer le fichier s'il n'existe pas
        if not os.path.exists(full_path):
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Créé: {file_path}")
        else:
            print(f"ℹ️  Existe déjà: {file_path}")
    
    print("\n" + "-" * 70)
    print("✅ Fichiers de base créés avec succès !")
    
    # Instructions finales
    print("\n" + "=" * 70)
    print("🎉 STRUCTURE DU PROJET CRÉÉE AVEC SUCCÈS !")
    print("=" * 70)
    
    print(f"\n📂 Emplacement du projet: {base_dir}")
    
    print("\n🚀 PROCHAINES ÉTAPES:")
    print("  1. Copiez vos modèles (.pkl) dans models/")
    print("  2. Copiez votre notebook dans notebooks/")
    print("  3. On va créer l'API dans api/app.py")
    print("  4. On va créer l'interface dans frontend/")
    
    print("\n💡 STRUCTURE CRÉÉE:")
    print(f"""
{base_dir}/
├── models/              ← Vos modèles .pkl ici
│   └── README.md
├── api/                 ← Code de l'API Flask
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
├── tests/               ← Scripts de test
│   ├── test_api.py
│   └── test_manual.sh
├── frontend/            ← Interface web
├── notebooks/           ← Votre notebook ici
├── docs/                ← Documentation
│   ├── API_DOCUMENTATION.md
│   └── USAGE_GUIDE.md
├── README.md            ← Page d'accueil GitHub
├── .gitignore
└── requirements.txt
    """)
    
    print("=" * 70)
    print(f"\n✅ Tout est prêt ! Continuez à travailler dans ce dossier.")
    print("=" * 70)


def create_models_readme():
    """README pour le dossier models"""
    return """# 📦 Dossier Models

## Contenu

Ce dossier contient les modèles ML sauvegardés.

### Fichiers requis :

1. **fake_news_model.pkl**
   - Modèle Logistic Regression entraîné
   - Taille: ~0.5 MB
   - Format: pickle

2. **tfidf_vectorizer.pkl**
   - Vectorizer TF-IDF
   - Taille: ~2.3 MB
   - Format: pickle

## Comment placer les modèles ici

Copiez les fichiers .pkl générés par votre notebook :

```bash
# Depuis votre notebook, après avoir exécuté la cellule de sauvegarde
# Les fichiers seront dans projet_NLP_V1/models/

# Copiez-les ici
```

## Vérification

Pour vérifier que les modèles sont bien présents :

```python
import os

models_dir = os.path.dirname(__file__)
model_path = os.path.join(models_dir, 'fake_news_model.pkl')
vectorizer_path = os.path.join(models_dir, 'tfidf_vectorizer.pkl')

print("Modèle présent:", os.path.exists(model_path))
print("Vectorizer présent:", os.path.exists(vectorizer_path))
```

## ⚠️ Important

- Ne versionnez PAS ces fichiers sur GitHub si ils sont trop gros (>100MB)
- Ajoutez `*.pkl` dans `.gitignore` si nécessaire
- Pour le projet, incluez les modèles car ils sont petits (~3MB total)
"""


def create_readme_content():
    """Contenu du README.md principal"""
    return """# 🎓 FCC Fake News Detector

> Projet de détection de fake news pour la Federal Communications Commission (FCC)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Academic-yellow)](LICENSE)

## 📋 Description

Ce projet utilise le Machine Learning pour détecter automatiquement les fake news dans les articles de presse. Le modèle est basé sur **Logistic Regression** avec vectorisation **TF-IDF** et atteint une précision de **98.34%**.

### 🎯 Objectifs

- ✅ Distinguer les articles authentiques des fake news
- ✅ Fournir une API REST pour l'intégration dans d'autres systèmes
- ✅ Aider la régulation du contenu médiatique pour la FCC

## 🚀 Quick Start

### Installation

```bash
# 1. Cloner le repository (ou télécharger)
git clone https://github.com/votre-username/fcc-fake-news-detector.git
cd fcc-fake-news-detector

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Vérifier que les modèles sont dans models/
ls models/

# 4. Lancer l'API
cd api
python app.py
```

### Utilisation Rapide

```bash
# Tester l'API avec curl
curl -X POST http://localhost:5000/predict \\
  -H "Content-Type: application/json" \\
  -d '{"text":"Breaking: Major scientific breakthrough announced"}'
```

## 📊 Performances du Modèle

| Métrique | Score | Description |
|----------|-------|-------------|
| **Accuracy** | 98.34% | Taux de prédictions correctes |
| **Precision** | 98.34% | Fiabilité des prédictions positives |
| **Recall** | 98.34% | Taux de détection des vrais positifs |
| **F1-Score** | 98.34% | Moyenne harmonique précision/recall |

### 📈 Résultats

- ✅ Sur 7,728 articles de test
- ✅ 7,600+ articles correctement classifiés
- ✅ Modèle équilibré sur les deux classes

## 🛠️ Technologies Utilisées

### Backend
- **Python 3.8+** - Langage principal
- **Flask** - Framework web pour l'API REST
- **Flask-CORS** - Gestion des requêtes cross-origin

### Machine Learning
- **scikit-learn** - Bibliothèque ML
- **TF-IDF Vectorizer** - Feature extraction (max_features=5000, n-grams=(1,2))
- **Logistic Regression** - Modèle de classification (max_iter=1000)

### Data Processing
- **pandas** - Manipulation de données
- **numpy** - Calculs numériques

## 📁 Structure du Projet

```
fcc-fake-news-detector/
│
├── 📂 models/                    # Modèles ML sauvegardés
│   ├── fake_news_model.pkl      # Modèle Logistic Regression
│   ├── tfidf_vectorizer.pkl     # Vectorizer TF-IDF
│   └── README.md
│
├── 📂 api/                       # Code API Flask
│   ├── app.py                   # Application Flask principale
│   ├── config.py                # Configuration
│   └── requirements.txt         # Dépendances API
│
├── 📂 tests/                     # Tests automatisés
│   ├── test_api.py              # Tests Python
│   └── test_manual.sh           # Tests manuels (bash)
│
├── 📂 frontend/                  # Interface web (optionnel)
│   └── index.html               # Page de test
│
├── 📂 notebooks/                 # Notebooks Jupyter
│   └── models.ipynb             # Notebook d'entraînement
│
├── 📂 docs/                      # Documentation
│   ├── API_DOCUMENTATION.md     # Documentation API
│   └── USAGE_GUIDE.md          # Guide d'utilisation
│
├── 📄 README.md                  # Ce fichier
├── 📄 .gitignore                # Fichiers ignorés par Git
└── 📄 requirements.txt          # Dépendances globales
```

## 📚 Documentation Complète

- 📖 [Documentation de l'API](docs/API_DOCUMENTATION.md)
- 📖 [Guide d'utilisation détaillé](docs/USAGE_GUIDE.md)
- 📖 [README Models](models/README.md)

## 🔌 API Endpoints

### 1. Health Check
```bash
GET /health
```

### 2. Predict News Authenticity
```bash
POST /predict
Content-Type: application/json

{
  "text": "Your article text here..."
}
```

**Response:**
```json
{
  "prediction": "Fake News",
  "confidence": 98.5,
  "probabilities": {
    "fake": 98.5,
    "reliable": 1.5
  }
}
```

## 💻 Exemples de Code

### Python

```python
import requests

url = "http://localhost:5000/predict"
data = {"text": "Breaking news: Major event happened today"}

response = requests.post(url, json=data)
result = response.json()

print(f"Prédiction: {result['prediction']}")
print(f"Confiance: {result['confidence']}%")
```

### JavaScript

```javascript
async function detectFakeNews(text) {
    const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });
    
    const result = await response.json();
    return result;
}
```

## 🧪 Tests

```bash
# Lancer les tests Python
python tests/test_api.py

# Lancer les tests manuels
bash tests/test_manual.sh
```

## 🚀 Déploiement

### Local
```bash
python api/app.py
```

### Production (exemple avec Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api.app:app
```

## 🤝 Contribution

Ce projet est développé dans le cadre d'un projet académique pour la FCC.

### Auteur
**Votre Nom** - Étudiant en Data Science

### Encadrement
**FCC (Federal Communications Commission)** - Projet de détection de fake news

## 📄 Licence

Projet académique - Tous droits réservés

## 🙏 Remerciements

- FCC pour le contexte du projet
- scikit-learn pour les outils ML
- Flask pour le framework web

---

⭐ **Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile sur GitHub !**

📧 **Contact:** votre.email@example.com
🔗 **LinkedIn:** [Votre Profil](https://linkedin.com/in/votre-profil)
"""


def create_gitignore_content():
    """Contenu du .gitignore"""
    return """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Environment
.env
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Models (décommentez si vous ne voulez pas versionner les modèles)
# models/*.pkl
"""


def create_requirements_content():
    """Contenu du requirements.txt"""
    return """flask==3.0.0
flask-cors==4.0.0
scikit-learn==1.3.2
numpy==1.24.3
pandas==2.0.3
requests==2.31.0
"""


def create_config_content():
    """Contenu du config.py"""
    return """\"\"\"
Configuration de l'API Flask
\"\"\"

import os

class Config:
    \"\"\"Configuration de base\"\"\"
    
    # Obtenir le chemin de base (dossier api/)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Dossier des modèles (un niveau au-dessus)
    MODEL_DIR = os.path.join(BASE_DIR, '..', 'models')
    
    # Chemins des modèles
    MODEL_PATH = os.path.join(MODEL_DIR, 'fake_news_model.pkl')
    VECTORIZER_PATH = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')
    
    # Configuration Flask
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000
    
    # Labels
    LABELS = {
        0: 'Fake News',
        1: 'Reliable News'
    }
"""


def create_test_script_content():
    """Contenu du test_manual.sh"""
    return """#!/bin/bash

# Script de test manuel de l'API
# Usage: bash test_manual.sh

echo "=========================================="
echo "Testing FCC Fake News Detector API"
echo "=========================================="

API_URL="http://localhost:5000"

# Test 1: Health check
echo -e "\\n1. Testing health endpoint..."
curl -s ${API_URL}/health | python -m json.tool

# Test 2: Fake news detection
echo -e "\\n2. Testing prediction - Fake News..."
curl -s -X POST ${API_URL}/predict \\
  -H "Content-Type: application/json" \\
  -d '{"text":"SHOCKING: Aliens landed in New York City yesterday!!!"}' \\
  | python -m json.tool

# Test 3: Reliable news detection
echo -e "\\n3. Testing prediction - Reliable News..."
curl -s -X POST ${API_URL}/predict \\
  -H "Content-Type: application/json" \\
  -d '{"text":"President announces new economic policy at White House press conference"}' \\
  | python -m json.tool

echo -e "\\n=========================================="
echo "Tests completed!"
echo "=========================================="
"""


def create_api_doc_content():
    """Contenu de la documentation API"""
    return """# 📚 API Documentation - FCC Fake News Detector

## Base URL

```
http://localhost:5000
```

## Endpoints

### 1. Health Check

Vérifie que l'API fonctionne correctement.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "ok",
  "model_loaded": true
}
```

---

### 2. Predict News Authenticity

Analyse un article et détermine s'il s'agit d'une fake news.

**Endpoint:** `POST /predict`

**Request Body:**
```json
{
  "text": "Article text to analyze..."
}
```

**Response:**
```json
{
  "prediction": "Fake News",
  "confidence": 98.5,
  "probabilities": {
    "fake": 98.5,
    "reliable": 1.5
  },
  "text_length": 150
}
```

**Status Codes:**
- `200 OK` - Prédiction réussie
- `400 Bad Request` - Texte manquant ou invalide
- `500 Internal Server Error` - Erreur du serveur

---

## Exemples d'utilisation

### Python

```python
import requests

url = "http://localhost:5000/predict"
data = {
    "text": "Breaking news: Major event happened today"
}

response = requests.post(url, json=data)
result = response.json()

print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']}%")
```

### JavaScript

```javascript
async function detectFakeNews(text) {
    const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    });
    
    const result = await response.json();
    console.log(result);
}
```

### cURL

```bash
curl -X POST http://localhost:5000/predict \\
  -H "Content-Type: application/json" \\
  -d '{"text":"Your article text here"}'
```
"""


def create_usage_guide_content():
    """Contenu du guide d'utilisation"""
    return """# 📖 Guide d'Utilisation - FCC Fake News Detector

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Télécharger/Cloner le projet**

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Vérifier les modèles**

Assurez-vous que les fichiers suivants existent dans `models/`:
- `fake_news_model.pkl`
- `tfidf_vectorizer.pkl`

---

## Utilisation

### 1. Lancer l'API

```bash
cd api
python app.py
```

Vous devriez voir:
```
✓ Modèle chargé avec succès
* Running on http://0.0.0.0:5000
```

### 2. Tester l'API

**Option A: Via Python**

```python
import requests

response = requests.post('http://localhost:5000/predict', 
    json={'text': 'Your article here'})
print(response.json())
```

**Option B: Via cURL**

```bash
curl -X POST http://localhost:5000/predict \\
  -H "Content-Type: application/json" \\
  -d '{"text":"Article text"}'
```

---

## Interprétation des Résultats

### Prédiction

- **"Fake News"** (0) - L'article est probablement faux
- **"Reliable News"** (1) - L'article est probablement authentique

### Confidence

Score de confiance entre 0 et 100%:
- **90-100%** - Très confiant
- **70-90%** - Confiant
- **50-70%** - Peu confiant
- **<50%** - Très incertain

---

## Troubleshooting

### Problème: "Modèle non trouvé"

**Solution:** Vérifiez que les fichiers .pkl sont dans `models/`

### Problème: "Port 5000 already in use"

**Solution:** Changez le port dans `api/config.py`

### Problème: CORS errors

**Solution:** CORS est déjà configuré. Vérifiez que l'API tourne.
"""


if __name__ == "__main__":
    create_project_structure()


import flask, sklearn, numpy, pandas; print('✅ Tout fonctionne dans VS Code !')