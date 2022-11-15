from django.urls import path
from . import views

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/student/', views.loginStudent, name='loginStudent'),
    path('login/faculty/', views.loginFaculty, name='loginFaculty'),
    path('register/', views.register, name='register'),
    path('register/student/', views.registerStudent, name='registerStudent'),
    path('register/faculty/', views.registerFaculty, name='registerFaculty'),

    # path('reset_password', auth_view.PasswordChangeView.as_view(), name='password_reset'),
    # path('reset_password_done', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_password_complete', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('reset_password/', views.reset_password, name='password_reset'),
    path('reset_change_password/', views.reset_change_password, name='password_reset_change')
]