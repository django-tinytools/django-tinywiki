from django import forms
from django.utils.translation import gettext_lazy as _, gettext
from ..models.language import WikiLanguage
from .. import settings
from django.contrib.auth import get_user_model

def _get_language_choices():
    ret = []
    for lang in WikiLanguage.objects.all().order_by("name"):
        if lang.is_builtin:
            ret.append((lang.code,gettext(lang.name)))
        else:
            ret.append((lang.code,lang.name))
    return ret

def _get_user_choices():
    ret = []
    for user in get_user_model().objects.all():
        inserted = False
        username = user.get_username()
        for i in range(len(ret)):
            if user.username < ret[i][1]:
                ret.insert(i,(user.id,username))
                inserted = True
        if not inserted:
            ret.append((user.id,username))

    return ret

class PageForm(forms.Form):
    slug = forms.CharField(max_length=512,
                           required=True,
                           label=_("Slug"))
    user = forms.ChoiceField(choices=_get_user_choices,
                             required=True,
                             label=_("User"))
    language = forms.ChoiceField(choices=_get_language_choices,
                                 required=True,
                                 label=_("Language"),
                                 initial=settings.TINYWIKI_DEFAULT_LANGUAGE)
    
    title = forms.CharField(max_length=512,
                            required=True,
                            label=_("Title"))
    content = forms.CharField(widget=forms.Textarea(),
                              required=False,
                              label=_("Content"))
    userlock = forms.BooleanField(initial=False,
                                  label=_("Do not allow other users to edit this page."))
    editlock = forms.BooleanField(initial=False,
                                  label=_("Do not allow editing of this page."))
    edited_reason = forms.CharField(initial="",
                                    empty_value=True,
                                    required=False,
                                    label=_("Reason for editing this page"))
    
class ImageUploadForm(forms.Form):
    alt_text = forms.CharField(max_length=1024,
                               required=True,
                               label=_("Alternative Text"))
    description = forms.CharField(max_length=1024,
                                  required=False,
                                  label=_("Descriptions"))
    image = forms.ImageField(label=_("Image to upload"))

class DeletePageForm(forms.Form):
    delete_page = forms.BooleanField(label=_("Delete Page?"),initial=False,required=False)
    delete_images = forms.BooleanField(label=_("Delete Images too?"),initial=False,required=False)