"""
API Flask pour la détection de Fake News
Projet FCC - Federal Communications Commission
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
import sys

# Configuration
app = Flask(__name__)
CORS(app)  # Active CORS pour permettre les requêtes depuis le frontend

# Variables globales pour stocker le modèle et le vectorizer
model = None
vectorizer = None

def load_models():
    """
    Charge le modèle et le vectorizer depuis les fichiers .pkl
    Cette fonction est appelée UNE SEULE FOIS au démarrage de l'API
    """
    global model, vectorizer
    
    print("=" * 60)
    print("🚀 CHARGEMENT DES MODÈLES")
    print("=" * 60)
    
    # Obtenir le chemin absolu du dossier 'models'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(base_dir, '..', 'models')
    
    # Chemins complets des fichiers
    model_path = os.path.join(models_dir, 'fake_news_model.pkl')
    vectorizer_path = os.path.join(models_dir, 'tfidf_vectorizer.pkl')
    
    print(f"\n📂 Dossier models: {os.path.abspath(models_dir)}")
    print(f"📄 Chemin modèle: {model_path}")
    print(f"📄 Chemin vectorizer: {vectorizer_path}")
    
    # Vérifier que les fichiers existent
    if not os.path.exists(model_path):
        print(f"\n❌ ERREUR: Modèle non trouvé à {model_path}")
        print("💡 Assurez-vous d'avoir copié fake_news_model.pkl dans models/")
        sys.exit(1)
    
    if not os.path.exists(vectorizer_path):
        print(f"\n❌ ERREUR: Vectorizer non trouvé à {vectorizer_path}")
        print("💡 Assurez-vous d'avoir copié tfidf_vectorizer.pkl dans models/")
        sys.exit(1)
    
    try:
        # Charger le modèle
        print("\n⏳ Chargement du modèle...")
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print("✅ Modèle chargé avec succès!")
        
        # Charger le vectorizer
        print("⏳ Chargement du vectorizer...")
        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        print("✅ Vectorizer chargé avec succès!")
        
        # Afficher les informations
        print("\n" + "=" * 60)
        print("📊 INFORMATIONS SUR LES MODÈLES")
        print("=" * 60)
        print(f"🤖 Modèle: {type(model).__name__}")
        print(f"📝 Vectorizer: {type(vectorizer).__name__}")
        print(f"📈 Nombre de features: {vectorizer.max_features}")
        print("=" * 60)
        
        print("\n✅ MODÈLES CHARGÉS AVEC SUCCÈS!")
        print("🚀 L'API est prête à recevoir des requêtes!\n")
        
    except Exception as e:
        print(f"\n❌ ERREUR lors du chargement des modèles:")
        print(f"   {str(e)}")
        sys.exit(1)


# ============================================================
# ENDPOINTS DE L'API
# ============================================================

@app.route('/health', methods=['GET'])
def health():
    """
    Endpoint de santé - Vérifie que l'API fonctionne
    """
    return jsonify({
        'status': 'ok',
        'model_loaded': model is not None and vectorizer is not None,
        'message': 'FCC Fake News Detector API is running'
    })


@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint de prédiction - Détecte si un article est fake ou reliable
    """
    
    # Vérifier que le modèle est chargé
    if model is None or vectorizer is None:
        return jsonify({
            'error': 'Modèle non chargé. Redémarrez le serveur.'
        }), 500
    
    # Vérifier que la requête contient du JSON
    if not request.is_json:
        return jsonify({
            'error': 'Content-Type doit être application/json'
        }), 400
    
    # Extraire les données
    data = request.get_json()
    
    # Vérifier que le champ 'text' existe
    if 'text' not in data:
        return jsonify({
            'error': 'Le champ "text" est requis',
            'example': {'text': 'Your article text here'}
        }), 400
    
    text = data.get('text', '').strip()
    
    # Vérifier que le texte n'est pas vide
    if not text:
        return jsonify({
            'error': 'Le texte ne peut pas être vide'
        }), 400
    
    # Faire la prédiction
    try:
        # Vectoriser le texte avec TF-IDF
        text_vectorized = vectorizer.transform([text])
        
        # Faire la prédiction
        prediction = model.predict(text_vectorized)[0]
        
        # Obtenir les probabilités
        probabilities = model.predict_proba(text_vectorized)[0]
        
        # Déterminer le label
        prediction_label = "Reliable News" if prediction == 1 else "Fake News"
        
        # Calculer la confiance
        confidence = float(max(probabilities) * 100)
        
        # Créer la réponse
        result = {
            'prediction': prediction_label,
            'prediction_code': int(prediction),
            'confidence': round(confidence, 2),
            'probabilities': {
                'fake': round(float(probabilities[0] * 100), 2),
                'reliable': round(float(probabilities[1] * 100), 2)
            },
            'text_length': len(text),
            'text_preview': text[:100] + '...' if len(text) > 100 else text
        }
        
        # Log dans la console
        print(f"\n📰 Prédiction effectuée:")
        print(f"   Texte: {text[:50]}...")
        print(f"   Résultat: {prediction_label} ({confidence:.2f}%)")
        
        return jsonify(result), 200
    
    except Exception as e:
        print(f"\n❌ Erreur lors de la prédiction:")
        print(f"   {str(e)}")
        
        return jsonify({
            'error': 'Erreur lors de la prédiction',
            'details': str(e)
        }), 500


@app.route('/', methods=['GET'])
def home():
    """
    Page d'accueil de l'API - Documentation rapide
    """
    return jsonify({
        'name': 'FCC Fake News Detector API',
        'version': '1.0.0',
        'description': 'API de détection de fake news pour la FCC',
        'endpoints': {
            'health': {
                'method': 'GET',
                'url': '/health',
                'description': 'Vérifier l\'état de l\'API'
            },
            'predict': {
                'method': 'POST',
                'url': '/predict',
                'description': 'Détecter si un article est fake',
                'body': {
                    'text': 'Article text to analyze'
                }
            }
        },
        'example': {
            'url': 'http://localhost:5000/predict',
            'method': 'POST',
            'body': {
                'text': 'Breaking news: Major event happened today'
            }
        }
    })


# ============================================================
# DÉMARRAGE DU SERVEUR
# ============================================================

if __name__ == '__main__':
    # Charger les modèles au démarrage
    load_models()
    
    # Lancer le serveur Flask
    print("=" * 60)
    print("🌐 DÉMARRAGE DU SERVEUR FLASK")
    print("=" * 60)
    print(f"📍 Host: 0.0.0.0")
    print(f"🔌 Port: 5000")
    print(f"🔗 URL: http://localhost:5000")
    print(f"⚙️  Mode Debug: Activé")
    print("=" * 60)
    print("\n📚 Endpoints disponibles:")
    print("   GET  /         - Documentation")
    print("   GET  /health   - État de l'API")
    print("   POST /predict  - Prédiction fake news")
    print("\n💡 Pour arrêter le serveur: Ctrl+C\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)