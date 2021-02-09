from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    