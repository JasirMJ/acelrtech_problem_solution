# Generated by Django 3.1.5 on 2021-01-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtable',
            name='CategoryL1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='CategoryL2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='ParentCode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='Size',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='itemtable',
            name='UPC',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
