from django.db import models
from django.urls import reverse
from django.utils.timezone import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin,BaseUserManager,AbstractBaseUser
from django.core.validators import RegexValidator

# Create your models here.
class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    create_uid= models.IntegerField('创建人ID', default=123456789, auto_created=True)
    create_username = models.CharField('创建人名称', max_length=30, default='admin', auto_created=True)
    operate_time = models.DateTimeField('操作时间', auto_now_add=True)
    operate_uid = models.IntegerField('操作人ID', default=123456789, auto_created=True)
    operate_username = models.CharField('操作人名称', max_length=30, default='admin', auto_created=True)

    class Meta:
        abstract = True

# 系统|站点配置
class SysConfig(BaseModel):
    site_name = models.CharField('站点名称', max_length=50)
    site_desc = models.CharField('站点描述', max_length=150)
    site_author = models.CharField('作者', max_length=100)
    site_company = models.CharField('公司', max_length=100)
    address = models.CharField('底部显示地址', max_length=150)
    telephone = models.CharField('底部显示电话', max_length=11)
    email = models.EmailField('邮箱', max_length=50)
    icp = models.CharField('备案号', max_length=15)
    remark = models.CharField('备注', max_length=200)

    def __str__(self):
        db_table = "sys_config"
        verbose_name = '站点配置'
        verbose_name_plural = 'SysConfig'

    def __str__(self):
        return self.site_name

# # 广告位
# class SysAdPosition(BaseModel):
#     name = models.CharField('广告位名称', max_length=50)
#     target_type = models.CharField('广告位类型', max_length=20)
#     width = models.IntegerField("广告位宽度", default=0)
#     is_enable = models.BooleanField('是否启用', default=True)
#
#     class Meta:
#         db_table = "sys_adposition"
#         ordering = ['-create_time']
#         verbose_name = '广告位'
#         verbose_name_plural = 'SysAdPositions'
#
#     def __str__(self):
#         return self.name
#
# # 广告记录
# class SysAdRecord(BaseModel):
#     name = models.CharField('广告名称', max_length=30)
#     slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
#                             help_text='根据name生成的，用于生成页面URL，必须唯一')
#     path = models.CharField('广告图片路径', max_length=200)
#     image = models.ImageField('广告图片', max_length=255, null=True, blank=True, upload_to='ad/%Y/%m')
#     is_enable = models.BooleanField('是否启用', default=True)
#     sort = models.IntegerField('排序', default=0)
#     adposition = models.ForeignKey(to='SysAdPosition', to_field='id')
#
#     class Meta:
#         db_table = 'sys_adrecord'
#         ordering = ['sort', '-create_time']
#         verbose_name = '广告记录'
#         verbose_name_plural = 'SysAdRecords'
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('sys_adrecord', args=(self.slug, ))

# 关于我们
# 联系我们
# class ChfAbout(BaseModel):
#     comp_name = models.CharField('公司名称', max_length=100)
#     slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
#                             help_text='根据name生成的，用于生成页面URL，必须唯一')
#     descr = models.TextField('公司简介', default=None, null=True, blank=True)
#     comp_culture = models.TextField('公司文化', default=None, null=True, blank=True)
#     org_structure = models.ImageField('图片', max_length=255, null=True, blank=True, upload_to='company/%Y/%m')
#     comp_honor = models.TextField('证书荣誉', default=None, null=True, blank=True)
#     is_enable = models.BooleanField('是否启用', default=True)
#
#     class Meta:
#         db_table = 'chf_about'
#         verbose_name = '关于我们'
#         verbose_name_plural = 'ChfAbouts'
#
#     def __str__(self):
#         return self.comp_name
#
#     def get_absolute_url(self):
#         return reverse('about', args=(self.slug, ))

# 用户,继承方式扩展

# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         if not username:
#             raise ValueError('Users must hanve a username')
#
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email)
#         )
#         user.is_active = True
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None):
#         user = self.create_user(username=username, email=email, password=password)
#
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
#     username = models.CharField('用户名', unique=True, max_length=30, validators=[alphanumeric])
#     email = models.EmailField('邮箱', unique=True, max_length=200)
#     first_name = models.CharField(max_length=30, null=True, blank=True)
#     last_name = models.CharField(max_length=50, null=True, blank=True)
#     is_active = models.BooleanField(default=True, null=False)
#     is_staff = models.BooleanField(default=False, null=False)
#
#     avatar = models.ImageField(upload_to='avatar/%Y.%m', default='avatar/default.png', max_length=200, blank=False,
#                                null=False)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     class Meta:
#         verbose_name = '用户信息'
#         verbose_name_plural = verbose_name
#         ordering = ['-id']
#
#     def get_full_name(self):
#         self.fullname = self.first_name + " " + self.last_name
#         return self.fullname
#
#     def get_short_name(self):
#         return self.username
#
#     def __str__(self):
#         return self.email


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200,
                               verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ')
    phone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号')
    nick_name = models.CharField(max_length=30, verbose_name='昵称')
    is_lock = models.BooleanField(default=False, verbose_name='是否锁定')
    is_enable = models.BooleanField(default=True, verbose_name='是否启用')

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     verbose_name = '用户'
    #     verbose_name_plural = verbose_name
    #     ordering = ['-id']

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

# 公司发展历程
class ChfCompanyHistory(BaseModel):
    timeline_title = models.CharField('时间标题', max_length=20, default=None, unique=True, null=True, blank=True)
    title = models.CharField('标题', max_length=100)
    breif = models.CharField('摘要', max_length=50, default=None, null=True, blank=True)
    content = models.TextField('描述', default=None, null=True, blank=True)
    cover_image_url = models.ImageField('图片', max_length=255, null=True, blank=True, upload_to='company/%Y/%m')
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_companyhistory'
        ordering = ['sort', '-create_time']
        verbose_name = '发展历程'
        verbose_name_plural = verbose_name  # 后台管理站点显示的Model名称
        # verbose_name_plural = 'ChfCompanyHistories'

    def __str__(self):
        return self.title

# 产品类型
class ChfProductType(BaseModel):
    name = models.CharField('类型名称', max_length=30)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_producttype'
        ordering = ['-create_time']
        verbose_name = '产品类型'
        # verbose_name_plural = 'ChfProductTypes'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 品牌产品
class ChfProduct(BaseModel):
    name = models.CharField('产品名称', max_length=100)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text='根据name生成的，用于生成页面URL，必须唯一')
    brief = models.CharField('产品摘要', max_length=50)
    content = models.TextField('产品描述', default=None, null=True, blank=True)
    cover_image_url = models.ImageField('图片', max_length=255, null=True, blank=True, upload_to='product/%Y/%m')
    read_count = models.IntegerField('浏览量', default=0)
    product_type = models.ForeignKey(to='ChfProductType', null=True, blank=True, on_delete=models.CASCADE, verbose_name='产品类型')
    sort = models.IntegerField('排序', default=0)
    is_recommand =  models.BooleanField('是否推荐', default=True)

    class Meta:
        db_table = 'chf_product'
        ordering = ['sort', '-create_time']
        verbose_name = '品牌产品'
        # verbose_name_plural = 'ChfProducts'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product', args=(self.slug, ))



# 品牌合作
class ChfPartner(BaseModel):
    name = models.CharField('名称', max_length=100)
    logo = models.ImageField('Logo', max_length=255, null=True, blank=True, upload_to='partner/%Y/%m')
    brief = models.CharField('简介', max_length=100)
    url = models.URLField('链接', max_length=255, null=True, blank=True)
    address = models.CharField('地址', max_length=100)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_partner'
        ordering = ['sort', '-create_time']
        verbose_name = '品牌合作'
        # verbose_name_plural = 'ChfPartners'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 社会责任
# 新闻资讯
class ChfNews(BaseModel):
    title = models.CharField('标题', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text='根据title生成的，用于生成页面URL，必须唯一')
    brief = models.CharField('摘要', max_length=50)
    content = models.TextField('内容', default=None, null=True, blank=True)
    read_count = models.IntegerField('浏览量', default=0)
    cover_image_url = models.ImageField('图片', max_length=255, null=True, blank=True, upload_to='news/%Y/%m')
    sort = models.IntegerField('排序', default=0)
    type = models.CharField('类型', max_length=10, choices=(('0', '新闻资讯'), ('1', '社会责任')), default=0)

    class Meta:
        db_table = 'chf_news'
        ordering = ['sort', '-create_time']
        verbose_name = '新闻资讯|社会责任'
        # verbose_name_plural = 'ChfProducts'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', args=(self.slug, ))

# 工作机会
class ChfJobRecruit(BaseModel):
    job_name = models.CharField('职位名称', max_length=50)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text='根据job_name生成的，用于生成页面URL，必须唯一')
    work_year = models.CharField('工作经验', max_length=20, default=None, null=True, blank=True)
    education = models.CharField('学历', max_length=10, choices=(
                                                ('0', '请选择'),
                                                ('1', '博士导师'),
                                                ('2', '博士后'),
                                                ('3', '博士'),
                                                ('4', '硕士'),
                                                ('5', '研究生'),
                                                ('6', '本科'),
                                                ('7', '大专'),
                                                ('8', '高中'),
                                                ('9', '初中'),
                                                ('10', '小学'),
                                                ('11', '其他'),
                                                ),
                                 default=0
                                 )
    work_prop = models.CharField('工作性质', max_length=5,
                                 choices=(
                                     ('0', '全职'),
                                     ('1', '兼职'),
                                     ('2', '自由职业'),
                                     ('3', '其他'),
                                 ),default=0
                                 )
    job_require = models.TextField('岗位要求', default=None, null=True, blank=True)
    skill_require = models.TextField('技能要求', default=None, null=True, blank=True)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_jobrecruit'
        ordering = ['sort', '-create_time']
        verbose_name = '工作机会'
        # verbose_name_plural = 'ChfJobRecruits'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobrecruit', args=(self.slug, ))

