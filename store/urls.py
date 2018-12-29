from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # front page

    path('login/', views.login, name='login'),  # login
    path('logout/', views.index, name='logout'),  # logout
    path('register/', views.index, name='register'),  # register player or developer

    path('player/', views.index, name='player_home'),  # show bought games @player
    path('player/purchases/', views.index, name='purchases'),  # show purchase history @player

    path('developer/', views.index, name='developer_home'),  # show own games @developer
    path('developer/submit/', views.index, name='submit'),  # submit new game @developer

    path('search/', views.index, name='search'),  # search, parameters via request.GET

    path('game/<slug:title>', views.index, name='game'),  # game details
    path('game/<slug:title>/buy/', views.index, name='buy'),  # buy game @player
    path('game/<slug:title>/play/', views.index, name='play'),  # play game @player @bought
    path('game/<slug:title>/edit/', views.index, name='edit'),  # edit game @developer
    path('game/<slug:title>/delete/', views.index, name='delete'),  # delete game @developer
]
