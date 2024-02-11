from django.core.exceptions import PermissionDenied
from . import functions
from functools import wraps


def perm_superuser():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapper_view(request,*args,**kwargs):
            if request.user and request.user.is_authenticated and request.user.is_superuser:
                return view_func(request,*args,**kwargs)
            raise PermissionDenied

        return _wrapper_view
    return decorator

def perm_can_edit_page():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapper_view(request,page,*args,**kwargs):
            if functions.auth.user_can_edit_page(request.user,page):
                return view_func(request,page,*args,**kwargs)
            raise PermissionDenied
        
        return _wrapper_view
    return decorator
