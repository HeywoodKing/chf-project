# Generated by Django 2.2.1 on 2019-05-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190505_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='chfproduct',
            name='is_recommand',
            field=models.BooleanField(default=True, verbose_name='是否推荐'),
        ),
    ]
