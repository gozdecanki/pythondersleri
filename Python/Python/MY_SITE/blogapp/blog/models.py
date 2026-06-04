from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


#abc.com/category/beyaz-esya
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False )

    def __str__(self):
     return f"{self.name}"
    
    def save(self,*args,**kwargs):
       self.slug= slugify(self.name)#slug ifadesini name a göre otomatik oluştur
       super().save(*args,**kwargs)

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length =200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug=models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False )
    #category = models.ForeignKey(Category,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    def save(self,*args,**kwargs):
       self.slug= slugify(self.title)#slug ifadesini title a göre otomatik oluştur
       super().save(*args,**kwargs)

