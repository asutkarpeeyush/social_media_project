from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from media_app.models.posts import Post


def index(request):
    """Landing Page."""
    page_name = "index.html"
    user_posts = Post.objects.all()
    return render(request, page_name, {'user_posts': user_posts})


@method_decorator(csrf_exempt, name='dispatch')
class SignUp(View):
    """ Sign up Views.
    """

    def _user_exists(self, username: str, email: str) -> tuple[bool, dict]:
        if User.objects.filter(username=username).exists():
            return (True, {"error": True, "error_msg": "Username already exists."})
        if User.objects.filter(email=email).exists():
            return (True, {"error": True, "error_msg": "Email already exists."})

        return (False, {})

    def get(self, request: HttpRequest, **kwargs: dict):
        page_name = "sign_up.html"
        return render(request, page_name, {})

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
        if not user:
            return render(request, page_name, {"error": True, "error_msg": "Signup Unsuccessful."})

        # Not needed during sign up.
        # user = auth.authenticate(username=username, password=password)
        # auth.login(request, user)

        # TODO: redirect the user to login page
        return redirect('media_app_login')


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    """
    Login Views.
    """

    def get(self, request: HttpRequest, **kwargs: dict):
        page_name = "login.html"
        return render(request, page_name, {})

    def post(self, request: HttpRequest, **kwargs: dict):
        page_name = "login.html"

        # fetch the form details
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        print(request.session.items())

        # validate user existence
        user = auth.authenticate(username=username, password=password)
        if not user:
            return render(request, page_name, {"error": True, "error_msg": "Login Unsuccessful."})

        # login the user to create a session
        auth.login(request, user)
        print(request.session.items())

        return redirect('media_app_index')


@login_required(login_url='media_app_login')
def logout(request):
    auth.logout(request)
    return redirect('media_app_index')
