from django.contrib import admin
from .models import BlogLeft, BlogRight, LatestBlogLeft, LatestBlogRight, Product 


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size')


class BlogLeftAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'content')



class BlogRightAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'content')


class LatestBlogLeftAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'content')



class LatestBlogRightAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'content')


admin.site.register(Product, ProductAdmin)
admin.site.register(BlogLeft, BlogLeftAdmin)
admin.site.register(BlogRight, BlogRightAdmin)
admin.site.register(LatestBlogLeft, LatestBlogLeftAdmin)
admin.site.register(LatestBlogRight, LatestBlogRightAdmin)

