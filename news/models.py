import uuid

from django.db import models


# Create your models here.
class News(models.Model):
    news_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    assigned_to_uuid = models.UUIDField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    news_text = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.news_uuid)
