# recommendation.py

import pandas as pd
from sentiment import analyze_mood

# Step 1: Load your CSV data into DataFrames
# Assuming your CSV has columns: 'Title', 'Genre', 'Description' for movies
movies_df = pd.read_csv('your_movie_database.csv')

# Assuming you have a separate CSV for songs with similar columns
songs_df = pd.read_csv('your_song_database.csv')

# Example of your song CSV structure:
# | Title            | Genre              | Description                    |
# |------------------|--------------------|---------------------------------|
# | Happy            | Pop                | A cheerful and uplifting song   |
# | Sad Song         | Ballad             | A melancholic ballad            |

# Step 4: Mapping mood to genres
mood_to_genre = {
    'positive': ['Comedy', 'Adventure', 'Romance', 'Pop', 'Dance'],
    'negative': ['Horror', 'Thriller', 'Drama', 'Sad', 'Ballad'],
    'neutral': ['Drama', 'Action', 'Mystery', 'Instrumental', 'Alternative']
}

# Step 5: Filter movies based on the detected mood
def recommend_movies(mood, movies_df):
    # Get genres matching the user's mood
    matching_genres = mood_to_genre[mood]
    
    # Filter the DataFrame to get movies matching the mood
    recommended_movies = movies_df[movies_df['Genre'].str.contains('|'.join(matching_genres), case=False, na=False)]
    
    return recommended_movies[['Title', 'Genre']]

# Step 5: Filter songs based on the detected mood
def recommend_songs(mood, songs_df):
    # Get genres matching the user's mood
    matching_genres = mood_to_genre[mood]
    
    # Filter the DataFrame to get songs matching the mood
    recommended_songs = songs_df[songs_df['Genre'].str.contains('|'.join(matching_genres), case=False, na=False)]
    
    return recommended_songs[['Title', 'Genre']]

# Step 6: Main function to recommend based on user's mood
def get_recommendations(user_input):
    # Analyze the user's mood
    mood = analyze_mood(user_input)
    print(f"Detected mood: {mood}")
    
    # Recommend movies/series based on the mood
    movie_recommendations = recommend_movies(mood, movies_df)
    
    # Recommend songs based on the mood
    song_recommendations = recommend_songs(mood, songs_df)
    
    # Display movie recommendations
    if movie_recommendations.empty:
        print("Sorry, we couldn't find any movie recommendations for your mood.")
    else:
        print("\nRecommended Movies for your mood:")
        print(movie_recommendations)

    # Display song recommendations
    if song_recommendations.empty:
        print("Sorry, we couldn't find any song recommendations for your mood.")
    else:
        print("\nRecommended Songs for your mood:")
        print(song_recommendations)

# Example usage
if __name__ == "__main__":
    user_input = input("How are you feeling today? ")
    get_recommendations(user_input)
