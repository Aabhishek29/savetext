from django.db import models


# Create your models here.


class Users(models.Model):
    name = models.CharField(
        max_length=30, blank=False,
    )
    emailId = models.EmailField(
        max_length=50, unique=True, blank=False
    )
    password = models.CharField(
        max_length=16, blank=False
    )

    def __str__(self):
        return self.name


class Files(models.Model):
    name = models.CharField(
        max_length=30, blank=False
    )
    docId = models.CharField(
        max_length=30, blank=False
    )
    createdAt = models.DateTimeField(blank=False)
    updatedAt = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name




