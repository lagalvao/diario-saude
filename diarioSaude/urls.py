from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #o core é o nome  da aplicação que voce criou
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]