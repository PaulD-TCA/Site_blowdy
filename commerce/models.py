from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    """fields of Product table"""
    p_name = models.CharField(max_length=200)
    p_summary = models.CharField(max_length=300)
    p_description = models.CharField(max_length=5000)
    p_image = models.FileField(upload_to='product_image')
    p_category = models.CharField(max_length=50)
    p_creation_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name
