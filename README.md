# 🎓 FCC Fake News Detector

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
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
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
