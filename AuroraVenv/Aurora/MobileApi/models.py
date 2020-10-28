from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Color(models.Model):
    colors_artist_name = models.CharField(max_length=100,blank=False)
    colors_song_title = models.CharField(max_length=100,blank=False)
    colors_artist_photo = models.URLField(blank=False)
    colors_cover_photo = models.URLField(blank=False)
    colors_video = models.URLField(blank=False)
    post_instagram_link = models.URLField(blank=True)
    post_date = models.DateField(auto_now_add=True)

    objects = models.Manager()


class Notification(models.Model):
    notification_title = models.CharField(max_length=50,blank=False)
    notification_message = models.CharField(max_length=150,blank=False)
    notification_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)

    objects = models.Manager()

class UserAccount(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    user_mobile = models.CharField(max_length=10,blank=False)
    user_street_address_1 = models.CharField(max_length=150,blank=False)
    user_street_address_2 = models.CharField(max_length=150,blank=True)
    user_city = models.CharField(max_length=150,blank=False)
    user_province = models.CharField(max_length=150,blank=False)
    user_country = models.CharField(max_length=150,blank=False)

    objects = models.Manager()
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    user_order_id = models.CharField(max_length=150,blank=False)
    order_song = models.CharField(max_length=150,blank=False)
    order_item = models.CharField(max_length=150,blank=False)
    order_date = models.DateField(auto_now_add=False)
    order_price = models.CharField(max_length=150,blank=False)
    order_placed = models.BooleanField()
    order_on_its_way = models.BooleanField()
    order_completed = models.BooleanField()

    objects = models.Manager()

#listen for when a new user has been created, if so execute the create_user_account function
def create_user_account(sender, **kwargs):
    if kwargs["created"]:
        new_user = UserAccount.objects.create(user=kwargs["instance"])
post_save.connect(create_user_account, sender=User)