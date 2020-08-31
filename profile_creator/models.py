from django.db import models

class User_Profile(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 200)
    display_picture = models.FileField()

    def __str__(self):
        return self.first_name
