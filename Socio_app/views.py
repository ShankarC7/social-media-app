
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from Socio_app.models import Users,Story,Post,ActiveFriend,UPost,UserProfile

from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
import random

from django.http import HttpResponseRedirect, JsonResponse
from .models import UPost  # Import your Upost model

from django.http import HttpResponse
from .models import Video
from Socio_app.models import Thread
from django.contrib.auth.decorators import login_required




from .forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# Storyvdo
def video_view(request):
    video_data = Video.objects.first()  # Fetch the video data from the database (you can use 'filter' or 'get' based on your logic)
    return render(request, 'index.html', {'video_data': video_data})
#Post

#def handle_post_submission(request):
   # if request.method == 'POST':
    #    post_text = request.POST.get('postTextArea', '')  
     #   video_file = request.FILES.get('videoInput')
      #  photo_file = request.FILES.get('photoInput')

       # new_post = Post(text=post_text)
        #if video_file:
         #   new_post.video = video_file
        #if photo_file:
         #   new_post.image = photo_file
        #new_post.save()

        #return HttpResponse('Post submitted successfully')
    #return HttpResponse('Failed to submit post')

#Story Video upload
def upload_video(request):
         # Assuming there's a title field in the form
        video_file = request.FILES['videoUpload']  # 'videoUpload' should match the input field name

        # Create and save the video object to the database
        new_video = Video( video_file=video_file)
        new_video.save()

         # Redirect to success page or handle as needed

        return render(request, 'index.html')  # Render the upload form template


#Search Box
def profile_view(request):
    user_profile = User.objects.get(user=request.user)  # Fetch the user's profile from the database
    return render(request, 'profile.html', {'user_profile': user_profile})

#index Html

def home(request):
   #p=UPost.objects.filter(is_active=True)
  # print(p)
  # context={}
  # context['UPosts']=p
   uposts = UPost.objects.all()  # Fetch UPost objects from the database
   context = {
        'UPosts': uposts 
    }
   return render(request,'index.html',context)
   
   #return render(request,'index.html')





def your_view(request):
    usernames = UPost.objects.values_list('username', flat=True)
    return render(request, 'index.html', {'usernames': usernames})


def get_usernames(request):
    usernames = UPost.objects.values_list('username', flat=True)
    return JsonResponse({'usernames': list(usernames)})
'''
def submit_post(request):
    if request.method == 'POST':
        text = request.POST.get('postTextArea', '')  # Get the text from the form
        image = request.FILES.get('photoInput')  # Get the image file from the form
        
        # Default username
        default_username = 'Kanhaiya'

        # Check if 'text' is not empty before saving
        if text.strip():  # This ensures the 'text' is not only whitespace
            new_post = UPost(description=text, image=image, username=default_username)
            new_post.save()
            return HttpResponseRedirect('home/')  # Change this to the appropriate URL

    return render(request, 'index.html')
'''
def submit_post(request):
    if request.method == 'POST':
        text = request.POST.get('postTextArea', '')  # Get the text from the form
        image = request.FILES.get('photoInput')  # Get the image file from the form
        
        # Default username
        default_username = 'Kanhaiya'

        # Fetch the default profile picture for the user 'Kanhaiya'
        user = User.objects.get(username=default_username)
        default_profile_pic = UserProfile.objects.get(user=user).profile_pic

        # Check if 'text' is not empty before saving
        if text.strip():  # This ensures the 'text' is not only whitespace
            new_post = UPost(description=text, image=image, username=default_username, profile_pic=default_profile_pic)
            new_post.save()
            return redirect('home')  # Change this to the appropriate URL

    return render(request, 'index.html')

def search(request):
    query = request.GET.get('query')
    if query:
        allposts = UserProfile.objects.filter(user__username__icontains=query)
        params = {'allpost': allposts}
        return render(request, 'search.html', params)
    else:
        return HttpResponse('No search query provided.')


def aftrlogin(request):
    uposts=UPost.objects.all()
    return render(request,'index.html',{'UPosts': uposts })

'''
def registration(request):
    if request.method == 'POST' :
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request,'index.html',{'user_form':user_form}) 
    else:
        user_form=RegistrationForm()
    return render(request,'register.html',{'user_form':user_form})

'''

def register(request):
    if request.method=='POST':
        uname =request.POST['uname']
        uemail =request.POST['uemail']
        upass =request.POST['upass']
        ucpass =request.POST['ucpass']
        profile_pic = request.FILES.get('profile_pic')
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Fields can not be Empty"
            return render (request,'register.html',context)
        elif upass != ucpass:
            context['errmsg']="Password  & confirm password didn't match"
            return render (request,'register.html',context)
        else:
         try:
                    u=User.objects.create(password=upass,username=uname,email=uemail)
                    u.set_password(upass)
                    u.save()

                    if profile_pic:
                     user_profile = UserProfile.objects.create(user=u, image=profile_pic)
                     user_profile.save()

                    context['success']="User created successfully !! Please Login"
                    return render(request,'register.html',context)
           
         # return HttpResponse("User Created Successfully")
         except Exception:
            context['errmsg']="User with same username already exists"
            return render(request,'register.html',context)
    else:
         return render(request,'register.html')


def user_login(request):
     if request.method =='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        #print(uname,"-",upass)
        #return HttpResponse("Data is fetched")
        context={}
        if uname=="" or upass=="":
            context['errmsg']="Fields should not be Empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u is not None:
                login(request,u)
                return redirect("/home")
            else:
                context['errmsg']="invalid Username and Password"
                return render(request,"login.html",context)
     else:
         return render(request,'login.html')
     
def user_logout(request):
    logout(request)
    return redirect('/login')

#------------------------message-----------------------------

def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)

def friends(request):
    return render(request,'friend.html')

def profile_form(request):
    # Pass the logged-in user to the template context
    return render(request, 'profile.html', {'user': request.user})

