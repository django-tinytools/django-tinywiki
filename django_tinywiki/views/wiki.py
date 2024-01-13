from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.utils.translation import gettext


_ = gettext

from .. import settings

from ..models import (
    WikiPage,
    WikiPageBackup,
    WikiLanguage,
)

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
            context = self.get_context(request,page=p)

        except WikiPage.DoesNotExist:
            if self.get_user_can_create_pages(request.user):
                return redirect(reverse(settings.TINYWIKI_PAGE_CREATE_URL))

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
    base_template = settings.TINYWIKI_BASE_TEMPLATE
    page_template = settings.TINYWIKI_PAGE_EDIT_TEMPLATE
    css = settings.TINYWIKI_CSS
    context_callback = settings.TINYWIKI_CONTEXT_CALLBACK

    def get(self,request,page=None):
        pass

    def post(self,request,page):
        pass

class WikiEditView(ViewBase):
    base_template = settings.TINYWIKI_BASE_TEMPLATE
    page_template = settings.TINYWIKI_PAGE_EDIT_TEMPLATE
    css = settings.TINYWIKI_CSS
    context_callback = settings.TINYWIKI_CONTEXT_CALLBACK

    def get(self,request,page):
        pass

    def post(self,request,page):
        pass
