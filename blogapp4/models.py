from django.db import models

class Validation(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.Email
    
class Movies(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='img/', max_length=255)
    release_date = models.DateField()
    rating = models.FloatField()
    language = models.CharField(max_length=50, default="Tamil")
    genre = models.CharField(max_length=100)
    actors = models.TextField(max_length=300)
    trailer = models.FileField(upload_to='videos/', blank=True, null=True)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

    
