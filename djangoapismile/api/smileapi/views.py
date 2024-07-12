from django.shortcuts import render
from rest_framework import generics, mixins
from .pagination import SmileAPIPagination
from .serializers import HeartRateSerializers, UserRegisterSerializers
from .models import HeartRate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.parsers import JSONParser,ParseError
from rest_framework import filters


User = get_user_model()

# Create your views here.

class HeartRateAPIView(mixins.CreateModelMixin, LoginRequiredMixin, generics.ListAPIView):
    # permission_classes          = [IsAuthenticated]
    serializer_class            = HeartRateSerializers
    pagination_class            = SmileAPIPagination
    filter_backends             = [filters.SearchFilter, filters.OrderingFilter]
    search_fields               = ('user__username', 'content')
    ordering_fields             = ('user__username', 'timestamp')
    queryset                    = HeartRate.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class HeartRateDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, LoginRequiredMixin, generics.RetrieveAPIView):
    permission_classes          = [IsAuthenticated]
    queryset                    = HeartRate.objects.all()
    serializer_class            = HeartRateSerializers
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)        


class RegisterAPIView(generics.CreateAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserRegisterSerializers
    permission_classes = [AllowAny]