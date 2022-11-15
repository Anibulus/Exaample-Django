from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import URLField
# Create your models here.

class Profile (models.Model):
    """Profile model
    Proxy model that extends the base data with order 
    information  """
    #Model field reference
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = URLField(max_length=200)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=14)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #Sobreescribe lo que muestra el objeto como identificador
    def __str__(self):
        return self.user.username

        