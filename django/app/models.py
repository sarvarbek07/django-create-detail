from django.db import models

class HomeModel(models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()

    def __str__(self):
        return self.title
