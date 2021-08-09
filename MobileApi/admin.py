from django.contrib import admin
from .models import Notification,Order,UserAccount,Color
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['user','user_mobile']
    ordering = ['-user']

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_user','notification_title']
    ordering = ['notification_user']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','user_order_id','order_date','order_placed','order_on_its_way','order_completed']
    ordering = ['-order_date']

class ColorsAdmin(admin.ModelAdmin):
    list_display = ['colors_artist_name','colors_song_title','post_date']
    ordering = ['-post_date']

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Color, ColorsAdmin)

admin.site.site_header = "Aurora Admin Panel"
admin.site.site_title = "Aurora Admin"
