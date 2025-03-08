import requests
from textblob import TextBlob

NEWS_API_KEY = "fe0ba38c6e154e519b098af01671d832"

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=fe0ba38c6e154e519b098af01671d832"
    response = requests.get(url)
    data = response.json()
    return data.get('articles',[])

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    return "neutral"

