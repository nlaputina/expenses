from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=288)
    key_words = models.CharField(max_length=288)

    def __str__(self):
        return self.name

    def to_dict(self):
        tags_info = {
            'tag_id': self.id,
            'name': self.name,
            'key_words': self.key_words,
        }

        return tags_info


class Expenses(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=288)
    amount = models.CharField(max_length=288)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['date']

    def to_dict(self):
        expenses_info = {
            'date': self.date,
            'description': self.description,
            'amount': self.amount,
            'tags': [tag.name for tag in self.tags.all()]
        }
        return expenses_info


class Income(models.Model):
    description = models.CharField(max_length=288)
    amount = models.CharField(max_length=288)

    def __str__(self):
        return self.description
