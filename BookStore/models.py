# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    show_on_site = models.BooleanField(default=True)
    class Meta:
        abstract =True

class Author(BaseModel):
    author_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    def __str__(self):
        return self.author_name

class Language(BaseModel):
    lang_name = models.CharField(max_length=100)
    def __str__(self):
        return self.lang_name

class Book(BaseModel):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200)
    author = models.ForeignKey(Author,related_name="book",null=True)
    description = models.TextField(blank=True, null=True)
    book_image = models.ImageField(blank=True,upload_to="Shelf/images",help_text="upload size should be 400X400")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    isbn = models.IntegerField(unique=True)
    release_date = models.DateField(help_text='Select release date for this Book')
    language = models.ForeignKey(Language,related_name='books',null=True)
    pages = models.CharField(max_length=3)
    def __str__(self):
        return self.title

