from django.urls import path

from . import views


urlpatterns = [
    path('get_data/', views.ApiImportSet.as_view({'get': 'create'})),
]