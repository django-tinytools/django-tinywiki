# Generated by Django 4.2.6 on 2024-01-02 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('is_builtin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=512, unique=True)),
                ('title', models.CharField(max_length=512)),
                ('content', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('edited_reason', models.CharField(blank=True, max_length=1024, null=True)),
                ('userlock', models.BooleanField(default=False)),
                ('editlock', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tinywiki_pages_created', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tinywiki_pages_edited', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tinywiki_pages', to='django_tinywiki.wikilanguage')),
            ],
        ),
        migrations.CreateModel(
            name='WikiPageBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=512)),
                ('title', models.CharField(max_length=512)),
                ('content', models.TextField(blank=True)),
                ('created_on', models.DateTimeField()),
                ('edited_on', models.DateTimeField()),
                ('edited_reason', models.CharField(blank=True, max_length=1024, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tinyiwki_pagebackups_created', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tinywiki_pagebackups_edited', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tinywiki_backup_pages', to='django_tinywiki.wikilanguage')),
                ('wiki_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backups', to='django_tinywiki.wikipage')),
            ],
        ),
    ]
