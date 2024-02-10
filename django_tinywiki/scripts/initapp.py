from .. import functions as func

from .. import settings
import sys

from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string

def run():
    UserModel = get_user_model()
    user = None
    try:
        user = UserModel.objects.get(email=settings.TINYWIKI_USER["email"])
        try:
            user.is_superuser = True
            user.save()
        except:
            pass
    except UserModel.DoesNotExist:
        try:
            user = UserModel.objects.create(**settings.TINYWIKI_USER)
            user.password = get_random_string(length=32)
            user.is_superuser = True
            user.save()
        except Exception as err:
            print(_("Unable to create TinyWiki user! ({error_message})").format(error_message=str(err)),file=sys.stderr)
            for i in UserModel.objects.filter(is_superuser=True).order_by('id'):
                if i.is_superuser:
                    user = i
                    break
    if user is None:
        raise LookupError("No user to select to initialize TinyWiki! ABORTING!")
    
    func.init.init_app(user)



