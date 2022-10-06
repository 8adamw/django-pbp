from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', wishlist_ajax, name='Wishlist_ajax'),
    path('ajax/submit/', wishlist_ajax_submit, name='Wishlist_ajax_submit'),
]