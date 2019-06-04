from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home import models

# Register your models here.
admin.site.site_header = '春和方 | 秦食皇 后台管理系统'
admin.site.site_title = '后台管理系统'


@admin.register(models.ChfUserProfile)
class ChfUserProfileAdmin(UserAdmin):
    list_display = ('username', 'password', 'email', 'nick_name', 'qq', 'phone', 'is_lock', 'is_enable')
    list_display_links = ('username', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfProduct)
class ChfProductAdmin(admin.ModelAdmin):
    # fields = ()
    # inlines = ()
    list_display = ('name', 'slug', 'brief', 'cover_image_url', 'read_count', 'product_type', 'sort', 'is_recommand', 'is_enable')
    list_display_links = ('name', )
    list_editable = ('sort', 'is_recommand', 'is_enable', 'product_type')
    list_filter = ('product_type', 'is_recommand', 'is_enable')
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username', )
    # fieldsets = (
    #     ('基本设置', {
    #         'fields': ('name', 'brief', 'product_type', )
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse', ),
    #         'fields': ('read_count', 'content', 'cover_image_url', 'sort', 'is_recommand')
    #     }),
    # )
    # list_max_show_all =
    # list_per_page =
    # list_select_related =
    # change_list_template =
    # sortable_by =
    search_fields = ('name', 'product_type', )
    # exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


@admin.register(models.ChfProductType)
class ChfProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_enable', 'data_filter_name')
    list_display_links = ('name', )
    list_editable = ('is_enable', 'sort', 'data_filter_name', )
    search_fields = ('name', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfPartner)
class ChfPartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'brief', 'url', 'address', 'sort', 'is_enable', )
    list_display_links = ('name', )
    list_editable = ('sort', 'is_enable', 'url', )
    search_fields = ('name', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfAbout)
class ChfAboutAdmin(admin.ModelAdmin):
    list_display = ('comp_name', 'title', 'comp_image', 'is_enable')
    list_display_links = ('comp_name', )
    list_editable = ('title', 'is_enable')
    search_fields = ('comp_name', 'title',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


@admin.register(models.ChfAboutResource)
class ChfAboutResourceAdmin(admin.ModelAdmin):
    list_display = ('type_code', 'type_name', 'image_url', 'sort', 'is_enable')
    list_display_links = ('type_name',)
    list_editable = ('type_code', 'sort', 'is_enable')
    search_fields = ('type_code', 'type_name')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username',)


@admin.register(models.ChfAnimateType)
class ChfAnimateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_name', 'descr', 'is_enable')
    list_display_links = ('id', )
    list_editable = ('name', 'class_name', 'is_enable', )
    search_fields = ('name', 'class_name', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfIndexPlate)
class ChfIndexPlateAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'plate_image_url', 'front_image', 'back_image', 'descr', 'animate_type',
    #                 'is_redirect_sub_page', 'sub_page_url', 'video_source', 'sort', 'is_enable', )
    list_display = ('id', 'title', 'descr', 'animate_type',
                    'is_redirect_sub_page', 'sub_page_url', 'video_source', 'sort', 'is_enable',)
    list_display_links = ('id', 'descr')
    list_editable = ('title', 'animate_type', 'is_redirect_sub_page', 'is_enable', 'sort', )
    search_fields = ('title', 'desc', 'animate_type')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfCompanyHistory)
class ChfCompanyHistoryAdmin(admin.ModelAdmin):
    # exclude = ('breif', 'content', )
    list_display = ('timeline_title', 'title', 'breif', 'cover_image_url', 'sort', 'is_enable', )
    list_display_links = ('timeline_title', )
    list_editable = ('title', 'is_enable', 'sort', )
    search_fields = ('title', 'breif', 'timeline_title')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


@admin.register(models.ChfJobRecruit)
class ChfJobRecruitAdmin(admin.ModelAdmin):
    # exclude = ('job_require', 'skill_require', )
    list_display = ('job_name', 'work_year', 'education', 'work_prop', 'sort', )
    list_display_links = ('job_name', )
    list_editable = ('education', 'work_prop', 'sort', )
    search_fields = ('job_name', 'work_year', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


@admin.register(models.ChfNews)
class ChfNewsAdmin(admin.ModelAdmin):
    # exclude = ('content', )
    list_display = ('title', 'brief', 'read_count', 'cover_image_url', 'type', 'sort', 'is_enable', )
    list_display_links = ('title', )
    list_editable = ('sort', 'read_count', 'type', 'is_enable', )
    search_fields = ('title', 'brief',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


@admin.register(models.ChfApplyRecord)
class ChfApplyRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'birthday', 'phone', 'email', 'is_get', 'is_inform', 'state', 'sort', 'create_time')
    list_display_links = ('name', )
    list_editable = ('is_get', 'is_inform', 'state', 'sort', )
    search_fields = ('name', 'sex', 'phone', 'email', 'is_get', 'is_inform', 'state', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfUserWateringRecord)
class ChfUserWateringRecordAdmin(admin.ModelAdmin):
    list_display = ('client_ip', 'client_host', 'client_user_agent', 'server_ip', 'server_host', 'server_port',
                    'init_amount', 'amount', 'final_amount', 'create_time')
    list_filter = ('client_ip', )
    search_fields = ('client_ip', 'client_host', 'client_user_agent', 'server_ip', 'server_host', 'server_port', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


@admin.register(models.ChfWateringQty)
class ChfWateringQtyAdmin(admin.ModelAdmin):
    list_display = ('amount', 'total_amount', 'operate_time')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
