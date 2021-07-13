from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.login_view, name="login"),
    path("signin/",views.signin_view),
    path("logout/",views.logout_view, name="logout"),
]