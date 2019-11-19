from django.contrib import admin
from home.models import IndexBanner, BlogType, BlogTag, BlogTable, Blog, Comments

# Register your models here.

admin.site.register(IndexBanner)
admin.site.register(BlogType)
admin.site.register(BlogTag)
admin.site.register(BlogTable)
admin.site.register(Blog)
admin.site.register(Comments)




# admin.site.register([IndexBanner, BlogType, BlogTag, BlogTable, Blog, Comments])
