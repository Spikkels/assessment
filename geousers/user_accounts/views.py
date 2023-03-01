from .models import Account
from .forms import AccountForm
from django.shortcuts import render, redirect
from .forms import AccountForm as accountForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """View function for registering new user accounts."""

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        account_form = AccountForm(request.POST)
        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save()
            account = account_form.save(commit=False)
            account.user = user
            account.save()
            return redirect('/')
    else:
        user_form = UserCreationForm()
        account_form = AccountForm()
    return render(request, 'register.html', {'user_form': user_form, 'account_form': account_form})


@login_required
def edit_account(request):
    """View function for editing user account information."""
    
    account = request.user.account
    if request.method == 'POST':
        form = accountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = accountForm(instance=account)
    return render(request, 'edit_account.html', {'form': form})

def map(request):
    """View function for displaying all user locations on a map."""
    
    accounts = Account.objects.all()
    return render(request, 'home.html', {'accounts': accounts})

@login_required
def account(request):
    """View function for displaying the user's account information."""
    
    account = Account.objects.get(user=request.user)
    return render(request, 'account.html', {'account': account})

