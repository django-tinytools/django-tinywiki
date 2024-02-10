from .view import ViewBase
from .. import settings
from django.shortcuts import render
from ..functions.init import init_app
from django.urls import reverse_lazy
from django.conf import settings as django_settings
from ..decorators import perm_superuser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ManageView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,self.base_template,context)
    
class InitializeView(ViewBase):
    template="django_tinywiki/manage/initialize.html"
    
    @method_decorator(login_required(login_url=settings.TINYWIKI_LOGIN_URL))
    @method_decorator(perm_superuser())
    def get(self,request,user=None):
        if not django_settings.DEBUG:
            try:
                init_app(request.user)
                init_success = True
            except:
                init_success = False
        else:
            init_app(request.user)
            init_success = True

        context = self.get_context(request,init_success=init_success)
        
        return render(request,self.template,context)
    
class PageListView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,self.base_template,context)
    
class PageView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,self.base_template,context)
    
class UserListView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,self.base_template,context)
    
class UserView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,self.base_template,context)