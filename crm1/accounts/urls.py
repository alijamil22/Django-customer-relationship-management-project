from django.urls import path
from . import views
urlpatterns = [
    # here the authentication and authorization will be implemented in the future.
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    # the main urls of the project
    path('',views.home,name='home'),
    path('user/',views.userPage,name='userPage'),
    path('account/',views.accountSettings,name='account'),
    path('products/',views.products,name='products'),
    path('customers/<str:pk>/',views.customer,name='customer'),
    path('create_order/<str:pk>/',views.createOrder,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),
]
