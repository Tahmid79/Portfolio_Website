from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    desc = models.TextField()
    img = models.CharField(max_length=20)

    def __str__(self):
        return self.title




