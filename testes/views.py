# from typing import ClassVar
# from django.db import models
# from django.views.generic import TemplateView
from django import forms
from django.shortcuts import render,redirect
# from django.http import HttpResponseRedirect
# from django.views.generic.edit import CreateView
# from django.http import FileResponse
from django.http.response import HttpResponse
# from django.template import RequestContext
# from django.contrib import messages
import re
# from filtros.models import Teste
from filtros.models import Script

from .models import Image,Result
# from .models import Upload

from django.urls import reverse_lazy
import cv2
import mimetypes
import os

# class UploadCreate(CreateView):
#     model = Upload
#     fields = ['image']
#     template_name = 'testes/upload.html'
#     success_url = reverse_lazy('inicio')

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["imagefile"]




def historico():
    hist_path='uploads/historico.txt'
    r='\n'.join([i.code_name for i in Result.objects.all()])
    with open(hist_path,'w') as file:
        file.write(r)
    path = open(hist_path, 'r')
    mime_type, _ = mimetypes.guess_type(hist_path)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % 'historico.txt'
    os.remove(hist_path)
    return response


def cont(context):
    categorias = ['imagem', 'limiarização', 'morfologia']
    filtros_sep = [[] for i in range(len(categorias)+1)]
    filtros = [[i.nome, i.pk, i.categoria] for i in Script.objects.filter()]
    for i in filtros:
        if (low := i[2].lower()) in categorias:
            filtros_sep[categorias.index(low)].append(i)
        else:
            filtros_sep[len(categorias)].append(i)
    for count, cat in enumerate(categorias):
        context[cat] = filtros_sep[count]
    context['outros'] = filtros_sep[len(categorias)]
    context['codigo'] = SKPT(last.code_pk).codigo if (
        last := Result.objects.last()) else ''




def save_result(scpt,url_out,pk):
    result = Result()
    result.imagefile.name = url_out[8:]
    result.code_name=scpt.nome
    result.code_pk=pk
    result.save()




def create_file(scpt,url_in,url_out):
    image_in=cv2.imread('.'+url_in)
    image_out=image_in
    loc=locals()
    print(scpt.codigo)
    try: exec(scpt.codigo, globals(),loc)
    except: pass
    cv2.imwrite('.'+url_out, loc['image_out'])




def last(url):
    if last:=Result.objects.last():
        return '/uploads'+last.imagefile.name
    else:
        return url




def SKPT(pk):
    return Script.objects.filter(pk=pk)[0]





def get_form(request):
    form= ImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        Result.objects.all().delete()
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))




def showimage(request):
    imagefile= lastimage.imagefile if (lastimage:=Image.objects.last()) else None

    if(ret:=get_form(request)):
        return ret

    url_init='/uploads/'+imagefile.name
    url_out = ''

    if request.method == 'POST':
        if request.POST.get("historico"):
            return historico()
        if pk:=request.POST.get("data"):
            scpt=SKPT(pk)
            url_in=last(url_init)
            url_out='/uploads/results/_'+url_in.split('/')[-1]
            create_file(scpt,url_in,url_out)
            save_result(scpt,url_out,pk)
            return redirect(request.META.get('HTTP_REFERER'))

    context= {'imagefile': url_init,
              'result_file':last(url_out),
              'filename': imagefile.name[8:] if imagefile else '',
              }
    cont(context)
    print()
    return render(request, 'testes/upload.html', context)
