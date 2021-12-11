from django.contrib import admin

from .models import Choice, Question


# Register your models here.


#admin.site.register(Question)


# class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']


# class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
        # (None,               {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date']}),
    # ]


class ChoiceInline(admin.TabularInline): # StackedInline
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display


#admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
