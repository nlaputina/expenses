import csv
from csv import DictReader
from django.core.management.base import BaseCommand
from statement.models import Expenses

import re
from datetime import datetime


class Command(BaseCommand):
    help = 'Load data from csv-file'

    def add_arguments(self, parser):
        # parser.add_argument('filename', nargs='+', type=str, help='filename for csv file')
        pass

    def handle(self, *args, **options):
        with open('/Users/natalia/Natalia_projects/expenses/statement/management/commands/TransactionHistory.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            list_of_dict = list(reader)
            short_list_of_dict = []
            for position in list_of_dict:
                if position['Debit']:
                    new_dict = {'Date': position['Date'], 'Description': position['Description'],
                                'Amount': position['Debit']}
                    short_list_of_dict.append(new_dict)
                    csv_file.close()
            for position in short_list_of_dict:
                description = position['Description']
                match = re.search(r'\d{4}-\d{2}-\d{2}', description)
                if match:
                    date = datetime.strptime(match.group(), '%Y-%m-%d').date()
                    position['Date'] = '{0.year}-{0.month}-{0.day}'.format(date)
                else:
                    convert_date = datetime.strptime(position['Date'], "%d/%m/%Y").strftime('%Y-%m-%d')
                    position['Date'] = convert_date

            for position in short_list_of_dict:
                note = Expenses(date=position['Date'], description=position['Description'], amount=position['Amount'])
                note.save()

            self.stdout.write('Done!')

