# Generated by Django 2.2.1 on 2019-05-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190526_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chfapplyrecord',
            name='birthday',
            field=models.DateField(default=None, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='chfapplyrecord',
            name='sort',
            field=models.IntegerField(default=1, verbose_name='排序'),
        ),
    ]
