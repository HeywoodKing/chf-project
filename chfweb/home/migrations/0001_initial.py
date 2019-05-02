# Generated by Django 2.2.1 on 2019-05-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChfAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_uid', models.IntegerField(default=123456789, verbose_name='创建人ID')),
                ('create_username', models.CharField(default='admin', max_length=30, verbose_name='创建人名称')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('operate_uid', models.IntegerField(default=123456789, verbose_name='操作人ID')),
                ('operate_username', models.CharField(default='admin', max_length=30, verbose_name='操作人名称')),
                ('comp_name', models.CharField(max_length=100, verbose_name='公司名称')),
                ('slug', models.SlugField(blank=True, help_text='根据name生成的，用于生成页面URL，必须唯一', max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('descr', models.TextField(blank=True, default=None, null=True, verbose_name='公司简介')),
                ('comp_culture', models.TextField(blank=True, default=None, null=True, verbose_name='公司文化')),
                ('org_structure', models.ImageField(blank=True, max_length=255, null=True, upload_to='company/%Y/%m', verbose_name='图片')),
                ('comp_honor', models.TextField(blank=True, default=None, null=True, verbose_name='证书荣誉')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': 'ChfAbouts',
                'db_table': 'chf_about',
            },
        ),
        migrations.CreateModel(
            name='ChfCompHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_uid', models.IntegerField(default=123456789, verbose_name='创建人ID')),
                ('create_username', models.CharField(default='admin', max_length=30, verbose_name='创建人名称')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('operate_uid', models.IntegerField(default=123456789, verbose_name='操作人ID')),
                ('operate_username', models.CharField(default='admin', max_length=30, verbose_name='操作人名称')),
                ('timeline_title', models.CharField(blank=True, default=None, max_length=20, null=True, unique=True, verbose_name='时间标题')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('breif', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='摘要')),
                ('content', models.TextField(blank=True, default=None, null=True, verbose_name='描述')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='company/%Y/%m', verbose_name='图片')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '发展历程',
                'verbose_name_plural': 'ChfCompHistories',
                'db_table': 'chf_comphistory',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ChfJobRecruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_uid', models.IntegerField(default=123456789, verbose_name='创建人ID')),
                ('create_username', models.CharField(default='admin', max_length=30, verbose_name='创建人名称')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('operate_uid', models.IntegerField(default=123456789, verbose_name='操作人ID')),
                ('operate_username', models.CharField(default='admin', max_length=30, verbose_name='操作人名称')),
                ('job_name', models.CharField(max_length=50, verbose_name='职位名称')),
                ('slug', models.SlugField(blank=True, help_text='根据job_name生成的，用于生成页面URL，必须唯一', max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('work_year', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='工作经验')),
                ('education', models.CharField(choices=[('0', '未知'), ('1', '博士导师'), ('2', '博士后'), ('3', '博士'), ('4', '硕士'), ('5', '研究生'), ('6', '本科'), ('7', '大专'), ('8', '高中'), ('9', '初中'), ('10', '小学'), ('11', '其他')], default=0, max_length=10, verbose_name='学历')),
                ('work_prop', models.CharField(choices=[('0', '全职'), ('1', '兼职'), ('2', '自由职业'), ('3', '其他')], default=0, max_length=5, verbose_name='工作性质')),
                ('job_require', models.TextField(blank=True, default=None, null=True, verbose_name='岗位要求')),
                ('skill_require', models.TextField(blank=True, default=None, null=True, verbose_name='技能要求')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '工作机会',
                'verbose_name_plural': 'ChfJobRecruits',
                'db_table': 'chf_jobrecruit',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ChfNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_uid', models.IntegerField(default=123456789, verbose_name='创建人ID')),
                ('create_username', models.CharField(default='admin', max_length=30, verbose_name='创建人名称')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('operate_uid', models.IntegerField(default=123456789, verbose_name='操作人ID')),
                ('operate_username', models.CharField(default='admin', max_length=30, verbose_name='操作人名称')),
                ('title', models.CharField(max_length=255, verbose_name='新闻标题')),
                ('slug', models.SlugField(blank=True, help_text='根据title生成的，用于生成页面URL，必须唯一', max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('brief', models.CharField(max_length=50, verbose_name='新闻摘要')),
                ('content', models.TextField(blank=True, default=None, null=True, verbose_name='新闻内容')),
                ('read_count', models.IntegerField(default=0, verbose_name='浏览量')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='news/%Y/%m', verbose_name='新闻图片')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '新闻资讯',
                'verbose_name_plural': 'ChfProducts',
                'db_table': 'chf_news',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ChfProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_uid', models.IntegerField(default=123456789, verbose_name='创建人ID')),
                ('create_username', models.CharField(default='admin', max_length=30, verbose_name='创建人名称')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('operate_uid', models.IntegerField(default=123456789, verbose_name='操作人ID')),
                ('operate_username', models.CharField(default='admin', max_length=30, verbose_name='操作人名称')),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('slug', models.SlugField(blank=True, help_text='根据name生成的，用于生成页面URL，必须唯一', max_length=255, null=True, unique=True, verbose_name='Slug')),
                ('brief', models.CharField(max_length=50, verbose_name='新闻摘要')),
                ('descr', models.TextField(blank=True, default=None, null=True, verbose_name='产品描述')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='product/%Y/%m', verbose_name='图片')),
                ('read_count', models.IntegerField(default=0, verbose_name='浏览量')),
                ('type_code', models.SmallIntegerField(default=0, verbose_name='产品类型')),
                ('type_name', models.CharField(max_length=30, verbose_name='产品类型名称')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '品牌产品',
                'verbose_name_plural': 'ChfProducts',
                'db_table': 'chf_product',
                'ordering': ['sort', '-create_time'],
            },
        ),
    ]
