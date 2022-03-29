from django.db import models


# Create your models here.
class News(models.Model):
    content = models.CharField(max_length=1000)
    picture = models.CharField(max_length=100)


    class Meta:
        db_table = "news"

from django.db import models

# Create your models here.
