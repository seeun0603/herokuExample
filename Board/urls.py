
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#static 기능을 사용하기 위해서 가져오는거

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls'), name='main'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
