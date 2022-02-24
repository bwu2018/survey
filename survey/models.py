from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=4)

    def _str_(self):
        return self.code