from django.urls import path

from famsapp import views

urlpatterns = [
   path('', views.admin_home, name='admin_home'),
   path('home/', views.home, name='home'),
   path('view_teacher/', views.view_teacher, name='view_teacher'),
   path('view_student/', views.view_student, name='view_student'),
   path('view_group/', views.view_group, name='view_group'),
   path('view_program/', views.view_program, name='view_program'),
   path('view_programreg/', views.view_programreg, name='view_programreg'),
   path('view_result/', views.view_result, name='view_result'),
   path('view_scoreboard/', views.view_scoreboard, name='view_scoreboard'),
   path('add_teacher/', views.add_teacher, name='add_teacher'),
   path('add_student/', views.add_student, name='add_student'),
   path('add_group/', views.add_group, name='add_group'),
   path('view_group/', views.view_group, name='view_group'),
   path('add_program/', views.add_program, name='add_program'),
   path('view_program/', views.view_program, name='view_program'),
   # path('update_student/', views.update_student, name='update_student'),

   path('teacher_home/', views.teacher_home, name='teacher_home'),
   path('home_teacher/', views.home_teacher, name='home_teacher'),
   path('student_view/', views.student_view, name='student_view'),
   path('program_view/', views.program_view, name='program_view'),
   path('view_registration/', views.view_registration, name='view_registration'),
   path('add_result/', views.add_result, name='add_result'),
   path('view_result/', views.view_result, name='view_result'),



]