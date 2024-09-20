# main.py

from sentiment import SentimentAnalyzer
from recommendation import Recommender

def main():
    # Create instances of the classes
    sentiment_analyzer = SentimentAnalyzer()
    recommender = Recommender('Series_name_dataset.csv', 'Music_dataset.csv')

    # Get user input
    user_input = input("How are you feeling today? ")

    # Analyze the user's mood
    mood = sentiment_analyzer.analyze_mood(user_input)
    print(f"Detected mood: {mood}")

    # Ask user for preference
    choice = int(input("Enter 1 for Series Recommedation\nEnter 2 for Songs Recommendation\nYour Input:"))

    # Provide recommendations based on the user's choice
    if choice == 1:
        movie_recommendations = recommender.recommend_movies(mood)
        if movie_recommendations.empty:
            print("Sorry, we couldn't find any series recommendations for your mood.")
        else:
            print("\nRecommended Series for your mood:")
            print(movie_recommendations.to_string(index=False))
        return user_input,choice
    elif choice == 2:
        song_recommendations = recommender.recommend_songs(mood)
        if song_recommendations.empty:
            print("Sorry, we couldn't find any song recommendations for your mood.")
        else:
            print("\nRecommended Songs for your mood:")
            print(song_recommendations.to_string(index=False))
        return user_input,choice
    else:
        print(choice)
        print("Invalid choice. Please enter 'series' or 'songs'.")
    


if __name__ == "__main__":
    main()