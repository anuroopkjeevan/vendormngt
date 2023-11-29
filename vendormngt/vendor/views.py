from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from django.db.models import Count, Avg, F
from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens for the user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({"access_token": access_token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VendorCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VendorListView(APIView):
    def get(self, request, *args, **kwargs):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VendorDetailView(APIView):
    def get(self, request, vendor_id, *args, **kwargs):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"detail": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VendorUpdateView(APIView):
    def put(self, request, vendor_id, *args, **kwargs):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"detail": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VendorDeleteView(APIView):
    def delete(self, request, vendor_id, *args, **kwargs):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"detail": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response({"detail": "Vendor deleted successfully."}, status=status.HTTP_204_NO_CONTENT)




@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderListView(APIView):
    def get(self, request, *args, **kwargs):
        orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderDetailView(APIView):
    def get(self, request, order_id, *args, **kwargs):
        try:
            order = PurchaseOrder.objects.get(pk=order_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PurchaseOrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)





@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderUpdateView(APIView):
    def put(self, request, order_id, *args, **kwargs):
        try:
            order = PurchaseOrder.objects.get(pk=order_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PurchaseOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class PurchaseOrderDeleteView(APIView):
    def delete(self, request, order_id, *args, **kwargs):
        try:
            order = PurchaseOrder.objects.get(pk=order_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response({"detail": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)





@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class VendorPerformanceView(APIView):
    def get(self, request, vendor_id, *args, **kwargs):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"detail": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)

        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
        quality_rating_avg = calculate_quality_rating_avg(vendor)
        average_response_time = calculate_average_response_time(vendor)
        fulfillment_rate = calculate_fulfillment_rate(vendor)

        performance_data = {
            "on_time_delivery_rate": on_time_delivery_rate,
            "quality_rating_avg": quality_rating_avg,
            "average_response_time": average_response_time,
            "fulfillment_rate": fulfillment_rate,
        }

        return Response(performance_data, status=status.HTTP_200_OK)


def calculate_on_time_delivery_rate(vendor):
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed', delivery_date__lte=timezone.now()
    ).count()
    total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()

    if total_completed_orders == 0:
        return 0.0

    return (completed_orders / total_completed_orders) * 100.0

def calculate_quality_rating_avg(vendor):
    completed_orders_with_rating = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed', quality_rating__isnull=False
    ).aggregate(avg_rating=Avg('quality_rating'))['avg_rating']

    if completed_orders_with_rating is None:
        return 0.0

    return completed_orders_with_rating

def calculate_average_response_time(vendor):
    acknowledged_orders = PurchaseOrder.objects.filter(
        vendor=vendor, acknowledgment_date__isnull=False
    ).exclude(acknowledgment_date=F('issue_date'))

    if not acknowledged_orders.exists():
        return 0.0

    total_response_time = sum(
        (order.acknowledgment_date - order.issue_date).total_seconds() / 60.0
        for order in acknowledged_orders
    )

    return total_response_time / acknowledged_orders.count()

def calculate_fulfillment_rate(vendor):
    successful_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status='completed', quality_rating__isnull=True
    ).count()

    total_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()

    if total_orders == 0:
        return 0.0

    return (successful_orders / total_orders) * 100.0
