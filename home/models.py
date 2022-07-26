from django.db import models

from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Categories(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Regions(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='author')
    description = models.TextField(max_length=200)
    sm = models.URLField()

    biography = models.TextField()

    def __str__(self):
        return self.name


class Articles(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    subtitle = models.TextField(max_length=300)
    content = models.TextField()
    preview_image = models.ImageField(upload_to='preview_articles', null=True)
    image = models.ImageField(upload_to='articles', null=True)

    tags = models.ManyToManyField(Tags)
    region = models.ForeignKey(Regions,on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(null=True, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField(max_length=350)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Articles)
def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
