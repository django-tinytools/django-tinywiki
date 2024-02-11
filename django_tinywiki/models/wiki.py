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
    contentfile_md5 = models.CharField(null=True,max_length=32,default=None)
    user = models.ForeignKey(settings.TINYWIKI_AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='tinywiki_pages_user')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.TINYWIKI_AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinywiki_pages_created")
    edited_on = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(
        settings.TINYWIKI_AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinywiki_pages_edited")
    edited_reason = models.CharField(
        null=True,
        blank=True,
        max_length=1024)
    userlock = models.BooleanField(default=False)
    editlock = models.BooleanField(default=False)

    class Meta:
        indexes=[
            models.Index(name="tinywiki_wp_slug_index",fields=["slug"]),
            models.Index(name="tinywiki_wp_lang_index",fields=["language"]),
            models.Index(name="tinywiki_wp_user_index",fields=["user",]),
            models.Index(name="tinywiki_wp_cby_index",fields=["created_by"]),
            models.Index(name="tinywiki_wp_con_index",fields=["created_on"]),
            models.Index(name="tinywiki_wp_eby_index",fields=["edited_by"]),
            models.Index(name="tinywiki_wp_eon_index",fields=["edited_on"]),
        ]

        permissions = [
            (settings.TINYWIKI_PERM_CREATE_PAGE, "User can create pages"),
            (settings.TINYWIKI_PERM_DELETE_PAGE, "User can delete pages"),
            (settings.TINYWIKI_PERM_EDIT_PAGE, "User can edit all pages"),
            (settings.TINYWIKI_PERM_EDIT_USER_PAGE, "User can edit the pages he owns"),
        ]

# WikiPage class

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
    user = models.ForeignKey(settings.TINYWIKI_AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name="tinywiki_pagebackups_user")
    created_on = models.DateTimeField(null=False)
    created_by = models.ForeignKey(
        settings.TINYWIKI_AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinyiwki_pagebackups_created")
    edited_on = models.DateTimeField(null=False)
    edited_by = models.ForeignKey(
        settings.TINYWIKI_AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tinywiki_pagebackups_edited")
    edited_reason = models.CharField(
        null=True,
        blank=True,
        max_length=1024)
    
    class Meta:
        indexes=[
            models.Index(name="tinywiki_wpb_slug_index",fields=["slug"]),
            models.Index(name="tinywiki_wpb_user_index",fields=["user"]),
            models.Index(name="tinywiki_wpb_eby_index",fields=["edited_by"]),
            models.Index(name="tinywiki_wpb_eon_index",fields=["edited_on"]),
            models.Index(name="tinywiki_wpb_cby_index",fields=["created_by"]),
            models.Index(name="tinywiki_wpb_con_index",fields=["created_on"]),
            models.Index(name="tinywiki_wpb_language_index",fields=["language"]),
        ]
# WikiPageBackup class
    
class WikiImage(models.Model):
    wiki_page = models.ForeignKey(WikiPage,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  related_name="images")
    builtin_id = models.IntegerField(null=True,
                                     unique=True)
    alt = models.CharField(max_length=1024)
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
    uploaded_by = models.ForeignKey(settings.TINYWIKI_AUTH_USER_MODEL,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="tinywiki_image_uploads")
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes=[
            models.Index(name="tinywiki_wikiimage_upby_index",fields=["uploaded_by"]),
            models.Index(name="tinywiki_wikiimage_upon_index",fields=["uploaded_on"]),
            models.Index(name="tinywiki_wikiimage_page_index",fields=["wiki_page"]),
            models.Index(name="tinywiki_wikiimage_bid_index",fields=["builtin_id"]),
        ]
# WikiImage class
    