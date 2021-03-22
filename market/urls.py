from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.home, name="home"),
    url(r'^predict/$', views.predict, name="predict"),
    path('survey/', views.survey, name="survey"),
    path('team/', views.team, name="team"),
    # url(r'^(?P<username>[\w-]+)', views.user, name="user"),

]
