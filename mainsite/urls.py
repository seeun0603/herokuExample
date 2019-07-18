from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name = 'home'),
    path('new/', views.newBoard, name='newBoard'),
    path('list/', views.listBoard, name='listBoard'),
    path('view/<int:id>/', views.viewBoard, name='viewBoard'),
    path('updateDelete/<int:id>',views.updateDelete, name ='updateDelete'), #url 경로로 넘어갈때는 스트링으로 넘어가기 때문에 강제로 숫자형으로 바꿔야하고, 그 매개변수로 받았기 때문에 넘겨야한다.
    path('updatepage/<int:id>',views.updatepage, name='updatepage'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

