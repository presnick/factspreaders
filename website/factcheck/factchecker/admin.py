from django.contrib import admin
from factcheck.factchecker.models import WebPage, Factcheck, Tweet


admin.site.register(WebPage)
admin.site.register(Tweet)
admin.site.register(Factcheck)