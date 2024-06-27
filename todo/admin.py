from django.contrib import admin
from todo.models import Todo


# Register your models here.
@admin.register(Todo)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
