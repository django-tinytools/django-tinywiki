from .view import ViewBase
from ..forms.auth import LoginForm,SignupForm
from django.contrib.auth.models import User,Group

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.conf import settings as django_settings
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password

from .. import settings
class LoginView(ViewBase):
    template="django_tinywiki/auth/login.html"

    def get(self,request):
        if request.user.is_authenticated:
            print("USER ALREADY LOGGED IN")
            if 'n' in request.GET:
                return redirect(urlsafe_base64_decode(request.GET['n']).decode('utf-8'))
            elif 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect(self.home_url)
        
        form = LoginForm()
        context = self.get_context(request,form=form)
        return render(request,self.template,context)

    def post(self,request):
        if request.user.is_authenticated:
            return redirect(self.home_url)
        
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
                if "n" in request.GET:
                    return redirect(urlsafe_base64_decode(request.GET['n']).decode('utf-8'))
                elif "next" in request.GET:
                    return redirect(request.GET['next'])
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
    template=settings.TINYWIKI_SIGNUP_TEMPLATE
    success_template=settings.TINYWIKI_SIGNUP_SUCCESS_TEMPLATE

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
            username=form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                context["errors"] += [_("Username \"{name}\" exists!").format(name=user.username)]
                name_is_valid = False
            except User.DoesNotExist:
                name_is_valid = True
                form_data["username"] = username
            try:
                user = User.objects.get(email=form.cleaned_data["email"])
                context["errors"] += [_("Email \"{email}\" exists!").format(email=user.email)]
                email_is_valid = False
            except User.DoesNotExist:
                email_is_valid = True
                form_data["email"] = form.cleaned_data["email"]

            if form.cleaned_data["password0"] == form.cleaned_data["password1"]:
                password = form.cleaned_data['password0']
                password_is_valid = True
            else:
                context["errors"] += [_("Passwords don't match!")]
                password_is_valid = False

            first_name = form.cleaned_data['first_name']
            form_data['first_name'] = first_name
            last_name = form.cleaned_data['last_name']
            form_data['last_name'] = last_name

            if not first_name:
                first_name = None
            if not last_name:
                last_name = None

            if name_is_valid and email_is_valid and password_is_valid:
                    user = User.objects.create(username=username,
                                               email=form.cleaned_data["email"],
                                               first_name=first_name,
                                               last_name=last_name)
                    user.password = make_password(password)
                    for grp_name in settings.TINYWIKI_DEFAULT_GROUPS:
                        try:
                            group = Group.objects.get(name=grp_name)
                            user.groups.add(group.id)
                        except Exception as err:
                            print("[django_tinywiki/views/auth.py:SignupView] Unable to add user to group {group}! ({reason})".format(
                                group=grp_name,
                                reason=str(err)
                            ))
                    user.save()

                    if "next" in request.GET:
                        context["login_url"] = self.login_url + "?next=" + request.GET["next"]
                    
                    return render(request,self.success_template,context)
                    
                
        if not "form" in context:
            context["form"] = SignupForm(form_data)

        return render(request,self.template,context)

class ProfileView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,"django_tinywiki/auth/signup.html",context)
        

    def post(self,request):
        pass

class SingupSuccess(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,settings.TINYWIKI_SIGNUP_SUCCESS_TEMPLATE,context)