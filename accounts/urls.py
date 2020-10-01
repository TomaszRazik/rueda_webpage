from django.urls import path, include, re_path
from figures import views as f_views
from accounts import views as a_views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='accounts/a_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', a_views.SignUpView.as_view(), name='signup'),

]
