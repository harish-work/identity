from django.urls import path
from .views import CreateIdentifyView,GetIdentifyView,IdentifyView
urlpatterns = [
    path('create_identify/', CreateIdentifyView.as_view(),name='create-identify'),
    path('get_identify/', GetIdentifyView.as_view(),name='get-identify'),
    path('identify/', IdentifyView.as_view(),name='identify'),
]