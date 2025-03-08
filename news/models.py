from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    content = models.TextField()
    sentiment = models.CharField(max_length=10, choices=[('positive','Positive'),('neutral','Neutral'),('negative','Negative')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
