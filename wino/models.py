# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime
from wesza.models import *

# Create your models here.

class Klasa(models.Model):
    literka = models.CharField(max_length=1)
    profil = models.CharField(max_length=50)
    def __unicode__(self):
        return u"%s (%s)" % (self.literka, self.profil)
    class Meta:
        ordering = ('literka','profil',)
        verbose_name = u'Klasa'
        verbose_name_plural = u'Klasy'

class Nauczyciel(models.Model):
    nazwisko = models.CharField(max_length=255)
    imiona = models.CharField(max_length=255)
    kod = models.CharField(max_length=10)
    def __unicode__(self):
        return u"%s %s %s" % (self.nazwisko, self.imiona, self.kod)
    class Meta:
        verbose_name = u'Nauczyciel'
        verbose_name_plural = u'Nauczyciele'
        ordering = ('nazwisko','imiona',)

class Dzialanie(models.Model):
    przedmiot = models.ForeignKey('wesza.Subject')
    nauczyciel = models.ForeignKey(Nauczyciel)
    rodzaj = models.ForeignKey(Category)
    nazwa = models.CharField(max_length=255)
    stare = models.BooleanField(default=False)
    def terminarz(self):
        return self.terminy.order_by('dzien','lekcja')
    def termproc(self):
        return 100.0/self.terminy.count()
    def __unicode__(self):
        return self.nazwa
    class Meta:
        verbose_name = u'Działanie'
        verbose_name_plural = u'Działania'

class Termin(models.Model):
    dzialanie = models.ForeignKey(Dzialanie, related_name='terminy')
    klasa = models.ForeignKey(Klasa)
    dzien = models.DateField()
    lekcja = models.IntegerField()
    juzbylo = models.BooleanField(default=False)
    def dnizost(self):
        return (self.dzien-datetime.date.today()).days
    def __unicode__(self):
        return u"%s - %s - %sx%i" % (self.dzialanie, self.klasa, self.dzien, self.lekcja)

class Komentarz(models.Model):
    dzialanie = models.ForeignKey(Dzialanie, related_name='komentarze')
    uzytkownik = models.ForeignKey(User)
    czas = models.DateTimeField(default=datetime.datetime.now)
    tresc = models.TextField()
    def __unicode__(self):
        return u"%s - %s - %s" % (self.dzialanie, self.uzytkownik, self.tresc[:40])

class Ustawienia(models.Model):
    osoba = models.ForeignKey(User, unique=True)
    klasa = models.ForeignKey(Klasa)
    def __unicode__(self):
        return u"Ustawienia: %s" % self.osoba
