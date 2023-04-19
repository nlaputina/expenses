import json

from django.core.management.base import BaseCommand
from statement.models import Expenses, Tag


class Command(BaseCommand):
    help = 'Add tags to database'

    def handle(self, *args, **options):
        expenses = Expenses.objects.all()
        tags = Tag.objects.all()
        for expense in expenses:
            for tag in tags:
                key_words = json.loads(tag.key_words)
                for key in key_words:
                    if key in expense.description:
                        expense.tags.add(tag)
                        break

        self.stdout.write('Done!')
