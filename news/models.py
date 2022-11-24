from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class Guruxlash(models.Model):
    ism = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta():
        verbose_name_plural = 'guruxlash'

    def get_absolute_url(self):
        return reverse('news_page', args=[self.slug])

    def __str__(self):
        return self.ism


# Blog post model
class Post(models.Model):
    gurux = models.ForeignKey(Guruxlash, related_name='gurux', on_delete=models.CASCADE)
    sarlovha = models.CharField(max_length=250,)
    slug = models.SlugField(max_length=255)
    matn = models.TextField()
    joylangan = models.DateTimeField(auto_now_add=True)
    rasm = models.ImageField(upload_to='image/')

    class Meta:
        verbose_name_plural='post'
        ordering=['-joylangan']

    def __str__(self):
        return self.sarlovha

    def get_absolute_url(self):
        return reverse('single_blog', args=[self.slug])

