from django.db import models
from django.db.models.signals import pre_save  

from .utils import generate_unique_slug

from .validators import validate_category

# Create your models here.



class RestaurantLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True)
    category    = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
