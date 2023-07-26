from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class showroom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural="showroom"
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    showroom = models.ForeignKey(showroom, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Staff"

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Brand"

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    engine = models.ForeignKey('Engine', on_delete=models.CASCADE)
    features = models.ManyToManyField('Feature')
    class Meta:
        verbose_name_plural="Model"

    def __str__(self):
        return self.name

class Engine(models.Model):
    name = models.CharField(max_length=100)
    specs = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural="Engine"

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Feature"

    def __str__(self):
        return self.name
