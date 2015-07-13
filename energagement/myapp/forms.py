from django import forms
from .models import StreetLighting1

# Create your forms here.
# class myForm(forms.Form):
#
#     ev = forms.BooleanField()

# class myForm(forms.Form):
#     stuff = forms.BooleanField(
#         [('a','A'),('b','B')],
#         widget = forms.Select(attrs = {
#             'onclick' : "alert('foo !');",
#             }
#         )
#     )

#attrs={'onclick':"alert('foo !');"}),


class myForm1(forms.Form):
    EV1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label="EV1")

class myForm2(forms.Form):
    EV2 = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label="EV2")

class myForm3(forms.Form):
    EV3 = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label="EV3")

class myForm4(forms.Form):
    kW = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label="kW")

class myForm5(forms.Form):
    kW_km = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label="kW/km")

class myForm6(forms.Form):
    Euro_km = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label="Euro/km")

class my_choose_time(forms.Form):
    choose_time = forms.ChoiceField(choices=[(x, x) for x in ('hour', 'day', 'week', 'month')])

class my_EV(forms.Form):
   EV = forms.ChoiceField(choices=[(x, x) for x in ([StreetLighting1.objects.all()])])