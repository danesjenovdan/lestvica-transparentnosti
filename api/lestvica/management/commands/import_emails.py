import csv

from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Municipality

class Command(BaseCommand):
    help = 'Imports municipalities\' emails.'

    def handle(self, *args, **options):
        with open('data/pp.csv', 'r') as pp_file:
            pp_municipalities = list(csv.DictReader(
                pp_file,
                delimiter=',',
                quotechar='"'
            ))
            for municipality in Municipality.objects.all():
                email = next(
                    m for m in pp_municipalities
                    if Municipality.standardize_municipality_name(
                        m['OBČINA'].replace('SLOV.', 'SLOVENSKIH').lower().replace(' ', '').replace('SLOV.', 'SLOVENSKIH')
                    ) == municipality.name.lower().replace(' ', '')
                    # the removal of spaces is a hack because of inconsistent
                    # use of "-"
                )['MAIL']
                
                municipality.email = email
                municipality.save()
