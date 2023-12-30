from django.contrib import admin
from Socio_app.models import Users,Story,Post,UPost,ActiveFriend,Video,UserProfile,Thread, ChatMessage
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q


# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','surname','username','email','is_active']
    list_filter=['is_active']

admin.site.register(Users, UsersAdmin)


class StoryAdmin(admin.ModelAdmin):
    list_display = ['id','video','username']
   
admin.site.register(Story, StoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','image','video']

admin.site.register(Post, PostAdmin)


class UPostAdmin(admin.ModelAdmin):
    list_display = ['id','post_date','description','image','video','is_active']
    list_filter=['is_active']
admin.site.register(UPost, UPostAdmin)


class ActiveFriendAdmin(admin.ModelAdmin):
    list_display = ['id','friend_name','last_active']

admin.site.register(ActiveFriend, ActiveFriendAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'video_file']
   
admin.site.register(Video, VideoAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','profile_pic']
   
admin.site.register(UserProfile, UserProfileAdmin)


admin.site.register(ChatMessage)


class ChatMessage(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessage]
    class Meta:
        model = Thread


admin.site.register(Thread, ThreadAdmin)
