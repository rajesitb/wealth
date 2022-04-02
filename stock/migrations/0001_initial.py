# Generated by Django 3.2.12 on 2022-02-06 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_number', models.CharField(blank=True, max_length=150, null=True)),
                ('stock_name', models.CharField(blank=True, max_length=150, null=True)),
                ('action_type', models.CharField(blank=True, max_length=150, null=True)),
                ('action_date', models.DateField(blank=True, null=True)),
                ('company_event', models.CharField(blank=True, max_length=150, null=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('recommendation', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_number', models.CharField(blank=True, max_length=150, null=True)),
                ('stock_record', models.TextField()),
                ('record_date', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.coaction')),
            ],
        ),
    ]
