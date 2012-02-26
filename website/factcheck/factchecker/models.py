from django.db import models

class WebPage(models.Model):
    url = models.URLField()
    source = models.CharField(max_length=50)
    fact = models.ForeignKey('Factcheck')
    remote_id = models.IntegerField()

class Tweet(models.Model):
    sender = models.CharField(max_length=30)
    tweet_date = models.DateField()
    content = models.TextField()
    fact = models.ForeignKey('Factcheck')
    remote_id = models.IntegerField()
    
class Factcheck(models.Model):
    title = models.CharField(max_length=30)
    claim = models.TextField()
    status = models.TextField()
    remote_id = models.IntegerField()