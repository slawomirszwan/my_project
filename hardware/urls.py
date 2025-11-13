from django.urls import path
from . import views


urlpatterns = [
    # 3 parametry  path, funkcję wskazanie na rozwiązanie co ma robić , nazwa rooty
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('numer/<int:numer_id>', views.numer, name='numer'), #http://127.0.0.1:8000/hardware/numer/54
    #ale nie  http://127.0.0.1:8000/hardware/numer/

]


