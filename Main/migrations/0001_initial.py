# Generated by Django 3.1.5 on 2021-01-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCode', models.CharField(max_length=20, unique=True)),
                ('CategoryL1', models.CharField(max_length=20)),
                ('CategoryL2', models.CharField(max_length=20)),
                ('UPC', models.CharField(max_length=20)),
                ('ParentCode', models.CharField(max_length=20)),
                ('MRPrice', models.FloatField()),
                ('Size', models.CharField(max_length=20)),
                ('Enabled', models.BooleanField()),
            ],
        ),
    ]