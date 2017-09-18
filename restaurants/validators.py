from django.core.exceptions import ValidationError

CATEGORIES = [
    'american', 
    'mexican', 
    'chinese', 
    'nepalese'
    ]


def validate_category(value):
    if value.lower() not in CATEGORIES:
        raise ValidationError("{} is not a valid category".format(value))
