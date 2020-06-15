from django.db import models

# Create your models here.
class Breed(models.Model):
      name = models.CharField(max_length=150)
      

      def __str__(self):
          return self.name

class BreedImage(models.Model):
    breed = models.ForeignKey(Breed, related_name='BreedImages', on_delete=models.CASCADE)
    breedImage = models.ImageField(upload_to='photos')
    
    