from django.contrib import admin

from lms.models import Chapter, Material, Question, Answer, CheckAnswer

admin.site.register(Chapter)

admin.site.register(Material)

admin.site.register(Question)

admin.site.register(Answer)

admin.site.register(CheckAnswer)
