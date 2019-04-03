from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name="index"),
    url('<int:questionID>/', views.detail, name="detail"),
    url('<int:questionID>/results/', views.results, name="results"),
    url('<int:questionID>/vote/', views.vote, name="vote"),
]
