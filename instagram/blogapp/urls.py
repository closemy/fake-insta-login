"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls.i18n import i18n_patterns
from blog.views import DosyaViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from blog.views import veri_ekle
#http://127.0.0.1:8000/          =>homepage
#http://127.0.0.1:8000/index     =>homepage
#http://127.0.0.1:8000/blogs     =>blogs
#http://127.0.0.1:8000/blogs/3   =>blogs_details
router = DefaultRouter()
router.register(r'dosyalar', DosyaViewSet, basename='dosya')
app_name = 'blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.index, name='index'),
    path('',views.homepageview, name='home'),
    path('create/', views.create_data, name='create_data'),
    path('update/<int:data_id>/', views.update_data, name='update_data'),
    path('delete/<int:data_id>/', views.delete_data, name='delete_data'),
    path('read/', views.read_data, name='read_data'),
    path('deneme/', DosyaViewSet.as_view({'post': 'create'}), name='dosyalar'),
    path('upload/', views.upload_file, name='upload_file'),
    path('api/add_data_and_upload/', views.add_data_and_upload_file, name='add_data_and_upload_api'),
    path('veri-ekle/', views.veri_ekle, name='veri_ekle'),
    ]+ router.urls
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
