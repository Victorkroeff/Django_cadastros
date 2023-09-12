from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    idade = models.IntegerField()
    