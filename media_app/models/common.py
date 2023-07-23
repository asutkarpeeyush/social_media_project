from django.db import models


# This model is abstract and a DB table won't be created for this.
class MetaInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
