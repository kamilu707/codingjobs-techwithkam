from django.contrib import admin
from django.urls import path
from coreapp.views import frontpage, signup, logout_view
from django.contrib.auth import views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='coreapp/login.html'), name="login"),
    path('logout/', logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
