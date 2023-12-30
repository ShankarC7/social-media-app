from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize > 80000000:
        raise ValidationError('maximum size 10 mb')