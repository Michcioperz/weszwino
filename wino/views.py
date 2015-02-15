from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from wino.models import Dzialanie, Termin, Komentarz
from django.contrib.auth.decorators import login_required
# Create your views here

class KommForm(forms.Form):
    tresc = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "wino/index.html", {'posts':Dzialanie.objects.exclude(stare=True)})

def single_post(request, pid):
    pst = get_object_or_404(Dzialanie, pk=pid)
    return render(request, "wino/post.html", {'pst':pst, 'trms':Termin.objects.filter(dzialanie=pst).order_by('dzien','lekcja'),'kmns':Komentarz.objects.filter(dzialanie=pst)})

@login_required
def addkomm(request, pid):
    pst = get_object_or_404(Dzialanie, pk=pid)
    if request.method == 'POST':
        form = KommForm(request.POST)
        if form.is_valid():
            Komentarz(tresc=form.cleaned_data['tresc'], uzytkownik=request.user, dzialanie=pst).save()
            return HttpResponseRedirect(u'/wino/post/%i/'%int(pid))
    else:
        form = KommForm()
    return render(request, "wino/addcomm.html", {'pst':pst,'form':form})
