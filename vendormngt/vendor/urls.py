from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    VendorCreateAPIView, VendorListView, VendorDetailView,
    VendorUpdateView, VendorDeleteView, PurchaseOrderCreateView,
    PurchaseOrderListView, PurchaseOrderDetailView, PurchaseOrderUpdateView,
    PurchaseOrderDeleteView, VendorPerformanceView,UserRegistrationAPIView,UserLoginAPIView
)

urlpatterns = [
    path('user/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('user/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vendors/', VendorListView.as_view(), name='vendo-list'),
    path('vendor/', VendorCreateAPIView.as_view(), name='vendor-create'),
    path('vendors/<int:vendor_id>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('vendors/<int:vendor_id>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('vendors/<int:vendor_id>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),
    path('orders/', PurchaseOrderCreateView.as_view(), name='order-create'),
    path('orders/list/', PurchaseOrderListView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', PurchaseOrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:order_id>/update/', PurchaseOrderUpdateView.as_view(), name='update-order'),
    path('orders/<int:order_id>/delete/', PurchaseOrderDeleteView.as_view(), name='delete-order'),
]
