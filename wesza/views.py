from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader, RequestContext
from wesza.models import Event, Category, Skladka
import datetime, markdown

# Create your views here.

def index(request):
    return HttpResponse(loader.get_template('wesza/index.html').render(RequestContext(request, {'cats':Category.objects.all().order_by('plural'),'posts':Event.objects.exclude(date__lt=datetime.date.today()).exclude(done=True).order_by('-pinned','date')})))

def skarb(request):
    return HttpResponse(loader.get_template('wesza/skarb.html').render(RequestContext(request, {'skladki':Skladka.objects.all().order_by('deadline')})))

def single_post(request, pid):
    try:
        pst = Event.objects.get(pk=pid)
    except Event.DoesNotExist:
        raise Http404
    return HttpResponse(loader.get_template('wesza/post.html').render(RequestContext(request, {'pst':pst})))

def posts_json(request):
    thing = []
    for h in Event.objects.exclude(date__lt=datetime.date.today()).exclude(done=True).order_by('-pinned','date'):
        if h.subject:
            sub = h.subject.name
        else:
            sub = None
        thing.append({'type':[h.category.codename,h.category.singular], 'date':[h.humdate(),(h.date-datetime.date.today()).days],'name':h.name,'description':h.description,'done':h.done,'subject':sub,'pinned':h.pinned,'pid':h.pk})
    return JsonResponse(thing, safe=False)

def oldapp(request):
    i = []
    for e in Event.objects.exclude(date__lt=datetime.date.today()).exclude(done=True).order_by('-pinned','date','-pk'):
        if e.subject:
            sub = e.subject.name
        else:
            sub = "brak przedmiotu"
    i.append(["%s - %s - %s - %s - %s" % (e.humdate(), e.category.singular, sub, e.name, e.description)])
    return HttpResponse(i)
