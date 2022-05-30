from django.urls import re_path as url, include
from django.conf import settings


urlpatterns = [
        url(r'^$', views.all_wallpapers, name='wallpapers'),
    url(r'^wallpaper/(?P<id>\d+)', views.wallpaper, name='wallpaper'),
    # url(r'^sports/'$, views.sport_wallpaper, name='sportWallpapers'),
    
    #url(r'^movie_wallpaper/', views.movie_wallpaper, name='movieWallpapers'),
    url(r'^search/', views.search_results, name='search_results')
    ]
    
