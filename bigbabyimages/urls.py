from django.conf.urls import url, include
from django.conf import settings


urlpatterns = [
  #url(r'^$', views.index, name='index'),
  url(r'register', views.register_new_user, name='register'),
  url(r'login', views.login_user, name='login'),