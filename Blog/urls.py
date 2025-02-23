from django.urls import path
from .views import post_list, post_details, signup_view, post_create, post_update, post_detele, post_like
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",post_list, name='post_list'),
    path("post/<int:id>/",post_details, name='post_details'),
    path("post/<int:id>/like",post_like, name='like'),
    
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup/',signup_view, name='signup'),
    
    path("post/create/", post_create, name='post_create'),
    path('post/update/<int:id>/', post_update, name='post_update'),
    path('post/delete/<int:id>/', post_detele, name='post_delete'),

]

