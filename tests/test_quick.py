"""
Test rapide de l'API FCC Fake News Detector
"""

import requests
import json

# URL de l'API
API_URL = "http://localhost:5000/predict"

# Articles de test
test_articles = [
    {
        "text": "SHOCKING: Aliens landed in New York City yesterday!!!",
        "expected": "Fake"
    },
    {
        "text": "President announces new economic policy at White House press conference",
        "expected": "Reliable"
    },
    {
        "text": "UNBELIEVABLE: Doctors don't want you to know this miracle cure!!!",
        "expected": "Fake"
    },
    {
        "text": "Scientists at Harvard Medical School publish peer-reviewed study on cancer research",
        "expected": "Reliable"
    }
]

print("=" * 70)
print("🧪 TEST DE L'API FCC FAKE NEWS DETECTOR")
print("=" * 70)

for i, article in enumerate(test_articles, 1):
    print(f"\n{'='*70}")
    print(f"Test {i}/4")
    print(f"{'='*70}")
    
    # Envoyer la requête
    response = requests.post(API_URL, json={"text": article["text"]})
    
    # Vérifier le statut
    if response.status_code == 200:
        result = response.json()
        
        # Afficher les résultats
        print(f"📰 Article: {article['text'][:60]}...")
        print(f"✅ Attendu: {article['expected']}")
        print(f"🎯 Prédit: {result['prediction']}")
        print(f"💯 Confiance: {result['confidence']}%")
        print(f"📊 Probabilités:")
        print(f"   - Fake News: {result['probabilities']['fake']}%")
        print(f"   - Reliable: {result['probabilities']['reliable']}%")
        
        # Vérifier si correct
        is_correct = (article['expected'] == "Fake" and "Fake" in result['prediction']) or \
                     (article['expected'] == "Reliable" and "Reliable" in result['prediction'])
        
        if is_correct:
            print("✅ CORRECT !")
        else:
            print("❌ INCORRECT")
    else:
        print(f"❌ Erreur HTTP {response.status_code}")
        print(response.text)

print(f"\n{'='*70}")
print("✅ TESTS TERMINÉS")
print(f"{'='*70}")# Tests API - À créer plus tard
