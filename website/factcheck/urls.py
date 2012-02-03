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
    (r'^facts/$', 'factchecker.views.facts'),
    (r'facts/(?P<fact_req>\d{1})/$', 'factchecker.views.tweets'),
    (r'$', 'factchecker.views.facts'),
)