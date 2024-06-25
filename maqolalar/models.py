from django.db import models

from users.models import User


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=255)
    batafsil = models.TextField()
    rasm = models.ImageField(upload_to='maqolalar/')
    sana = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    korish_soni = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.sarlavha
