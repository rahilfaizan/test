# Generated by Django 3.2.4 on 2021-08-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateData',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('element_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=200)),
            ],
        ),
    ]
