from django.db import models


class StudentRegistration(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=120)
    cpf = models.IntegerField()
    number = models.IntegerField()
    email = models.CharField(max_length=120)
    create_at = models.DateTimeField(auto_now_add=True)