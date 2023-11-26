from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Index
from .models import accounts
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.http import JsonResponse
from django.utils.translation import activate, get_language
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import MyFileModel
from .serializers import DosyaSerializer, AccountsSerializer
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from .forms import VeriForm
from django.contrib import messages

def index(request):
    return render(request,"blog/index.html")

def blogs(request):
    return render(request,"blog/blogs.html")

def blogs_details(request, id):
    return render(request,"blog/blog-details.html",{
       "id":id
    })  

def homepageview(request):
    return render(request, 'index.html')

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

def create_data(request):
    new_data = Index(isim='Yusuf', soyisim='Çelebi', email='yusufclb41@gmail.com', calistigibirim='stajyer', maas='700')
    new_data.save()
    return redirect('/')
    

def update_data(request, data_id):
    data = Index.objects.get(id=data_id)
    data.isim = 'deneme'
    data.soyisim = 'deneme'
    data.save()

def delete_data(request, data_id):
    data = accounts.objects.get(accountid=data_id)
    data.delete()    

def read_data(request):
    data_list = accounts.objects.all()

def upload_file(request):
   
    
    return redirect('/')

class DosyaViewSet(viewsets.ViewSet):
 serializer_class = DosyaSerializer
 
@api_view(['POST'])
def add_data_and_upload_file(request):
    if request.method == 'POST':
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        uploaded_file = request.FILES.get('uploadfiles')
        if uploaded_file:
            filename = request.data.get('filename')
            upload_folder = filename
            new_filename = f'{upload_folder}/{uploaded_file.name}'

            with open(new_filename, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

        return Response({'message': 'Veri ve dosya yükleme başarılı.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def veri_ekle(request):
    if request.method == 'POST':
        form = VeriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veri başarıyla kaydedildi.')
            return redirect('/')  # ya da istediğiniz başka bir sayfaya yönlendirin
        else:
            messages.error(request, 'Form geçerli değil. Lütfen hataları kontrol edin.')
    else:
        form = VeriForm()

    return render(request, 'base.html', {'form': form})



