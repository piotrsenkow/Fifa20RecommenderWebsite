from django.shortcuts import render
from django.http import HttpResponse
from .models import St

def home(request):
    return render(request, 'main_app/home.html')


def about(request):
    return render(request, 'main_app/about.html')


def camview(request):
    return render(request, 'main_app/cam.html')


def cbview(request):
    return render(request, 'main_app/cb.html')


def cdmview(request):
    return render(request, 'main_app/cdm.html')


def cfview(request):
    return render(request, 'main_app/cf.html')


def cmview(request):
    return render(request, 'main_app/cw.html')


def gkview(request):
    return render(request, 'main_app/gk.html')


def lbview(request):
    return render(request, 'main_app/lb.html')


def lmview(request):
    return render(request, 'main_app/lm.html')


def lwview(request):
    return render(request, 'main_app/lw.html')


def lwbview(request):
    return render(request, 'main_app/lwb.html')


def rbview(request):
    return render(request, 'main_app/rb.html')


def rmview(request):
    return render(request, 'main_app/rm.html')


def rwview(request):
    return render(request, 'main_app/rw.html')


def rwbview(request):
    return render(request, 'main_app/rwb.html')


def stview(request):
    qs = St.objects.all()
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = St.objects.order_by('nationality').values('nationality').distinct()
    team_names = St.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/st.html', context)
