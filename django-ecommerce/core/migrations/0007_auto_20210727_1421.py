# Generated by Django 2.2.14 on 2021-07-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210727_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
