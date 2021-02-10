from django.db import models


class Field(models.Model):
    fieldname=models.CharField(max_length=100,unique=True)

class Human(models.Model):
    humanname = models.CharField(max_length=100, unique=True)

class Task(models.Model):
    taskname = models.CharField(max_length=100, unique=True)

class Work(models.Model):
    year=models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    extend = models.FloatField()

    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    human = models.ForeignKey(Human, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)




#
# class Category(models.Model):
#     category_name = models.CharField(max_length=100, unique=True)
#
#
#
# class Restaurant(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     restaurant_name = models.CharField(max_length=100)
#     restaurant_link = models.CharField(max_length=100)
#     restaurant_content = models.TextField()
#     restaurant_keyword = models.CharField(max_length=100)
#
#

