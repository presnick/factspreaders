from django.db import models

class WebPage(models.Model):
    url = models.URLField()
    source = models.CharField(max_length=50)
    fact = models.ForeignKey('Factcheck')

class Tweet(models.Model):
    sender = models.CharField(max_length=30)
    tweet_date = models.DateField()
    content = models.TextField()
    fact = models.ForeignKey('Factcheck')

class Factcheck(models.Model):
    title = models.CharField(max_length=30)
    claim = models.TextField()
    status = models.TextField()