from django.db import models

class Expenses (models.Model):
    date = models.DateField()
    description = models.CharField(max_length=288)
    amount = models.CharField(max_length=288)

    def __str__(self):
        return self.description