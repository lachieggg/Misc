# Generated by Django 4.0.5 on 2022-06-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_link_shortened'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='usages',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
