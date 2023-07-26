from django.contrib import admin
from .models import showroom, Staff, Brand, Model, Engine, Feature

class ModelInline(admin.TabularInline):
    model = Model

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'showroom')
    search_fields = ('name', 'position', 'showroom__name')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ModelInline]

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'engine_specs')
    list_filter = ('brand',)

    def engine_specs(self, obj):
        return obj.engine.specs

    engine_specs.short_description = 'Engine Specs'

admin.site.register(showroom)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Engine)
admin.site.register(Feature)
