from .view import ViewBase
from ..forms.auth import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.conf import settings as django_settings

class LoginView(ViewBase):
    def get(self,request):
        if request.user.is_authenticated:
            if 'next' in reqeust.GET:
                return redirect(urlsafe_base64_decode(reqeust.GET['next']))
            return redirect(reverse("tinywiki:index"))
        form = LoginForm()
        context = self.get_context(request)

        context['form'] = form

        return render(request,"django_tinywiki/auth/login.html",context)

    def post(self,request):
        form = LoginForm(request.POST)
        context = self.get_context(request)

        if form.is_valid():
            user = None
            
            if '@' in form.cleaned_data['name']:
                try:
                    u = User.objects.get(email=form.cleaned_data["name"])
                    username = u.username
                except User.DoesNotExist:
                    username = form.cleaned_data["name"]
            else:
                username = form.cleaned_data["name"]

            user = authenticate(request,
                                username=username,
                                password=form.cleaned_data['password'])

                
            if user is not None:
                login(request,user)
                if "next" in request.GET:
                    return redirect(urlsafe_base64_decode(request.GET['next']))
                return redirect(reverse("tinywiki:index"))

        context['form'] = LoginForm()
        return render(request,"django_tinywiki/auth/login.html",context)

class LogoutView(ViewBase):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)

        context = self.get_context(request)
        
        return render(request,"django_tinywiki/auth/logout.html",context)

class SignupView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,"django_tinywiki/auth/signup.html",context)

    def post(self,request):
        pass

class ProfileView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,"django_tinywiki/auth/signup.html",context)
        

    def post(self,request):
        pass