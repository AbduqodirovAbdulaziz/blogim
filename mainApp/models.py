from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.article} - {self.text[:32]}"


class SocialMedia(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='social-media/', blank=True, null=True)
    url = models.URLField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
