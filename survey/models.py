from django.db import models

# Create your models here.
class Answer(models.Model):
    slug = models.SlugField(null=False, unique=True)
    code = models.CharField(max_length=4)
    num_players = models.IntegerField(default=1)
    text = models.CharField(max_length=300)

    def _str_(self):
        return self.text

# class Answer(models.Model):
#     room_code = models.ForeignKey(Room, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)

#     def __str__(self):
#         return self.text
