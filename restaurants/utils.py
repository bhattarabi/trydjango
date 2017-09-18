from django.utils.text import slugify

import random
import string


DONT_USE = ['create']

def generate_random_string(size=10, 
            chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def generate_unique_slug(instance, new_slug=None):
    
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
        
    if slug in DONT_USE:
        new_slug = "{slug}-{randstr}".format(
                        slug=slug,
                        randstr=generate_random_string(size=4)
                    )
        return generate_unique_slug(instance, new_slug=new_slug)
        
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                        slug=slug,
                        randstr=generate_random_string(size=4)
                    )
        
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug
