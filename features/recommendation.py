# recommendation.py

import pandas as pd

class Recommender:
    def __init__(self, movies_file, songs_file):
        self.movies_df = pd.read_csv(movies_file)
        self.songs_df = pd.read_csv(songs_file)

        self.mood_to_genre = {
            "positive": [
                "Comedy",
                "Adventure",
                "Romance",
                "Pop",
                "Indie",
                "Dance",
                "Chill",
                "Rock",
                "Folk"
            ],
            "negative": [
                "Thriller",
                "Horror",
                "Drama",
                "Dark Comedy",
                "Melancholic Pop"
            ],
            "neutral": [
                "Historical",
                "Action",
                "Documentaries",
                "Instrumental"
            ]
        }

    def recommend_movies(self, mood):
        matching_genres = self.mood_to_genre[mood]
        recommended_movies = self.movies_df[self.movies_df['Genre'].str.contains('|'.join(matching_genres), case=False, na=False)]
        return recommended_movies[['Series Name', 'Genre', 'Language']]

    def recommend_songs(self, mood):
        matching_genres = self.mood_to_genre[mood]
        recommended_songs = self.songs_df[self.songs_df['Genre'].str.contains('|'.join(matching_genres), case=False, na=False)]
        return recommended_songs[['Song Name', 'YouTube Link']]
