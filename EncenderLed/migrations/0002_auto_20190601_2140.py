# Generated by Django 2.1.5 on 2019-06-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EncenderLed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iluminacion',
            name='led',
            field=models.IntegerField(default=0),
        ),
    ]