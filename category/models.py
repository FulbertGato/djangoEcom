from django.db import models

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=50)
    slug=models.CharField(max_length=100,unique=True)
    description= models.CharField(max_length=255, blank=True)
    cat_image=models.ImageField(upload_to='photos/categories', blank=True)
    class Meta:
        verbose_name= 'category'
        verbose_name_plural='categories'
    def __str__(self) -> str:
        return self.category_name