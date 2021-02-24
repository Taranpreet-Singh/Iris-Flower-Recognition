from django import forms

class FlowerForm(forms.Form):
    s_len = forms.FloatField()
    s_wid = forms.FloatField()
    p_len = forms.FloatField()
    p_wid = forms.FloatField()
