from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin,BaseUserManager,AbstractBaseUser
# from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
# from datetime import datetime
from django.db.models import BooleanField as _BooleanField
# import pytz


# Create your models here.
class BooleanField(_BooleanField):
    def get_prep_value(self, value):
        if value in (0, '0', 'false', 'False'):
            return False
        elif value in (1, '1', 'true', 'True'):
            return True
        else:
            return super(BooleanField, self).get_prep_value(value)

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


# AbstractBaseUser中只含有3个field: password, last_login和is_active.
# 如果你对django user model默认的first_name, last_name不满意,
# 或者只想保留默认的密码储存方式, 则可以选择这一方式.
class ChfUserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200,
                               verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ')
    phone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号')
    nick_name = models.CharField(max_length=30, verbose_name='昵称')
    # is_lock = models.BooleanField(default=False, verbose_name='是否锁定', choices=((0, '否'), (1, '是')))
    # is_enable = models.BooleanField(default=True, verbose_name='是否启用', choices=((0, '否'), (1, '是')))

    class Meta(AbstractUser.Meta):
        db_table = 'chf_userprofile'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    # class Meta:
    #     db_table = 'chf_userprofile'
    #     verbose_name = '用户'
    #     verbose_name_plural = verbose_name
    #     ordering = ['-id']

    def __str__(self):
        return self.username

    # def create_user(self, username, nickname, password=None):
    #     # create user here
    #     pass
    #
    # def create_superuser(self, username, password):
    #     # create superuser here
    #     pass


class BaseModel(models.Model):
    # default=datetime.now().replace(tzinfo=pytz.utc)
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    create_uid = models.IntegerField('创建人ID', default=123456789, auto_created=True)
    create_username = models.CharField('创建人名称', max_length=30, default='admin', auto_created=True)
    operate_time = models.DateTimeField('操作时间', auto_now=True)
    operate_uid = models.IntegerField('操作人ID', default=123456789, auto_created=True)
    operate_username = models.CharField('操作人名称', max_length=30, default='admin', auto_created=True)

    class Meta:
        abstract = True


# 系统相关
# class SysSetting(BaseModel):
#
#     class Meta:
#         db_table = 'sys_setting'
#         verbose_name = '系统相关'
#         verbose_name_plural = verbose_name


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

    class Meta:
        db_table = "sys_config"
        verbose_name = '站点配置'
        verbose_name_plural = 'SysConfig'

    def __str__(self):
        return self.site_name


# 导航菜单管理
class SysNav(BaseModel):
    code = models.CharField('标识', max_length=20, default=None)
    name = models.CharField('名称', max_length=50)
    url = models.CharField('链接', max_length=200)
    remark = models.CharField('描述', max_length=300, blank=True)
    parent = models.ForeignKey(to='self', default=0, null=True, blank=True, related_name='children',
                               verbose_name='父级', limit_choices_to={'is_delete': False, 'is_root': True},
                               on_delete=models.CASCADE)
    is_root = models.BooleanField('是否一级菜单', default=True)
    is_delete = models.BooleanField('是否删除', default=False)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = "sys_nav"
        ordering = ['sort', '-create_time']
        verbose_name = '导航菜单管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


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


# banner图管理
class ChfBanner(BaseModel):
    """
    nav:
    """
    nav = models.ForeignKey(to='SysNav', default=None, null=True, blank=True, related_name='navs',
                              related_query_name='nav_query', on_delete=models.CASCADE, verbose_name='Banner页面')
    image_url = models.ImageField('图片', default=None, null=True, blank=True, upload_to='banner/%Y/%m')
    text = models.CharField('Banner上文本描述', max_length=150, default=None)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_banner'
        ordering = ['nav', 'sort', '-create_time']
        verbose_name = 'Banner管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nav.name


# 品牌介绍图片资源
class ChfAboutResource(BaseModel):
    """
    type_code: 1 企业文化 2 品牌荣誉 3 企业资质 4 团队风采 5 品牌故事
    """
    type_code = models.PositiveSmallIntegerField('图片业务类型', default=0)
    type_name = models.CharField('图片业务类型名称', max_length=15, default=None)
    image_url = models.ImageField('图片', default=None, null=True, blank=True, upload_to='company/%Y/%m')
    about = models.ForeignKey(to='ChfAbout', default=None, null=True, blank=True, related_name='about_resource',
                              related_query_name='about', on_delete=models.CASCADE, verbose_name='品牌介绍')
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_aboutresource'
        ordering = ['sort', '-create_time']
        verbose_name = '品牌介绍图片资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


# 关于我们
# 品牌介绍
class ChfAbout(BaseModel):
    comp_name = models.CharField('公司名称', max_length=100)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text='根据name生成的，用于生成页面URL，必须唯一')
    title = models.CharField('公司简介标题', max_length=100)
    content = models.TextField('公司简介', default=None, null=True, blank=True)
    comp_image = models.ImageField('公司简介图片', max_length=255, null=True, blank=True, upload_to='company/%Y/%m')
    # culture = models.ForeignKey(to='ChfAboutResource', related_name='culture_resource', to_field='type_code',
    #                             default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='企业文化')
    # honor = models.ForeignKey(to='ChfAboutResource', related_name='honor_resource', to_field='type_code',
    #                           default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='品牌荣誉')
    # aptitude = models.ForeignKey(to='ChfAboutResource', related_name='aptitude_resource', to_field='type_code',
    #                              default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='企业资质')
    # team = models.ForeignKey(to='ChfAboutResource', related_name='team_resource', to_field='type_code',
    #                          default=None, null=True, blank=True, on_delete=models.CASCADE, verbose_name='团队风采')
    # brand_story = models.ForeignKey(to='ChfAboutResource', related_name='brand_story_resource', to_field='type_code',
    #                                 default=None, null=True, blank=True, on_delete=models.CASCADE,
    #                                 verbose_name='品牌故事')
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_about'
        verbose_name = '品牌介绍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comp_name

    def get_absolute_url(self):
        return reverse('about', args=(self.slug, ))

    def profile(self):
        if len(str(self.content)) > 40:
            return '{}...'.format(str(self.content)[0:40])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = u'公司简介'


# 动画类型
class ChfAnimateType(BaseModel):
    name = models.CharField('动画名称', max_length=30, default=None)
    class_name = models.CharField('class样式名', max_length=50, default='flip')
    descr = models.CharField('动画描述', max_length=100, default=None, null=True, blank=True)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_animatetype'
        ordering = ['-create_time']
        verbose_name = '动画类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def profile(self):
        if len(str(self.descr)) > 50:
            return '{}...'.format(str(self.descr)[0:50])
        else:
            return str(self.descr)

    profile.allow_tags = True
    profile.short_description = u'动画描述'


# 首页板块管理
class ChfIndexPlate(BaseModel):
    title = models.CharField('板块标题', max_length=8, default=None)
    plate_image_url = models.ImageField('图标', max_length=255, null=True, blank=True, upload_to='index_plate/%Y/%m')
    front_image = models.ImageField('正面图', max_length=255, null=True, blank=True, upload_to='index_plate/%Y/%m')
    back_image = models.ImageField('背面图', max_length=255, null=True, blank=True, upload_to='index_plate/%Y/%m')
    descr = models.CharField('简介', max_length=100, default=None, null=True, blank=True)
    is_redirect_sub_page = models.BooleanField('是否跳转到子页面', default=True)
    sub_page_url = models.CharField('子页面地址', max_length=150, default=None, null=True, blank=True)
    video_source = models.FileField('视频文件地址', max_length=200, default=None, null=True, blank=True, upload_to='media/%Y/%m')
    animate_type = models.ForeignKey(to='ChfAnimateType', null=True, blank=True, on_delete=models.CASCADE, verbose_name='动画类型')
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_indexplate'
        ordering = ['sort', '-create_time']
        verbose_name = '首页板块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def profile(self):
        if len(str(self.descr)) > 20:
            return '{}...'.format(str(self.descr)[0:20])
        else:
            return str(self.descr)

    profile.allow_tags = True
    profile.short_description = u'简介'


# class ChfUserProfileBase(AbstractBaseUser):
#     identifier = models.CharField(max_length=50, unique=True)
#     nickname = models.CharField(max_length=10, unique=True)
#     data_of_birth = models.DateField()
#     height = models.FloatField()
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'identifier'
#     REQUIRED_FIELDS = ['date_of_birth', 'height']
#
#     def get_full_name(self):
#         return self.identifier
#
#     def get_short_name(self):
#         return self.nickname


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

    def profile(self):
        if len(str(self.content)) > 20:
            return '{}...'.format(str(self.content)[0:20])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = u'描述'


# 产品类型
class ChfProductType(BaseModel):
    name = models.CharField('类型名称', max_length=30)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)
    data_filter_name = models.CharField('数据类型标识', max_length=20, default='*')

    class Meta:
        db_table = 'chf_producttype'
        ordering = ['sort', '-create_time']
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
    brief = models.CharField('产品摘要', max_length=40)
    content = models.TextField('产品描述', default=None, null=True, blank=True)
    mall_url = models.URLField('在线商城地址', default=None, null=True, blank=True)
    cover_image_url = models.ImageField('图片', max_length=255, null=True, blank=True, upload_to='product/%Y/%m')
    read_count = models.IntegerField('浏览量', default=0)
    product_type = models.ForeignKey(to='ChfProductType', null=True, blank=True, on_delete=models.CASCADE, verbose_name='产品类型')
    sort = models.IntegerField('排序', default=0)
    is_recommand = models.BooleanField('是否推荐', default=True)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_product'
        ordering = ['sort', '-create_time']
        verbose_name = '品牌产品'
        # verbose_name_plural = 'ChfProducts'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        # return reverse('product', args=(self.slug, ))
        self.slug = slugify(self.name)
        super(ChfProduct, self).get_absolute_url(*args, **kwargs)

    def brief_profile(self):
        if len(str(self.brief)) > 10:
            return '{}...'.format(str(self.brief)[0:10])
        else:
            return str(self.brief)

    brief_profile.allow_tags = True
    brief_profile.short_description = u'产品简介'

    def profile(self):
        if len(str(self.content)) > 40:
            return '{}...'.format(str(self.content)[0:40])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = u'产品描述'


# 合作伙伴
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
        verbose_name = '合作伙伴'
        # verbose_name_plural = 'ChfPartners'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def profile(self):
        if len(str(self.brief)) > 20:
            return '{}...'.format(str(self.brief)[0:20])
        else:
            return str(self.brief)

    profile.allow_tags = True
    profile.short_description = u'简介'


# 合作共赢 品牌合作
class ChfCooperation(BaseModel):
    title = models.CharField('名称', max_length=100)
    content = models.TextField('内容', default=None, null=True, blank=True)
    type = models.CharField('类型', max_length=10, choices=(('0', '合作政策'), ('1', '项目优势'), ('2', '经销商问答'),
                                                          ('3', '支持与服务')), default=0)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_cooperation'
        ordering = ['sort', '-create_time']
        verbose_name = '合作共赢'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def profile(self):
        if len(str(self.content)) > 30:
            return '{}...'.format(str(self.content)[0:30])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = u'内容'


# # 合作共赢 品牌合作-合作政策
# class ChfCooperationPolicy(BaseModel):
#     title = models.CharField('名称', max_length=100)
#     content = models.TextField('内容', default=None, null=True, blank=True)
#     is_enable = models.BooleanField('是否启用', default=True)
#
#     class Meta:
#         db_table = 'chf_cooperationpolicy'
#         ordering = ['-create_time']
#         verbose_name = '合作政策'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.title
#
#     def profile(self):
#         if len(str(self.content)) > 30:
#             return '{}...'.format(str(self.content)[0:30])
#         else:
#             return str(self.content)
#
#     profile.allow_tags = True
#     profile.short_description = u'内容'
#
#
# # 合作共赢 品牌合作-项目优势
# class ChfCooperationSuperiority(BaseModel):
#     title = models.CharField('名称', max_length=100)
#     content = models.TextField('内容', default=None, null=True, blank=True)
#     is_enable = models.BooleanField('是否启用', default=True)
#
#     class Meta:
#         db_table = 'chf_cooperationsuperiority'
#         ordering = ['-create_time']
#         verbose_name = '项目优势'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.title
#
#     def profile(self):
#         if len(str(self.content)) > 30:
#             return '{}...'.format(str(self.content)[0:30])
#         else:
#             return str(self.content)
#
#     profile.allow_tags = True
#     profile.short_description = u'内容'
#
#
# # 合作共赢 品牌合作-经销商问答
# class ChfCooperationQuestion(BaseModel):
#     title = models.CharField('名称', max_length=100)
#     content = models.TextField('内容', default=None, null=True, blank=True)
#     is_enable = models.BooleanField('是否启用', default=True)
#
#     class Meta:
#         db_table = 'chf_cooperationquestion'
#         ordering = ['-create_time']
#         verbose_name = '经销商问答'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.title
#
#     def profile(self):
#         if len(str(self.content)) > 30:
#             return '{}...'.format(str(self.content)[0:30])
#         else:
#             return str(self.content)
#
#     profile.allow_tags = True
#     profile.short_description = u'内容'


# 社会责任
# 新闻资讯
class ChfNews(BaseModel):
    title = models.CharField('标题', max_length=64)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text='根据title生成的，用于生成页面URL，必须唯一')
    brief = models.CharField('摘要', max_length=120)
    content = models.TextField('内容', default=None, null=True, blank=True)
    read_count = models.IntegerField('浏览量', default=0)
    cover_image_url = models.ImageField('图片', max_length=255, null=True, blank=True, upload_to='news/%Y/%m')
    sort = models.IntegerField('排序', default=0)
    type = models.CharField('类型', max_length=10, choices=(('0', '新闻资讯'), ('1', '社会责任')), default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_news'
        ordering = ['sort', '-create_time']
        verbose_name = '新闻资讯|社会责任'
        # verbose_name_plural = 'ChfProducts'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news', args=(self.slug, ))

    def get_absolute_url(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ChfNews, self).get_absolute_url(*args, **kwargs)

    def profile(self):
        if len(str(self.content)) > 20:
            return '{}...'.format(str(self.content)[0:20])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = u'内容'


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
                                 ), default=0)
    # job_require = models.TextField('岗位要求', default=None, null=True, blank=True)
    # skill_require = models.TextField('技能要求', default=None, null=True, blank=True)
    content = models.TextField('招聘要求', default=None, null=True, blank=True)
    sort = models.IntegerField('排序', default=0)
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_jobrecruit'
        ordering = ['sort', '-create_time']
        verbose_name = '工作机会'
        # verbose_name_plural = 'ChfJobRecruits'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.job_name

    # def get_absolute_url(self):
    #     return reverse('jobrecruit', args=(self.slug, ))

    def get_absolute_url(self, *args, **kwargs):
        self.slug = slugify(self.job_name)
        super(ChfJobRecruit, self).get_absolute_url(*args, **kwargs)

    def profile(self):
        if len(str(self.content)) > 80:
            return '{}...'.format(str(self.content)[0:80])
        else:
            return str(self.content)

    # 如何将一个TextField字段设为safe
    profile.allow_tags = True
    profile.short_description = u'招聘要求'


# 用户抢购优惠券表
class ChfApplyRecord(BaseModel):
    name = models.CharField('姓名', max_length=100)
    sex = models.CharField('性别', max_length=5,
                           choices=(
                               ('0', '男'),
                               ('1', '女'),
                               ('2', '保密'),
                               ('3', '未知'),
                           ), default=0)
    birthday = models.DateField('生日', default=None, null=None, blank=None)
    phone = models.CharField('电话', max_length=11)
    email = models.EmailField('邮箱', max_length=50)
    is_get = models.BooleanField('是否已领取', default=False)
    is_inform = models.BooleanField('是否已通知', default=False)
    state = models.SmallIntegerField('是否中奖', default=0,
                                     choices=(
                                         (0, '未中奖'),
                                         (1, '中奖'),
                                     ))
    sort = models.IntegerField('排序', default=1)
    
    class Meta:
        db_table = "chf_applyrecord"
        ordering = ['sort', '-create_time']
        verbose_name = '用户抢券记录'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name


# 用户浇水记录
class ChfUserWateringRecord(BaseModel):
    client_ip = models.GenericIPAddressField('客户端IP', default='127.0.0.1', protocol='both')
    client_host = models.CharField('客户端主机名', default=None, max_length=100)
    client_port = models.IntegerField('客户端端口', default=0)
    client_user_agent = models.CharField('客户端浏览器', default=None, max_length=255)
    server_ip = models.GenericIPAddressField('服务器IP', default='127.0.0.1', protocol='both')
    server_host = models.CharField('服务器主机名', default=None, max_length=100)
    server_port = models.IntegerField('服务器端口', default=0)
    init_amount = models.IntegerField('期初水量', default=0)
    amount = models.IntegerField('本次水量', default=0)
    final_amount = models.IntegerField('期末水量', default=0)

    class Meta:
        db_table = "chf_userwateringrecord"
        ordering = ['-create_time']
        verbose_name = '用户浇水记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.client_ip

    def profile(self):
        if len(str(self.client_user_agent)) > 60:
            return '{}...'.format(str(self.client_user_agent)[0:60])
        else:
            return str(self.client_user_agent)

    profile.allow_tags = True
    profile.short_description = u'客户端浏览器'


# 浇水量余额表
class ChfWateringQty(BaseModel):
    amount = models.IntegerField('水量余额', default=0)
    total_amount = models.IntegerField('浇水总量', default=0)

    class Meta:
        db_table = "chf_wateringqty"
        ordering = ['-create_time']
        verbose_name = '浇水量余额表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.amount)


# 申请模板表
class ChfTableTemplate(BaseModel):
    name = models.CharField('名称', max_length=30, default=None)
    file = models.FileField('文件', max_length=255, upload_to='file/%Y/%m')
    is_enable = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'chf_tabletemplate'
        ordering = ['-create_time']
        verbose_name = '申请表格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def profile(self):
        if len(str(self.file)) > 20:
            return '{}...'.format(str(self.file)[0:20])
        else:
            return str(self.file)

    profile.allow_tags = True
    profile.short_description = u'文件'


# 问题汇总列表
class ChfQuestion(BaseModel):
    name = models.CharField('问题标题', max_length=200)
    content = models.TextField('问题描述',  default=None, null=True, blank=True)
    type = models.SmallIntegerField('问题类型', default=-1,
                                    choices=(
                                         (-1, '不是问题'),
                                         (0, '浏览器问题'),
                                         (1, '操作系统问题'),
                                         (2, '真bug'),
                                         (3, '其他问题'),
                                    ))
    state = models.SmallIntegerField('问题状态', default=-1,
                                     choices=(
                                         (-1, '待解决'),
                                         (0, '未解决'),
                                         (1, '已解决'),
                                         (2, '延期处理'),
                                     ))

    class Meta:
        db_table = "chf_question"
        ordering = ['-create_time']
        verbose_name = '问题汇总列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    def profile(self):
        if len(str(self.content)) > 60:
            return '{}...'.format(str(self.content)[0:60])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = u'问题描述'


