from django.contrib import admin
from django.urls import path, include
from trenhelp.views import TrenhelpListView,loginPage,registerPage,logoutPage

urlpatterns = [
    path('',TrenhelpListView.as_view(),name='list_view'),
    path('trenhelp/',include('trenhelp.urls')),
    path('admin/', admin.site.urls),
    path('login/',loginPage, name='login'),
    path('logout/',logoutPage, name='logout'),
    path('register/',registerPage, name='register')
]
