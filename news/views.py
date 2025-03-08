from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import fetch_news, analyze_sentiment
from .models import NewsArticle

@api_view(['GET'])
def get_news(request):
    news_data = fetch_news()
    articles = []

    for news in news_data:
        sentiment = analyze_sentiment(news['description'] or news['title'])
        article = NewsArticle.objects.create(
            title = news['title'],
            url = news['url'],
            content = news['description'] or '',
            sentiment = sentiment
        )
        articles.append({
            "title" : article.title,
            "url" : article.url,
            "sentiment" : article.sentiment,

        })

    return Response(articles)