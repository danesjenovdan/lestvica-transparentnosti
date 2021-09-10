import csv
import json

from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Question

import json


class Command(BaseCommand):
    help = 'Adds max_score to questions.'

    def handle(self, *args, **options):
        with open('data/odgovori.json', 'r') as infile:
            answers = json.load(infile)
            for answer in answers:
                question = Question.objects.get(text=answer['question'])
                question.max_score = max(answer['answers'].values())
                question.save()
