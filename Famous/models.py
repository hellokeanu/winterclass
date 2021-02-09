from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)



class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    restaurant_name = models.CharField(max_length=100)
    restaurant_link = models.CharField(max_length=100)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length=100)



