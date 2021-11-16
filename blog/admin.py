from django.contrib import admin
# Register your models here.

from blog.models import Post
class ostAdmin(admin.ModelAdmin) :
    date_hierarchy = 'updated_date'
    # fields = ('title', 'content')
admin.site.register(Post, ostAdmin)
