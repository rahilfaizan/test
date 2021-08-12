
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('getconvo/', views.GetMsg.as_view()),
    path('contactapi/', views.ApiList.as_view()),
    path('tempapi/', views.TempList.as_view()),
    path('postmessage/', views.PostMessage),
    path('postcontact/', views.PostContact),
]
