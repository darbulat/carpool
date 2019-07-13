from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.timezone import now


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Pool(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    vk_id = models.PositiveIntegerField(default=1)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    passenger = models.CharField(max_length=100, blank=True)
    dateTime = models.DateField(default=now)
    time = models.TimeField(default=now)
    tot = models.PositiveIntegerField(default=1)
    source = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, blank=True)
    note = models.TextField(blank=True, null=True)




    def __str__(self):
        return self.user.first_name + ' ' + self.source + '-' + self.dest + ' ' + self.passenger + '\n Телефон: ' + \
               self.phone_number + ' Дата: ' + str(self.dateTime) + ' Время: ' + str(self.time)

    def __self__(self):
        return self.user.first_name + ' ' + self.source + '-' + self.dest
