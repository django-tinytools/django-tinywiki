from django.views import View

from .. import settings
from django.contrib.auth.models import Group

class ViewBase(View):
    base_template = settings.TINYWIKI_BASE_TEMPLATE
    header_title = settings.TINYWIKI_TITLE
    css = settings.TINYWIKI_CSS
    context_callback = settings.TINYWIKI_CONTEXT_CALLBACK
    home_url = settings.TINYWIKI_HOME_URL
    page_view_url = settings.TINYWIKI_PAGE_VIEW_URL
    page_edit_url = settings.TINYWIKI_PAGE_EDIT_URL
    login_url = settings.TINYWIKI_LOGIN_URL
    logout_url = settings.TINYWIKI_LOGOUT_URL
    signup_url = settings.TINYWIKI_SIGNUP_URL

    def get_user_can_create_pages(self,user):
        if user.is_authenticated:
            if user.is_superuser:
                return True

            required_groups = ['wiki-admin','wiki-author']
            for check_group in Group.objects.all():
                if check_group.name in required_groups:
                    return True

        return False

    def get_user_can_edit_page(self,user,page=None):
        if user.is_authenticated:
            if user.is_superuser:
                return True
            if user.groups.filter(name="wiki-admin"):
                return True

            if page.editlock:
                return False

            if page.userlock:
                if page.created_by.id == user.id:
                    return True
                return False

            if user.groups.filter('wiki-author'):
                return True

        return False

    def user_can_delete_pages(self,user):
        if user.is_authenticated:
            if user.is_superuser or user.groups.filter(name="wiki-admin"):
                return True
        return False

    def get_context(self,request,page=None,**kwargs):
        context = {
            'base_template': self.base_template,
            'css': self.css,
            'user_can_create_pages': self.get_user_can_create_pages(request.user),
            'user_can_edit_page': self.get_user_can_edit_page(request.user,page),
            'header_title': self.header_title,
            'login_url': self.login_url,
            'logout_url': self.logout_url,
            'signup_url': self.signup_url,
            'home_url': self.home_url,
        }
        context.update(kwargs)
        context.update(self.context_callback(request))

        return context