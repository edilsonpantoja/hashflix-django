# Generated by Django 4.0.2 on 2022-02-09 18:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumb', models.ImageField(upload_to='thumb_movies')),
                ('description', models.TextField(max_length=1000)),
                ('category', models.CharField(choices=[('ANALYSIS', 'Analyses'), ('PROGRAMMING', 'Programming'), ('Presentation', 'Presentation'), ('OTHERS', 'Others')], max_length=15)),
                ('visualizations', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
