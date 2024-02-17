from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to="products/img")  
    title = models.CharField(max_length=20)
    offer = models.IntegerField(null=True,blank=True)
    link = models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("PRODUCT")
        verbose_name_plural = ("PRODUCT") 