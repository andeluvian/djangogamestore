from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('library/', views.library, name='library'),
    path('user/', views.user_profile, name='user_profile'),

    path('developer/', views.developer_profile_page, name='dev_profile'),
    path('developer/submit/', views.add_game, name='add_game'),

    path('game/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('game/<int:pk>/edit/', views.GameEditView.as_view(), name='game_edit'),
    path('game/<int:pk>/play/', views.game, name='game'),
    path('game/<int:pk>/play/save/', views.save, name='save'),
    path('game/<int:pk>/play/load/', views.load, name='load'),

    path('api/v1/game/<int:pk>/score/', views.api_score, name='api_score'),
    path('api/v1/game/<int:pk>/score/submit/', views.api_score_submit, name='api_score_submit'),
]
