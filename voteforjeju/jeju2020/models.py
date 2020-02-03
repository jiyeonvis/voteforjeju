from django.db import models

# Create your models here.
class Candidate(models.Model):
    REGION_CHOICES = ( ('gab', '제주갑'), ('eul','제주을'), ('byeong', '제주병'), )
    PARTY_CHOICES = ( ('jhd', 'jhd'), ('dmj', 'dmj'), ('jed', 'jed'), )
    name = models.CharField(max_length=100)
    number = models.FloatField(default=0)
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
    more_info = models.URLField(max_length=200)


class Press(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete = models.CASCADE, primary_key=True)
    upload = models.FileField(upload_to = 'files/', blank=True)

