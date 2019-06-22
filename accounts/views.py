from django.shortcuts import render
from django.http import HttpResponseRedirect

from accounts.forms import RegistrationForm


def register(request):

    error = ""
    done = False
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            error += "Invalid information/ Email already in use."
        else:
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(form.cleaned_data["password1"])
            user.save()
            done = True

    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'error': error, 'done': done, })
