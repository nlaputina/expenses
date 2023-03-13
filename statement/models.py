from django.db import models


class Expenses(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=288)
    amount = models.CharField(max_length=288)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['date']

    def to_dict(self):
        expenses_info = {
            'date': self.date,
            'description': self.description,
            'amount': self.amount
        }
        return expenses_info


class Income(models.Model):
    description = models.CharField(max_length=288)
    amount = models.CharField(max_length=288)

    def __str__(self):
        return self.description

#
# class Category(models.Model):
