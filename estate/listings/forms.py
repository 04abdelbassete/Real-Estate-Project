from django import forms

from .models import House, PlotOfLand


class HouseForm(forms.ModelForm):
    
    class Meta:
        model = House
        exclude = ('added_at', 'updated_at',)

class PlotOfLandForm(forms.ModelForm):

    class Meta:
        model = PlotOfLand
        exclude = ('added_at', 'updated_at')
