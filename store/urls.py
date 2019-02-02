from django.urls import path
from . import views
from authentication import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),

    # path('login/', auth_views.login_view, name='login'), # login
    # path('logout/', views.index, name='index'), # logout
    # path('register/', views.index, name='index'), # register player or developer

    # path('player/', views.index, name='index'), # show bought games @player
    # path('player/purchases/', views.index, name='index'), # show purchase history @player
    #
    path('developer/', views.developer_profile_page, name='dev_profile'),  # show own games @developer
    path('developer/submit/', views.add_game, name='add_game'),  # submit new game @developer
    #
    # path('search/', views.index, name='index'), # search, parameters via request.GET
    #
    # path('game/<slug:title>', views.index, name='index'), # game details
    # path('game/<slug:title>/buy/', views.index, name='index'), # buy game @player
    # path('game/<slug:title>/play/', views.index, name='index'), # play game @player @bought
    # path('game/<slug:title>/edit/', views.index, name='index'), # edit game @developer
    # path('game/<slug:title>/delete/', views.index, name='index'), # delete game @developer
]
