# Generated by Django 2.2.2 on 2019-06-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190615_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chfindexplate',
            name='descr',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='简介'),
        ),
    ]