from django.shortcuts import render
from rest_framework import generics
from .models import Breed
from .serializers import BreedSerializer, BreedSerializerRandom
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
# Create your views here.

class BreedList(generics.ListCreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    pagination_class = None
    

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    pagination_class = None
    
class BreedDetailRandom(generics.RetrieveUpdateDestroyAPIView):
    
    

    def get_queryset(self):
        return Breed.objects.filter(id=self.kwargs['pk'])
    serializer_class = BreedSerializerRandom 
    

    
        
