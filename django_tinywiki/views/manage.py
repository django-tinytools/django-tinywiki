from .view import ViewBase
from .. import settings
from django.shortcuts import render
from ..functions import init_app
from django.urls import reverse_lazy
class ManageView(ViewBase):
    def get(self,request):
        context = self.get_context(request)
        return render(request,self.base_template,context)
    
class InitializeView(ViewBase):
    template="django_tinywiki/manage/initialize.html"
    def get(self,request):
        try:
            init_app(request.user)
            init_success = True
        except:
            init_success = False

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