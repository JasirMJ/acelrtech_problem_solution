# Generated by Django 3.1.5 on 2021-01-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20210108_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='ItemName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
