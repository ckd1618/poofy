from django.contrib import admin
from .models import Category,Product
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name','slug'] 
  #assign the value of the name field to the slug field
  prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
  list_display = ['thumbnail', 'image','name','price','stock','available','created','updated']
  list_editable = ['price','stock','available']
  prepopulated_fields = {'slug':('name',)}
  list_per_page = 20

  def thumbnail(self,obj):
    return format_html('<img src="{}" style="width: 40px; height: 40px;" />'.format(obj.image.url))
  thumbnail.description = 'thumbnail'

#the following code achieves the same as the above code
# class ProductAdmin(ImportExportModelAdmin):
#   list_display = ['name','price','stock','available','created','updated']
#   list_editable = ['price','stock','available']
#   prepopulated_fields = {'slug':('name',)}
#   list_per_page = 20
# admin.site.register(Product,ProductAdmin)

#if you don't need import/export
# class ProductAdmin(admin.ModelAdmin):
#   list_display = ['name','price','stock','available','created','updated']
#   list_editable = ['price','stock','available']
#   prepopuated_fields = {'slug':('name',)}
#   list_per_page = 20
# admin.site.register(Product,ProductAdmin)
