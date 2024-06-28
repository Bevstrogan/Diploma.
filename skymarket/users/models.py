from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choises = ((USER, USER), (ADMIN, ADMIN))


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="Почта")
    first_name = models.CharField(max_length=40, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    role = models.CharField(max_length=20, choices=UserRoles.choises, default=UserRoles.USER, verbose_name="Роль пользователя")
    image = models.ImageField(upload_to="photos/", verbose_name="Фото", blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name="Признак активности")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]