from django.contrib import admin
from django.urls import path, include  # make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # assuming your app is named 'myapp'
]
