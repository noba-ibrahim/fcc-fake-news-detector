# 📖 Guide d'Utilisation - FCC Fake News Detector

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
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
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
