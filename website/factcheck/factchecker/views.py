from django.shortcuts import render_to_response
from factcheck.factchecker.models import Factcheck, Tweet

def facts(request):
    facts = Factcheck.objects.all()
    return render_to_response('facts.html', {'facts': facts})

def tweets(request, fact_req):
    fact_obj = Factcheck.objects.get(id=fact_req)
    tweets = Tweet.objects.filter(fact=fact_obj)
    return render_to_response('tweets.html', {'fact': fact_obj, 'tweets': tweets})