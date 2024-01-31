from django.db import models
from .. import settings

from .language import WikiLanguage

class WikiPage(models.Model):
    slug = models.SlugField(
        null=False,
        blank=False,
        max_length=512,
        unique=True)
    title = models.CharField(
        null=False,
        blank=False,
        max_length=512)
    language = models.ForeignKey(
        WikiLanguage,
        on_delete=models.RESTRICT,
        null=False,
        related_name="tinywiki_pages")
    content = models.TextField(null=False,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='tinywiki_pages_user')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinywiki_pages_created")
    edited_on = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinywiki_pages_edited")
    edited_reason = models.CharField(
        null=True,
        blank=True,
        max_length=1024)
    userlock = models.BooleanField(default=False)
    editlock = models.BooleanField(default=False)

class WikiPageBackup(models.Model):
    wiki_page = models.ForeignKey(
        WikiPage,
        on_delete=models.CASCADE,
        related_name="backups")
    slug = models.SlugField(
        null=False,
        blank=False,
        max_length=512)
    title = models.CharField(
        null=False,
        blank=False,
        max_length=512)
    language = models.ForeignKey(
        WikiLanguage,
        on_delete=models.RESTRICT,
        null=False,
        related_name="tinywiki_backup_pages")
    content = models.TextField(null=False,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name="tinywiki_pagebackups_user")
    created_on = models.DateTimeField(null=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinyiwki_pagebackups_created")
    edited_on = models.DateTimeField(null=False)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinywiki_pagebackups_edited")
    edited_reason = models.CharField(
        null=True,
        blank=True,
        max_length=1024)
    
class WikiImage(models.Model):
    wiki_page = models.ForeignKey(WikiPage,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name="images")
    builtin_id = models.IntegerField(null=True,
                                     unique=True)
    alt = models.CharField(max_length=1024,
                           null=True,
                           blank=True)
    description = models.CharField(max_length=1024,
                                   null=True,
                                   blank=True)
    image = models.ImageField(upload_to='images/original',
                              storage=settings.TINYWIKI_MEDIA_STORAGE)
    image_wiki = models.ImageField(storage=settings.TINYWIKI_MEDIA_STORAGE,
                                   null=True,
                                   upload_to='images/wiki')
    image_preview = models.ImageField(storage=settings.TINYWIKI_MEDIA_STORAGE,
                                      null=True,
                                      upload_to='images/preview')
    image_sidebar = models.ImageField(storage=settings.TINYWIKI_MEDIA_STORAGE,
                                      null=True,
                                      upload_to='images/sidebar')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL,
                                    null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    