from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings
#docker-compose run app sh -c "python manage.py makemigrations core"
class UserManager(BaseUserManager):
    def create_user(self,email,password = None,**extra_fields):
        #creates and saves a new user
        if email == None:
            raise ValueError("Users must have an email")
        user = self.model(email= self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        #supporting multiple databases
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    #custom user model that supports using email instead of username
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    #settings used to retrieve auth user model
class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    )
    #referencing foreign key to the user object

    def __str__(self):
        return (self.name)

class Ingredient(models.Model):
    """Ingredient to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    )
    #referencing foreign key to the user object

    def __str__(self):
        return (self.name)
