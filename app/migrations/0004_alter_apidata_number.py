# Generated by Django 3.2.4 on 2021-08-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_senderdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apidata',
            name='number',
            field=models.CharField(max_length=50),
        ),
    ]
