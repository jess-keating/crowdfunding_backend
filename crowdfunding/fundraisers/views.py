from rest_framework import generics
from .models import Fundraiser
from .serializers import FundraiserSerializer

class FundraiserList(generics.ListCreateAPIView):
    queryset = Fundraiser.objects.all()
    serializer_class = FundraiserSerializer