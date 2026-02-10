from django.contrib import admin
from .models import Post, Author, Tag, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ("tags",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address')

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user_name')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
