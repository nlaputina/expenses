
import re
from datetime import datetime


def parsing_csv():
    import csv

    with open('TransactionHistory.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        list_of_dict = list(reader)
        short_list_of_dict = []
        for position in list_of_dict:
            new_dict = {'Date':position['Date'], 'Description':position['Description'], 'Amount': position['Debit']}
            short_list_of_dict.append(new_dict)
        csv_file.close()
        return short_list_of_dict


parsing_csv()


def find_a_date(list_of_dict):
    for position in list_of_dict:
        description = position['Description']
        match = re.search(r'\d{4}-\d{2}-\d{2}', description)
        if match:
            date = datetime.strptime(match.group(), '%Y-%m-%d').date()
            position['Date'] = '{0.day}/{0.month}/{0.year}'.format(date)
    print(list_of_dict)

find_a_date(parsing_csv())
