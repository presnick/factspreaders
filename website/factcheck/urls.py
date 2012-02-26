from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^factcheck/', include('factcheck.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    (r'^facts/$', 'factchecker.views.facts'),
    (r'facts/(?P<fact_req>\d+)/$', 'factchecker.views.tweets'),
    (r'^more_f$', 'factchecker.views.more_facts'),
    (r'^more_t$', 'factchecker.views.more_tweets'),  
    (r'$', 'factchecker.views.facts'),
)
