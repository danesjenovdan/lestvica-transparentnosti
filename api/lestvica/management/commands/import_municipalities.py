# TODO
- vključenost pusti kot podnaslov, pobriši druge tri, tudi obveščanje je podnaslov, ne glavni naslov

import csv

from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Municipality

class Command(BaseCommand):
    help = 'Imports municipalities'

    def handle(self, *args, **options):
        # downloaded, deleted first line, added first column title VPRAŠANJE
        # changed Derstrnik to Destrnik
        # changed Kanal ob Soči to Kanal
        # deleted line containing IGNORE ME, SEM POBRISANO VPRAŠANJE
        # deleted lines containing SKUPAJ (case sensitive)
        # deleted empty lines (completely empty - commas only)
        # deleted empty lines Participativni proračun, Posvetovanja z občani, Predlogi in pripombe občanov
        with open('data/rezultati.csv', 'r') as results_file:
            # downloaded
            with open('data/proracuni.csv', 'r') as budgets_file:
                # downloaded
                # changed SELNICA to SELNICA OB DRAVI
                # changed line 53 SVETI JURIJ to SVETI JURIJ OB ŠČAVNICI
                with open('data/prebivalstvo.csv', 'r') as populations_file:
                    results = list(csv.DictReader(
                        results_file,
                        delimiter=',',
                        quotechar='"',
                    ))
                    budgets = [
                        (
                            Municipality.standardize_municipality_name(budget[0]),
                            budget[1],
                        ) for budget in csv.reader(
                            budgets_file,
                            delimiter=',',
                            quotechar='"',
                        )
                    ]
                    populations = [
                        (
                            Municipality.standardize_municipality_name(population[0]),
                            population[1],
                        ) for population in csv.reader(
                            populations_file,
                            delimiter=',',
                            quotechar='"',
                        )
                    ]

                    municipality_names = list(results[0].keys())[1:]
                    standardized_municipality_names = list(
                        map(
                            Municipality.standardize_municipality_name,
                            municipality_names
                        )
                    )
                    
                    for i, municipality_name in enumerate(municipality_names):
                        budget = float(
                            next(
                                filter(
                                    lambda x: x[0] == standardized_municipality_names[i],
                                    budgets
                                )
                            )[1].replace(',', '').strip()
                        )
                        population = int(
                            next(
                                filter(
                                    lambda x: x[0] == standardized_municipality_names[i],
                                    populations
                                )
                            )[1]
                        )
                        print(i, municipality_name, budget, population)

                        _municipality, _created = Municipality.objects.get_or_create(
                            name=municipality_name,
                            budget=budget,
                            population=population,
                        )
