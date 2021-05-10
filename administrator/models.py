from django.db import models

# Create your models here.
class Mobile(models.Model):
    model_name=models.CharField(max_length=30,unique=True)
    manufacturer=models.CharField(max_length=120)
    specs = models.CharField(max_length=120)
    image=models.ImageField(upload_to="images/")
    price = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
        return self.model_name
