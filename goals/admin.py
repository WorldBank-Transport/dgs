from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from import_export.admin import ImportExportModelAdmin
from .models import (Plan, Goal, Target, Indicator, Component, Progress,
                     Area)
from .resources import GoalResource, TargetResource, IndicatorResource


class ProgressInline(admin.TabularInline):
    model = Progress
    exclude = ['slug']


class ComponentInline(admin.TabularInline):
    model = Component.indicators.through
    exclude = ['slug']


class AreaAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PlanAdmin(ImportExportModelAdmin):
    list_display = ['code', 'name', 'description']
    list_display_links = ['code', 'name']
    prepopulated_fields = {"slug": ("name",)}


class GoalAdmin(ImportExportModelAdmin):
    resource_class = GoalResource
    list_display = ['code', 'name', 'description']
    list_display_links = ['code', 'name']
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['id']


class TargetAdmin(ImportExportModelAdmin):
    resource_class = TargetResource
    list_display = ['code', 'description']
    list_display_links = ['code', 'description']
    list_filter = ['goal']
    search_fields = ['code', 'description']
    ordering = ['id']


class IndicatorAdmin(ImportExportModelAdmin):
    resource_class = IndicatorResource
    list_display = ['code', 'description']
    list_display_links = ['code', 'description']
    list_filter = ['target__goal', 'stats_available', 'agency',
                   'data_source']
    search_fields = ['code', 'description']
    ordering = ['id']
    inlines = [ComponentInline]


class ComponentAdmin(ImportExportModelAdmin):
    filter_horizontal = ['indicators']
    list_display = ['code', 'name']
    list_display_links = ['code', 'name']
    list_filter = ['indicators__target__goal']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['code', 'name']
    ordering = ['id']
    inlines = [ProgressInline]


class ProgressAdmin(ImportExportModelAdmin):
    list_display = ['component_code', 'component_name', 'year', 'value',
                    'value_unit']
    list_display_links = ['component_name', 'year', 'value']
    list_filter = ['year', 'component__indicators']
    search_fields = ['component__indicators__code',
                     'component__indicators__description']
    ordering = ['id']
    list_select_related = ['component']


admin.site.register(Area, AreaAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Progress, ProgressAdmin)

