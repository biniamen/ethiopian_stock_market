from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from django.conf import settings  # Import settings for file management
from .models import User
from .serializers import UserSerializer
import os  # Import os for file handling

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    # Endpoint to view user's portfolio balance
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def portfolio(self, request, pk=None):
        user = self.get_object()
        return Response({'portfolio_balance': user.portfolio_balance})

    # Endpoint to update user's portfolio balance
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def update_portfolio(self, request, pk=None):
        user = self.get_object()
        amount = request.data.get('amount', 0)
        user.update_balance(float(amount))
        return Response({'message': 'Portfolio balance updated successfully.', 'portfolio_balance': user.portfolio_balance})

    # Endpoint to upload KYC document for verification
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def upload_kyc(self, request, pk=None):
        user = self.get_object()
        if 'kyc_document' in request.FILES:
            user.kyc_document = request.FILES['kyc_document']
            user.kyc_verified = False
            user.save()
            return Response({'message': 'KYC document uploaded successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No document provided.'}, status=status.HTTP_400_BAD_REQUEST)

    # Endpoint to check user's KYC verification status
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def check_kyc_status(self, request, pk=None):
        user = self.get_object()
        return Response({'kyc_verified': user.kyc_verified})

    # Endpoint to retrieve the KYC document
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAdminUser])
    def get_kyc_document(self, request, pk=None):
        user = self.get_object()
        if user.kyc_document:
            file_path = user.kyc_document.path
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), content_type='application/pdf')  # Change 'application/pdf' if the document type is different
            else:
                return Response({'error': 'File not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'No KYC document uploaded.'}, status=status.HTTP_400_BAD_REQUEST)

        # Endpoint to verify user's KYC document
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def verify_kyc(self, request, pk=None):
        user = self.get_object()
        user.kyc_verified = True  # Set KYC status to verified
        user.save()
        return Response({'message': 'User KYC verified successfully.'}, status=status.HTTP_200_OK)
