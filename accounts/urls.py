from django.urls import path
from . import views
from django.conf.urls import url
app_name = "accounts"

urlpatterns = [
    url(r'signup', views.signup, name="signup"),
    url(r'login', views.login, name="login"),
    url(r'logout', views.logout, name="logout"),
    url(r'forget', views.forget, name="forget"),
    url(r'update', views.update, name="update"),
    # path('user_detail', views.user_detail, name="user"),
]
