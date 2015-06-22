from django import forms
from .models import StreetLighting

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
test=StreetLighting.objects.get(id=1).municipality
#i=0
#for test in StreetLighting.objects.get():
 #   class myForm[i](forms.Form):
  #      EV[i] = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label=test.code)

class myForm1(forms.Form):
    EV1 = forms.BooleanField(widget=forms.CheckboxInput(attrs={}),required=True, label=test)

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