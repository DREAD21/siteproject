from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=255, default='')
    meal_del = models.CharField(max_length=30, blank=True)
    site_del = models.DateField(null=True, blank=True)
    email = models.EmailField(default='', blank=True)
    vk_link = models.CharField(max_length=255, blank=True)



class Pushkin_card(models.Model):

    category = models.CharField(max_length=255, default='')
    event_name = models.CharField(max_length=255, default= '')
    address = models.CharField(max_length=255, default='', blank=True)
    date = models.DateField()
    descriptions = models.TextField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return (self.event_name)


class park(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название парка')
    adress = models.CharField(max_length=255, verbose_name='адрес парка')
    objects = models.Manager()

class cafe(models.Model):

    name = models.CharField(max_length=255, verbose_name='название кафе')
    adress = models.CharField(max_length=255, verbose_name='адрес кафе')
    rating = models.FloatField(default=0, null=True, blank=True)
    allrate = models.FloatField(default=0, null=True, blank=True)

class flowershop(models.Model):

    name = models.CharField(max_length=255, verbose_name='название магазина')
    adress = models.CharField(max_length=255, verbose_name='адрес кафе')

class aquapark(models.Model):

    name = models.CharField(max_length=255, verbose_name='название аквапарка')
    adress = models.CharField(max_length=255, verbose_name='адрес аквапарка')
    information = models.TextField(default='')
    rating = models.FloatField(default=0, null=True, blank=True)
    allrate = models.FloatField(default=0, null=True, blank=True)
    amount = models.IntegerField(default=1)
    image = models.ImageField(default='')
    objects = models.Manager()

    def __str__(self):
        return (self.name)

class cinema(models.Model):

    name = models.CharField(max_length=255, verbose_name='название кинотеатра')
    adress = models.CharField(max_length=255, verbose_name='адрес кинотеатра')
    station = models.CharField(max_length=255, verbose_name='стацния', default='')
    rating = models.FloatField(default=0, null=True, blank=True)
    allrate = models.FloatField(default=0, null=True, blank=True)
    amount = models.IntegerField(default=1)
    objects = models.Manager()

    def __str__(self):
        return (self.name)

class advices(models.Model):

    advice = models.TextField()


class theater(models.Model):

    name = models.CharField(max_length=255, verbose_name='название кинотеатра')
    adress = models.CharField(max_length=255, verbose_name='адрес кинотеатра')
    station = models.CharField(max_length=255, verbose_name='стацния', default='')
    allrate = models.FloatField(default=0, null=True, blank=True)
    rating = models.FloatField(default=0, null=True, blank=True)
    amount = models.IntegerField(default=1)
    objects = models.Manager()
    def __str__(self):
        return (self.name)


class Comment(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='')
    article_id = models.CharField(max_length=1000, default='')
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return (self.content[0:20])

