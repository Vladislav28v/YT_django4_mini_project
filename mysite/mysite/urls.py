from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('myapp/', include('myapp.urls',namespace="myapp")),
    path('admin/', admin.site.urls),

]
