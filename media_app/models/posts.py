from django.db import models
from django.contrib.auth.models import User
from .common import MetaInfo


class Post(MetaInfo):
    user = models.ForeignKey(User, related_name='post',
                             on_delete=models.CASCADE, null=True)
    caption = models.TextField()
    image = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = "post"


class LikePost(MetaInfo):
    post = models.ForeignKey(
        Post, related_name='like_post', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='like_post', on_delete=models.CASCADE)

    class Meta:
        db_table = "like_post"
