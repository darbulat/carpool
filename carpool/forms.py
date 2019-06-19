from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pool


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'password1', 'password2', )


CHOICE = (
    ("Кижинга", _("Кижинга")),
    ("Улан-Удэ", _("Улан-Удэ")),
    ("Хоринск", _("Хоринск")),
)


class PoolForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    tot = forms.IntegerField(widget=forms.NumberInput(), label="Мест")
    dateTime = forms.DateTimeField(widget=forms.widgets.DateTimeInput(), label="Дата отправления YYYY-MM-DD HH:MM")
    source = forms.ChoiceField(choices=CHOICE, label="Откуда", initial='', widget=forms.Select())
    dest = forms.ChoiceField(choices=CHOICE, label="куда", initial='', widget=forms.Select())
    paid = forms.BooleanField(required=False, label="оплата")
    amount = forms.IntegerField(widget=forms.NumberInput(), required=False, label="стоимость")

    class Meta:
        model = Pool
        fields = ('user', 'tot', 'dateTime', 'source', 'dest', 'paid', 'amount',)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PoolForm, self).__init__(*args, **kwargs)


CHOICES = (
    (1, _("Кижинга")),
    (2, _("Улан-Удэ")),
    (3, _("Хоринск")),
)


class filterForm(forms.Form):
    source = forms.ChoiceField(choices=CHOICES, label="Откуда", initial='', widget=forms.Select())
    dest = forms.ChoiceField(choices=CHOICES, label="Куда", initial='', widget=forms.Select())
    free = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    tot = forms.IntegerField(widget=forms.NumberInput(), label="кол-во")
    date = forms.DateField(widget=forms.SelectDateWidget(), label="Дата")


class DeleteForm(forms.Form):
    pk = forms.IntegerField(widget=forms.HiddenInput())


class AddForm(forms.Form):
    pk = forms.IntegerField(widget=forms.HiddenInput())
