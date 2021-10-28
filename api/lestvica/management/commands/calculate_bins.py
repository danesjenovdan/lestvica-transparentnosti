import csv
import json

from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Municipality, Question, Answer, Recommendation

import numpy as np
import entropy_based_binning as ebb


class Command(BaseCommand):
    help = 'Calculates bins for index scores.'

    def handle(self, *args, **options):
        municipalities = Municipality.objects.all().order_by('id')
        indexes = municipalities[0].groups.keys()
        for index in indexes:
            print(f'Calculating {index} ...')
            D = np.array([m.groups[index]['score'] for m in municipalities])
            _, A = np.unique(D, return_inverse=True)
            A = A.reshape(D.shape)
            B = ebb.bin_sequence(A, nbins=5)

            joined = list(
                map(
                    lambda x: {
                        'municipality': municipalities[x[0]],
                        'bin': x[1]
                    },
                    enumerate(B)
                )
            )

            print(f'Calculated {index}, here it comes:')
            print(index)
            print(f'ID\tminimum\tmaximum\tmembers')
            for i in range(5):
                filtered = list(
                    filter(
                        lambda x: x['bin'] == i,
                        joined
                    )
                )
                minimum = round(min([m['municipality'].groups[index]['score'] for m in filtered]), 3)
                maximum = round(max([m['municipality'].groups[index]['score'] for m in filtered]), 3)
                number_of_members = len(filtered)

                print(f'{i} \t{minimum} \t{maximum} \t{number_of_members}')
            print('##################')
