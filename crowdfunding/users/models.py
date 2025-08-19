from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username #whenever you get told to print out as a string please return the result to be the username (specified item)
    




# Create your models here.
