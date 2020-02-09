from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField

# Create your models here.
class Candidate(models.Model):
    REGION_CHOICES = ( ('gab', '제주갑'), ('eul','제주을'), ('byeong', '제주병'), )
    PARTY_CHOICES = ( ('jhd', 'jhd'), ('dmj', 'dmj'), ('jed', 'jed'), )

    name = models.CharField(max_length=100, default='후보')
    number = models.IntegerField(default=0)
    slogan = models.CharField(max_length=50, default="slogan")
    region = models.CharField(max_length=10, choices=REGION_CHOICES, default='무소속')
    party = models.CharField(max_length=10, choices=PARTY_CHOICES, default='무소속')
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    detail_info = models.TextField(blank=True)


class Promise(models.Model):
    candidate = models.OneToOneField(
         Candidate, 
         on_delete = models.CASCADE,
         primary_key = True,
         )
    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    text4 = models.TextField(blank=True)
    text5 = models.TextField(blank=True)
    text6 = models.TextField(blank=True)
    text7 = models.TextField(blank=True)
    text8 = models.TextField(blank=True)
    text9 = models.TextField(blank=True)
    text10 = models.TextField(blank=True)
    text11 = models.TextField(blank=True)
    more_info = models.URLField(max_length=200)


class Press(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, default='hi')
    headline = models.CharField(max_length=200, default='기사 제목')
    where = models.CharField(max_length=20, default='에디터')
    link = models.URLField(max_length=200, null=True)
    when = models.DateTimeField(auto_now=False, auto_now_add=False)
