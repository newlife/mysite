from django.urls import include, path
from django.contrib import admin
from polls.views import index

urlpatterns = [
    path('index/',index),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
