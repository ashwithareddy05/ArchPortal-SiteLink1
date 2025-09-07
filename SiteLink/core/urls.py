from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('firm/dashboard/', views.firm_dashboard, name='firm_dashboard'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),

    path('internship/apply/<int:internship_id>/', views.apply_internship, name='apply_internship'),
    path('firm/post-internship/', views.post_internship, name='post_internship'),
    path('firm/internship/<int:internship_id>/delete/', views.delete_internship, name='delete_internship'),
    path('firm/internship/<int:internship_id>/applicants/', views.view_applicants, name='view_applicants'),
    path('firm/approve_project/<int:project_id>/', views.approve_project, name='approve_project'),

    path('internships/', views.internships_list, name='internships_list'),
    path('internship/<int:pk>/', views.internship_detail, name='internship_detail'),

    path('success/', TemplateView.as_view(template_name='core/success.html'), name='success'),
]
