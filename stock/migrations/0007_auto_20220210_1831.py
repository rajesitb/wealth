# Generated by Django 3.2.12 on 2022-02-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20220210_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaction',
            name='agm_egm',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coaction',
            name='rd',
            field=models.DateField(blank=True, null=True),
        ),
    ]