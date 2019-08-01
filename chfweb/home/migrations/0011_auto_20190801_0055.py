# Generated by Django 2.2.2 on 2019-07-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_chfquestion_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chfquestion',
            name='state',
            field=models.SmallIntegerField(choices=[(-1, '待解决'), (0, '未解决'), (1, '已解决'), (2, '延期处理'), (3, '不予处理'), (4, '需第三方处理')], default=-1, verbose_name='问题状态'),
        ),
        migrations.AlterField(
            model_name='chfquestion',
            name='type',
            field=models.SmallIntegerField(choices=[(-1, '不是问题'), (0, '浏览器问题'), (1, '操作系统问题'), (2, 'bug'), (3, '其他问题'), (4, '重复问题'), (5, '第三方问题')], default=-1, verbose_name='问题类型'),
        ),
    ]
