from django.contrib import admin
from django.urls import path

from coreapp.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]
