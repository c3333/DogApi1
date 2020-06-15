from rest_framework import serializers
from .models import Breed, BreedImage

class BreedSerializer(serializers.ModelSerializer):
  
   
    class Meta:
        model = Breed
        fields = ['name', 'BreedImages']
        
class BreedSerializerRandom(serializers.ModelSerializer):
  
   
    class Meta:
        model = Breed
        fields = ['id', 'BreedImages']
        