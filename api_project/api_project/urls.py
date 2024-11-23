from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include URLs from the api app
]



from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]

