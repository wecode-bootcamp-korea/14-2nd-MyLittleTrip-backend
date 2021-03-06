from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=10)
    email         = models.EmailField(max_length=30)
    password      = models.CharField(max_length=200, null=True)
    phone_number  = models.CharField(max_length=20, null=True)
    card_number   = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'users'
