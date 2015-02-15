from django.contrib import admin
from wino.models import Klasa, Nauczyciel, Termin, Dzialanie, Komentarz, Ustawienia

# Register your models here.

for m in [Nauczyciel,  Ustawienia]:
    admin.site.register(m)

class TerminInline(admin.StackedInline):
    ordering = ('dzien','lekcja',)
    model = Termin
    extra = 1

@admin.register(Dzialanie)
class DzialanieAdmin(admin.ModelAdmin):
    inlines = [TerminInline]
    list_display = ('nauczyciel', 'przedmiot', 'rodzaj', 'stare',)

@admin.register(Klasa)
class KlasaAdmin(admin.ModelAdmin):
    list_display = ('literka', 'profil',)
    ordering = ('literka',)

@admin.register(Komentarz)
class KomentarzAdmin(admin.ModelAdmin):
    list_display = ('dzialanie', 'uzytkownik', 'czas', 'tresc',)
    ordering = ('-czas',)
