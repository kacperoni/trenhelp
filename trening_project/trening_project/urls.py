from django.contrib import admin
from django.urls import path, include
from trenhelp.views import TrenhelpListView

urlpatterns = [
    path('',TrenhelpListView.as_view(),name='list_view'),
    path('trenhelp/',include('trenhelp.urls')),
    path('admin/', admin.site.urls),
]
