from django.db import models
from django.contrib.auth.models import User  # 추가

class Bookmark(models.Model):
   id = models.AutoField(primary_key = True)
   title = models.CharField(null = True,max_length = 100,blank=True)
   url = models.URLField('url', unique = True)
   owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)   # 추가

   def __str__(self):
      return self.title

