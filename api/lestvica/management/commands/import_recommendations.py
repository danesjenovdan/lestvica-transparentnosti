import csv
import json

from django.core.management.base import BaseCommand, CommandError

from lestvica.models import Municipality, Question, Answer, Recommendation


class Command(BaseCommand):
    help = 'Imports recommendations. This assumes municipalities and answers already exist.'

    def handle(self, *args, **options):
        for municipality in Municipality.objects.all():
            simple_recommendations = [
                {
                    'question': 'Ali so zapisniki / transkripti / glasovanja objavljeni v strojno berljivem formatu?',
                    'score': 1,
                    'title': 'Občina naj objavlja podatke o delu občinskega sveta v strojno berljivih formatih.',
                    'text': 'Samo strojno berljivi podatki raziskovalcem in novinarjem omogočajo poglobljeno analizo dela občine.',
                    'importance': 20,
                },
                {
                    'question': 'Ali so zapisniki / transkripti / glasovanja objavljeni v strojno berljivem formatu?',
                    'score': 0,
                    'title': 'Občina naj preneha objavljati skenirane datoteke v formatu PDF in prične objavljati podatke o delu občinskega sveta v strojno berljivih formatih.',
                    'text': 'Podatke, objavljene v skeniranih datotekah PDF, je težje najti in analizirati.',
                    'importance': 19,
                },
                {
                    'question': 'Ali so javno objavljeni kontaktni podatki članov občinskega sveta (elektronski naslov, telefonska številka ...)? ',
                    'score': 0,
                    'title': 'Občina naj objavi kontaktne podatke (vsaj elektronske naslove) občinskih svetnikov.',
                    'text': 'Občani morajo imeti možnost kontaktiranja svoje izvoljene predstavnike.',
                    'importance': 18,
                },
                {
                    'question': 'Ali je organizirana javna razprava glede predloga proračuna in ali je vabilo na javno razpravo objavljeno na spletnem mestu občine?',
                    'score': 0,
                    'title': 'Občina naj organizira javno razpravo glede predloga proračuna in objavi vabilo na na spletnem mestu občine.',
                    'text': 'Organizirana javna razprava o letnih proračunih občanom namreč omogoča informiranje in podajanje predlogov o porabi občinskih sredstev.',
                    'importance': 17,
                },
                {
                    'question': 'Ali ima občina objavljeno izjavo o dostopnosti spletnega mesta?',
                    'score': -1,
                    'title': 'Občina naj pripravi in objavi izjavo o dostopnosti spletnega mesta.',
                    'text': 'Občine z izjavo, ki so jo dolžne objaviti po zakonu, pojasnijo, katere vsebine niso dostopne osebam z oviranostmi, razloge za takšno nedostopnost, ter navedbe nadomestnih možnosti dostopa.',
                    'importance': 12,
                },
                {
                    'question': 'Ali občina izvaja participativni proračun?',
                    'score': 0,
                    'title': 'Občina naj uvede participativni proračun.',
                    'text': 'Participativni proračun je eden najbolj naprednih mehanizmov vključevanja občanov v odločanje o porabi javnih sredstev, hkrati pa bistveno dviguje nivo njihove aktivacije.',
                    'importance': 11,
                },
                {
                    'question': 'Ali obstajajo transkripti sej občinskega sveta?',
                    'score': 0,
                    'title': 'Občina naj začne objavljati celovite in natančne zapisnike sej občinskega sveta.',
                    'text': 'Le transkripti ali pa celoviti in natančni zapisniki lahko občanom omogočajo ustrezno informiranje o delu občinskega sveta ter njegovo nadziranje.',
                    'importance': 10,
                },
                {
                    'question': 'Ali se proračun sprejema z enim ali dvema branjema?',
                    'score': 0,
                    'title': 'Občina naj sprejme proračun v dveh branjih.',
                    'text': 'Sprejemanje v dveh branjih omogoča, da se občani seznanijo z vsebino predloga, slišijo kritike proračuna z vrst občinskih svetnikov, se v času med prvim in drugim branjem dodatno informirajo ter nato vključijo z lastnimi predlogi ali pripombami.',
                    'importance': 9,
                },
                {
                    'question': 'Ali se proračun sprejema v zakonskem roku?',
                    'score': 0,
                    'title': 'Občina naj začne sprejemati proračun v zakonsko določenem roku.',
                    'text': 'Za transparentnost in vključenost občanov je pomembno proračun sprejeti pred začetkom leta, saj lahko zamikanje posega v možnost občanov, da so informirani ali sodelujejo v tem procesu.',
                    'importance': 8,
                },
                {
                    'question': 'Ali obstajajo kakšni poskusi narediti proračun bolj transparenten / razumljiv občanom?',
                    'score': 0,
                    'title': 'Občina naj predstavi proračun na občanom razumljiv način.',
                    'text': 'Proračun je izjemno zahteven dokument, zato lahko poenostavljene, grafično podkrepljene ali interpretativno pojasnjene postavke močno dvignejo informiranost občanov in tako krepijo njihovo participacijo.',
                    'importance': 7,
                },
                {
                    'question': 'Ali se spustni meniji odprejo s klikom (in odklikom) oziroma ali spletno mesto nima spustnega menija?',
                    'score': 0,
                    'title': 'Občina naj z uporabo elementov, ki se aktivirajo na klik, vsakomur zagotovi enostaven dostop do navigacije.',
                    'text': 'Za odprtje spustnih menijev naj občani kliknejo in odkliknejo gumb na miški ter se ne zgolj postavijo z miško na spustni meni, kar je pomembno predvsem zaradi dostopnosti navigacije osebam z motoričnimi ali kognitivnimi ovirami.',
                    'importance': 4,
                }
            ]
            for recommendation in simple_recommendations:
                print(municipality, recommendation)
                if Answer.objects.get(
                    municipality=municipality,
                    question__text=recommendation['question']
                ).score == recommendation['score']:
                    recommendation, _created = Recommendation.objects.get_or_create(
                        municipality=municipality,
                        title=recommendation['title'],
                        text=recommendation['text'],
                        importance=recommendation['importance'],
                    )
            
            # first complex recommendation
            # If 26 < 2: 
            if Answer.objects.get(
                municipality=municipality,
                question__text='Ali je na spletnem mestu javno objavljeno, kdaj je bil kakšen dokument objavljen?'
            ).score < 2:
                recommendation, _created = Recommendation.objects.get_or_create(
                    municipality=municipality,
                    title='Občina naj spletne objave konsistentno opremi z datumom objave.',
                    text='Le na tak način lahko občina dokaže, da so bili dokumenti objavljeni v časovnem obdobju, ki ga določa zakonodaja oziroma občinski poslovnik.',
                    importance=16,
                )

            # second complex recommendation
            # If ((59 - 61) = 0) OR (64 = 0) OR (65 = 0):
            first_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali spletno mesto uporablja element H za označbo naslovov v HTML kodi?'
            )
            second_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali so nekateri teksti zakodirani v slike?'
            )
            third_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali je spletno mesto berljivo, če ga povečamo na 200 %?'
            )
            fourth_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali spletno mesto omogoča navigacijo zgolj s tipkovnico?'
            )
            if ((first_answer.score - second_answer.score) == 0) or (third_answer == 0) or (fourth_answer == 0):
                recommendation, _created = Recommendation.objects.get_or_create(
                    municipality=municipality,
                    title='Občina naj zagotovi, da je do vseh vsebin na spletnem mestu možno dostopati s tipkovnico in pomožnimi tehnologijami, vključno z lupami, bralniki zaslona in orodji za prepoznavanje govora.',
                    text='Na ta način lahko občina dostop do vsebin zagotovi tudi osebam z oviranostmi.',
                    importance=15,
                )

            # third complex recommendation
            # If (17 - 22) < 1: 
            first_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali so seje delovnih teles najavljene vnaprej na spletnem mestu občine?'
            )
            second_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali so rezultati glasovanj objavljeni poimensko za vsakega svetnika? '
            )
            if (first_answer.score - second_answer.score) < 1:
                recommendation, _created = Recommendation.objects.get_or_create(
                    municipality=municipality,
                    title='Občina naj zagotovi večjo transparentnost dela delovnih teles občinskega sveta.',
                    text='Delovna telesa so sestavni deli lokalne samouprave in pogosto močno vplivajo na odločitve, ki jih svetniki sprejemajo na sejah občinskega sveta.',
                    importance=14,
                )
            
            # fourth complex recommendation
            # If 31 < 2:
            if Answer.objects.get(
                municipality=municipality,
                question__text='Ali ima občina objavljeno prečiščeno verzijo poslovnika na svojem spletnem mestu?'
            ).score < 2:
                recommendation, _created = Recommendation.objects.get_or_create(
                    municipality=municipality,
                    title='Občina naj objavi zadnjo prečiščeno verzijo poslovnika na svojem spletnem mestu.',
                    text='Poslovniki urejajo številna področja delovanja občin in so kot taki ključen dokument, ki občanom omogoča razumevanje njihovih pravic.',
                    importance=13,
                )
            
            # fifth complex recommendation
            # If 62 - 63 = 0:
            first_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali je barvni kontrast med tekstom in ozadjem spletne strani vsaj 4,5:1?'
            )
            second_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali je barvni kontrast med povezavami in ozadjem spletne strani vsaj 3:1?'
            )
            if (first_answer.score - second_answer.score) == 0:
                recommendation, _created = Recommendation.objects.get_or_create(
                    municipality=municipality,
                    title='Občina naj olajša ogled vsebin z uporabo ustreznih barvnih kontrastov med ospredjem in ozadjem na spletnem mestu.',
                    text='Ustrezen barvni kontrast občanom omogoči, da lažje razlikujejo med različnimi deli spletnega mesta.',
                    importance=6,
                )

            # sixth complex recommendation
            # If 66 - c68 = 0:
            first_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali naslov strani opisuje njeno vsebino?'
            )
            second_answer = Answer.objects.get(
                municipality=municipality,
                question__text='Ali ima dokument poimensko jasno ime?'
            )
            if (first_answer.score - second_answer.score) < 1:
                recommendation, _created = Recommendation.objects.get_or_create(
                    municipality=municipality,
                    title='Občina naj uporablja razumljiva in jasna poimenovanja podstrani, povezav in dokumentov.',
                    text='Ustrezna poimenovanja so ključna za orientacijo in razumevanje spletnega mesta in pričakovanje informacije ali vsebine, do katere želijo občani dostopati.',
                    importance=5,
                )
