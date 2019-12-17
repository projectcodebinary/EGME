from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from shopping import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.shopping,name='shop' ),
    path('Login/',views.Login,name='Login'),
    path('Logout/',views.Logout,name='Logout'),
    path('SignUp/', views.SignUp,name='SignUp'),
    path('ChangePassword/', views.ChangePassword,name='ChangePassword'),
    path('index/',views.index, name='index'),
    path('index/Logout',views.Logout, name='Logout'),
]
