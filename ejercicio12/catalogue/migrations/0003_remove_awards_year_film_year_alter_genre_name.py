# Generated by Django 4.0.6 on 2022-07-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_film_genre_alter_awards_award_remove_film_awards_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awards',
            name='year',
        ),
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Write the film genre (thriller, comedy, drama,...).', max_length=12),
        ),
    ]
