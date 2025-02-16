from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
