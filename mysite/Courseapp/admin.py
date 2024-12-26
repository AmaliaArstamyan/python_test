from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'quantity')
    search_fields = ('title',)
    list_filter = ('rate',)
    ordering = ('-rate',)  

admin.site.register(Course, CourseAdmin)


