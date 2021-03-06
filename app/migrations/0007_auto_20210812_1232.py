# Generated by Django 3.2.4 on 2021-08-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_webhook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('receiver_id', models.CharField(blank=True, max_length=50, null=True)),
                ('conversationId', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField()),
                ('number', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='messagetemplate',
            name='receiver_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='webhook',
            name='conversationId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='webhook',
            name='receiver_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='webhook',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
