from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=50)

    def __str__(self):
        return '%s (%s)' % (self.name, self.description)
