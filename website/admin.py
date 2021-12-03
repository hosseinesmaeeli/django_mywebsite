from django.contrib import admin

# Register your models here.
from website.models import Contact,Newsletter

class ContactAdmin(admin.ModelAdmin) :
    date_hierarchy = 'updated_date'
    # fields = ('title', 'content')
    list_display = ('name' ,'email','created_date')
    list_filter = ('email',)
    search_fields = ['name','message']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
 