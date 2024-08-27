from django.urls import include, path
from rest_framework import routers
from .views import FornecedorViewSet


router = routers.DefaultRouter()
router.register(r'fornecedor', FornecedorViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
