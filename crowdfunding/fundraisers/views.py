from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Fundraiser, Pledge
from .serializers import (FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer,)
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly


# ========== Fundraiser Views ==========
class FundraiserList(APIView):
    """
    List view for Fundraisers
    Handles listing all fundraisers and creating new fundraising campaigns
    GET: Available to all users
    POST: Only available to authenticated users
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Lists all fundraising campaigns
        Returns: JSON response containing all fundraisers
        """
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a new fundraising campaign
        Requires: Authenticated user
        Links: Created fundraiser to authenticated user as owner
        Returns: 201 CREATED or 400 BAD REQUEST
        """
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FundraiserDetail(APIView):
    """
    Detail view for individual Fundraisers
    Handles retrieving, updating specific fundraising campaigns
    GET: Available to all users
    PUT: Only available to fundraiser owner
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Helper method to retrieve specific fundraiser
        Args: pk (int) - Primary key of fundraiser
        Returns: Fundraiser object or 404 if not found
        """
        try:
            fundraiser = Fundraiser.objects.get(pk=pk)
            self.check_object_permissions(self.request, fundraiser)
            return fundraiser
        except Fundraiser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieves detailed information for specific fundraiser
        Args: pk (int) - Primary key of fundraiser
        Returns: Detailed JSON response of fundraiser
        """
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updates specific fundraiser details
        Args: pk (int) - Primary key of fundraiser
        Requires: User must be fundraiser owner
        Allows: Partial updates of fundraiser fields
        Returns: Updated fundraiser data or 400 BAD REQUEST
        """
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


# ========== Pledge Views ==========
class PledgeList(APIView):
    """
    List view for Pledges
    Handles listing all pledges and creating new pledges
    GET: Available to all users
    POST: Only available to authenticated users
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Lists all pledges
        Returns: JSON response containing all pledges
        """
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Creates a new pledge
        Requires: Authenticated user
        Links: Created pledge to authenticated user as supporter
        Returns: 201 CREATED or 400 BAD REQUEST
        """
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PledgeDetail(APIView):
    """
    Detail view for individual Pledges
    Handles retrieving, updating specific pledges
    GET: Available to all users
    PUT: Only available to pledge supporter
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]

    def get_object(self, pk):
        """
        Helper method to retrieve specific pledge
        Args: pk (int) - Primary key of pledge
        Returns: Pledge object or 404 if not found
        """
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieves detailed information for specific pledge
        Args: pk (int) - Primary key of pledge
        Returns: JSON response of pledge details
        """
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updates specific pledge details
        Args: pk (int) - Primary key of pledge
        Requires: User must be pledge supporter
        Allows: Partial updates of pledge fields
        Returns: Updated pledge data or 400 BAD REQUEST
        """
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
