from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('store/<str:pk>/', views.render_items, name="item"),
]
