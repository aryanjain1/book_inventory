from django.contrib import admin
from django.urls import path
from .views import sign_up,user_login,store,book,edit_book,user_logout,show_book,show_store,del_book,search

urlpatterns = [
    path('register/',sign_up,name='register'),
    path('login/',user_login),
    path('logout/',user_logout,name='logout'),
    path('store/',store,name='addstore'),
    path('book/<int:idd>/<str:id>/<str:title>/<path:img>',book,name='book'),
    path('show/<int:id>',show_book,name='show_book'),
    path('show1/',show_store,name='store'),
    path('show/edit_book/<int:id>/',edit_book),
    path('show/del_book/<int:id>/',del_book),
    path('search/<int:idd>',search,name='search'),
    path('', show_store),


]
