# Generated by Django 2.2.1 on 2019-06-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190603_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chfindexplate',
            name='video_source',
            field=models.FileField(blank=True, default=None, max_length=200, null=True, upload_to='media/%Y/%m', verbose_name='视频文件地址'),
        ),
    ]