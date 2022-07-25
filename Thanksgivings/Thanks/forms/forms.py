from django import forms
from ..models import Thanks

class Thanks(forms.ModelForm):
	class Meta:
		model = Thanks
		fields = '__all__'
	thanks_id = forms.CharField(required=True)
	thanks_date = forms.DateField(required=True)
	thanks_title = forms.CharField(required=True, max_length=100)
	thanks_description = forms.CharField(required=True, max_length=1000)
	givethanks_count = forms.CharField(max_length=1000,required=True)
class GiveThanks(forms.Form):
	thanks_title = forms.CharField(max_length=100, required = True)
	thanks_description = forms.CharField(max_length = 1000, required = True, widget=forms.Textarea)
	givethanks_count = forms.CharField(max_length=1000, required = True)
class Thanksgiving(forms.Form):
	thanks_title = forms.CharField(max_length=100, required = True)
	thanks_description = forms.CharField(max_length = 1000, required = True, widget=forms.Textarea)
