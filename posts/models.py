"""Post Models"""

from users.models import Profile
from django.contrib.auth.models import User
from django.db import models




class Post(models.Model):
    """Post model."""
    #Protect o set null
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) #Evita referencia circular APP.Model

    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='post/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        #return '{} by @ {}'.format(self.tite, self.user.username)
        return f'{self.title} by @ {self.user.username}'