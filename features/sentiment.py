import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the Sentiment Intensity Analyzer
        self.sia = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text):
        # Analyze the sentiment of the given text
        score = self.sia.polarity_scores(text)
        sentiment = self.determine_sentiment(score)
        return score, sentiment
    
    def determine_sentiment(self, score):
        # Determine overall sentiment based on compound score
        compound = score['compound']
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

# Example of testing sentiment analysis
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    
    text_samples = input("How are you feeling today? ")
    score, sentiment = analyzer.analyze_sentiment(text_samples)

    print(f"Detected Sentiment: {sentiment}")