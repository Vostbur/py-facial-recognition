from django.db import models

class FaceImage(models.Model):
    image = models.ImageField(upload_to='images/')
