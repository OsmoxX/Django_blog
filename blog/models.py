from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='posts')
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    slug = models.SlugField(unique=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
