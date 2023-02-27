from django.urls import path
from mysite import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('shopping_detail/',views.shopping_detail,name='shopping_detail'),
    path('form/',views.form_name_view,name='form')
]
