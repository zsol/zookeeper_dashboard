from django.conf.urls import patterns

urlpatterns = patterns('zookeeper_dashboard.zktree.views',
    (r'^(?P<path>.*)/$','index'),
    (r'^$','index'),
)
