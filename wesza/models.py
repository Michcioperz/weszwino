# encoding: utf-8
from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    codename = models.CharField(u"nazwa kodowa", max_length="30")
    singular = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)
    def __unicode__(self):
        return self.singular
    class Meta:
        verbose_name = u"Kategoria"
        verbose_name_plural = u"Kategorie"
        ordering = ('plural',)

class Subject(models.Model):
    name = models.CharField("nazwa", max_length=150)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        verbose_name = u"Przedmiot"
        verbose_name_plural = u"Przedmioty"

class Event(models.Model):
    category = models.ForeignKey(Category)
    subject = models.ForeignKey(Subject, null=True, blank=True)
    teacher = models.ForeignKey('wino.Nauczyciel', null=True, blank=True, verbose_name=u"Nauczyciel (jeśli się różni)")
    name = models.CharField("nazwa", max_length=250)
    description = models.TextField("opis", null=True, blank=True)
    date = models.DateField("termin", null=True, blank=True)
    done = models.BooleanField("niepotrzebne", default=False)
    pinned = models.BooleanField("przypięte", default=False)
    def humdate(self):
        if self.daysleft() == 0:
            return "dzisiaj"
        elif self.daysleft() == 1:
            return "jutro"
        else:
            return "za %i dni" % self.daysleft()
    def daysleft(self):
        return (self.date-datetime.date.today()).days
    def __unicode__(self):
        return u"[%i][%i] %s - %s - %s - %s" % (self.done, self.pinned, self.category.singular, self.subject or "brak przedmiotu", self.name, self.description or "brak opisu")
    class Meta:
        ordering = ('-pinned','date','category','subject','name',)
        verbose_name = u"Zdarzenie"
        verbose_name_plural = u"Zdarzenia"

class Skladka(models.Model):
    name = models.CharField(max_length=250)
    kwota = models.FloatField()
    deadline = models.DateField(null=True, blank=True)
    potrzebne = models.IntegerField(default=33)
    def wplaleft(self):
        return self.potrzebne-self.wplaty.count()
    def daysleft(self):
        return ((self.deadline or datetime.date.today())-datetime.date.today()).days
    def __unicode__(self):
        return u"%s - %ix%.2f - %s" % (self.name, self.potrzebne, self.kwota, self.deadline)
    class Meta:
        verbose_name = u"Składka"
        verbose_name_plural = u"Składki"

class Wplata(models.Model):
    skladka = models.ForeignKey(Skladka,related_name='wplaty')
    osoba = models.CharField(max_length=30)
    kwota = models.FloatField()
    def __unicode__(self):
        return u"%s - %s %.2f" % (self.skladka.name, self.osoba, self.kwota)
    class Meta:
        verbose_name = u"Wpłata"
        verbose_name_plural = u"Wpłaty"

