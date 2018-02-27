# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title','author','price','active','isbn','release_date','language','pages',)
    list_filter = ('author'),
    prepopulated_fields = {'slug': ('title',),}

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('author_name',)
    prepopulated_fields = {'slug': ('author_name',),}

class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ('lang_name',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Language,LanguageAdmin)