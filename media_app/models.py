from django.db import models
from django.contrib.auth.models import User


# This model is abstract and a DB table won't be created for this.
class MetaInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(MetaInfo):
    user = models.ForeignKey(
        User, related_name='profile', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "profile"


class Post(MetaInfo):
    user = models.ForeignKey(User, related_name='post',
                             on_delete=models.CASCADE)
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
