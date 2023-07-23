from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from media_app.models.posts import Post, LikePost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


@method_decorator(csrf_exempt, name='dispatch')
class UserPost(LoginRequiredMixin, View):
    # login_url = reverse_lazy('media_app_login')
    login_url = '/login'

    def post(self, request: HttpRequest, **kwargs: dict):
        # fetch the post params
        caption = request.POST.get('caption', '')
        image = request.FILES.get('image_upload', None)

        # create a post
        try:
            post = Post(caption=caption)
            post.save()
            # Post.objects.create(user=request.user,
            #                     caption=caption, image=image)
        except Exception as e:
            # return redirect('media_app_index')
            return redirect('media_app_index', {"error": True, "error_msg": "Invalid Post Details."})

        return redirect('media_app_index')


@method_decorator(csrf_exempt, name='dispatch')
class UserPostLike(View):
    def get(self, request: HttpRequest, post_id: int, **kwargs: dict):
        post = Post.objects.get(id=post_id)
        if not post:
            return redirect('media_app_index', {"error": True, "error_msg": "Unable to like the post since it doesn't exist."})

        # create a like on the post
        try:
            LikePost.objects.create(user_id=request.user.id, post_id=post_id)
        except Exception as e:
            return redirect('media_app_index', {"error": True, "error_msg": "Unable to like the post."})

        return redirect('media_app_index')
