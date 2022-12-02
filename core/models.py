from django.db import models
from django.urls import reverse

# Create your models here.
#BLOG MODEL
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
    sarlovha = models.CharField(max_length=250)
    sarlovha_ru = models.CharField(max_length=250)
    sarlovha_en = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255)
    matn = models.TextField(blank=True, null=True)
    matn_ru = models.TextField(blank=True, null=True)
    matn_en = models.TextField(blank=True, null=True)
    matn2 = models.TextField(null=True, blank=True)
    matn2_ru = models.TextField(null=True, blank=True)
    matn2_en = models.TextField(null=True, blank=True)
    matn3 = models.TextField(null=True, blank=True)
    matn3_ru = models.TextField(null=True, blank=True)
    matn3_en = models.TextField(null=True, blank=True)
    joylangan = models.DateTimeField(auto_now_add=True)
    rasm = models.ImageField(upload_to='image/')

    class Meta:
        verbose_name_plural='post'
        ordering=['-joylangan']

    def __str__(self):
        return self.sarlovha

    def get_absolute_url(self):
        return reverse('single_blog', args=[self.slug])


class Portfolio(models.Model):
    sarlovha = models.CharField(max_length=255, blank=True, null=True)
    sarlovha_ru = models.CharField(max_length=255, blank=True, null=True)
    sarlovh_en = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255,  blank=True, null=True)
    matn = models.TextField(blank=True, null=True)
    matn_ru = models.TextField(blank=True, null=True)
    matn_en = models.TextField(blank=True, null=True)
    rasm = models.ImageField(upload_to='image/', default='')
    client = models.CharField(max_length=255,  blank=True, null=True)
    xizmat = models.CharField(max_length=255,  blank=True, null=True)
    joylangan = models.DateTimeField(auto_now_add=True)
    vaqt = models.DateTimeField()

    def __str__(self):
        return self.sarlovha

    class Meta:
        ordering = [
            '-joylangan'
        ]

    def get_absolute_url(self):
        return reverse('single_portfolio', args=[self.slug])







