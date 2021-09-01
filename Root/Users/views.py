""" Users Authentication """

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = "account/login.html"


class DashboardTemp(LoginRequiredMixin, View):
    """View of dashboard"""

    login_url = "/"
    # template_name = "pages/home.html"
    def get(self, request, *args, **kwargs):

        cntx = {
            "user": request.user,
        }
        return render(request, "pages/home.html", cntx)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = "account/login.html"
