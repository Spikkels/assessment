from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from .models import Account
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

@login_required
def account(request):
    account = Account.objects.get(user=request.user)
    return render(request, 'account.html', {'account': account})

@login_required
def edit_account(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        account.home_address = request.POST.get('home_address')
        account.phone_number = request.POST.get('phone_number')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        account.location = Point(float(lng), float(lat))
        account.save()
        return redirect('account')
    return render(request, 'edit_account.html', {'account': account})

def map(request):
    accounts = Account.objects.all()
    return render(request, 'map.html', {'accounts': accounts})
