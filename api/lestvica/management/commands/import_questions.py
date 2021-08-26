import csv
import json

from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Municipality, Group, Question, Answer


class Command(BaseCommand):
    help = 'Imports questions. This assumes municipalities already exist.'

    @staticmethod
    def parse_score(score):
        try:
            return float(score)
        except ValueError:
            # sometimes it says NAPAKA - return 0
            return 0

    @staticmethod
    def get_answer_text(question_i, score, answers):
        if 'NAPAKA' in score:
            return 'Občina ni odgovorila na zastavljeno vprašanje.'
        return next(
            filter(
                lambda x: answers[question_i]['answers'][x] == Command.parse_score(score),
                answers[question_i]['answers'].keys()
            )
        )

    def handle(self, *args, **options):
        answer_file = open('data/odgovori.json', 'r')
        answers = json.load(answer_file)
        # downloaded, deleted first line, added first column title VPRAŠANJE
        # changed Derstrnik to Destrnik
        # changed Kanal ob Soči to Kanal
        # deleted line containing IGNORE ME, SEM POBRISANO VPRAŠANJE
        # deleted lines containing SKUPAJ (case sensitive)
        # deleted empty lines (completely empty - commas only)
        # deleted empty lines Participativni proračun, Posvetovanja z občani, Predlogi in pripombe občanov
        with open('data/rezultati.csv', 'r') as results_file:
            results = list(csv.DictReader(
                results_file,
                delimiter=',',
                quotechar='"',
            ))

            municipality_names = list(results[0].keys())[1:]
            standardized_municipality_names = list(
                map(
                    Municipality.standardize_municipality_name,
                    municipality_names
                )
            )

            parent_group = None
            current_group = None
            question_i = 0
            for i, line in enumerate(results):
                # check if it's a group
                if line[municipality_names[10]] == '':
                    # check if it's a master group
                    if (
                        results[i + 1][municipality_names[10]] == ''
                    ) or (
                        line['VPRAŠANJE'].strip() == 'DOSTOPNOST SPLETNEGA MESTA'
                    ) or (
                        line['VPRAŠANJE'].strip() == 'PRORAČUN'
                    ):
                        current_group, _group_created = Group.objects.get_or_create(
                            name=line['VPRAŠANJE'],
                        )
                        parent_group = current_group
                    else:
                        current_group, _group_created = Group.objects.get_or_create(
                            name=line['VPRAŠANJE'],
                            parent=parent_group
                        )
                    print('[GROUP]: ' + line['VPRAŠANJE'])
                else: # it must be a question
                    question, _question_created = Question.objects.get_or_create(
                        group=current_group,
                        text=answers[question_i]['question'], #line['VPRAŠANJE'],
                        original_text=line['VPRAŠANJE'],
                    )
                    print('[QUESTION]: ' + line['VPRAŠANJE'])

                    for municipality_name in municipality_names:
                        municipality = Municipality.objects.get(name=municipality_name)
                        _answer, _answer_created = Answer.objects.get_or_create(
                            question=question,
                            municipality=municipality,
                            score=self.parse_score(line[municipality_name]),
                            text=self.get_answer_text(question_i, line[municipality_name], answers),
                        )

                    question_i += 1
        print('\n############\n# SUCCESS! #\n############\n')
        print('Questions and answers were imported successfully!\n')
