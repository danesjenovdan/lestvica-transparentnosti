from django.db import models

class Group(models.Model):
    parent = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True)
    name = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    original_text = models.TextField(blank=False, null=False, editable=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, blank=False, null=False)
    municipality = models.ForeignKey('Municipality', on_delete=models.CASCADE, blank=False, null=False)
    score = models.FloatField(blank=False, null=False)
    text = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.municipality.name} - {self.question.text}: {self.score}'


class Recommendation(models.Model):
    municipality = models.ForeignKey('Municipality', on_delete=models.CASCADE, blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    importance = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return f'{self.municipality.name} - {self.title} - {self.importance}'


class GroupBucket(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False, default=0)
    minimum = models.FloatField(blank=False, null=False)
    maximum = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.group.name}: {self.minimum}-{self.maximum}'


class Bucket(models.Model):
    CHOICES = (
        ('population', 'population'),
        ('budget', 'budget'),
        ('score', 'score'),
    )

    category = models.TextField(blank=False, null=False, choices=CHOICES)
    order = models.IntegerField(blank=False, null=False, default=0)
    minimum = models.FloatField(blank=False, null=False)
    maximum = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.category}: {self.minimum}-{self.maximum}'


class Municipality(models.Model):
    name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    budget = models.FloatField(blank=False, null=False)
    population = models.IntegerField(blank=False, null=False)
    rank = models.IntegerField(blank=False, null=False, default=0)

    @property
    def groups(self):
        master_groups = Group.objects.filter(parent__isnull=True)

        output = {}
        for master_group in master_groups:
            score = Answer.objects.filter(
                models.Q(question__group__parent=master_group) | models.Q(question__group=master_group),
                municipality=self,
            ).aggregate(
                models.Sum('score')
            )['score__sum']

            output[master_group.name] = {
                'score': score,
                'bucket': GroupBucket.objects.get(
                    minimum__lte=score,
                    maximum__gte=score,
                    group=master_group
                ).order
            }

        return output

    @property
    def total_score(self):
        return Answer.objects.filter(
            municipality=self
        ).aggregate(
            models.Sum('score')
        )['score__sum']

    @property
    def total_bucket(self):
        score = Answer.objects.filter(
            municipality=self
        ).aggregate(
            models.Sum('score')
        )['score__sum']

        return Bucket.objects.get(
            category='score',
            minimum__lte=self.total_score,
            maximum__gte=self.total_score,
        ).order


    @property    
    def questions(self):
        # questions = Question.objects.all()
        return Answer.objects.filter(
            municipality=self,
        ).values('question__text', 'score', 'text')
    
    @property
    def bucket_peers(self):
        population_bucket = Bucket.objects.get(
            category='population',
            minimum__lte=self.population,
            maximum__gte=self.population,
        )
        population_peers = Municipality.objects.filter(
            population__gte=population_bucket.minimum,
            population__lte=population_bucket.maximum,
        )

        budget_bucket = Bucket.objects.get(
            category='budget',
            minimum__lte=self.budget,
            maximum__gte=self.budget,
        )
        budget_peers = Municipality.objects.filter(
            budget__gte=budget_bucket.minimum,
            budget__lte=budget_bucket.maximum,
        )

        score_bucket = Bucket.objects.get(
            category='score',
            minimum__lte=self.total_score,
            maximum__gte=self.total_score,
        )
        score_peers = filter(
            lambda x: x.total_score > score_bucket.minimum and x.total_score < score_bucket.maximum,
            Municipality.objects.all()
        )

        return {
            'population': [{'name': peer.name, 'id': peer.id, 'total_score': peer.total_score, 'population': peer.population} for peer in population_peers],
            'budget': [{'name': peer.name, 'id': peer.id, 'total_score': peer.total_score, 'budget': peer.budget} for peer in budget_peers],
            'score': [{'name': peer.name, 'id': peer.id, 'total_score': peer.total_score} for peer in score_peers]
        }

    @property
    def recommendations(self):
        return Recommendation.objects.filter(
            municipality=self
        ).order_by(
            '-importance'
        ).values(
            'title',
            'text',
            'importance'
        ).distinct()

    
    def __str__(self):
        return self.name

    @staticmethod
    def standardize_municipality_name(municipality_name):
        return municipality_name.lower().replace(
            ' - ',
            '-'
        ).replace(
            'mestna',
            ''
        ).replace(
            'občina',
            ''
        ).strip().split('/')[0].strip()
