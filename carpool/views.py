from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse
from .tokens import account_activation_token
import datetime

from .forms import SignUpForm, PoolForm, filterForm, DeleteForm, AddForm
from .models import Pool, User


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
        allrides = Pool.objects.filter(dateTime__gte=datetime.date.today(), tot__gt=0)
        addform = []
        if request.method == 'POST' and 'filter' in request.POST:
            filter = filterForm(request.POST)
            indate = request.POST['date_year'] + '-' + request.POST['date_month'] + '-' + request.POST['date_day']
            CHOICES = {'1': "Кижинга", '2': "Улан-Удэ", '3': "Хоринск", }
            allrides = Pool.objects.filter(source=CHOICES[request.POST['source']],
                                           dest=CHOICES[request.POST['dest']],
                                           tot__gte=request.POST['tot'],
                                           dateTime=indate,
                                           )
        else:
            filter = filterForm()
        for ride in allrides:
            addform += [AddForm(initial={'pk': ride.pk})]
        if request.method == 'POST' and 'del' in request.POST:
            form = DeleteForm(request.POST)
            my_pool = Pool.objects.get(pk=form['pk'].value())
            my_pool.tot = my_pool.tot + 1
            my_pool.save()
            allrides = Pool.objects.filter(dateTime__gte=datetime.date.today(), tot__gt=0)
        if request.method == 'POST' and 'add' in request.POST:
            form = AddForm(request.POST)
            my_pool = Pool.objects.get(pk=form['pk'].value())
            my_pool.tot = my_pool.tot - 1
            my_pool.save()
            allrides = Pool.objects.filter(dateTime__gte=datetime.date.today(), tot__gt=0)
        delform = []
        addform = []
        for ride in allrides:
            addform += [AddForm(initial={'pk': ride.pk})]
        return render(request, 'index.html',
                      {'allrides': allrides, 'filter': filter, 'delform': delform,
                       'addform': addform})
    else:
        return redirect('login')


def addPool(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PoolForm(request.POST, initial={'user': request.user})
            if form.is_valid():
                form.save()
        else:
            form = PoolForm(initial={'user': request.user})
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
