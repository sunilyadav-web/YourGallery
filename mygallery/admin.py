from csv import list_dialects
from django.contrib import admin
from mygallery.models import User,Gallery,Category

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','user','image','title','category','date']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','realname','emailid','password']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cat','user']