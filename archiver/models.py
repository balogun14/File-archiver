from django.db import models

# Create your models here.


class Archiver(models.Model):
    title = models.CharField(max_length=300)

    # file = models.FileField(upload_to=)
    def __str__(self):
        return self.title
