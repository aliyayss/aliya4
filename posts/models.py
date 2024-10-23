from django.db import models

class  Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
class Post(models.Model):
    image = models.ImageField( null=True, blank=True)
    title = models.CharField(max_length=70)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name



    