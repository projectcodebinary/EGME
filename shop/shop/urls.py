from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from shopping import views
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^paytm/', include('paytm.urls')),
    # url(r'^changesizes/$',views.changesizes, name='changesizes'),
    url(r'^additem/$',views.addditem, name='addditem'),
    url(r'^checkout/$',views.checkout, name='checkout'),
    url(r'^$',views.nav, name='nav'),
    url(r'^SignUp/$', views.SignUp, name = 'signup'),
    url(r'^Login/$', views.Login, name = 'login'),
    url(r'^Logout/$', views.Logout, name = 'logout'),
    url(r'^ChangePassword/$', views.ChangePassword, name = 'changepassword'),
    url(r'^home/$', views.Home, name = 'Home'),
    url(r'^char/$', views.changeaddr, name = 'changeaddr'),
    url(r'^Logout/home/$', views.Home, name = 'Home'),
    path('admin/', admin.site.urls),
    url(r'^nav/$', views.nav , name = 'nav'),
    # url(r'^', views.product_list, name='product-list'),
    url(r'^index/$', views.index , name = 'index'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', views.add_to_cart, name="add_to_cart"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', views.delete_from_cart, name='delete_item'),
    url(r'^order-summary/$', views.order_details, name="order_summary"),
    url(r'^details/(?P<items>[-\w]+)/$', views.details,name='details'),
  ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()