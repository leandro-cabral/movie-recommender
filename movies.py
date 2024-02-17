import pandas as pd 
import random as rd

# Read the Data Frame 
df_movies = pd.read_csv('imdb_top_1000.csv')
df_animes = pd.read_csv('animes.csv')

# Save the Data Frames in a tuple and choose one of the Data Frames to be recommended
options = [df_movies, df_animes]
df_choice = rd.choice(options)

# Choose one item of the Data Frame based on the Data Frame choosed before 
if df_choice.equals(df_movies):
    movie_choice = rd.choice(df_movies['Series_Title'])
    print(f"Today's Recomendation is a serie/movie: {movie_choice}")

elif df_choice.equals(df_animes):
    movie_choice = rd.choice(df_animes['anime'])
    print(f"Today's Recomendation is an anime: {movie_choice}")


