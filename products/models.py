from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')


class BlogLeft(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='media')


class BlogRight(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='media')


class LatestBlogLeft(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateField()
    content = models.TextField(550)
    image = models.ImageField(upload_to='media')


class LatestBlogRight(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateField()
    content = models.TextField(550)
    image = models.ImageField(upload_to='media')
