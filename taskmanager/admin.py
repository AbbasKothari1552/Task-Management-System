from django.contrib import admin

from .models import Task, Tag

class TaskAdmin(admin.ModelAdmin):

    list_display = ('user','title','tag','priority','date','time',)
    list_filter = ('user','tag','date','time',)
    search_fields = ('user','task',)

class TagAdmin(admin.ModelAdmin):

    list_display = ('name','user','is_default',)
    list_filter = ('name','user',)
    search_fields = ('user',)



admin.site.register(Task,TaskAdmin)
admin.site.register(Tag,TagAdmin)
