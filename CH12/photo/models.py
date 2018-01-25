from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse # 장고 2.0 에서 변경

from photo.fields import ThumbnailImageField

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

class Photo(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,)  # 2.0 부터 on_delete 옵션 필수
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')    # Custom field
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))