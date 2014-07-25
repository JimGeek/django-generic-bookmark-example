from django.contrib import admin

from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','time')
    readonly_fields = ('time',)

admin.site.register(Article, ArticleAdmin)