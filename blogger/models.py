from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Ronny Dsouza ",related_name="Blogger")
    title = models.CharField(max_length = 100,verbose_name = "Title")
    content = models.CharField(max_length = 1000)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Select Date")
    article_image = models.FileField(blank = True,null = True,verbose_name="Image")
    slug = models.SlugField(unique=True, max_length=100)
    tags = models.CharField(blank =True, max_length = 200)
    meta_title = models.CharField(blank =True, max_length = 100)
    meta_description = models.CharField(blank =True, max_length = 200)
    keyphrase = models.CharField(blank =True, max_length = 200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Descpition",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Ronny Dsouza")
    comment_content = models.CharField(max_length = 200,verbose_name = "Blogger")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']