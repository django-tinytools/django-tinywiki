from .view import ViewBase
from ..forms.auth import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.conf import settings as django_settings
from django.utils.translation import gettext as _

from .. import settings
class LoginView(ViewBase):
    template="django_tinywiki/auth/login.html"

    def get(self,request):
        if request.user.is_authenticated:
            if 'next' in request.GET:
                return redirect(urlsafe_base64_decode(request.GET['next']))
            return redirect(reverse(self.home_url))
        form = LoginForm()
        context = self.get_context(request,form=form)

        return render(request,self.template,context)

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
                return redirect(self.home_url)

        context['form'] = LoginForm()
        return render(request,"django_tinywiki/auth/login.html",context)

class LogoutView(ViewBase):
    template="django_tinywiki/auth/logout.html"

    def get(self,request):
        if request.user.is_authenticated:
            logout(request)

        context = self.get_context(request)
        
        return render(request,self.template,context)

class SignupView(ViewBase):
    template="django_tinywiki/auth/signup.html"
    success_template="django_tinywiki/auth/signup-success.html"

    def get(self,request):
        context = self.get_context(request)
        
        form = SignupForm()
        context["form"] = form
        return render(request,self.template,context)

    def post(self,request):
        form = SignupForm(request.POST)
        context = self.get_context(request)
        context["errors"] = []

        if form.is_valid():
            form_data={}
            try:
                user = User.objects.get(username=form.cleaned_data["name"])
                context["errors"] += [_("Username \"{name}\" exists!").format(name=user.username)]
                name_is_valid = False
            except User.DoesNotExist:
                name_is_valid = True
                form_data["name"] = form.cleaned_data["name"]

            try:
                user = User.objects.get(email=form.cleaned_data["email"])
                context["errors"] += [_("Email \"{email}\" exists!").format(email=user.email)]
                email_is_valid = False
            except User.DoesNotExist:
                email_is_valid = True
                form_data["email"] = form.cleaned_data["email"]

            if name_is_valid and email_is_valid:
                if form.cleaned_data["password0"] == form.cleaned_data["password1"]:
                    user = User.objects.add(username=form.cleaned_data["name"],email=form.cleaned_data["email"])
                    user.password = form.cleaned_data["password0"]
                    user.groups.add(name="wiki-user")
                    user.save()

                    if "next" in request.GET:
                        context["login_url"] = self.login_url + "?next=" + request.GET["next"]
                    
                    return render(request,self.success_template,context)
                else:
                    context["errors"] += [_("Passwords don't match!")]
                
        if not "form" in context:
            context["form"] = SignupForm(form_data)

        return render(request,self.template,context)

class ProfileView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,"django_tinywiki/auth/signup.html",context)
        

    def post(self,request):
        pass