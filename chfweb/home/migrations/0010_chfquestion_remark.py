# Generated by Django 2.2.2 on 2019-07-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_chfaboutresource_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chfquestion',
            name='remark',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='备注'),
        ),
    ]