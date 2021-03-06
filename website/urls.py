from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('teachers', views.teachers, name='teachers'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
