from django.contrib import admin

# Register your models here.
from Tester.models import user





class UserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'userEmail', 'userResult','userDate','userTime')
    list_editable = ('userResult','userDate','userTime')
    search_fields = ('userName','id')
admin.site.site_header = 'Covid Test Registration'
admin.site.register(user,UserAdmin)
