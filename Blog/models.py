from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model
from autoslug.fields import AutoSlugField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    blog = RichTextField()
    slug = AutoSlugField(populate_from='title')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
