import streamlit as st
import pandas as pd
import numpy as np

# Injecter du CSS personnalisé pour gérer l'alignement et l'esthétique des sous-titres et des contenus
st.markdown(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-bottom: 30px;
        padding: 10px;
        border-radius: 8px;
        background-color: #f9f9f9;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .container img {
        max-width: 200px;
        margin-bottom: 15px;
    }
    .title-section {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
        color: #333333;
    }
    .section-left, .section-right {
        margin: 0 20px;
    }
    .subtitle {
        font-size: 18px;
        font-weight: bold;
        margin: 10px 0;
        color: #555555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Charger les données des films
try:
    movie_data = pd.read_csv("data/movie_clean_v16_12_24.csv")
    christmas_movies = pd.read_csv("data/filmnoelrecommendation.csv")
except FileNotFoundError as e:
    st.error(f"Erreur : {e}")
    movie_data, christmas_movies = None, None

# Titre principal de l'application
st.title("RECOMMANDATIONS")

# Disposition en colonnes pour Top 5 des films
col_left, col_right = st.columns([1, 1])

# Section des films de Noël
with col_left:
    if christmas_movies is not None:
        st.markdown('<div class="title-section section-left">Suggestions films de Noël 🎄</div>', unsafe_allow_html=True)
        top_christmas_movies = christmas_movies.head(5)
        for _, row in top_christmas_movies.iterrows():
            st.markdown(
                f"""
                <div class="container">
                    <img src="{row['poster_path']}" alt="Poster du film">
                    <div class="subtitle"><strong>Titre :</strong> {row['original_title']}</div>
                    <div><em>Synopsis :</em> {row['overview']}</div>
                    <a href="https://www.imdb.com/title/{row['imdb_id']}" target="_blank">Voir la bande-annonce</a>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Section des films les plus recommandés
with col_right:
    if movie_data is not None:
        st.markdown('<div class="title-section section-right">Top 5 des films les plus populaires 🎥</div>', unsafe_allow_html=True)
        top_movies = movie_data.sort_values(by="popularity", ascending=False).head(5)
        for _, row in top_movies.iterrows():
            st.markdown(
                f"""
                <div class="container">
                    <img src="{row['poster_path']}" alt="Poster du film">
                    <div class="subtitle"><strong>Titre :</strong> {row['original_title']}</div>
                    <div><em>Synopsis :</em> {row['overview']}</div>
                    <a href="https://www.imdb.com/title/{row['imdb_id']}" target="_blank">Voir la bande-annonce</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
