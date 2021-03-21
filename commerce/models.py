from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    """fields of Product table"""
    p_name = models.CharField(max_length=200)
    p_description = models.CharField(max_length=1000)
    p_image = models.FileField(upload_to='product_image')
    p_category = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name
