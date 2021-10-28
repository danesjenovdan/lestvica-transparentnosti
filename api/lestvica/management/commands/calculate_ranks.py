from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Municipality

class Command(BaseCommand):
    help = 'Calculates municipalities\' ranks.'

    def handle(self, *args, **options):
        previous_score = None
        previous_rank = None
        ms = list(Municipality.objects.all())
        ms.sort(key=lambda m: m.total_score, reverse=True)
        for i, m in enumerate(ms):
            if m.total_score == previous_score:
                m.rank = previous_rank
            else:
                m.rank = i + 1
            previous_score = m.total_score
            previous_rank = m.rank

        for m in ms:
            print(f'{m.rank}\t{m.name}\t{m.total_score}')
