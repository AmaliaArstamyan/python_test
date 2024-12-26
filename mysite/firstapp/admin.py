from django.contrib import admin
from .models import Question, Choice, FirstappUser, Userlog


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["question_text", "pub_date"] // OR

    # fieldsets = [                          // OR
    #     ("Main information", {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"]}),
    # ]

    fieldsets = [
        ("Main information", {"fields": ["question_text"], "classes": ["collapse"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date"]

 

class FirstappUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'country']

    def get_full_name(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(FirstappUser, FirstappUserAdmin)
admin.site.register(Userlog)
# Register your models here.
