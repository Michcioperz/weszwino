from django.contrib import admin
from wesza.models import *
# Register your models here.

admin.site.register(Subject)
admin.site.register(Category)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pinned', 'done', 'date', 'subject', 'teacher', 'name',)
    list_filter = ['pinned', 'done', 'date', 'subject', 'teacher']
    ordering = ['done', '-pinned', 'date', 'subject', 'teacher', 'name', 'description']

@admin.register(Wplata)
class WplataAdmin(admin.ModelAdmin):
    list_display = ('skladka', 'osoba', 'kwota',)
    list_filter = ('skladka', 'osoba',)

class WplataInline(admin.StackedInline):
    model = Wplata

@admin.register(Skladka)
class SkladkaAdmin(admin.ModelAdmin):
    list_display = ('name','kwota','deadline',)
    inlines = [WplataInline]
