from django.conf.urls import url
from bookmark.views import BookmarkLV, BookmarkDV

app_name="bookmark"

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]
