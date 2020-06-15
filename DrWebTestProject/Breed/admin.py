from django.contrib import admin
from .models import Breed, BreedImage
# Register your models here.

class BreedImageInLine(admin.TabularInline):
    model = BreedImage

class BreedAdmin(admin.ModelAdmin):
    inlines = [
        BreedImageInLine
    ]

admin.site.register(Breed, BreedAdmin)
