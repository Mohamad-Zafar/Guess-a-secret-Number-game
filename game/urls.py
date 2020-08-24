from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("r'^login/$'", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("guessgame/<str:id>", views.guessgame, name="guessgame"),
    path("end_game", views.end_game, name="end_game"),
    path("showhistory/<str:id>", views.showhistory, name="showhistory"),
]
