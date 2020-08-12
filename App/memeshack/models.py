
from django.db import models
from django.utils import timezone

class memes(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
