from django.urls import path
from .views import auth_views, profile_views, post_views

urlpatterns = [
    # auth related
    path('sign_up', auth_views.SignUp.as_view(), name='media_app_sign_up'),
    path('login', auth_views.Login.as_view(), name='media_app_login'),
    path('logout', auth_views.logout, name='media_app_logout'),

    # Posts related
    path('post/<int:post_id>', post_views.UserPost.as_view(), name='media_app_post'),
    path('post', post_views.UserPost.as_view(),
         name='media_app_post'),  # redundant urls
    path('like_post/<int:post_id>', post_views.UserPostLike.as_view(),
         name='media_app_post_like'),

    # profile related
    path('profile', profile_views.Profile.as_view(), name='media_app_profile'),

    # default
    path('', auth_views.index, name='media_app_index')
]
