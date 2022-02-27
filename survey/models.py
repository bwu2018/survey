from django.db import models

# Create your models here.
class Room(models.Model):
    # slug = models.SlugField(null=False, unique=True)
    code = models.CharField(max_length=4)
    num_players = models.IntegerField(default=1)

    def _str_(self):
        return self.code

class Answer(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.CharField(max_length=300)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
