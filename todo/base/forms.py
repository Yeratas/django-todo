from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Task

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs.update(
            {'class':'px-1 py-2 w-full border-2 border-sky-600 rounded-lg :outline-none', 'placeholder':'Username'})
        
        self.fields['email'].widget.attrs.update(
            {'class':'px-1 py-2 w-full border-2 border-sky-600 rounded-lg :outline-none', 'placeholder':'Email'})
        
        self.fields['password1'].widget.attrs.update(
            {'class':'px-1 py-2 w-full border-2 border-sky-600 rounded-lg :outline-none', 'placeholder':'Password1'})
        
        self.fields['password2'].widget.attrs.update(
            {'class':'px-1 py-2 w-full border-2 border-sky-600 rounded-lg :outline-none', 'placeholder':'Password2'})
        
    def save(self):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','completion']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['title'].widget.attrs.update(
            {'class':'p-1 w-full border-2 border-sky-600 rounded-lg :outline-none'}
        )
        self.fields['description'].widget.attrs.update(
            {'class':'p-1 w-full border-2 border-sky-600 rounded-lg :outline-none'}
        )
        self.fields['completion'].widget.attrs.update(
            {'class':'p-2 m-2'}
        )