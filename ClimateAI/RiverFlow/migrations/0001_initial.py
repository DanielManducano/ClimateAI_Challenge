# Generated by Django 3.1.2 on 2021-03-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prec_Zone_0', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_1', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_2', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_3', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_4', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_5', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_6', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_7', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Prec_Zone_8', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_0', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_1', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_2', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_3', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_4', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_5', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_6', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_7', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Temp_Zone_8', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Flow', models.DecimalField(decimal_places=4, max_digits=24)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]
