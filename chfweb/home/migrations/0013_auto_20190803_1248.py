# Generated by Django 2.2.2 on 2019-08-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190803_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysconfig',
            name='telephone',
            field=models.CharField(default='', max_length=15, verbose_name='底部显示电话'),
        ),
    ]
