from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pictures'

urlpatterns = [
    url('', views.index, name='index'),
    url('search/', views.search_results, name='search'),
    # url('location/(?P<location>\w+)/', views.image_location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)