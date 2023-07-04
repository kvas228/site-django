from django.contrib import admin
from .models import zakazi
from .models import articles

admin.site.register(zakazi)
class Articleadmin(admin.ModelAdmin):
    fields = ["article_image"]
    extra = 2
admin.site.register(articles)