from django.contrib import admin
from home import models

# Register your models here.
admin.site.site_header = '春和方 | 秦食皇 后台管理系统'
admin.site.site_title = '后台管理系统'

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'nick_name', 'qq', 'phone', 'is_lock', 'is_enable')
    list_display_links = ('username', )
    # class Media:
    #     js = (
    #         '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
    #         '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
    #         '/static/plugins/kindeditor-4.1.10/config.js',
    #     )

@admin.register(models.ChfProduct)
class ChfProductAdmin(admin.ModelAdmin):
    # fields = ()
    # inlines = ()
    list_display = ('name', 'slug', 'brief', 'cover_image_url', 'read_count', 'product_type', 'sort', 'is_recommand', 'is_enable')
    list_display_links = ('name', 'product_type', )
    list_editable = ('sort', 'is_recommand', 'is_enable')
    list_filter = ('product_type', 'is_recommand', 'is_enable')
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username', )
    # fieldsets = (
    #     (None, {
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
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username',)
    search_fields = ('name', )


@admin.register(models.ChfPartner)
class ChfPartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'brief', 'url', 'address', 'sort', 'is_enable', )
    list_display_links = ('name', )
    list_editable = ('sort', 'is_enable', 'url', )
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username',)
    search_fields = ('name', )

# @admin.register(models.ChfAbout)
# class ChfAboutAdmin(admin.ModelAdmin):
#     list_display = ('comp_name', 'org_structure', 'is_enable')
#     list_display_links = ('comp_name', )
#     exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username', )
#
#     # class Media:
#     #     js = (
#     #         '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
#     #         '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
#     #         '/static/plugins/kindeditor-4.1.10/config.js',
#     #     )

@admin.register(models.ChfCompanyHistory)
class ChfCompanyHistoryAdmin(admin.ModelAdmin):
    # exclude = ('breif', 'content', )
    list_display = ('timeline_title', 'title', 'breif', 'cover_image_url', 'sort', 'is_enable', )
    list_display_links = ('timeline_title', )
    list_editable = ('title', 'is_enable', )
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username', )

    # class Media:
    #     js = (
    #         '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
    #         '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
    #         '/static/plugins/kindeditor-4.1.10/config.js',
    #     )

@admin.register(models.ChfJobRecruit)
class ChfJobRecruitAdmin(admin.ModelAdmin):
    # exclude = ('job_require', 'skill_require', )
    list_display = ('job_name', 'work_year', 'education', 'work_prop', 'sort', )
    list_display_links = ('job_name', )
    list_editable = ('education', 'work_prop', 'sort', )
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username', )

@admin.register(models.ChfNews)
class ChfNewsAdmin(admin.ModelAdmin):
    # exclude = ('content', )
    list_display = ('title', 'brief', 'read_count', 'cover_image_url', 'sort', )
    list_display_links = ('title', )
    list_editable = ('sort', 'read_count', )
    exclude = ('create_uid', 'create_username', 'operate_uid', 'operate_username', )
