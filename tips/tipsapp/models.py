from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=300)
    id_number = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.name
