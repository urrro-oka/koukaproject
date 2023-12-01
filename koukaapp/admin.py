from django.contrib import admin
from .models import Category,ArimsPost,Monster

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class MonsterAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

class PhotoPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links= ('id','title')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Monster,MonsterAdmin)
admin.site.register(ArimsPost,PhotoPostAdmin)