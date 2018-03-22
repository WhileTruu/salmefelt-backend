from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name_et = models.CharField(max_length=255, blank=False)
    name_en = models.CharField(max_length=255, blank=False)
    description_et = models.TextField()
    description_en = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name_en)

class ProductImage(models.Model):
    owner = models.ForeignKey(User, related_name='product_images', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
