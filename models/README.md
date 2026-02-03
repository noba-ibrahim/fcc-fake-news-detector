# 📦 Dossier Models

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
