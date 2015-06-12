from django import forms

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

class myForm(forms.Form):
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick':"alert('foo !');"}),required=True, label="Status")