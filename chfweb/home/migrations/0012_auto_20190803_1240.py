# Generated by Django 2.2.2 on 2019-08-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190801_0055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sysconfig',
            options={'verbose_name': '站点配置', 'verbose_name_plural': '站点配置'},
        ),
        migrations.AddField(
            model_name='sysconfig',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AddField(
            model_name='sysconfig',
            name='logo_bottom',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='sys/%Y/%m', verbose_name='底部logo'),
        ),
        migrations.AddField(
            model_name='sysconfig',
            name='qrcode',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='sys/%Y/%m', verbose_name='二维码'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='address',
            field=models.CharField(default='', max_length=150, verbose_name='底部显示地址'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='email',
            field=models.EmailField(default='', max_length=50, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='icp',
            field=models.CharField(default='', max_length=15, verbose_name='备案号'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='remark',
            field=models.CharField(default='', max_length=200, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='site_author',
            field=models.CharField(default='', max_length=100, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='site_company',
            field=models.CharField(default='', max_length=100, verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='site_desc',
            field=models.CharField(default='', max_length=150, verbose_name='站点描述'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='site_name',
            field=models.CharField(default='', max_length=50, verbose_name='站点名称'),
        ),
        migrations.AlterField(
            model_name='sysconfig',
            name='telephone',
            field=models.CharField(default='', max_length=11, verbose_name='底部显示电话'),
        ),
    ]