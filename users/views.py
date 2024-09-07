from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Retrieve all user objects
    serializer_class = UserSerializer  # Use UserSerializer for data serialization

    # Define permissions based on request method
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [permissions.IsAdminUser()]  # Only admins can create, update, delete
        return [permissions.IsAuthenticated()]  # All authenticated users can read

    # Endpoint to view user's portfolio balance
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def portfolio(self, request, pk=None):
        user = self.get_object()  # Get the specific user instance
        return Response({'portfolio_balance': user.portfolio_balance})

    # Endpoint to update user's portfolio balance
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def update_portfolio(self, request, pk=None):
        user = self.get_object()  # Get the specific user instance
        amount = request.data.get('amount', 0)  # Get amount from request data
        user.update_balance(float(amount))  # Update the balance
        return Response({'message': 'Portfolio balance updated successfully.', 'portfolio_balance': user.portfolio_balance})

    # Endpoint to upload KYC document for verification
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def upload_kyc(self, request, pk=None):
        user = self.get_object()  # Get the specific user instance
        if 'kyc_document' in request.FILES:
            user.kyc_document = request.FILES['kyc_document']  # Save KYC document
            user.kyc_verified = False  # Set KYC status to False until verified
            user.save()
            return Response({'message': 'KYC document uploaded successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No document provided.'}, status=status.HTTP_400_BAD_REQUEST)

    # Endpoint to check user's KYC verification status
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def check_kyc_status(self, request, pk=None):
        user = self.get_object()  # Get the specific user instance
        return Response({'kyc_verified': user.kyc_verified})
