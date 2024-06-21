from django.urls import path, include


from .views import dashboard, view_application, view_dashboard_job

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('view_application/<int:application_id>/', view_application, name='view_application'),
    path('view_dashboard_job/<int:job_id>/', view_dashboard_job, name='view_dashboard_job'),
    

]