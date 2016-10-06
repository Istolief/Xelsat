from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    brand = models.ForeignKey('catalog.Brand', null=True)
    category = models.ForeignKey('catalog.Category',  null=True)
    description = models.TextField()
    img = models.FileField(upload_to='product_img', default='None')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=200)
    img = models.FileField(upload_to='brand_img', default='None')
    slug = models.SlugField(default='')  # todo: проверить slug должен быть уникальным

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='')  # todo: проверить slug должен быть уникальным
    owner = models.ForeignKey('catalog.Category', null=True, blank=True)

    def __str__(self):
        return self.title
