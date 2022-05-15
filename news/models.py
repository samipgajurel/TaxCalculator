from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000)
    picture = models.CharField(max_length=100,blank=True,null=True)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    dateCreated = models.DateTimeField(default=timezone.now())
    lastModified = models.DateTimeField(default=timezone.now())
    # dateApproved = models.DateTimeField(default=timezone.now())
    # isApproved = models.BooleanField(default=False)



    class Meta:
        db_table = "news"

from django.db import models

# Create your models here.
