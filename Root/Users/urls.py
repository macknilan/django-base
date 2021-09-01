"""Users URLs."""

from django.urls import path
from Root.Users.views import LoginView, DashboardTemp, LogoutView

app_name = "users"
urlpatterns = [
    path("", view=LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("dashboard/", view=DashboardTemp.as_view(), name="temp"),
    path("logout/", view=LogoutView.as_view(), name="logout"),
]
