from django.core.exceptions import PermissionDenied
from functools import wraps

def perm_superuser():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapper_view(request,*args,**kwargs):
            print(dir(request))
            if request.user and request.user.is_authenticated and request.user.is_superuser:
                return view_func(request,*args,**kwargs)
            raise PermissionDenied

        return _wrapper_view
    return decorator