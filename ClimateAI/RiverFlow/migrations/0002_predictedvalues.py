# Generated by Django 3.1.2 on 2021-03-29 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RiverFlow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PredictedValue', models.DecimalField(decimal_places=4, max_digits=24)),
            ],
        ),
    ]