from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ('id', 'author','title', 'content','created_date','article_image','slug','tags','meta_title','meta_description','keyphrase')