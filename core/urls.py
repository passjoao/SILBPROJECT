from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pesquisar/', views.RequestListViews.as_view(), name='pesquisa'),
    path('referencia/<int:pk>/', views.RequestDetailView.as_view(), name='request-detail'),
]