from django.conf import settings
from django.conf.urls import include, patterns

urlpatterns = patterns('zookeeper_dashboard',
    (r'^cluster/', include('zookeeper_dashboard.zkadmin.urls')),
    (r'^tree/', include('zookeeper_dashboard.zktree.urls')),
    (r'^$', include('zookeeper_dashboard.zkadmin.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './css'}),
    )
