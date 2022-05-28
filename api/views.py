from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .serializers import CompanySerializer, FuelinfoSerializer, StationSerializer #HeroSerializer, UserSerializer, PostSerializer, CompanySerializer
from .models import Hero, Post, Company, Station, Fuelinfo
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
import jwt    
class Auth(generics.ListAPIView):
    serializer_class = CompanySerializer        
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        #owner = self.request.query_params.get('pk')
        owner = self.kwargs['pk']
        queryset = Company.objects.all()
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        return queryset
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class Auth_all(generics.ListAPIView):
    serializer_class = CompanySerializer        
    def get_queryset(self):
        queryset = Company.objects.all()
        token_user = jwt.decode(self.kwargs['token'], options={"verify_signature": False})
        owner = token_user.get('user_id')
        return queryset
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
class User(generics.ListAPIView):
    serializer_class = CompanySerializer        
    def get_queryset(self):
        token_user = jwt.decode(self.kwargs['pk'], options={"verify_signature": False})
        queryset = Company.objects.all()
        owner = token_user.get('user_id')
        queryset = queryset.filter(owner=owner)
        return queryset
        #permission_classes = [permissions.IsAuthenticatedOrReadOnly,
         #                 IsOwnerOrReadOnly]

class CoompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CompanyCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        token_user = jwt.decode(self.kwargs['token'], options={"verify_signature": False})
        owner = token_user.get('user_id')
        serializer.save(owner=owner)

#треба шамана
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    #def get_queryset(self):
    queryset = Company.objects.all()     
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #(queryset, many=True)
        #queryset = queryset.filter(id=self.kwargs['pk'])
        #return queryset
    #lookup_fields = ['owner', 'id']

class StationCreate(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()     
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StationList(generics.ListAPIView):
    serializer_class = StationSerializer        
    queryset = Station.objects.all()

class FuelinfoCreate(generics.ListCreateAPIView):
    queryset = Fuelinfo.objects.all()
    serializer_class = FuelinfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FuelinfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fuelinfo.objects.all()     
    serializer_class = FuelinfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FuelinfoList(generics.ListAPIView):
    serializer_class = FuelinfoSerializer        
    queryset = Fuelinfo.objects.all()   