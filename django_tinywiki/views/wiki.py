from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.utils.translation import gettext
from django.contrib.auth import get_user_model

import re

_ = gettext

from .. import settings

from ..models import (
    WikiPage,
    WikiPageBackup,
    WikiLanguage,
    WikiImage
)

from ..forms.wiki import PageForm

import os

from ..functions import (
    user_can_create_pages,
    get_language_code,
    render_markdown)

from .view import ViewBase
# Create your views here.

class WikiPageView(ViewBase):
    page_template = settings.TINYWIKI_PAGE_VIEW_TEMPLATE

    def get_context(self,request,page=None,**kwargs):
        context = super().get_context(request,page=page,**kwargs)
        if page:
            context.update({
                "header_subtitle": page.title,
                "title":page.title,
                "content": render_markdown(page.content)
            })

        return context

    def get(self,request,page):

        try:
            p = WikiPage.objects.get(slug=page)
            pattern = re.compile("\!\[\[([0-9]+?)\]\]")
            page_images = p.images.all()
            re_linked_images = [int(i) for i in re.findall(pattern,p.content)]            

            orphaned_images = []
            image_ids = []


            for i in page_images:
                image_ids.append(i.id)
                if i.id not in re_linked_images:
                    orphaned_images.append(i)   
            

            context = self.get_context(request=request,page=p,
                                       images=page_images,
                                       orphaned_images=orphaned_images)

        except WikiPage.DoesNotExist:
            if self.get_user_can_create_pages(request.user):
                return redirect(reverse(settings.TINYWIKI_PAGE_CREATE_URL,args=[page]))

            context = self.get_context(request)

            content_file = os.path.join(os.path.dirname(__file__),"en.404.md")
            title = _("404 - Page not found!")
            check_file = os.path.join(os.path.dirname(__file__),'.'.join((get_language_code,"404","md")))
            if os.path.isfile(check_file):
                content_file = check_file

            with open(content_file,"r") as ifile:
                page_content = ifile.read()

            context.update({
                'header_subtitle': title,
                'title': title,
                'content': render_markdown(page_content)
            })

        return render(request,self.page_template,context)

class WikiIndexView(WikiPageView):
    index_page=settings.TINYWIKI_INDEX

    def get(self,request):
        return WikiPageView.get(self,request,page=self.index_page)

class WikiCreateView(ViewBase):
    template = settings.TINYWIKI_PAGE_EDIT_TEMPLATE
    
    def get(self,request,page=None):
        context=self.get_context(request=request)
        if page:
            try:
                p = WikiPage.objects.get(slug=page)
                return redirect(reverse(settings.TINYWIKI_PAGE_EDIT_URL,kwargs={'page':page}))
            except WikiPage.DoesNotExist:
                pass
        #user_language = request.user.wiki_language
        form_defaults={
            'user':request.user,
        }
        if page is not None:
            form_defaults['slug'] = page
        context['form'] = PageForm(form_defaults)
        return render(request,self.template,context)

    def post(self,request,page=None):
        context = self.get_context(request=request,page=page)

        form = PageForm(request.POST)
        context['form'] = form

        if form.is_valid():
            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(id=form.cleaned_data['user'])
            except UserModel.DoesNotExist:
                user = request.user

            try:
                language = WikiLanguage.objects.get(code=form.cleaned_data['language'])
            except WikiLanguage.DoesNotExist:
                language = WikiLanguage.objects.all().order_by('id')[0]
                
            create_page_kwargs = {
                'slug': form.cleaned_data['slug'],
                'user': user,
                'title': form.cleaned_data['title'],
                'language': language,
                'content': form.cleaned_data['content'],
                'created_by': request.user,
                'edited_by': request.user,
                'userlock': form.cleaned_data['userlock'],
                'editlock': form.cleaned_data['editlock'],
                'edited_reason': "Page created",
            }

            try:
                p = WikiPage.objects.create(**create_page_kwargs)
                return redirect(reverse(settings.TINYWIKI_PAGE_VIEW_URL,kwargs={'page':p.slug}))
            except Exception as error:
                context['error'] = str(error)
                
        return render(request,self.template,context)

class WikiEditView(ViewBase):
    template = settings.TINYWIKI_PAGE_EDIT_TEMPLATE

    def get(self,request,page):
        
        try:
            p = WikiPage.objects.get(slug=page)
        except WikiPage.DoesNotExist:
            return redirect(reverse(settings.TINYWIKI_PAGE_CREATE_URL,kwargs={'page':page}))
        
        if p.user:
            page_user_id = p.user.id
        else:
            page_user_id = request.user.id

        form_data={
            'slug':page,
            'user':page_user_id,
            'language':p.language.code,
            'title': p.title,
            'content': p.content,
            'userlock': p.userlock,
            'editlock': p.editlock
        }
        form = PageForm(form_data)

        context = self.get_context(request=request,page=p,form=form,slug=p.slug)
        
        return render(request,self.template,context)
    
    def post(self,request,page):
        
        try:
            p = WikiPage.objects.get(id=page)
        except WikiPage.DoesNotExist:
            return redirect(reverse(settings.TINYWIKI_PAGE_CREATE_URL,kwargs={'page':page}))
        
        form = PageForm(request.POST)
        if form.is_valid():
            UserModel = get_user_model()
            
            backup_kwargs = {
                'wiki_page': p,
                'slug': p.slug,
                'title': p.title,
                'language': p.language,
                'content': p.content,
                'user': p.user,
                'created_on': p.created_on,
                'created_by': p.created_by,
                'edited_on': p.edited_on,
                'edited_by': p.edited_by,
                'edited_reason': p.edited_reason
            }
            pbackup = WikiPageBackup.objects.create(**backup_kwargs)

            if p.slug != form.cleaned_data['slug']:
                p.slug = form.cleaned_data['slug']

            p.title = form.cleaned_data['title']
            try:
                p.user = UserModel.objects.get(id=form.cleaned_data['user'])
            except UserModel.DoesNotExist:
                pass

            try:
                p.language = WikiLanguage.objects.get(code=form.cleaned_data['language'])
            except WikiLanguage.DoesNotExist:
                pass

            p.content = form.cleaned_data['content']
            p.editlock = form.cleaned_data['editlock']
            p.userlock = form.cleaned_data['userlock']
            p.edited_by = request.user
            p.edited_reason = form.cleaned_data['edited_reason']
            p.save()

            return redirect(reverse(settings.TINYWIKI_PAGE_VIEW_URL,kwargs={'page':p.slug}))

        context = self.get_context(request=request,page=p,form=form,slug=p.slug)

        return render(request,self.base_template,context)
