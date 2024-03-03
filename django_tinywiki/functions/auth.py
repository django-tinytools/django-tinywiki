from .. import settings
from ..models.wiki import WikiPage

def user_is_superuser(user):
    return (user and user.is_authenticated and user.is_superuser)


def user_can_create_pages(user):
    if not user.is_authenticated:
        return False

    if user.is_superuser and settings.TINYWIKI_SUPERUSER_IS_WIKI_ADMIN:
        return True
    
    if hasattr(user,"is_staff") and user.is_staff and settings.TINYWIKI_STAFF_IS_WIKI_ADMIN:
        return True
    return user.has_perm(settings.TINYWIKI_USERPERM_CREATE_PAGE)

def user_can_delete_pages(user):
    if not user.is_authenticated:
        return False
    
    if user.is_superuser and settings.TINYWIKI_SUPERUSER_IS_WIKI_ADMIN:
        return True
    
    if hasattr(user,"is_staff") and user.is_staff and settings.TINYWIKI_STAFF_IS_WIKI_ADMIN:
        return True
    
    return user.has_perm(settings.TINYWIKI_USERPERM_DELETE_PAGE)

def user_can_edit_pages(user):
    if not user.is_authenticated:
        return False
    
    if user.is_superuser and settings.TINYWIKI_SUPERUSER_IS_WIKI_ADMIN:
        return True
    
    if hasattr(user,"is_staff") and user.is_staff and settings.TINYWIKI_STAFF_IS_WIKI_ADMIN:
        return True
    
    return user.has_perm(settings.TINYWIKI_USERPERM_EDIT_PAGE)

def user_can_edit_page(user,page):
    if not user.is_authenticated:
        return False
    
    if not page:
        return False
    
    if user.is_superuser and settings.TINYWIKI_SUPERUSER_IS_WIKI_ADMIN:
        return True
    
    if hasattr(user,"is_staff") and user.is_staff and settings.TINYWIKI_STAFF_IS_WIKI_ADMIN:
        return True
    
    if isinstance(page,str):
        try:
            p = WikiPage.objects.get(slug=page)
        except WikiPage.DoesNotExist:
            return False
    elif isinstance(page,int):
        try:
            p = WikiPage.objects.get(id=page)
        except WikiPage.DoesNotExist:
            return False
    else:
        p = page

    if user.has_perm(settings.TINYWIKI_USERPERM_ADMIN):
        return True
    
    if not p.editlock and user.has_perm(settings.TINYWIKI_USERPERM_EDIT_PAGE):
        if not p.userlock:
            return True
        else:
            return p.user.id == user.id
        
    if (user.has_perm(settings.TINYWIKI_USERPERM_EDIT_USER_PAGE) and (p.user.id == user.id)):
        return True
    return False
