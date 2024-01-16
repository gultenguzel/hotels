# Generated by Django 5.0.1 on 2024-01-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_alter_hotels_discounted_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='map_link',
            field=models.TextField(default='deneme', verbose_name='Link for google maps'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='embed_link',
            field=models.TextField(verbose_name='Link for iframe tag'),
        ),
    ]