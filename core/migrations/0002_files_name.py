# Generated by Django 4.2.6 on 2025-02-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='name',
            field=models.CharField(blank=True, max_length=1025, null=True, verbose_name='Name'),
        ),
    ]
