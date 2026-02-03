# 📚 API Documentation - FCC Fake News Detector

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
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Your article text here"}'
```
