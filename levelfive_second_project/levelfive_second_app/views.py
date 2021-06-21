from django.shortcuts import render
from levelfive_second_app.forms import UserForm,UserProfileForm
from django.contrib.auth.models import User

#This all import for login and logout............................
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
#................................................................
# Create your views here.
def index(request):
    return render(request,'levelfive_second_app/index.html')

def register(request):
    registered = False


    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        user_profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit = False)
            profile.user = user  #creating that OneToOneField relation

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True



        else:
            print(user.errors,profile.errors)

    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()

    return render(request,'levelfive_second_app/register.html',context = {'user_form':user_form , 'user_profile_form':user_profile_form,'registered':registered})

def userlogin(request):

    if request.method == "POST":
        username = username.POST.get('username')
        password = password.POST.get('password')

        user = authenticate(username = 'username' , password = 'password')

        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse(index))

            else:
                return HttpResponse('Account not activate')


        else:
            print('Someone tried to login with username:{} and password:{}'.format(username,password))
    else:
        return render(request,'levelfive_second_app/login_logout.html',{})

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))
