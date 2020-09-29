from django.contrib import admin
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['car_name', 'content']
    prepopulated_fields = {'slug': ('car_name',)}
  

admin.site.register(Car)
