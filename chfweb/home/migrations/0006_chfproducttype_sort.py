# Generated by Django 2.2.1 on 2019-05-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_chfproduct_is_recommand'),
    ]

    operations = [
        migrations.AddField(
            model_name='chfproducttype',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='排序'),
        ),
    ]