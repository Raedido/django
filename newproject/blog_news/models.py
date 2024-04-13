from django.db import models

# Create your models here.

class NewsModel(models.Model):
    description = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=1000, null=True)
    url = models.CharField(max_length=1000, null=True)
    content = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = "blog"
    #Add more fields---