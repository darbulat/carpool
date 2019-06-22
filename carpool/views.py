from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm as LoginForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from .tokens import account_activation_token
import datetime

from .forms import SignUpForm, PoolForm, filterForm, DeleteForm, AddForm
from .models import Pool, User


def IITmail(request):
    return True


def new(request):
    error = ""
    done = False
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            error += "Invalid information/ Email already in use."
        else:
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password2"])
            user.is_active = True
            user.save()
            done = True

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'error': error, 'done': done, })


def dashboard(request):
    if request.user.is_authenticated:
        allrides = Pool.objects.filter(dateTime__date__gt=datetime.date.today(), tot__gt=0)
        myrides = Pool.objects.filter(slots=request.user, dateTime__date__gt=datetime.date.today())
        delform = []
        addform = []
        for ride in myrides:
            delform += [DeleteForm(initial={'pk': ride.pk})]
        if request.method == 'POST' and 'filter' in request.POST:
            filter = filterForm(request.POST)
            indate = request.POST['date_year'] + '-' + request.POST['date_month'] + '-' + request.POST['date_day']
            CHOICES = {'1': "Кижинга", '2': "Улан-Удэ", '3': "Хоринск", }
            if 'free' in request.POST:
                allrides = Pool.objects.filter(source=CHOICES[request.POST['source']],
                                               dest=CHOICES[request.POST['dest']], tot__gte=request.POST['tot'],
                                               paid=False, dateTime__date=indate, )
            else:
                allrides = Pool.objects.filter(source=CHOICES[request.POST['source']],
                                               dest=CHOICES[request.POST['dest']], tot__gte=request.POST['tot'],
                                               paid=True, dateTime__date=indate, )
        else:
            filter = filterForm()
        for ride in allrides:
            addform += [AddForm(initial={'pk': ride.pk})]
        if request.method == 'POST' and 'del' in request.POST:
            form = DeleteForm(request.POST)
            my_pool = Pool.objects.get(pk=form['pk'].value())
            my_pool.slots.remove(request.user)
            my_pool.tot = my_pool.tot + 1
            my_pool.save()
            allrides = Pool.objects.filter(dateTime__date__gt=datetime.date.today(), tot__gt=0)
        if request.method == 'POST' and 'add' in request.POST:
            form = AddForm(request.POST)
            my_pool = Pool.objects.get(pk=form['pk'].value())
            my_pool.slots.add(request.user)
            my_pool.tot = my_pool.tot - 1
            my_pool.save()
            allrides = Pool.objects.filter(dateTime__date__gt=datetime.date.today(), tot__gt=0)
        myrides = Pool.objects.filter(slots=request.user, dateTime__date__gt=datetime.date.today())
        delform = []
        addform = []
        for ride in myrides:
            delform += [DeleteForm(initial={'pk': ride.pk})]
        for ride in allrides:
            addform += [AddForm(initial={'pk': ride.pk})]
        return render(request, 'index.html',
                      {'allrides': allrides, 'myrides': myrides, 'filter': filter, 'delform': delform,
                       'addform': addform})
    else:
        return redirect('login')


def addPool(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PoolForm(request.POST, initial={'paid': False, 'user': request.user})
            if form.is_valid():
                form.save()
        else:
            form = PoolForm(initial={'paid': False, 'user': request.user})
        return render(request, 'add.html', {'form': form})
    else:
        return redirect('login')


def activate(request, uidb64, token):
    try:
        user = User.objects.get(pk=uidb64)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    account_activation_token.check_token(user, token)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
