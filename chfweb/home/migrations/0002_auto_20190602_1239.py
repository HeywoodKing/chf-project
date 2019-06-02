# Generated by Django 2.2.1 on 2019-06-02 04:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chfapplyrecord',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfapplyrecord',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfcompanyhistory',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfcompanyhistory',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfjobrecruit',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfjobrecruit',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfnews',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfnews',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfpartner',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfpartner',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfproduct',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfproduct',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfproducttype',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfproducttype',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfuserwateringrecord',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfuserwateringrecord',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='chfwateringqty',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='chfwateringqty',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='operate_time',
            field=models.DateTimeField(auto_now=True, verbose_name='操作时间'),
        ),
    ]
