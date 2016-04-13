from django.contrib import admin

from .models import SimplePlace, Skill, Skills, Dated

# Register your models here.
admin.site.register(SimplePlace)
admin.site.register(Skill)
admin.site.register(Skills)
admin.site.register(Dated)