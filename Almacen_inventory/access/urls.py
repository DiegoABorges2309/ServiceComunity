from django.urls import path, include
from .views import LoginView
from rest_framework import routers
from access import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsersViewSet)
router.register(r'Preguntas Secretas', views.QuestionsViewSet)

urlpatterns = [
    path('a', include(router.urls)),
    path('login/', LoginView.as_view(), name= 'login'),
]