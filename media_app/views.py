from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth


def index(request):
    """Landing Page."""
    page_name = "index.html"
    return render(request, page_name, {})


@method_decorator(csrf_exempt, name='dispatch')
class SignUp(View):
    """ Sign up Views.
    """

    def get(self, request: HttpRequest, **kwargs: dict):
        page_name = "sign_up.html"
        return render(request, page_name, {})

    def _user_exists(self, username: str, email: str) -> tuple[bool, dict]:
        if User.objects.filter(username=username).exists():
            return (True, {"error": True, "error_msg": "Username already exists."})
        if User.objects.filter(email=email).exists():
            return (True, {"error": True, "error_msg": "Email already exists."})

        return (False, {})

    def post(self, request: HttpRequest, **kwargs: dict):
        # TODO: Convert this to a Django form

        page_name = "sign_up.html"

        # fetch the form details
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # validate user existence
        exists, error_details = self._user_exists(
            username=username, email=email)
        if exists:
            return render(request, page_name, error_details)

        # save the user to the DB and authenticate the user if valid
        # user = User(username=username, email=email, password=password)
        # user.save()
        user = User.objects.create_user(
            username=username, email=email, password=password)  # creates an object in User table
        # this should provide an authenticated session
        user = auth.authenticate(username=username, password=password)

        # redirect appropriately
        if not user:
            return render(request, page_name, {"error": True, "error_msg": "Signup Unsuccessful."})

        auth.login(request, user)
        return redirect('media_app_index')
