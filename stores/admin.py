from django.contrib import admin
from .models import Store, MenuItem
# Register your models here.

class MenuItemInLine(admin.TabularInline):
	model = MenuItem
	extra = 1

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ('name', 'notes',)
	inlines = (MenuItemInLine,)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('store', 'name', 'price', )


