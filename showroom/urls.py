
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register('vehicles', views.VehiclesViewSet, basename='vehicles')
router.register('sellers', views.SellerViewSet, basename='sellers')
router.register('saves', views.SaveViewSet, basename='saves')

vehicle_router = routers.NestedDefaultRouter(
    router, 'vehicles', lookup='vehicles')
vehicle_router.register(
    'images', views.VehicleImageViewSet, basename='vehicle-images')

save_router = routers.NestedDefaultRouter(router, 'saves', lookup='saves')
save_router.register('saveditems', views.SavedItemViewSet, basename='saveditems')

seller_router = routers.NestedDefaultRouter(router, 'sellers', lookup='sellers')
seller_router.register('follows', views.FollowViewSet, basename='follows')

urlpatterns = router.urls + save_router.urls + \
    vehicle_router.urls + seller_router.urls
