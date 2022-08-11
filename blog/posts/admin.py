from django.contrib import admin
from .models import Posts, Comments


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'pub_date', 'post')
    list_display_links = ('author', 'post')


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)
