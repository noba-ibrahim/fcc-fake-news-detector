/* ============================================================
   CONFIGURATION
   ============================================================ */

const API_URL = 'http://localhost:5000/predict';

// Exemples prédéfinis
const examples = [
    {
        text: "Scientists at Harvard Medical School have published a groundbreaking peer-reviewed study on cancer treatment. The research team, led by Dr. Johnson, conducted extensive clinical trials over five years with promising results. The findings were published in the Journal of Medical Research and have been validated by independent experts in the field.",
        label: "Article fiable"
    },
    {
        text: "SHOCKING!!! You won't believe what happened next! Doctors HATE this one simple trick! Click here NOW to discover the secret they don't want you to know! This will change your life FOREVER!!!",
        label: "Fake news"
    },
    {
        text: "BREAKING: UNBELIEVABLE discovery that Big Pharma doesn't want you to know! This miracle cure will SHOCK you! Scientists are STUNNED by these results! SHARE before it gets DELETED!!!",
        label: "Clickbait suspect"
    }
];

/* ============================================================
   FONCTIONS PRINCIPALES
   ============================================================ */

/**
 * Utiliser un exemple prédéfini
 */
function useExample(index) {
    const example = examples[index];
    document.getElementById('articleText').value = example.text;
    
    // Notification
    showNotification(`Exemple chargé : ${example.label}`, 'info');
}

/**
 * Effacer le texte
 */
function clearText() {
    document.getElementById('articleText').value = '';
    document.getElementById('results').style.display = 'none';
}

/**
 * Analyser un autre article
 */
function analyzeAnother() {
    clearText();
    document.getElementById('articleText').focus();
}

/**
 * Fonction principale d'analyse
 */
async function analyzeArticle() {
    const text = document.getElementById('articleText').value.trim();
    
    // Validation
    if (!text) {
        showNotification('⚠️ Veuillez entrer un texte à analyser', 'warning');
        return;
    }
    
    if (text.length < 20) {
        showNotification('⚠️ Le texte est trop court (minimum 20 caractères)', 'warning');
        return;
    }
    
    // Désactiver le bouton et afficher le loading
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    
    analyzeBtn.disabled = true;
    loading.style.display = 'block';
    results.style.display = 'none';
    
    try {
        // Appel à l'API
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });
        
        if (!response.ok) {
            throw new Error(`Erreur HTTP: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Afficher les résultats
        displayResults(data);
        
    } catch (error) {
        console.error('Erreur:', error);
        showNotification('❌ Erreur lors de l\'analyse. Vérifiez que l\'API est lancée.', 'error');
    } finally {
        // Réactiver le bouton et cacher le loading
        analyzeBtn.disabled = false;
        loading.style.display = 'none';
    }
}

/**
 * Afficher les résultats
 */
function displayResults(data) {
    const results = document.getElementById('results');
    
    // Déterminer si c'est fake ou reliable
    const isFake = data.prediction === 'Fake News';
    
    // Icône et couleur
    const icon = isFake ? '🔴' : '✅';
    const color = isFake ? 'var(--danger-color)' : 'var(--success-color)';
    
    // Mettre à jour l'icône
    document.getElementById('predictionIcon').textContent = icon;
    
    // Mettre à jour le label
    const predictionLabel = document.getElementById('predictionLabel');
    predictionLabel.textContent = data.prediction;
    predictionLabel.style.color = color;
    
    // Mettre à jour la confiance
    document.getElementById('confidenceText').textContent = 
        `Confiance : ${data.confidence}%`;
    
    // Mettre à jour les probabilités
    document.getElementById('fakeProba').textContent = 
        `${data.probabilities.fake}%`;
    document.getElementById('reliableProba').textContent = 
        `${data.probabilities.reliable}%`;
    
    // Animer les barres de progression
    setTimeout(() => {
        document.getElementById('fakeBar').style.width = 
            `${data.probabilities.fake}%`;
        document.getElementById('reliableBar').style.width = 
            `${data.probabilities.reliable}%`;
    }, 100);
    
    // Mettre à jour les détails
    document.getElementById('textLength').textContent = 
        `${data.text_length} caractères`;
    document.getElementById('textPreview').textContent = 
        data.text_preview;
    
    // Afficher les résultats avec animation
    results.style.display = 'block';
    results.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    
    // Notification de succès
    const message = isFake 
        ? '🔴 Fake News détecté !' 
        : '✅ Article fiable détecté !';
    showNotification(message, isFake ? 'warning' : 'success');
}

/**
 * Afficher une notification
 */
function showNotification(message, type = 'info') {
    // Créer la notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Styles inline pour la notification
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        border-radius: 8px;
        color: white;
        font-weight: 600;
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        max-width: 400px;
    `;
    
    // Couleurs selon le type
    const colors = {
        success: '#10b981',
        error: '#ef4444',
        warning: '#f59e0b',
        info: '#2563eb'
    };
    
    notification.style.background = colors[type] || colors.info;
    
    // Ajouter au body
    document.body.appendChild(notification);
    
    // Supprimer après 4 secondes
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 4000);
}

/* ============================================================
   EVENT LISTENERS
   ============================================================ */

// Permettre d'envoyer avec Ctrl+Enter
document.getElementById('articleText').addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.key === 'Enter') {
        analyzeArticle();
    }
});

// Vérifier que l'API est accessible au chargement
window.addEventListener('load', async function() {
    try {
        const response = await fetch('http://localhost:5000/health');
        if (response.ok) {
            console.log('✅ API connectée');
        }
    } catch (error) {
        showNotification('⚠️ API non accessible. Assurez-vous qu\'elle est lancée.', 'warning');
    }
});

/* ============================================================
   ANIMATIONS CSS (ajoutées dynamiquement)
   ============================================================ */

const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
```

**Sauvegardez (Ctrl+S)**

---

## 🎬 TESTER L'INTERFACE

### **Étape 1 : Assurez-vous que l'API tourne**

**Dans le terminal de l'API, vérifiez que vous voyez :**
```
* Running on http://127.0.0.1:5000