from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'store'
urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("<int:product_type>/", views.index, name="index"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name='add-to-cart'),
    path("quantity-up/<int:item_id>/", views.quantity_up, name="quantity-up"),
    path("quantity-down/<int:item_id>/", views.quantity_down, name="quantity-down"),
    path("contact/", views.contact, name="contact"),
    path("about-us/", views.about_us, name="about-us")
]