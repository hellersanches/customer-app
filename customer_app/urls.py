from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_customer, name='create'),
    path('success/', views.success_view, name='success'),
    path('customers/', views.list_customers, name='list'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete'),
]
