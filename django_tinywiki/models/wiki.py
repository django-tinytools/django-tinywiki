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
