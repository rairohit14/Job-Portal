from django.urls import path
from. import views

urlpatterns = [
    path('',views.home),
    path('register/', views.register),        #register page login
    path('login/', views.user_login),         #user login url
    path('logout/', views.user_logout),       #user logout url
    path('dashboard/', views.dashboard),      #dashboard url
    path('create-job/', views.create_job),    #job post url
    path('jobs/', views.job_list),            #job list url
    path('apply/<int:job_id>/', views.apply_job),     # Apply job feature url
    path('applied-jobs/', views.applied_jobs),        # Applied Jobs Page url
]