from django.urls import include, path
from rest_framework import routers

from service import views

router = routers.DefaultRouter()
router.register(r'warehouse', views.WarehouseViewSet)
router.register(r'carmodel', views.CarModelViewSet)
router.register(r'workingprice', views.WorkingPriceViewSet)
router.register(r'acceptor', views.AcceptorViewSet)
router.register(r'maintenance', views.MaintenanceViewSet)
router.register(r'avto', views.AvtoViewSet)
router.register(r'registration', views.RegistrationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls