from django.contrib import admin
from django.urls import path
from grabezy_app import views

urlpatterns = [
    path('',views.entry,name='Login'),
    path('index',views.index,name='Index'),
    path('about/',views.about,name='About'),
    path('contact/',views.contact,name='Contact'),
    path('search/',views.search,name='Search'),
    path('electronics/',views.electronics,name='Electronics'),
    path('fashion/',views.fashion,name='Fashion'),
    path('grocery/',views.grocery,name='Grocery'),
    path('cart/',views.cart,name='Cart'),
    path('checkout/',views.checkout,name='Checkout'),
    path('tracker/',views.tracker,name='Tracker'),
    path('profile/',views.profile,name='Profile'),
    path('service/',views.service,name='Service'),
    path('termofuse/',views.termofuse,name='TermOfuse'),
    path('privacy/',views.privacy,name='Privacy'),
    path('signup',views.handlesignup,name='signup'),
    path('home',views.home,name='Home'),
    path('logout',views.handlelogout,name='Logout'),
    path('success',views.success,name='Success'),
]
