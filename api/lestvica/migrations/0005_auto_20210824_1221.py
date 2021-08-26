# Generated by Django 3.2.6 on 2021-08-24 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lestvica', '0004_alter_answer_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='original_text',
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('importance', models.IntegerField(default=0)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lestvica.municipality')),
            ],
        ),
    ]
