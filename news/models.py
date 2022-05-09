from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000)
    picture = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    dateCreated = models.DateTimeField(default=timezone.now())
    dateApproved = models.DateTimeField(default=timezone.now())
    isApproved = models.BooleanField(default=False)



    class Meta:
        db_table = "news"

from django.db import models

# Create your models here.
