from django.urls import path, re_path
from  . import  views

urlpatterns = [
    re_path(r'^books_drf/$', views.Books.as_view()),
    re_path(r'^books_drf/(?P<pk>\d+)/$', views.Books.as_view()),
]
