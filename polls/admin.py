from django.contrib import admin

# Register your models here.
from .models import Question

# class QuestionAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Question

admin.site.register(Question)