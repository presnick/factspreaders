from django.shortcuts import render_to_response
from django.template.context import RequestContext
from factcheck.factchecker.models import Factcheck, Tweet
import json
import urllib
import urllib2

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def more_facts(request):
    try:
        last_article_id = Factcheck.objects.order_by('remote_id').reverse()[0].remote_id
    except:
        last_article_id = 0
    new_count = fetch_articles(last_article_id, 5)
    return render_to_response('Status.html', {'last_id': last_article_id, 'new_count': new_count}, context_instance=RequestContext(request))
    

def more_tweets(request):
    facts = Factcheck.objects.order_by('remote_id').reverse()
    for fact in facts:
        try:
            last_id = Tweet.objects.order_by('remote_id').reverse()[0]
        except:
            last_id = 0
        fetch_tweets(fact.remote_id, fact, last_id, 5)
    return render_to_response('Status.html', {'last_id': 0, 'new_count': 0}, context_instance=RequestContext(request))
       
    
def facts(request):
    facts = Factcheck.objects.order_by('id').reverse()
    return render_to_response('Facts.html', {'facts': facts}, context_instance=RequestContext(request))

def tweets(request, fact_req):
    fact_obj = Factcheck.objects.get(id=fact_req)
    
    tweets = Tweet.objects.filter(fact__id=fact_req).order_by('id').reverse()
    return render_to_response('Tweets.html', {'fact': fact_obj, 'tweets': tweets}, context_instance=RequestContext(request))

def fetch_tweets(article_id, article_obj, last_id, limit):
    url = "http://newton.si.umich.edu/rumors_demo/rumors.php"
    params = { "func": "getTweets", "article_id": article_id, "algorithm_id": 1, "last_tweet_id:": last_id, "ret_limit": limit }
    data = urllib.urlencode(params)
    
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    
    tweets = json.loads(response.read()) #15 is start of JSON, -19 is end of JSON
    
    #if tweet_dict != None: 
    if tweets:
        for tweet in tweets:
            tw = Tweet(remote_id=int(tweet["TID"]), content=tweet["CONTENT"], tweet_date="2012-02-21", fact=article_obj)
            tw.save()

def fetch_articles(last_id, limit):
    url = "http://newton.si.umich.edu/rumors_demo/rumors.php"
    params = { "func": "getArticles", "last_article_id": last_id, "ret_limit": limit }
    data = urllib.urlencode(params)
    
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    
    article_list = json.loads(response.read()) #15 is start of JSON, -19 is end of JSON
    if article_list != None:
        for article in article_list:
            fc = Factcheck(remote_id=article["QID"], title=article['TITLE'], claim=article['CONTENT'])
            fc.save()