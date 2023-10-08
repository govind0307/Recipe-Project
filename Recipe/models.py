from django.db import models

# Create your models here.

class vege(models.Model):
    vege_name = models.CharField(max_length=100)
    vege_description = models.TextField()
    vege_image = models.ImageField(upload_to="vege")