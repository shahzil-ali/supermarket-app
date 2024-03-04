from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError('The username field must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=200, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]


    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="subcategories")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, related_name="items")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
        return self.name


