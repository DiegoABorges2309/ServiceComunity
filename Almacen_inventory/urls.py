from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include("inventory_management.urls")),
    path('access/', include("access.urls"))
]