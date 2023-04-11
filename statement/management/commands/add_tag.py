import json

from django.core.management.base import BaseCommand
from statement.models import Expenses, Tag
from itertools import product


class Command(BaseCommand):
    help = 'Add tags to database'

    def add_arguments(self, parser):
        # parser.add_argument('filename', nargs='+', type=str, help='filename for csv file')
        pass

    def handle(self, *args, **options):
        expenses = Expenses.objects.all()
        tags = Tag.objects.all()
        for expense in expenses:
            for tag in tags:
                key_words = json.loads(tag.key_words)
                for key in key_words:
                    if key in expense.description:
                        tag.expenses_set.add(expense)
                        # expense.save()
                        break
                    else:
                        pass
        #
        self.stdout.write('Done!')
