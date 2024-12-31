import streamlit as st
import pandas as pd
import numpy as np

# Injecter du CSS personnalisé pour aligner les titres et élargir la barre de recherche
st.markdown(
    """
    <style>
    .title-left {
        text-align: left;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .title-right {
        text-align: right;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .search-bar {
        width: 95%;
        margin: auto;
        padding: 10px;
        font-size: 16px;
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

# Barre de recherche pour entrer le nom d'un film
film_name = st.text_input("Entrez le nom d'un film :", placeholder="Exemple : Titanic", key="film_name")

# Disposition en colonnes pour Top 5 des films
col_left, col_right = st.columns([1, 1])

# Section des films de Noël
with col_left:
    if christmas_movies is not None:
        st.markdown('<div class="title-left">Top 5 des films de Noël 🎄</div>', unsafe_allow_html=True)
        top_christmas_movies = christmas_movies.head(5)
        for _, row in top_christmas_movies.iterrows():
            st.image(row["poster_path"], width=200)
            st.markdown(f"**Titre :** {row['original_title']}")
            st.markdown(f"**Synopsis :** {row['overview']}")
            st.markdown(f"[Voir la bande-annonce](https://www.imdb.com/title/{row['imdb_id']})", unsafe_allow_html=True)

# Section des films les plus recommandés
with col_right:
    if movie_data is not None:
        st.markdown('<div class="title-right">Top 5 des films les plus recommandés 🎥</div>', unsafe_allow_html=True)
        top_movies = movie_data.sort_values(by="popularity", ascending=False).head(5)
        for _, row in top_movies.iterrows():
            st.image(row["poster_path"], width=200)
            st.markdown(f"**Titre :** {row['original_title']}")
            st.markdown(f"**Synopsis :** {row['overview']}")
            st.markdown(f"[Voir la bande-annonce](https://www.imdb.com/title/{row['imdb_id']})", unsafe_allow_html=True)

# Vérification si le film recherché est dans les Top 5
if film_name:
    is_in_christmas = (
        christmas_movies["original_title"]
        .str.contains(film_name, case=False, na=False)
        .any()
        if christmas_movies is not None
        else False
    )
    is_in_top_movies = (
        movie_data["original_title"]
        .str.contains(film_name, case=False, na=False)
        .any()
        if movie_data is not None
        else False
    )

    # Rediriger si le film n'est pas dans les Top 5
    if not is_in_christmas and not is_in_top_movies:
        st.experimental_set_query_params(page="similar_movies", film=film_name)
        st.experimental_rerun()
