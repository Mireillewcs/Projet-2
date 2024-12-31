import streamlit as st
import pandas as pd


# Titre principal de l'application
st.title("affiche")

movie_data = pd.read_csv("data\movie_clean_v16_12_24.csv")
st.dataframe(movie_data)