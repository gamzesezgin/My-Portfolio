from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Mail(models.Model):
    mail = models.CharField(max_length=50)
    message = models.CharField(max_length=400)

    def __str__(self):
        return f"Mail: {self.mail}, Message: {self.message}"