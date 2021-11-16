from django.contrib import admin

# Register your models here.
from website.models import Contact

class ContactAdmin(admin.ModelAdmin) :
    date_hierarchy = 'updated_date'
    # fields = ('title', 'content')
admin.site.register(Contact, ContactAdmin)
