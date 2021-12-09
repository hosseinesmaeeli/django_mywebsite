from django.contrib import admin
# Register your models here.

from blog.models import Post,category,Comment
class ostAdmin(admin.ModelAdmin) :
    date_hierarchy = 'updated_date'
    # fields = ('title', 'content')
    list_display = ('title' ,'author','counted_views','status','login_required','published_date','created_date')
    list_filter = ('status','author',)
    search_fields = ['title','content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title', 'content')
    empty_value_display = ('-empty-')
    list_display = ('name' ,'post','approved','created_date')
    list_filter = ('post','approved',)
    search_fields = ['name','post']

admin.site.register(category)
admin.site.register(Post, ostAdmin)
admin.site.register(Comment,CommentAdmin)