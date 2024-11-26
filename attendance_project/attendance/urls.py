from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),

    # models in this data base
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('departments/', views.department_list, name='department_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('students/', views.student_list, name='student_list'),
    path('attendance/', views.attendance_form, name='attendance_form'),
    path('attendance_list/', views.attendance_list, name='attendance_list'),

    #editing urls links
    path('edit_teacher/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('edit_department/<int:pk>/', views.edit_department, name='edit_department'),
    path('edit_subject/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('edit_subject/', views.edit_subject, name='edit_subject'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('edit_teacher/', views.edit_teacher, name='edit_teacher'),
    path('edit_department/<int:pk>/', views.edit_department, name='edit_department'),
    path('edit_subject/', views.edit_subject, name='edit_subject'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),

    #deleting models link
    path('delete_subject/<int:pk>/', views.delete_subject, name='delete_subject'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('delete_teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),

    #adding models
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_department/', views.add_department, name='add_department'),

    #user functionality
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', LoginView.as_view(template_name='attendance/login.html'), name='login'),
]
