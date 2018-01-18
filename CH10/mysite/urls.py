from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static  # 추가
from django.conf import settings            # 추가

from mysite.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),  # 추가
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 추가
