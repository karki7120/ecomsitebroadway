from django.db import models

# Create your models here.

STATUS = (('active', 'active'),('', 'inactive'))

class Category(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300, unique=True)
    description = models.CharField(max_length= 300)


    def __str__(self):
        return self.name




class SubCategory(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length= 300)


    def __str__(self):
        return self.name

class slider(models.Model):
    name = models.CharField(max_length= 300)
    slug = models.CharField(max_length= 300)
    description = models.TextField(max_length= 300)
    image = models.ImageField(upload_to = 'media' )
    rank = models.IntegerField()
    status = models.CharField(max_length= 300, choices = STATUS)

    def __str__(self):
        return self.name