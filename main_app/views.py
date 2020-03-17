from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Cam, Cb, Cdm, Cf, Cm, Gk, Lb, Lm, Lw, Lwb, Rb, Rm, Rw, Rwb, St
from .forms import RatingsForm

def home(request):
    return render(request, 'main_app/home.html')


def about(request):
    return render(request, 'main_app/about.html')


def camview(request):
    qs = Cam.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Cam.objects.order_by('nationality').values('nationality').distinct()
    team_names = Cam.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/cam.html', context)


def cbview(request):
    qs = Cb.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Cb.objects.order_by('nationality').values('nationality').distinct()
    team_names = Cb.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/cb.html', context)


def cdmview(request):
    qs = Cdm.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Cdm.objects.order_by('nationality').values('nationality').distinct()
    team_names = Cdm.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/cdm.html', context)


def cfview(request):
    qs = Cf.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Cf.objects.order_by('nationality').values('nationality').distinct()
    team_names = Cf.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/cf.html', context)


def cmview(request):
    qs = Cm.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Cm.objects.order_by('nationality').values('nationality').distinct()
    team_names = Cm.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/cm.html', context)


def gkview(request):
    qs = Gk.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Gk.objects.order_by('nationality').values('nationality').distinct()
    team_names = Gk.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/gk.html', context)


def lbview(request):
    qs = Lb.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Lb.objects.order_by('nationality').values('nationality').distinct()
    team_names = Lb.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/lb.html', context)


def lmview(request):
    qs = Lm.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Lm.objects.order_by('nationality').values('nationality').distinct()
    team_names = Lm.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/lm.html', context)


def lwview(request):
    qs = Lw.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Lw.objects.order_by('nationality').values('nationality').distinct()
    team_names = Lw.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/lw.html', context)


def lwbview(request):
    qs = Lwb.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Lwb.objects.order_by('nationality').values('nationality').distinct()
    team_names = Lwb.objects.order_by('club').values('club').distinct()

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
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    return render(request, 'main_app/lwb.html', context)


def rbview(request):
    qs = Rb.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Rb.objects.order_by('nationality').values('nationality').distinct()
    team_names = Rb.objects.order_by('club').values('club').distinct()

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
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    return render(request, 'main_app/rb.html', context)


def rmview(request):
    qs = Rm.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Rm.objects.order_by('nationality').values('nationality').distinct()
    team_names = Rm.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/rm.html', context)


def rwview(request):
    qs = Rw.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Rw.objects.order_by('nationality').values('nationality').distinct()
    team_names = Rw.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/rw.html', context)


def rwbview(request):
    qs = Rwb.objects.all()
    page = request.GET.get('page', 1)
    name_query = request.GET.get('playernamefield')
    nationality = request.GET.get('nationalityfield')
    team = request.GET.get('teamfield')

    countries = Rwb.objects.order_by('nationality').values('nationality').distinct()
    team_names = Rwb.objects.order_by('club').values('club').distinct()

    if name_query != '' and name_query is not None:
        qs = qs.filter(long_name__icontains=name_query)
    if nationality != 'Choose...' and nationality != None:
        qs = qs.filter(nationality__icontains=nationality)
    if team != 'Choose...' and team != None:
        qs = qs.filter(club__icontains=team)
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/rwb.html', context)


def stview(request):
    qs = St.objects.all()
    page = request.GET.get('page', 1)
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
    paginator = Paginator(qs, 25)
    qs = paginator.page(page)

    context = {
        'queryset': qs,
        'nationalities': countries,
        'teams': team_names
    }

    return render(request, 'main_app/st.html', context)


def stplayerview(request, playerid):
    player_id = St.objects.get(sofifa_id=playerid)
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            current_user = request.user
            print(request.user)
            print(current_user.id)
            rating.user_id = current_user.id
            rating.sofifa_id = player_id.sofifa_id
            rating.position = player_id.player_positions
            rating.save()
            messages.success(request, 'Rating submitted successfully!')
            return(render(request, "main_app/home.html"))
        else:
            form = RatingsForm()
            return(render(request, "main_app/home.html"))

    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def gkplayerview(request, playerid):
    player_id = Gk.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def camplayerview(request, playerid):
    player_id = Cam.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def cbplayerview(request, playerid):
    player_id = Cb.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def cdmplayerview(request, playerid):
    player_id = Cdm.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def cfplayerview(request, playerid):
    player_id = Cf.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def cmplayerview(request, playerid):
    player_id = Cm.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def lbplayerview(request, playerid):
    player_id = Lb.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def lmplayerview(request, playerid):
    player_id = Lm.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def lwplayerview(request, playerid):
    player_id = Lw.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def lwbplayerview(request, playerid):
    player_id = Lwb.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def rbplayerview(request, playerid):
    player_id = Rb.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def rmplayerview(request, playerid):
    player_id = Rm.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def rwplayerview(request, playerid):
    player_id = Rw.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


def rwbplayerview(request, playerid):
    player_id = Rwb.objects.get(sofifa_id=playerid)
    context = {
        'profile_id': player_id,
        'form': RatingsForm
    }
    return render(request, 'main_app/profile.html', context)


