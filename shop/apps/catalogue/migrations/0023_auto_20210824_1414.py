# Generated by Django 3.1.4 on 2021-08-24 13:14

from django.db import migrations
import shop.models.fields.slugfield


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0022_auto_20210210_0539"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=shop.models.fields.slugfield.SlugField(
                max_length=255, verbose_name="Slug"
            ),
        ),
    ]
