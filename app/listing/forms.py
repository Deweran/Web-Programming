from django.forms import ModelForm
from .models import Listing

class Listing_Form(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'