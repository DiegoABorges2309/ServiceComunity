# Generated by Django 5.1.3 on 2024-11-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_item', models.CharField(max_length=20)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.IntegerField()),
                ('lot', models.CharField(max_length=25)),
                ('exp', models.DateField()),
            ],
        ),
    ]
