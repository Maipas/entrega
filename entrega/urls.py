from django.contrib import admin
from django.urls import path, include
from entrega.views import index, contacto, search, login_view,logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('carreras/', include ('carreras.urls')),
    path('alumnos/', include ('alumnos.urls')),
    path('docentes/', include ('docentes.urls')),
    path('contacto/', contacto, name = 'contacto'),
    path('search/', search, name = 'search'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)