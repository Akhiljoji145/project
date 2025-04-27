from django.urls import path
from . import views
app_name='movie'
urlpatterns = [
    path('',views.home,name='home'),
    path('user_home/<int:user_id>/',views.user_home,name='userhome'),
    path('login/',views.login,name='login'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('logout/',views.logout_view,name='logout'),
    path('moviedetail/<int:mov_id>/',views.moviedetail,name='moviedetail'),
    path('moviedetail/<str:user_name>/<int:mov_id>/',views.usermoviedetail,name='usermoviedetail'),
    path('register/',views.user_reg,name='register'),
    path('user_details/<int:user_id>/',views.user_details, name='userdetails'),
    path('category/<int:cat_name>/',views.cat_movie, name='category'),
]