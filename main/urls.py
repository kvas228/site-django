from django.contrib import admin
from django.urls import path
from . import views


from django.conf.urls import include
from django.template.defaulttags import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import upload_image
import  django.contrib.staticfiles


urlpatterns = [
    path('admin',admin.site.urls),
    path('',views.index,name='home'),
    path('about-us',views.index1,name = 'about'),
    path('comments',views.index2,name = 'comments'),
    path('new',views.index3,name = 'new'),
    path('upload/', upload_image, name='upload_image'),
    path('m1',views.m1,name='m1'),
    path('m2',views.m2,name='m2'),
    path('m3',views.m3,name='m3'),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
