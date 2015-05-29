from django import forms

# Create your forms here.
class myForm(forms.Form):

    ev = forms.BooleanField()