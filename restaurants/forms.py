from django import forms

from .models import RestaurantLocation

from .validators import validate_category

class RestaurantCreateForm(forms.Form):
    name        = forms.CharField()
    location    = forms.CharField(required=False)
    category    = forms.CharField(required=False)


class RestaurantLocationCreateForm(forms.ModelForm):
    
    class Meta:
        model = RestaurantLocation
        fields = [
            "name",
            "location",
            "category"
            ]
        
    #custom validation for model fields 
    #append 'clean_' to the field name
    def clean_name(self):
        name = self.cleaned_data.get("name")
        
        if name == "name":
            raise forms.ValidationError("'name' is an invalid name!")
        return name
