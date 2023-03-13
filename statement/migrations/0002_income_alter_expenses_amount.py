# Generated by Django 4.1.7 on 2023-02-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=288)),
                ('amount', models.CharField(max_length=288)),
            ],
        ),
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.CharField(max_length=288),
        ),
    ]