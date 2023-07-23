from django.shortcuts import render
from django.http import HttpRequest
from django.views import View


class Profile(View):
    def get(self, request: HttpRequest, **kwargs: dict):
        page_name = "profile_settings.html"
        return render(request, page_name, {})

    # TODO: capability to update the profile.
