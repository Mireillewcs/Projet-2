import pandas as pd

# Chemins des fichiers
movie_clean_path = "data/movie_clean_v16_12_24.csv"
filmnoel_path = "data/filmnoelrecommendation.csv"

try:
    # Charger les fichiers
    movie_data = pd.read_csv(movie_clean_path)
    christmas_movies = pd.read_csv(filmnoel_path)
    
    # Afficher la structure des fichiers
    print("=== Movie Data ===")
    print("Colonnes :", movie_data.columns.tolist())
    print("Dimensions :", movie_data.shape)
    print(movie_data.head(), "\n")
    
    print("=== Christmas Movies ===")
    print("Colonnes :", christmas_movies.columns.tolist())
    print("Dimensions :", christmas_movies.shape)
    print(christmas_movies.head())
except Exception as e:
    print(f"Erreur lors du chargement des fichiers : {e}")
