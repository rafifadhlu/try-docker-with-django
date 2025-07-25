from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj = ...):
            
            current_user = request.user
            if current_user.has_perm("article.publish_article"):
                readonly_fields =[
                    'slug',
                    'published',
                    'updated',
                    'created'
                ]
                return readonly_fields
            elif current_user.has_perm("article.add_article") :
                 readonly_fields =[
                    'updated',
                    'is_published',
                    'updated',
                    'created'
                ]
                 return readonly_fields
    
    list_display = ['id','judul','is_published']

admin.site.register(Article,ArticleAdmin)