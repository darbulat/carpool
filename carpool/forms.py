from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pool


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'e-mail'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторить пароль'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


CHOICE = (
    ("Кижинга", _("Кижинга")),
    ("Улан-Удэ", _("Улан-Удэ")),
    ("Хоринск", _("Хоринск")),
)

CHOICE_PASS = (
    ("Пассажир", _("Пассажир")),
    ("Водитель", _("Водитель")),
)


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PoolForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    passenger = forms.ChoiceField(choices=CHOICE_PASS, label="Пассажир", widget=forms.Select())
    tot = forms.IntegerField(widget=forms.NumberInput(), label="Мест")
    dateTime = forms.DateField(widget=DateInput(format="%d/%m/%Y"), label="Дата отправления")
    time = forms.TimeField(widget=TimeInput(), label='Время отправления')
    source = forms.ChoiceField(choices=CHOICE, label="Откуда", initial='', widget=forms.Select())
    dest = forms.ChoiceField(choices=CHOICE, label="куда", initial='', widget=forms.Select())
    amount = forms.IntegerField(widget=forms.NumberInput(), required=False, label="стоимость")
    phone_number = forms.CharField(widget=forms.TextInput(), required=False, label="номер телефона")
    note = forms.CharField(widget=forms.TextInput(), required=False, label='Дополнительная информация')

    class Meta:
        model = Pool
        fields = ('user', 'passenger', 'tot', 'dateTime', 'time', 'source', 'dest', 'amount', 'phone_number', 'note')

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
    tot = forms.IntegerField(widget=forms.NumberInput(), label="кол-во")
    date = forms.DateField(widget=forms.SelectDateWidget(), label="Дата")


class DeleteForm(forms.Form):
    pk = forms.IntegerField(widget=forms.HiddenInput())


class AddForm(forms.Form):
    pk = forms.IntegerField(widget=forms.HiddenInput())
