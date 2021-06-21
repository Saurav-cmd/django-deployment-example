from django import forms
from levelfive_second_app.models import UserprofileDetail
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserprofileDetail
        fields = ('profile_picture','site_protifilo')
