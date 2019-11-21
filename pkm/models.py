from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Location(models.Model):
    name = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
        # Shows up in the admin list
    def __str__(self):
        return self.name

class Property(models.Model):
    kind = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )

        # Shows up in the admin list
    def __str__(self):
        return self.kind

class Area(models.Model):
    place = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )

        # Shows up in the admin list
    def __str__(self):
        return self.place


class Pokemon(models.Model) :
    name = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    prop = models.ForeignKey(Property, on_delete=models.SET_NULL,null = True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL,null = True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    catch_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trainer = models.ForeignKey('Profile', on_delete=models.CASCADE)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Comment', related_name='comments_owned')
    picture = models.BinaryField(null=True, editable=True)
    pkmdex = models.ForeignKey('Pokedex',on_delete=models.SET_NULL, null = True)
    # Shows up in the admin list
    def __str__(self):
        return self.name

class Comment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    pkm = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'

class Profile(models.Model):    #Trainer Table
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collect = models.ManyToManyField('Pokemon',
        through='Pokemon', related_name='pokemons_trainer')
    avatar = models.BinaryField(null=True, editable=True)
    gallary = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Gallary', related_name='gallary_owned')
        # Shows up in the admin list
    def __str__(self):
        return self.name

class Pokedex(models.Model):
    name = models.CharField(
            max_length=128,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Gallary(models.Model):
    title = models.CharField(max_length=100,null=True)
    pic = models.BinaryField(null=True, editable=True)
    discp = models.CharField(max_length=1000,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title






