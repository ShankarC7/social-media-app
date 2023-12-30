from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Q
# Create your models here.

# Story vdo
class Video(models.Model):
  #  User = Upost.User
    video_file = models.FileField(upload_to='uploaded_videos/')
    username = models.CharField(max_length=100, default='Anonymous')

    def __str__(self):
        return f"Video uploaded by {self.username} ({self.id})"
#active Friends

class ActiveFriend(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=100)
    last_active = models.DateTimeField()

    def __str__(self):
        return f"{self.friend_name} - Last Active: {self.last_active}"

#UserPosts
class UPost(models.Model):
    username = models.CharField(max_length=100)  # Assuming the user is represented by a username for simplicity
    post_date = models.DateTimeField(auto_now_add=True)  # Date and time of the post
    description = models.TextField()  # Description of the post
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # For storing post images
    profile_pic = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)  # For storing post videos
    like_count = models.PositiveIntegerField(default=0)  # Like count for the post
    comment_count = models.PositiveIntegerField(default=0)  # Comment count for the post
    is_active=models.BooleanField(default=True,verbose_name="Available")
    def __str__(self):
        return f"Post by {self.username} at {self.post_date}"



#Post 

class Post(models.Model):
    text = models.TextField(default='')  # For storing the post text
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # For storing post images
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)  # For storing post videos
    username = models.CharField(max_length=100,  default='Anonymous')
    # You can add more fields as needed, such as user reference, timestamps, etc.

    def __str__(self):
        return f"Post by {self.username} ({self.id})"




#Story
class Story(models.Model):

    video = models.FileField(upload_to='story_videos/')  # For storing story videos
    username = models.CharField(max_length=100)  # Name of the user associated with the story

    # You can add more fields as needed, such as timestamps, user references, etc.

    def __str__(self):
        return self.username
    

# Search box 
class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    is_active=models.BooleanField(default=True,verbose_name="Available")
    # You can add more fields as needed, such as name, bio, etc.

    def __str__(self):
        return self.username

def default_profile_pic():
    return "/static/images/upload.png"  # Path to your default image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
    upload_to='profile_pics/',
    default=default_profile_pic,
    blank=True,
    null=True
    )

    # Other profile-related fields can be added here as needed

    def __str__(self):
        return self.user.username

    
class postinfo(models.Model):
    title=models.CharField(max_length=70)
    image=models.ImageField(upload_to='posts/')
    video=models.FileField(upload_to='posts/')
    description=models.TextField()
    def __str__(self):
        return self.description




User = get_user_model()

# Create your models here.

class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
