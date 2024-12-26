from django.urls import path

from . import views

app_name = "firstapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("register/", views.register, name = "register"),
    path("login/", views.login, name = "login"),
    path("logout/", views.logout, name='logout')
]