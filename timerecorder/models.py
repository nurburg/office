from django.db import models

# Create your models here.
class Recorder(models.Model):
    name = models.Charfield(max_length=50)



