# Generated by Django 3.2.17 on 2023-02-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20200801_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productalert',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
