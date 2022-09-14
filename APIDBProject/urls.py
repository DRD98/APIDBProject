from django.urls import re_path
from DBApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^db/get/', views.get_none, name = 'get'),
    re_path(r'^db/get-val/', views.get, name = 'get_val'),
    re_path(r'^db/post/', views.post, name = 'post'),
    re_path(r'^db/put-raw/', views.put_raw, name = 'putraw'),
    re_path(r'^db/post-form/', views.post_form, name = 'postform'),
    re_path(r'^db/del/', views.delete, name = 'del'),
    re_path(r'^db/put/', views.put, name = 'put'),
    re_path(r'^db/upload/', views.upload, name = 'upload')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
