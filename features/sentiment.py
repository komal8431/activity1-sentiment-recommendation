# sentiment.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure NLTK resources are downloaded
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def analyze_mood(self, user_input):
        sentiment_scores = self.sid.polarity_scores(user_input)
        if sentiment_scores['compound'] >= 0.05:
            return 'positive'
        elif sentiment_scores['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

