# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import UploadFileForm
import django_excel as excel
from .models import *


def IndexView(request):
    all_books = Book.objects.all()
    return render(request,'index.html', {'all_books': all_books})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES('file')
            return excel.make_response(filehandle.get_sheet(),"xls",file_name="download")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request,'upload_form.html',{'form': form,
                                              'title': 'Excel file upload and download example',
                                              'header': ('Please choose any excel file')
                                              })

#def import_data(request):
 #   if request.method == "POST":
  #      form = UploadFileForm(request.POST,
   #                           request.FILES)

#        def lang_func(row):
 #           q = Language.objects.filter(slug=row[0])[0]
  #          row[0] = q
   #         return row
    #    if form.is_valid():
     #       request.FILES['file'].save_book_to_database(
      #          models=[Language,],
       #         initializers=[None, lang_func],
        #        mapdicts=[
         #           ['lang_name'],
          #          ]
           # )
            #return redirect(upload_file)
       # else:
        #    return HttpResponseBadRequest()
    #else:
     #   form = UploadFileForm()
      #  return render(request, 'upload_form.html', {'form': form,
       #                                             'title': 'Excel file upload and download example',
        #                                            'header': ('Please choose any excel file')
         #                                           })








