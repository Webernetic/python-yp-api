from django.db import models


# Create your models here.
class Option(models.Model):  
    option_name = models.TextField()
    option_value = models.TextField()
    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"

