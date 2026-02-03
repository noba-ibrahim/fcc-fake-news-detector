"""
Configuration de l'API Flask
"""

import os

class Config:
    """Configuration de base"""
    
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
