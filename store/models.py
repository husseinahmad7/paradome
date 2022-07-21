from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User


class ProductsCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductsCategory, related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='store/')
    thumbnail = models.ImageField(blank=True, null=True, upload_to='store/')
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'
    
    def make_thumbnail(self, image):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(300,300)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=f'thumb{image.name}')
        return thumbnail