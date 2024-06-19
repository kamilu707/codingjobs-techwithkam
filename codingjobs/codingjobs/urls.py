from django.contrib import admin
from django.urls import path
from coreapp.views import frontpage, signup, logout_view
from django.contrib.auth import views

from apps.job.views import job_detail
from apps.userprofile.views import dashboard

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='coreapp/login.html'), name="login"),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),

    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
]
