from django.db import models

# Create your models here.
STATUS = (('active','active'),('','default'))
class Category(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length = 400)
    logo = models.CharField(blank=True , max_length=50)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=400)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #for deleting the subcategory auomatically if the category field is deleted
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500,blank=True)
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS,max_length=50)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500, blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

STOCK = (('In stock','In stock'),('Out of stock','Out of stock'))
LABEL = (('new','new'),('hot','hot'),('sale','sale'))

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    dis_price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.CharField(choices=STOCK,max_length=500)
    labels = models.CharField(choices=LABEL,max_length=50,blank=True)

    def __str__(self):
        return self.name


