"""
Application Streamlit - FCC Fake News Detector
Détection de fake news avec Machine Learning
"""

import streamlit as st
import pickle
import os
from pathlib import Path

# Configuration de la page
st.set_page_config(
    page_title="FCC Fake News Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Cache pour charger les modèles une seule fois
@st.cache_resource
def load_models():
    """Charge le modèle et le vectorizer"""
    try:
        # Chemins absolus des modèles basés sur l'emplacement du script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'models', 'fake_news_model.pkl')
        vectorizer_path = os.path.join(base_dir, 'models', 'tfidf_vectorizer.pkl')
        
        # Charger le modèle
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        # Charger le vectorizer
        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        
        return model, vectorizer
    except Exception as e:
        st.error(f"Erreur lors du chargement des modèles: {e}")
        return None, None

# Charger les modèles
model, vectorizer = load_models()

# Header
st.title("🛡️ FCC Fake News Detector")
st.markdown("### Détection automatique de fake news avec Machine Learning")
st.markdown("---")

# Sidebar avec infos
with st.sidebar:
    st.header("📊 Informations")
    st.markdown("""
    **Modèle:** Logistic Regression  
    **Précision:** 98.34%  
    **Features:** TF-IDF (5000)  
    **Dataset:** 32,456 articles
    """)
    
    st.markdown("---")
    
    st.header("ℹ️ À propos")
    st.markdown("""
    Projet développé pour la **Federal Communications Commission (FCC)**.
    
    Le modèle analyse le contenu textuel pour distinguer les articles authentiques des fake news.
    """)
    
    st.markdown("---")
    
    st.header("📈 Performances")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Accuracy", "98.34%")
        st.metric("Precision", "98.34%")
    with col2:
        st.metric("Recall", "98.34%")
        st.metric("F1-Score", "98.34%")

# Main content
if model is not None and vectorizer is not None:
    st.success("✅ Modèles chargés avec succès !")
    
    # Tabs pour organiser le contenu
    tab1, tab2, tab3 = st.tabs(["📰 Analyse", "🧪 Exemples", "📚 Documentation"])
    
    with tab1:
        st.header("Analyser un article")
        st.markdown("Collez le texte de l'article ci-dessous pour détecter s'il s'agit d'une fake news.")
        
        # Zone de texte
        article_text = st.text_area(
            "Texte de l'article",
            height=200,
            placeholder="Exemple: Breaking news: Scientists at Harvard Medical School have published a groundbreaking study..."
        )
        
        # Boutons
        col1, col2 = st.columns([1, 5])
        with col1:
            analyze_button = st.button("🔍 Analyser", type="primary", use_container_width=True)
        with col2:
            clear_button = st.button("🗑️ Effacer", use_container_width=True)
        
        if clear_button:
            st.rerun()
        
        # Analyse
        if analyze_button:
            if not article_text.strip():
                st.warning("⚠️ Veuillez entrer un texte à analyser.")
            elif len(article_text.strip()) < 20:
                st.warning("⚠️ Le texte est trop court (minimum 20 caractères).")
            else:
                with st.spinner("Analyse en cours..."):
                    try:
                        # Vectorisation
                        text_vectorized = vectorizer.transform([article_text])
                        
                        # Prédiction
                        prediction = model.predict(text_vectorized)[0]
                        probabilities = model.predict_proba(text_vectorized)[0]
                        
                        # Résultats
                        st.markdown("---")
                        st.header("📊 Résultats de l'analyse")
                        
                        # Déterminer le type
                        is_fake = prediction == 0
                        label = "Fake News" if is_fake else "Reliable News"
                        confidence = max(probabilities) * 100
                        
                        # Affichage selon le résultat
                        if is_fake:
                            st.error(f"### 🔴 {label}")
                            st.error(f"**Confiance : {confidence:.2f}%**")
                        else:
                            st.success(f"### ✅ {label}")
                            st.success(f"**Confiance : {confidence:.2f}%**")
                        
                        # Métriques
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric(
                                "Probabilité Fake News",
                                f"{probabilities[0]*100:.2f}%"
                            )
                        with col2:
                            st.metric(
                                "Probabilité Reliable",
                                f"{probabilities[1]*100:.2f}%"
                            )
                        with col3:
                            st.metric(
                                "Longueur du texte",
                                f"{len(article_text)} caractères"
                            )
                        
                        # Barres de progression
                        st.markdown("#### Distribution des probabilités")
                        st.progress(probabilities[0], text=f"Fake News: {probabilities[0]*100:.1f}%")
                        st.progress(probabilities[1], text=f"Reliable News: {probabilities[1]*100:.1f}%")
                        
                        # Aperçu du texte
                        with st.expander("📄 Aperçu du texte analysé"):
                            preview = article_text[:200] + "..." if len(article_text) > 200 else article_text
                            st.text(preview)
                        
                    except Exception as e:
                        st.error(f"❌ Erreur lors de l'analyse: {e}")
    
    with tab2:
        st.header("🧪 Exemples prédéfinis")
        st.markdown("Testez rapidement avec ces exemples :")
        
        examples = {
            "Article fiable - Recherche scientifique": "Scientists at Harvard Medical School have published a groundbreaking peer-reviewed study on cancer treatment. The research team, led by Dr. Johnson, conducted extensive clinical trials over five years with promising results. The findings were published in the Journal of Medical Research and have been validated by independent experts in the field.",
            
            "Fake news - Clickbait": "SHOCKING!!! You won't believe what happened next! Doctors HATE this one simple trick! Click here NOW to discover the secret they don't want you to know! This will change your life FOREVER!!!",
            
            "Fake news - Conspirationniste": "BREAKING: UNBELIEVABLE discovery that Big Pharma doesn't want you to know! This miracle cure will SHOCK you! Scientists are STUNNED by these results! SHARE before it gets DELETED!!!",
            
            "Article fiable - Politique": "President announces new economic policy at White House press conference. The comprehensive plan, developed over six months of consultation with economic advisors, aims to address inflation concerns. Treasury Secretary provided detailed briefings to congressional leaders.",
        }
        
        for title, text in examples.items():
            with st.expander(f"📄 {title}"):
                st.text_area(
                    "Texte",
                    value=text,
                    height=100,
                    key=f"example_{title}",
                    disabled=True
                )
    
    with tab3:
        st.header("📚 Documentation")
        
        st.subheader("🤖 Comment ça fonctionne ?")
        
        st.markdown("""
        **1. Vectorisation TF-IDF**
        - Le texte est transformé en vecteur numérique
        - 5000 features extraites
        - N-grams: (1, 2)
        
        **2. Modèle Logistic Regression**
        - Classification binaire
        - Entraîné sur 24,728 articles
        - Testé sur 7,728 articles
        
        **3. Prédiction**
        - 0 = Fake News
        - 1 = Reliable News
        - Score de confiance basé sur les probabilités
        """)
        
        st.markdown("---")
        
        st.subheader("📊 Dataset")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total articles", "32,456")
        with col2:
            st.metric("Articles d'entraînement", "24,728")
        with col3:
            st.metric("Articles de test", "7,728")
        
        st.markdown("---")
        
        st.subheader("🎯 Performances du modèle")
        
        perf_col1, perf_col2 = st.columns(2)
        with perf_col1:
            st.metric("Accuracy", "98.34%", delta="Excellent")
            st.metric("Precision", "98.34%", delta="Excellent")
        with perf_col2:
            st.metric("Recall", "98.34%", delta="Excellent")
            st.metric("F1-Score", "98.34%", delta="Excellent")
        
        st.markdown("---")
        
        st.subheader("⚠️ Limitations")
        
        st.markdown("""
        - Le modèle est optimisé pour les articles en anglais
        - Les textes très courts peuvent donner des résultats moins fiables
        - Le modèle reflète les patterns des données d'entraînement
        """)
        
        st.markdown("---")
        
        st.subheader("👤 À propos du projet")
        
        st.markdown("""
        Projet développé dans le cadre d'une mission pour la **Federal Communications Commission (FCC)**.
        
        **Technologies utilisées:**
        - Python 3.11
        - scikit-learn
        - Streamlit
        - TF-IDF Vectorization
        - Logistic Regression
        """)

else:
    st.error("❌ Impossible de charger les modèles.")
    st.info("Vérifiez que les fichiers fake_news_model.pkl et tfidf_vectorizer.pkl sont présents dans le dossier 'models/'")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🛡️ FCC Fake News Detector | Powered by Machine Learning</p>
    <p>© 2024 - Projet Académique</p>
</div>
""", unsafe_allow_html=True)