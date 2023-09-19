from django.conf.urls.static import static
from django.urls import path

from ImageProcessor import settings
from ImageUpload import views

urlpatterns = [
    path('form/', views.form_upload, name='form_upload'),
    path('images/', views.list_of_files, name='list_of_files')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

