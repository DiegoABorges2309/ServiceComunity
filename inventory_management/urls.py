from django.urls import path
from .views import ItemGeneral, ItemSpecific

urlpatterns = [
    path('apisGeneral/', ItemGeneral.as_view()),
    path('apisSpecific/<str:name_item>/', ItemSpecific.as_view()),
]