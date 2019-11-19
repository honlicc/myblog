from django.contrib import admin
from home.models import IndexBanner, BlogType, BlogTag, BlogTable, Blog, Comments

# Register your models here.

# admin.site.register(IndexBanner)
# admin.site.register(BlogType)
# admin.site.register(BlogTag)
# admin.site.register(BlogTable)
# admin.site.register(Blog)
# admin.site.register(Comments)


class TestTinymce_Admin(admin.ModelAdmin):

    class Media:
        js = [
            '/static/js/jquery.min.js',   # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',   # 手动添加文件，用户初始化参数
        ]

admin.site.register([IndexBanner, BlogType, BlogTag, BlogTable, Blog, Comments])
