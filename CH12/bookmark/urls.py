from django.conf.urls import url
from bookmark.views import *    # 변경

app_name="bookmark"

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

    url(r'^add/$', BookmarkCreateView.as_view(), name='add'),
    url(r'^change/$', BookmarkChangeLV.as_view(), name='change'),
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDeleteView.as_view(), name='delete'),
]
