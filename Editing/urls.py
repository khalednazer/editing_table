from django.urls import path, include
from . import views
urlpatterns = [
    path('aaa/',views.test, name='bbb' ),
    path('test',views.confDel, name='test' ),

]